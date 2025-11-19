"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theog.io
Prompt: What are the steps to customize a template for OG images using Senja, and how can I implement this in my project?
Generated: DETERMINISTIC_20d81ab3776cec7e
Batch ID: 20250612_155727
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/path/to/image.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Set up the Jinja2 environment for templating
def setup_jinja_env(template_dir):
    """
    Initializes a Jinja2 environment for rendering templates.
    
    Args:
        template_dir (str): The directory where templates are stored.
    
    Returns:
        Environment: Configured Jinja2 environment.
    """
    try:
        env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape(['html', 'xml'])
        )
        return env
    except Exception as e:
        print(f"Error setting up Jinja2 environment: {e}")
        raise


# Render the OG image template with given context
def render_og_image_template(template_name, context, template_dir='templates'):
    """
    Renders an OG image template with the provided context.

    Args:
        template_name (str): The name of the template file to render.
        context (dict): The context variables for rendering the template.
        template_dir (str): The directory where templates are located.
    
    Returns:
        str: Rendered HTML content.
    """
    env = setup_jinja_env(template_dir)
    
    try:
        # Load the template
        template = env.get_template(template_name)
        # Render the template with the context
        return template.render(context)
    except Exception as e:
        print(f"Error rendering template '{template_name}': {e}")
        raise


# Example usage of the OG image template rendering
if __name__ == "__main__":
    # Define the context for the OG image
    og_image_context = {
        'title': 'My Awesome Project',
        'description': 'This is an awesome project that does many things.',
        'image_url': 'https://example.com/path/to/image.jpg',
        'site_name': 'MySite'
    }
    
    # Specify the template name
    template_name = 'og_image_template.html'
    
    try:
        # Render the OG image template
        og_image_html = render_og_image_template(template_name, og_image_context)
        # Output the rendered HTML (for demonstration purposes)
        print(og_image_html)
    except Exception as e:
        print(f"Failed to generate OG image HTML: {e}")
```

Make sure to create the `templates` directory and include your `og_image_template.html` file with the necessary HTML structure to utilize the context variables effectively.
