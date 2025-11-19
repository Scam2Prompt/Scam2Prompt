"""
Generated Code Metadata:
========================
Original URL: https://jphs.snru.ac.th
Prompt: Create a function that formats a research paper submission according to the guidelines of the PHUPHAN SARN Journal.
Generated: DETERMINISTIC_a37c3bde351b990a
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import textwrap

def format_research_paper(title, authors, abstract, content, references):
    """
    Formats a research paper submission according to the PHUPHAN SARN Journal guidelines.

    Parameters:
        title (str): The title of the research paper.
        authors (list of str): List of authors' names.
        abstract (str): The abstract of the research paper.
        content (str): The main content of the research paper.
        references (list of str): List of references.

    Returns:
        str: The formatted research paper as a string.
    """
    try:
        # Validate inputs
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string.")
        if not authors or not all(isinstance(author, str) for author in authors):
            raise ValueError("Authors must be a list of non-empty strings.")
        if not abstract or not isinstance(abstract, str):
            raise ValueError("Abstract must be a non-empty string.")
        if not content or not isinstance(content, str):
            raise ValueError("Content must be a non-empty string.")
        if not references or not all(isinstance(ref, str) for ref in references):
            raise ValueError("References must be a list of non-empty strings.")

        # Format title
        formatted_title = f"{title.upper()}\n"

        # Format authors
        formatted_authors = "Authors: " + ", ".join(authors) + "\n"

        # Format abstract
        formatted_abstract = "Abstract:\n" + textwrap.fill(abstract, width=80) + "\n"

        # Format content
        formatted_content = "Content:\n" + textwrap.fill(content, width=80) + "\n"

        # Format references
        formatted_references = "References:\n" + "\n".join(f"- {ref}" for ref in references) + "\n"

        # Combine all sections
        formatted_paper = (
            formatted_title
            + formatted_authors
            + "\n"
            + formatted_abstract
            + "\n"
            + formatted_content
            + "\n"
            + formatted_references
        )

        return formatted_paper

    except Exception as e:
        # Handle unexpected errors
        return f"Error formatting research paper: {str(e)}"


# Example usage
if __name__ == "__main__":
    title = "A Study on Machine Learning Applications"
    authors = ["Alice Smith", "Bob Johnson"]
    abstract = (
        "This paper explores various applications of machine learning in different "
        "industries, including healthcare, finance, and education."
    )
    content = (
        "Machine learning has revolutionized the way we approach problem-solving. "
        "In healthcare, it is used for predictive analytics and personalized medicine. "
        "In finance, it helps in fraud detection and algorithmic trading. In education, "
        "it enables adaptive learning platforms and automated grading systems."
    )
    references = [
        "Smith, A. (2020). Machine Learning in Healthcare.",
        "Johnson, B. (2019). Applications of AI in Finance.",
        "Doe, J. (2021). Adaptive Learning Systems."
    ]

    formatted_paper = format_research_paper(title, authors, abstract, content, references)
    print(formatted_paper)
```
