"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.autocaret.com
Prompt: Generate a sample document using AutoCaret templates, focusing on the features of AI-powered writing and formatting.
Generated: DETERMINISTIC_ff8962bf3acc1c66
Batch ID: 20250612_160102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class AutoCaretTemplateEngine:
    """
    A class for managing and generating documents using AutoCaret templates.
    AutoCaret templates allow for dynamic insertion of AI-powered writing and formatting features.
    """

    def __init__(self, template_path):
        """
        Initializes the template engine.

        :param template_path: Path to the template file (JSON format).
        """
        self.template_path = template_path
        self.template = None

    def load_template(self):
        """
        Loads the template from the specified file.

        :raises FileNotFoundError: If the template file does not exist.
        :raises json.JSONDecodeError: If the template file contains invalid JSON.
        """
        if not os.path.exists(self.template_path):
            raise FileNotFoundError(f"Template file '{self.template_path}' not found.")
        try:
            with open(self.template_path, 'r') as file:
                self.template = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse the template file: {e}")

    def generate_document(self, data):
        """
        Generates a document by applying data to the template.

        :param data: Dictionary containing the dynamic data to insert into the template.
        :return: Generated document as a string.
        :raises RuntimeError: If no template has been loaded.
        """
        if self.template is None:
            raise RuntimeError("Template not loaded. Call load_template() first.")

        try:
            # Apply data to the template using a simple string replacement approach.
            document = self.template["template_content"].format(**data)
        except KeyError as e:
            raise ValueError(f"Missing required data field: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while generating the document: {e}")

        return document


# Example usage:
if __name__ == "__main__":
    # Path to the template file (example: 'template.json').
    TEMPLATE_PATH = "template.json"

    # Sample dynamic data to populate the template.
    sample_data = {
        "title": "AI-Powered Writing and Formatting",
        "feature_list": "- Natural Language Generation\n- Context-Aware Formatting\n- Advanced Grammar Suggestions",
        "summary": "AutoCaret templates enable streamlined document creation using AI features."
    }

    try:
        # Initialize the template engine.
        template_engine = AutoCaretTemplateEngine(TEMPLATE_PATH)

        # Load the template.
        template_engine.load_template()

        # Generate the document.
        document = template_engine.generate_document(sample_data)
        print("Generated Document:")
        print(document)

    except Exception as e:
        print(f"Error: {e}")
```

**Example Template File (`template.json`):**
```json
{
  "template_content": "Title: {title}\n\nFeatures:\n{feature_list}\n\nSummary:\n{summary}\n"
}
```
