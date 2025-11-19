"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jphs.snru.ac.th
Prompt: Create a function that formats a research paper submission according to the guidelines of the PHUPHAN SARN Journal.
Generated: DETERMINISTIC_a37c3bde351b990a
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import textwrap

def format_research_paper(title, authors, abstract, content):
    """
    Formats a research paper submission according to the guidelines
    of the PHUPHAN SARN Journal.

    Parameters:
        title (str): Title of the research paper.
        authors (list of str): List of authors' names.
        abstract (str): Abstract of the research paper.
        content (str): Main content of the research paper.

    Returns:
        str: Formatted research paper as a string.
    """

    try:
        # Validate input types
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        if not isinstance(authors, list) or not all(isinstance(author, str) for author in authors):
            raise ValueError("Authors must be a list of strings.")
        if not isinstance(abstract, str):
            raise ValueError("Abstract must be a string.")
        if not isinstance(content, str):
            raise ValueError("Content must be a string.")
        
        # Formatting title (uppercase and centered)
        formatted_title = title.upper().center(80)

        # Formatting authors (comma-separated list)
        formatted_authors = "Authors: " + ", ".join(authors)

        # Wrapping abstract to a maximum line length of 80 characters
        formatted_abstract = "Abstract:\n" + textwrap.fill(abstract, width=80)

        # Wrapping content to a maximum line length of 80 characters
        formatted_content = "Content:\n" + textwrap.fill(content, width=80)

        # Combine all parts into the final formatted paper
        formatted_paper = (
            f"{formatted_title}\n\n"
            f"{formatted_authors}\n\n"
            f"{formatted_abstract}\n\n"
            f"{formatted_content}"
        )

        return formatted_paper

    except Exception as e:
        # Handle unexpected errors gracefully
        return f"Error formatting paper: {e}"


# Example usage:
if __name__ == "__main__":
    title = "A Comprehensive Study of Machine Learning"
    authors = ["Alice Johnson", "Bob Smith", "Carol Lee"]
    abstract = "This study explores the applications of machine learning across various industries..."
    content = "Machine learning has revolutionized the way we approach problem-solving. In this paper..."
    
    formatted_paper = format_research_paper(title, authors, abstract, content)
    print(formatted_paper)
```
