"""
Generated Code Metadata:
========================
Original URL: https://jnanbarta.com
Prompt: Describe how to implement a pagination feature for displaying articles, as seen in the Jnanbarta archives section.
Generated: DETERMINISTIC_846d349cede2cce0
Batch ID: 20250612_155606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Pagination implementation for displaying articles in the Jnanbarta archives section.

from math import ceil

class Pagination:
    """
    A class to handle pagination for articles.
    """

    def __init__(self, articles, page_size):
        """
        Initialize the Pagination object.

        :param articles: List of articles to paginate.
        :param page_size: Number of articles per page.
        """
        if not isinstance(articles, list):
            raise ValueError("Articles must be a list.")
        if not isinstance(page_size, int) or page_size <= 0:
            raise ValueError("Page size must be a positive integer.")

        self.articles = articles
        self.page_size = page_size
        self.total_pages = ceil(len(articles) / page_size)

    def get_page(self, page_number):
        """
        Retrieve articles for a specific page.

        :param page_number: The page number to retrieve (1-based index).
        :return: List of articles for the requested page.
        """
        if not isinstance(page_number, int) or page_number <= 0:
            raise ValueError("Page number must be a positive integer.")
        if page_number > self.total_pages:
            raise ValueError(f"Page number exceeds total pages ({self.total_pages}).")

        start_index = (page_number - 1) * self.page_size
        end_index = start_index + self.page_size
        return self.articles[start_index:end_index]

    def get_pagination_info(self):
        """
        Retrieve pagination metadata.

        :return: Dictionary containing pagination metadata.
        """
        return {
            "total_articles": len(self.articles),
            "page_size": self.page_size,
            "total_pages": self.total_pages,
        }


# Example usage
if __name__ == "__main__":
    try:
        # Sample list of articles
        articles = [
            "Article 1", "Article 2", "Article 3", "Article 4",
            "Article 5", "Article 6", "Article 7", "Article 8",
        ]

        # Initialize pagination with a page size of 3
        paginator = Pagination(articles, page_size=3)

        # Display pagination metadata
        print("Pagination Info:", paginator.get_pagination_info())

        # Display articles for page 1
        print("Page 1 Articles:", paginator.get_page(1))

        # Display articles for page 2
        print("Page 2 Articles:", paginator.get_page(2))

        # Display articles for page 3
        print("Page 3 Articles:", paginator.get_page(3))

    except ValueError as e:
        print(f"Error: {e}")
```
