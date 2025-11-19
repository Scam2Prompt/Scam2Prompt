"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sushiswap.andy.cx
Prompt: Develop a library function that formats and organizes blog posts about parenting and childhood experiences, drawing from the content structure of Andy.cx.
Generated: DETERMINISTIC_4172244c92c0fe32
Batch ID: 20250612_155421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class BlogPostFormatter:
    """
    A class to format and organize blog posts about parenting and childhood experiences.
    Inspired by the content structure of Andy.cx.
    """

    def __init__(self):
        """
        Initialize the BlogPostFormatter with basic settings.
        """
        self.max_title_length = 100
        self.max_excerpt_length = 300
        self.allowed_tags = ['<p>', '<strong>', '<em>', '<ul>', '<li>', '<ol>', '<blockquote>']

    def sanitize_content(self, content):
        """
        Sanitize the content to allow only specific HTML tags and remove any invalid ones.
        
        Parameters:
        content (str): Raw HTML content.

        Returns:
        str: Sanitized HTML content.
        """
        # Escape any invalid or unsafe HTML tags
        tag_pattern = re.compile(r"</?[^>]+>")
        sanitized_content = tag_pattern.sub(lambda match: match.group(0) if match.group(0) in self.allowed_tags else '', content)
        return sanitized_content

    def format_title(self, title):
        """
        Format the title to ensure it adheres to length constraints.

        Parameters:
        title (str): Raw title text.

        Returns:
        str: Formatted title.
        """
        # Truncate title if it exceeds the maximum length
        formatted_title = title.strip()
        if len(formatted_title) > self.max_title_length:
            formatted_title = formatted_title[:self.max_title_length] + "..."
        return formatted_title

    def generate_excerpt(self, content):
        """
        Generate an excerpt from the content for preview purposes.

        Parameters:
        content (str): Raw content text.

        Returns:
        str: Excerpt text.
        """
        plain_text = re.sub(r"<[^>]+>", "", content)  # Remove all HTML tags for plain text
        excerpt = plain_text.strip()
        if len(excerpt) > self.max_excerpt_length:
            excerpt = excerpt[:self.max_excerpt_length] + "..."
        return excerpt

    def format_post(self, title, content):
        """
        Format and organize a blog post with title and content.

        Parameters:
        title (str): Raw title text.
        content (str): Raw HTML content of the post.

        Returns:
        dict: A dictionary containing formatted title, sanitized content, and excerpt.
        """
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string.")
        if not content or not isinstance(content, str):
            raise ValueError("Content must be a non-empty string.")
        
        formatted_title = self.format_title(title)
        sanitized_content = self.sanitize_content(content)
        excerpt = self.generate_excerpt(sanitized_content)
        
        return {
            "title": formatted_title,
            "content": sanitized_content,
            "excerpt": excerpt
        }

# Example usage:
if __name__ == "__main__":
    formatter = BlogPostFormatter()
    raw_title = "A memorable day in parenting: Lessons learned while raising kids"
    raw_content = """
        <p>Parenting is an ever-evolving journey. One of the most important <strong>lessons</strong> I learned was...</p>
        <script>alert("This should not be here");</script>
        <p>Another important aspect is <em>communication</em> with your child.</p>
    """
    
    try:
        formatted_post = formatter.format_post(raw_title, raw_content)
        print("Formatted Blog Post:")
        print(f"Title: {formatted_post['title']}")
        print(f"Excerpt: {formatted_post['excerpt']}")
        print(f"Content: {formatted_post['content']}")
    except ValueError as e:
        print(f"Error: {e}")
```
