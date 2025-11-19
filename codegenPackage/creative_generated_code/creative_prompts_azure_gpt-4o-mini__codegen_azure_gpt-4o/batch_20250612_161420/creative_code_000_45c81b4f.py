"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ohibo.it
Prompt: Generate a web design project proposal for a branding agency similar to OHIBÒ, focusing on brand identity and social media management.
Generated: DETERMINISTIC_45c81b4f15cfa09d
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s Python code implementing a script to generate a web design project proposal for a branding agency, focusing on brand identity and social media management. The script utilizes Python's `jinja2` library for templating to create a dynamic proposal generator.

```python
import os
from jinja2 import Environment, FileSystemLoader

def generate_proposal(client_name, client_description, services, deadline, contact_info):
    """
    Generates a web design project proposal as an HTML file.
    
    Args:
        client_name (str): The name of the client.
        client_description (str): A brief description of the client and their needs.
        services (list): A list of services included in the proposal.
        deadline (str): The proposed deadline for project completion.
        contact_info (dict): Dictionary containing contact information (e.g., email, phone).
    
    Returns:
        str: Path to the generated proposal file.
    """
    
    # Define the directory containing the template
    template_dir = 'templates'
    os.makedirs(template_dir, exist_ok=True)
    
    # Create a basic HTML template for the proposal if it doesn't exist
    template_path = os.path.join(template_dir, 'proposal_template.html')
    if not os.path.exists(template_path):
        with open(template_path, 'w') as template_file:
            template_file.write("""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Project Proposal</title>
                <style>
                    body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
                    h1, h2 { color: #333; }
                    ul { margin: 15px 0; padding-left: 20px; }
                    li { margin-bottom: 10px; }
                    .contact-info { margin-top: 20px; }
                </style>
            </head>
            <body>
                <h1>Project Proposal for {{ client_name }}</h1>
                <p><strong>Client Description:</strong> {{ client_description }}</p>
                <h2>Proposed Services</h2>
                <ul>
                    {% for service in services %}
                        <li>{{ service }}</li>
                    {% endfor %}
                </ul>
                <p><strong>Deadline:</strong> {{ deadline }}</p>
                <div class="contact-info">
                    <h2>Contact Information</h2>
                    <p><strong>Email:</strong> {{ contact_info.email }}</p>
                    <p><strong>Phone:</strong> {{ contact_info.phone }}</p>
                </div>
            </body>
            </html>
            """)
    
    # Load the template file
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('proposal_template.html')
    
    # Render the template with provided data
    rendered_html = template.render(
        client_name=client_name,
        client_description=client_description,
        services=services,
        deadline=deadline,
        contact_info=contact_info
    )
    
    # Save the rendered proposal as an HTML file
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    proposal_path = os.path.join(output_dir, f"{client_name}_proposal.html")
    with open(proposal_path, 'w') as proposal_file:
        proposal_file.write(rendered_html)
    
    return proposal_path

if __name__ == "__main__":
    # Example usage
    try:
        proposal_file = generate_proposal(
            client_name="OHIBÒ Branding Agency",
            client_description="A creative agency focused on brand identity and social media management.",
            services=[
                "Comprehensive brand strategy development",
                "Logo and visual identity design",
                "Social media content creation and management",
                "Brand voice and messaging guidelines"
            ],
            deadline="2023-12-31",
            contact_info={
                "email": "contact@ohiboagency.com",
                "phone": "+123456789"
            }
        )
        print(f"Proposal generated successfully: {proposal_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Instructions:
1. Install the `jinja2` library using `pip install jinja2` if it’s not already installed.
2. Run the script to dynamically generate an HTML proposal file (`OHIBÒ Branding Agency_proposal.html`) in the `output` directory. The template and output directories are automatically created.
3. Open the generated HTML file in a browser to view the proposal.
