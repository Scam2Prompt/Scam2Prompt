"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.xxcw51.com
Prompt: Write a program to generate a custom internship report template based on the examples in "精选印刷实习报告四篇" from xxcw51.com.
Generated: DETERMINISTIC_252fe68b601193da
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from jinja2 import Environment, FileSystemLoader

# Set up the Jinja2 environment to load templates from the current directory
env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))

# Define a function to generate an internship report
def generate_internship_report(internship_data, template_name='internship_report_template.html'):
    """
    Generate a custom internship report based on provided data.

    Args:
        internship_data (dict): A dictionary containing internship details.
        template_name (str): The name of the template file to use for generating the report.

    Raises:
        FileNotFoundError: If the specified template file does not exist.
        KeyError: If required data keys are missing in the internship_data.

    Returns:
        str: Rendered HTML report as a string.
    """
    try:
        # Load the specified template
        template = env.get_template(template_name)
    except Exception as e:
        raise FileNotFoundError(f"Template '{template_name}' could not be loaded: {e}")

    # Check for required keys in the internship data
    required_keys = ['intern_name', 'company_name', 'duration', 'tasks']
    for key in required_keys:
        if key not in internship_data:
            raise KeyError(f"Missing required data key: '{key}'")

    # Render the template with the provided internship data
    report_html = template.render(internship_data)
    
    return report_html

# Sample data for the internship report
internship_data = {
    'intern_name': '张三',
    'company_name': 'XX科技有限公司',
    'duration': '2023年7月 - 2023年8月',
    'tasks': [
        '参与项目开发',
        '撰写项目文档',
        '进行市场调研'
    ]
}

# Generate the report and save it to a file
def save_report(report_html, filename='internship_report.html'):
    """
    Save the generated HTML report to a file.

    Args:
        report_html (str): The HTML content of the report.
        filename (str): The name of the file to save the report to.

    Raises:
        IOError: If there is an issue writing to the file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(report_html)
    except Exception as e:
        raise IOError(f"Error saving report to '{filename}': {e}")

if __name__ == '__main__':
    try:
        # Generate the internship report
        report = generate_internship_report(internship_data)
        
        # Save the report to an HTML file
        save_report(report)
        print("Internship report generated successfully: 'internship_report.html'")
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Note: 
- You would need to create a Jinja2 template file named `internship_report_template.html` in the same directory as this script. The template should contain placeholders for `intern_name`, `company_name`, `duration`, and `tasks` to render the report correctly.
