import requests
import streamlit as st

def fetch_news(published_after, limit=10):
    """Fetch news articles"""
    NEWS_API_URL = "https://api.stockdata.org/v1/news/all"
    API_TOKEN = "bS2jganHVlFYtAly7ttdHYLrTB0s6BmONWmFEApD"  # Consider moving this to st.secrets

    params = {
        "api_token": API_TOKEN,
        "countries": "sa",
        "filter_entities": "true",
        "limit": limit,
        "published_after": published_after,
        "language": "en"
    }
    try:
        response = requests.get(NEWS_API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("data", [])
    except Exception as e:
        st.error(f"Error fetching news: {str(e)}")
        return []
```

Key changes:
1. Updated the `NEWS_API_URL` to use the stockdata.org API.
2. Changed the API token to the one provided in your URL.
3. Removed the `must_have_entities` and `group_similar` parameters as they don't appear to be supported by this API.
4. Adjusted the return statement to match the expected structure of the API response.

Please note:
- It's generally not a good practice to include API keys directly in your code. Consider moving the API_TOKEN to your `st.secrets` for better security.
- Make sure to review the stockdata.org API documentation to ensure you're using all available and relevant parameters.
- The `published_after` parameter should be a string in the format "YYYY-MM-DDTHH:MM".

You can call this function in your main code like this:

```python
news_articles = fetch_news("2023-06-02T11:01", limit=10)
```

This will fetch up to 10 news articles published after June 2, 2023, at 11:01 AM, related to Saudi Arabia. Adjust the date and time as needed for your application.
