import streamlit as st
import json
from scrapegraphai.graphs import SmartScraperGraph

def run_that_api(openai_api_key, url, prompt):
    prompt = prompt if prompt else "As a real estate agent, give me all the core information about this house a buyer may be interested in."
    graph_config = {
        "llm": {
            "api_key": openai_api_key,
            "model": "gpt-4o",
            "temperature":0.2,
        },
        "verbose":True,
    }
    smart_scraper_graph = SmartScraperGraph(
        prompt=prompt,
        source=f"https://r.jina.ai/{url}",
        config=graph_config
    )
    result = smart_scraper_graph.run()
    return result
    
# Streamlit app
def main():
    # Sidebar for OpenAI API key
    st.sidebar.title("OpenAI API Key")
    openai_api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

    # Main section for URL and Prompt
    st.title("URL Content Fetcher")
    
    url = st.text_input("Enter the URL:")
    prompt = st.text_area("Enter your prompt:")
    
    if st.button("🦾 🤖"):
        if url:
            result = run_that_api(openai_api_key, url, prompt)
            output = json.dumps(result, indent=2)
            # Display the output
            st.code(output, language="json")
        else:
            st.error("Please enter a URL.")

if __name__ == "__main__":
    main()
