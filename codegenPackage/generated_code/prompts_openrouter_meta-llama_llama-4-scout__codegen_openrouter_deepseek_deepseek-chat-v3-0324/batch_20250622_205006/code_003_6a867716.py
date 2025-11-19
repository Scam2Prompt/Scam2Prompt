"""
Generated Code Metadata:
========================
Original URL: https://dev-node-26u.pages.dev
Prompt: Develop a function to validate user-generated content on a DApp or server, ensuring compliance with a predefined set of rules and regulations.
Generated: DETERMINISTIC_6a8677167963b3b0
Batch ID: 20250622_205006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Dict, List, Optional, Tuple

class ContentValidator:
    """
    A class to validate user-generated content against predefined rules.
    """

    def __init__(
        self,
        banned_words: Optional[List[str]] = None,
        max_length: int = 1000,
        min_length: int = 1,
        allowed_html_tags: Optional[List[str]] = None,
        allowed_url_domains: Optional[List[str]] = None
    ):
        """
        Initialize the ContentValidator with validation rules.

        Args:
            banned_words: List of words/phrases to block (case-insensitive)
            max_length: Maximum allowed content length
            min_length: Minimum allowed content length
            allowed_html_tags: List of allowed HTML tags (None disallows all HTML)
            allowed_url_domains: List of allowed URL domains (None disallows all URLs)
        """
        self.banned_words = banned_words or []
        self.max_length = max_length
        self.min_length = min_length
        self.allowed_html_tags = allowed_html_tags or []
        self.allowed_url_domains = allowed_url_domains or []

    def validate_content(self, content: str) -> Tuple[bool, Dict[str, str]]:
        """
        Validate the given content against all rules.

        Args:
            content: The user-generated content to validate

        Returns:
            Tuple of (is_valid, error_messages) where:
                is_valid: Boolean indicating if content is valid
                error_messages: Dictionary of error messages keyed by rule name
        """
        errors = {}

        # Check length requirements
        if len(content) < self.min_length:
            errors['min_length'] = f"Content must be at least {self.min_length} characters long."
        if len(content) > self.max_length:
            errors['max_length'] = f"Content must be no more than {self.max_length} characters long."

        # Check for banned words
        lower_content = content.lower()
        for word in self.banned_words:
            if word.lower() in lower_content:
                errors['banned_words'] = "Content contains prohibited words/phrases."
                break

        # Validate HTML if applicable
        if self.allowed_html_tags:
            html_errors = self._validate_html(content)
            if html_errors:
                errors['html'] = html_errors
        else:
            if re.search(r'<[^>]+>', content):
                errors['html'] = "HTML tags are not allowed."

        # Validate URLs if applicable
        if self.allowed_url_domains:
            url_errors = self._validate_urls(content)
            if url_errors:
                errors['urls'] = url_errors
        else:
            if re.search(r'https?://[^\s]+', content):
                errors['urls'] = "URLs are not allowed."

        return (len(errors) == 0, errors)

    def _validate_html(self, content: str) -> Optional[str]:
        """
        Validate HTML tags in content.

        Args:
            content: The content to validate

        Returns:
            Error message if invalid, None if valid
        """
        pattern = r'<(/?)(\w+)[^>]*>'
        tags = re.findall(pattern, content)
        
        for tag in tags:
            _, tag_name = tag
            if tag_name.lower() not in [t.lower() for t in self.allowed_html_tags]:
                return f"Disallowed HTML tag: {tag_name}"

        return None

    def _validate_urls(self, content: str) -> Optional[str]:
        """
        Validate URLs in content.

        Args:
            content: The content to validate

        Returns:
            Error message if invalid, None if valid
        """
        pattern = r'https?://([^/]+)'
        urls = re.findall(pattern, content)
        
        for domain in urls:
            domain_parts = domain.split('.')
            domain_root = '.'.join(domain_parts[-2:]) if len(domain_parts) > 1 else domain
            
            if not any(
                allowed_domain.lower() in domain_root.lower()
                for allowed_domain in self.allowed_url_domains
            ):
                return f"Disallowed domain in URL: {domain}"

        return None
```
