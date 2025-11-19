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
import re

class PaperFormatError(Exception):
    """Custom exception for paper formatting errors."""
    pass

def format_research_paper(title, authors, abstract, keywords, content):
    """
    Formats a research paper submission according to the PHUPHAN SARN Journal guidelines.
    
    Parameters:
        title (str): The title of the research paper.
        authors (list): A list of author names.
        abstract (str): The abstract of the paper.
        keywords (list): Keywords related to the paper.
        content (str): The main content of the paper.
        
    Returns:
        str: The formatted research paper.
        
    Raises:
        PaperFormatError: If any formatting rules are violated.
    """
    
    # Validate input parameters
    if not isinstance(title, str) or not title.strip():
        raise PaperFormatError("Title must be a non-empty string.")
    if not isinstance(authors, list) or not authors:
        raise PaperFormatError("Authors must be a non-empty list of strings.")
    for author in authors:
        if not isinstance(author, str) or not author.strip():
            raise PaperFormatError("Each author must be a non-empty string.")
    if not isinstance(abstract, str) or not abstract.strip():
        raise PaperFormatError("Abstract must be a non-empty string.")
    if not isinstance(keywords, list) or not keywords:
        raise PaperFormatError("Keywords must be a non-empty list of strings.")
    for keyword in keywords:
        if not isinstance(keyword, str) or not keyword.strip():
            raise PaperFormatError("Each keyword must be a non-empty string.")
    if not isinstance(content, str) or not content.strip():
        raise PaperFormatError("Content must be a non-empty string.")

    # Format title
    formatted_title = f"Title: {title.strip()}\n"

    # Format authors
    formatted_authors = "Authors: " + ", ".join(author.strip() for author in authors) + "\n"
    
    # Format abstract
    formatted_abstract = f"Abstract: {abstract.strip()}\n"

    # Format keywords
    formatted_keywords = "Keywords: " + ", ".join(keyword.strip() for keyword in keywords) + "\n"
    
    # Format content
    formatted_content = f"Content:\n{content.strip()}\n"

    # Assemble the final formatted paper
    formatted_paper = (formatted_title + formatted_authors + 
                       formatted_abstract + formatted_keywords + 
                       formatted_content)
    
    return formatted_paper

# Example usage:
if __name__ == "__main__":
    try:
        title = "Research on Python Code Formatting"
        authors = ["John Doe", "Jane Smith"]
        abstract = "This paper explores best practices in Python code formatting."
        keywords = ["Python", "Code", "Formatting"]
        content = "In this paper, we will discuss various aspects of code formatting in Python."
        
        print(format_research_paper(title, authors, abstract, keywords, content))
    except PaperFormatError as e:
        print(f"Error: {e}")
```
