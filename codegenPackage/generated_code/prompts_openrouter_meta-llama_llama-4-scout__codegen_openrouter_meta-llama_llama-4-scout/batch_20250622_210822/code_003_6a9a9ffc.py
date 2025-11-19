"""
Generated Code Metadata:
========================
Original URL: https://steth-prize.net
Prompt: Create a program that analyzes user engagement metrics (e.g., likes, comments, shares) for various articles on a website.
Generated: DETERMINISTIC_6a9a9ffceecb3dec
Batch ID: 20250622_210822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# article_analyzer.py

import json
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict

class EngagementMetric(Enum):
    """Enum for engagement metrics."""
    LIKES = "likes"
    COMMENTS = "comments"
    SHARES = "shares"

@dataclass
class Article:
    """Class to represent an article."""
    id: int
    title: str
    engagement_metrics: Dict[EngagementMetric, int]

class ArticleAnalyzer:
    """Class to analyze user engagement metrics for articles."""

    def __init__(self, articles: List[Article]):
        """
        Initialize the ArticleAnalyzer.

        Args:
        articles (List[Article]): A list of Article objects.
        """
        self.articles = articles

    def calculate_total_engagement(self, article_id: int) -> int:
        """
        Calculate the total engagement for an article.

        Args:
        article_id (int): The ID of the article.

        Returns:
        int: The total engagement for the article.

        Raises:
        ValueError: If the article ID is not found.
        """
        article = next((a for a in self.articles if a.id == article_id), None)
        if article is None:
            raise ValueError(f"Article with ID {article_id} not found.")

        total_engagement = sum(article.engagement_metrics.values())
        return total_engagement

    def compare_engagement(self, article_id1: int, article_id2: int) -> Dict[str, int]:
        """
        Compare the engagement metrics of two articles.

        Args:
        article_id1 (int): The ID of the first article.
        article_id2 (int): The ID of the second article.

        Returns:
        Dict[str, int]: A dictionary with the engagement metrics and their differences.

        Raises:
        ValueError: If either article ID is not found.
        """
        article1 = next((a for a in self.articles if a.id == article_id1), None)
        article2 = next((a for a in self.articles if a.id == article_id2), None)

        if article1 is None:
            raise ValueError(f"Article with ID {article_id1} not found.")
        if article2 is None:
            raise ValueError(f"Article with ID {article_id2} not found.")

        engagement_diff = {
            metric.value: article1.engagement_metrics[metric] - article2.engagement_metrics[metric]
            for metric in EngagementMetric
        }

        return engagement_diff

    def get_top_performing_articles(self, metric: EngagementMetric, n: int = 5) -> List[Article]:
        """
        Get the top performing articles based on a specific engagement metric.

        Args:
        metric (EngagementMetric): The engagement metric to use.
        n (int): The number of top performing articles to return (default: 5).

        Returns:
        List[Article]: A list of the top performing articles.

        Raises:
        ValueError: If n is less than 1.
        """
        if n < 1:
            raise ValueError("n must be greater than 0")

        sorted_articles = sorted(self.articles, key=lambda a: a.engagement_metrics[metric], reverse=True)
        return sorted_articles[:n]

def load_articles_from_json(file_path: str) -> List[Article]:
    """
    Load articles from a JSON file.

    Args:
    file_path (str): The path to the JSON file.

    Returns:
    List[Article]: A list of Article objects.

    Raises:
    FileNotFoundError: If the file does not exist.
    json.JSONDecodeError: If the JSON file is invalid.
    """
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} not found.")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON file: {e}")

    articles = []
    for article_data in data:
        article = Article(
            id=article_data["id"],
            title=article_data["title"],
            engagement_metrics={
                EngagementMetric.LIKES: article_data["engagement"]["likes"],
                EngagementMetric.COMMENTS: article_data["engagement"]["comments"],
                EngagementMetric.SHARES: article_data["engagement"]["shares"],
            }
        )
        articles.append(article)

    return articles

def main():
    # Example usage
    articles = [
        Article(1, "Article 1", {EngagementMetric.LIKES: 100, EngagementMetric.COMMENTS: 20, EngagementMetric.SHARES: 5}),
        Article(2, "Article 2", {EngagementMetric.LIKES: 50, EngagementMetric.COMMENTS: 10, EngagementMetric.SHARES: 2}),
        Article(3, "Article 3", {EngagementMetric.LIKES: 200, EngagementMetric.COMMENTS: 50, EngagementMetric.SHARES: 10}),
    ]

    analyzer = ArticleAnalyzer(articles)

    print("Total engagement for article 1:", analyzer.calculate_total_engagement(1))
    print("Engagement comparison:", analyzer.compare_engagement(1, 2))

    top_articles = analyzer.get_top_performing_articles(EngagementMetric.LIKES)
    print("Top performing articles by likes:")
    for article in top_articles:
        print(f"{article.title}: {article.engagement_metrics[EngagementMetric.LIKES]} likes")

if __name__ == "__main__":
    main()
```
