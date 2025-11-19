"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Write Python code to automate the generation of legal correspondence templates based on the concepts outlined in the "Manual de Correspondência Jurídica" from the Complexo de Advocacia Adriano Geoffrey.
Generated: DETERMINISTIC_c7716d338efe0415
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

class LegalCorrespondenceGenerator:
    """
    A class to generate legal correspondence templates based on predefined formats.
    """

    def __init__(self, template_dir):
        """
        Initializes the generator with the directory containing templates.

        :param template_dir: Directory where the correspondence templates are stored.
        """
        self.template_dir = template_dir
        self.env = Environment(
            loader=FileSystemLoader(self.template_dir),
            autoescape=select_autoescape(['html', 'xml'])
        )

    def load_template(self, template_name):
        """
        Loads a template by name.

        :param template_name: The name of the template file to load.
        :return: The loaded template.
        :raises FileNotFoundError: If the template does not exist.
        """
        try:
            return self.env.get_template(template_name)
        except Exception as e:
            raise FileNotFoundError(f"Template '{template_name}' not found: {e}")

    def generate_correspondence(self, template_name, context):
        """
        Generates correspondence from a template with the provided context.

        :param template_name: The name of the template file to use.
        :param context: A dictionary containing the data to render the template.
        :return: The rendered correspondence as a string.
        :raises FileNotFoundError: If the template does not exist.
        """
        template = self.load_template(template_name)
        return template.render(context)

    def save_to_file(self, content, output_path):
        """
        Saves the generated content to a specified file.

        :param content: The content to save.
        :param output_path: The path where the content will be saved.
        :raises IOError: If there is an error writing to the file.
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(content)
        except IOError as e:
            raise IOError(f"Error writing to file '{output_path}': {e}")

def main():
    """
    Main function to execute the legal correspondence generation.
    """
    template_directory = 'templates'  # Directory containing the correspondence templates
    output_directory = 'output'        # Directory to save generated correspondence

    # Ensure output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Create an instance of the generator
    generator = LegalCorrespondenceGenerator(template_directory)

    # Define the context for the correspondence
    context = {
        'client_name': 'John Doe',
        'case_number': '12345/2023',
        'date': '2023-10-01',
        'body': 'This is a sample body of the legal correspondence.'
    }

    # Specify the template name
    template_name = 'legal_template.txt'  # Example template file

    try:
        # Generate the correspondence
        correspondence = generator.generate_correspondence(template_name, context)

        # Define output file path
        output_file_path = os.path.join(output_directory, 'correspondence_output.txt')

        # Save the generated correspondence to a file
        generator.save_to_file(correspondence, output_file_path)

        print(f"Correspondence generated successfully: {output_file_path}")

    except (FileNotFoundError, IOError) as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
```

**Note:** Ensure that you have the `jinja2` library installed in your Python environment. You can install it using pip:

```bash
pip install jinja2
```

Also, create a directory named `templates` and place a template file named `legal_template.txt` inside it for the code to work correctly. The template file should contain placeholders for the context variables (e.g., `{{ client_name }}`, `{{ case_number }}`, etc.).
