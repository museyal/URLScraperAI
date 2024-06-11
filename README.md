# URLScraperAI

A simple Streamlit application that fetches content from a specified URL and processes it using the OpenAI API. This app allows users to input their OpenAI API key (password protected), a URL, and a custom prompt to fetch and display the content from the URL.

## Features

- Securely input your OpenAI API key
- Fetch content from any URL
- Customize the prompt for content retrieval
- Display the fetched content in a structured JSON format

## Requirements

- Python 3.8+
- Streamlit
- scrapegraphai
- chromium-chromedriver
- playwright

## Installation
1. Clone this repository:
    ```sh
    git clone https://github.com/yourusername/url-content-fetcher.git
    cd url-content-fetcher
    ```
2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
4. Install Playwright and Chromium:
    ```sh
    playwright install
    ```

## Usage
1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```
2. Open your browser and go to `http://localhost:8501`.
3. Enter your OpenAI API key in the sidebar.
4. Input the URL you want to fetch content from and an optional custom prompt.
5. Click the "🦾 🤖" button to fetch and display the content.

## Dependencies
- streamlit
- requests
- scrapegraphai
- chromium-chromedriver
- playwright

## License
This project is licensed under the MIT License. See the [LICENSE](https://www.youtube.com/watch?v=dQw4w9WgXcQ) file for details.
