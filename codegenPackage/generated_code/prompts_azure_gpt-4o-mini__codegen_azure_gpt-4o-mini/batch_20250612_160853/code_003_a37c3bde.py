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
import re

class ResearchPaperFormatter:
    """
    A class to format research paper submissions according to the PHUPHAN SARN Journal guidelines.
    """

    def __init__(self, title, authors, abstract, body, references):
        """
        Initializes the ResearchPaperFormatter with the provided paper details.

        :param title: Title of the research paper
        :param authors: List of authors
        :param abstract: Abstract of the research paper
        :param body: Main body of the research paper
        :param references: List of references
        """
        self.title = title
        self.authors = authors
        self.abstract = abstract
        self.body = body
        self.references = references

    def format_title(self):
        """Formats the title of the paper."""
        return f"# {self.title}\n"

    def format_authors(self):
        """Formats the authors of the paper."""
        authors_str = ', '.join(self.authors)
        return f"**Authors:** {authors_str}\n\n"

    def format_abstract(self):
        """Formats the abstract of the paper."""
        return f"## Abstract\n{self.abstract}\n\n"

    def format_body(self):
        """Formats the main body of the paper."""
        return f"## Main Body\n{self.body}\n\n"

    def format_references(self):
        """Formats the references of the paper."""
        formatted_references = "\n".join([f"{i + 1}. {ref}" for i, ref in enumerate(self.references)])
        return f"## References\n{formatted_references}\n"

    def format_paper(self):
        """Formats the entire research paper according to the journal's guidelines."""
        try:
            formatted_paper = (
                self.format_title() +
                self.format_authors() +
                self.format_abstract() +
                self.format_body() +
                self.format_references()
            )
            return formatted_paper
        except Exception as e:
            raise RuntimeError("An error occurred while formatting the paper.") from e


# Example usage
if __name__ == "__main__":
    title = "The Impact of AI on Modern Research"
    authors = ["Alice Smith", "Bob Johnson"]
    abstract = "This paper explores the implications of artificial intelligence in research methodologies."
    body = "The body of the paper discusses various aspects of AI..."
    references = [
        "Smith, A. (2023). AI in Research. Journal of AI Studies.",
        "Johnson, B. (2022). The Future of Research. Research Trends."
    ]

    formatter = ResearchPaperFormatter(title, authors, abstract, body, references)
    formatted_paper = formatter.format_paper()
    print(formatted_paper)
```
