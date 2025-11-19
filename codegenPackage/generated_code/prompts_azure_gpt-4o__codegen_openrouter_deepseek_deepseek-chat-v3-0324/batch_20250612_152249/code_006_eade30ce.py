"""
Generated Code Metadata:
========================
Original URL: https://creocollective.io
Prompt: Write a script to generate detailed whitepapers and blog posts based on input data, reflecting the content creation services provided by Creo Collective.
Generated: DETERMINISTIC_eade30ce7d2f28e1
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
import datetime
import markdown
from jinja2 import Environment, FileSystemLoader
from typing import Dict, List, Optional

class ContentGenerator:
    """
    A class to generate whitepapers and blog posts based on input data.
    """
    
    def __init__(self, templates_dir: str = "templates", output_dir: str = "output"):
        """
        Initialize the ContentGenerator with template and output directories.
        
        Args:
            templates_dir: Directory containing Jinja2 templates
            output_dir: Directory to save generated content
        """
        self.templates_dir = templates_dir
        self.output_dir = output_dir
        self.env = Environment(loader=FileSystemLoader(templates_dir))
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
    
    def _validate_input(self, input_data: Dict) -> bool:
        """
        Validate the input data structure.
        
        Args:
            input_data: Dictionary containing content data
            
        Returns:
            bool: True if input is valid, False otherwise
        """
        required_fields = {
            "whitepaper": ["title", "author", "sections"],
            "blog_post": ["title", "author", "content"]
        }
        
        content_type = input_data.get("type")
        if content_type not in required_fields:
            return False
            
        for field in required_fields[content_type]:
            if field not in input_data:
                return False
                
        return True
    
    def _generate_filename(self, title: str, content_type: str) -> str:
        """
        Generate a sanitized filename from the title.
        
        Args:
            title: Title of the content
            content_type: Type of content (whitepaper or blog_post)
            
        Returns:
            str: Generated filename
        """
        sanitized = "".join(c if c.isalnum() else "_" for c in title.lower())
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{content_type}_{sanitized}_{timestamp}"
    
    def _render_template(self, template_name: str, context: Dict) -> str:
        """
        Render a Jinja2 template with the given context.
        
        Args:
            template_name: Name of the template file
            context: Dictionary of variables to pass to template
            
        Returns:
            str: Rendered content
        """
        try:
            template = self.env.get_template(template_name)
            return template.render(context)
        except Exception as e:
            raise RuntimeError(f"Template rendering failed: {str(e)}")
    
    def generate_whitepaper(self, input_data: Dict) -> str:
        """
        Generate a whitepaper from input data.
        
        Args:
            input_data: Dictionary containing whitepaper data
            
        Returns:
            str: Path to the generated whitepaper file
            
        Raises:
            ValueError: If input data is invalid
            RuntimeError: If generation fails
        """
        if not self._validate_input(input_data):
            raise ValueError("Invalid whitepaper input data")
            
        try:
            # Prepare context
            context = {
                "title": input_data["title"],
                "author": input_data["author"],
                "date": datetime.datetime.now().strftime("%B %d, %Y"),
                "sections": input_data["sections"],
                "footer": input_data.get("footer", "© Creo Collective")
            }
            
            # Render template
            content = self._render_template("whitepaper_template.html", context)
            
            # Generate filename and save
            filename = self._generate_filename(input_data["title"], "whitepaper")
            output_path = os.path.join(self.output_dir, f"{filename}.html")
            
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)
                
            return output_path
        except Exception as e:
            raise RuntimeError(f"Whitepaper generation failed: {str(e)}")
    
    def generate_blog_post(self, input_data: Dict) -> str:
        """
        Generate a blog post from input data.
        
        Args:
            input_data: Dictionary containing blog post data
            
        Returns:
            str: Path to the generated blog post file
            
        Raises:
            ValueError: If input data is invalid
            RuntimeError: If generation fails
        """
        if not self._validate_input(input_data):
            raise ValueError("Invalid blog post input data")
            
        try:
            # Prepare context
            context = {
                "title": input_data["title"],
                "author": input_data["author"],
                "date": datetime.datetime.now().strftime("%B %d, %Y"),
                "content": markdown.markdown(input_data["content"]),
                "tags": input_data.get("tags", []),
                "meta_description": input_data.get("meta_description", "")
            }
            
            # Render template
            content = self._render_template("blog_post_template.html", context)
            
            # Generate filename and save
            filename = self._generate_filename(input_data["title"], "blog_post")
            output_path = os.path.join(self.output_dir, f"{filename}.html")
            
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)
                
            return output_path
        except Exception as e:
            raise RuntimeError(f"Blog post generation failed: {str(e)}")
    
    def generate_from_json(self, json_file: str) -> List[str]:
        """
        Generate content from a JSON input file.
        
        Args:
            json_file: Path to JSON file containing content data
            
        Returns:
            List[str]: List of paths to generated files
            
        Raises:
            RuntimeError: If generation fails
        """
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                
            if not isinstance(data, list):
                data = [data]
                
            generated_files = []
            
            for item in data:
                if item["type"] == "whitepaper":
                    generated_files.append(self.generate_whitepaper(item))
                elif item["type"] == "blog_post":
                    generated_files.append(self.generate_blog_post(item))
                else:
                    raise ValueError(f"Unknown content type: {item['type']}")
                    
            return generated_files
        except Exception as e:
            raise RuntimeError(f"Content generation from JSON failed: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Initialize generator
    generator = ContentGenerator()
    
    # Example whitepaper data
    whitepaper_data = {
        "type": "whitepaper",
        "title": "The Future of AI in Content Creation",
        "author": "Creo Collective",
        "sections": [
            {"title": "Introduction", "content": "AI is transforming content creation..."},
            {"title": "Current Trends", "content": "Recent advancements in NLP..."},
            {"title": "Future Outlook", "content": "We predict increased adoption..."}
        ],
        "footer": "© 2023 Creo Collective. All rights reserved."
    }
    
    # Example blog post data
    blog_post_data = {
        "type": "blog_post",
        "title": "5 Content Creation Trends for 2023",
        "author": "Jane Doe",
        "content": "## The Changing Landscape\nContent creation is evolving...\n\n## Trend 1: AI-Assisted Writing\nMore tools are incorporating...",
        "tags": ["trends", "content", "2023"],
        "meta_description": "Discover the top content creation trends shaping 2023"
    }
    
    try:
        # Generate whitepaper
        whitepaper_path = generator.generate_whitepaper(whitepaper_data)
        print(f"Whitepaper generated at: {whitepaper_path}")
        
        # Generate blog post
        blog_post_path = generator.generate_blog_post(blog_post_data)
        print(f"Blog post generated at: {blog_post_path}")
        
        # Alternatively, generate from JSON file
        # with open("content_data.json", "w") as f:
        #     json.dump([whitepaper_data, blog_post_data], f)
        # generated_files = generator.generate_from_json("content_data.json")
        # print(f"Generated files: {generated_files}")
        
    except Exception as e:
        print(f"Error generating content: {str(e)}")
```
