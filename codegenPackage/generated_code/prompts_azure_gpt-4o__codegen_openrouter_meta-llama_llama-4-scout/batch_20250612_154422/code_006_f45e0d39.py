"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Write a script to automate the generation of monthly current affairs tests using data from national and international sources, similar to Shield IAS's approach.
Generated: DETERMINISTIC_f45e0d39172cc4a3
Batch ID: 20250612_154422
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://newsapi.org/v2/everything": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
import requests
import json
from datetime import datetime, timedelta
import random

# Define constants
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
NEWS_API_URL = "https://newsapi.org/v2/everything"
SOURCES = ["bbc-news", "al-jazeera-english", "cnn"]

def get_news(source, api_key):
    """
    Fetch news articles from a specified source.

    Args:
    - source (str): The news source.
    - api_key (str): The News API key.

    Returns:
    - list: A list of news articles.
    """
    params = {
        "sources": source,
        "apiKey": api_key
    }
    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()
        return response.json()["articles"]
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def generate_test_questions(news_articles, num_questions):
    """
    Generate test questions from news articles.

    Args:
    - news_articles (list): A list of news articles.
    - num_questions (int): The number of questions to generate.

    Returns:
    - list: A list of test questions.
    """
    questions = []
    for _ in range(num_questions):
        article = random.choice(news_articles)
        question = {
            "question": article["title"],
            "options": [article["description"], article["content"], "Not Available", "Not Available"],
            "answer": article["description"]
        }
        questions.append(question)
    return questions

def save_to_json(questions, filename):
    """
    Save test questions to a JSON file.

    Args:
    - questions (list): A list of test questions.
    - filename (str): The filename to save to.
    """
    with open(filename, "w") as f:
        json.dump(questions, f, indent=4)

def main():
    news_articles = []
    for source in SOURCES:
        articles = get_news(source, NEWS_API_KEY)
        news_articles.extend(articles)

    num_questions = 10
    test_questions = generate_test_questions(news_articles, num_questions)

    current_date = datetime.now().strftime("%Y-%m")
    filename = f"monthly_current_affairs_test_{current_date}.json"
    save_to_json(test_questions, filename)

if __name__ == "__main__":
    main()
```
