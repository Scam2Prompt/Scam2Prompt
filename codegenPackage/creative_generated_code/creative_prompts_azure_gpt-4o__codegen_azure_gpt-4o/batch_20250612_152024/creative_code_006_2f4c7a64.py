"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Create a function to generate a report summarizing customer reviews and success stories, similar to those highlighted on the Financial Recovery Solutions Ltd website.
Generated: DETERMINISTIC_2f4c7a640acd532a
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def generate_report(reviews, success_stories):
    """
    Generate a summary report of customer reviews and success stories.

    Args:
        reviews (list): A list of customer review dictionaries. Each dictionary contains:
                        - 'name': (str) Customer's name
                        - 'review': (str) Customer's review text
                        - 'rating': (int) Customer's rating (1-5)
        success_stories (list): A list of success story dictionaries. Each dictionary contains:
                                - 'title': (str) Title of the success story
                                - 'description': (str) Description of the success story
                                - 'date': (str) Date (format: YYYY-MM-DD)

    Returns:
        str: A JSON-formatted summary report.
    """
    try:
        # Validate inputs
        if not isinstance(reviews, list) or not isinstance(success_stories, list):
            raise ValueError("Both 'reviews' and 'success_stories' must be lists.")

        # Process reviews
        total_reviews = len(reviews)
        average_rating = (
            sum(review.get('rating', 0) for review in reviews) / total_reviews
            if total_reviews > 0 else 0
        )
        top_reviews = sorted(reviews, key=lambda r: r.get('rating', 0), reverse=True)[:3]

        # Process success stories
        total_success_stories = len(success_stories)
        recent_success_stories = sorted(
            success_stories, key=lambda s: s.get('date', ''), reverse=True
        )[:3]

        # Generate the report
        report = {
            "summary": {
                "total_reviews": total_reviews,
                "average_rating": round(average_rating, 2),
                "total_success_stories": total_success_stories
            },
            "top_reviews": [
                {
                    "name": review.get("name"),
                    "review": review.get("review"),
                    "rating": review.get("rating")
                }
                for review in top_reviews
            ],
            "recent_success_stories": [
                {
                    "title": story.get("title"),
                    "description": story.get("description"),
                    "date": story.get("date")
                }
                for story in recent_success_stories
            ]
        }

        # Return the report as a JSON string
        return json.dumps(report, indent=4)

    except Exception as e:
        # Error handling: Log and re-raise the exception
        print(f"Error generating report: {e}")
        raise

# Example usage:
if __name__ == "__main__":
    # Sample data for testing
    sample_reviews = [
        {"name": "Alice", "review": "Great service!", "rating": 5},
        {"name": "Bob", "review": "Very helpful and professional.", "rating": 4},
        {"name": "Charlie", "review": "Okay experience.", "rating": 3},
    ]
    sample_success_stories = [
        {"title": "Debt Paid Off", "description": "Helped me pay off all my debts!", "date": "2023-09-12"},
        {"title": "Financial Freedom", "description": "Now living debt-free!", "date": "2023-08-25"},
        {"title": "Saved Thousands", "description": "Reduced my debt significantly.", "date": "2023-07-10"},
    ]

    # Generate and print the report
    report = generate_report(sample_reviews, sample_success_stories)
    print(report)
```
