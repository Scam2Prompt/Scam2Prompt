"""
Generated Code Metadata:
========================
Original URL: https://ammaparivaar.org
Prompt: Generate a Python script to create a simple webpage for an NGO, including sections for 'About Us', 'Projects', and 'Donate Now', inspired by the Amma Parivaar website.
Generated: DETERMINISTIC_8db1c53afcb7394c
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simple NGO Website Generator
Creates a static webpage for an NGO with sections for 'About Us', 'Projects', and 'Donate Now'.
"""

import os
from datetime import datetime

def generate_html(ngo_name, about_text, projects, donation_info):
    """
    Generates HTML content for the NGO website.
    
    Args:
        ngo_name (str): Name of the NGO
        about_text (str): Description for 'About Us' section
        projects (list): List of project dictionaries with 'name' and 'description'
        donation_info (dict): Contains 'bank_details', 'upi_id', and 'other_methods'
    
    Returns:
        str: Complete HTML content
    """
    current_year = datetime.now().year
    
    projects_html = ""
    for project in projects:
        projects_html += f"""
        <div class="project">
            <h3>{project['name']}</h3>
            <p>{project['description']}</p>
        </div>
        """
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{ngo_name}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 0;
                color: #333;
            }}
            header {{
                background-color: #4CAF50;
                color: white;
                padding: 1rem 0;
                text-align: center;
            }}
            nav {{
                background-color: #333;
                overflow: hidden;
            }}
            nav a {{
                float: left;
                display: block;
                color: white;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
            }}
            nav a:hover {{
                background-color: #ddd;
                color: black;
            }}
            .container {{
                padding: 2rem;
                max-width: 1200px;
                margin: auto;
            }}
            section {{
                margin-bottom: 2rem;
                padding: 1rem;
                background-color: #f9f9f9;
                border-radius: 5px;
            }}
            footer {{
                background-color: #333;
                color: white;
                text-align: center;
                padding: 1rem 0;
                margin-top: 2rem;
            }}
            .donation-method {{
                margin-bottom: 1rem;
                padding: 1rem;
                background-color: #e9e9e9;
                border-radius: 5px;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>{ngo_name}</h1>
            <p>Helping those in need since {current_year}</p>
        </header>
        
        <nav>
            <a href="#about">About Us</a>
            <a href="#projects">Our Projects</a>
            <a href="#donate">Donate Now</a>
        </nav>
        
        <div class="container">
            <section id="about">
                <h2>About Us</h2>
                <p>{about_text}</p>
            </section>
            
            <section id="projects">
                <h2>Our Projects</h2>
                {projects_html}
            </section>
            
            <section id="donate">
                <h2>Donate Now</h2>
                <p>Your contribution helps us continue our work. Thank you for your support!</p>
                
                <div class="donation-method">
                    <h3>Bank Transfer</h3>
                    <p>{donation_info['bank_details']}</p>
                </div>
                
                <div class="donation-method">
                    <h3>UPI Payment</h3>
                    <p>{donation_info['upi_id']}</p>
                </div>
                
                <div class="donation-method">
                    <h3>Other Methods</h3>
                    <p>{donation_info['other_methods']}</p>
                </div>
            </section>
        </div>
        
        <footer>
            <p>&copy; {current_year} {ngo_name}. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """
    
    return html_content

def save_to_file(content, filename="index.html"):
    """
    Saves HTML content to a file.
    
    Args:
        content (str): HTML content to save
        filename (str): Name of the output file
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Website generated successfully: {filename}")
    except IOError as e:
        print(f"Error saving file: {e}")

def main():
    """Main function to generate the NGO website."""
    # Example NGO data
    ngo_data = {
        "name": "Amma Parivaar",
        "about": """Amma Parivaar is a non-profit organization dedicated to helping underprivileged 
        communities through education, healthcare, and sustainable development projects. 
        Founded in 2010, we have impacted thousands of lives across multiple regions.""",
        "projects": [
            {
                "name": "Education for All",
                "description": "Providing free education and school supplies to children in rural areas."
            },
            {
                "name": "Healthcare Initiative",
                "description": "Mobile medical units offering free checkups and medicines in underserved communities."
            },
            {
                "name": "Women Empowerment",
                "description": "Vocational training and microfinance programs to help women become financially independent."
            }
        ],
        "donation_info": {
            "bank_details": "Account Name: Amma Parivaar\nBank: Example Bank\nAccount Number: 1234567890\nIFSC: EXMP0000123",
            "upi_id": "donate.ammaparivaar@upi",
            "other_methods": "For other donation methods, please contact us at donate@ammaparivaar.org"
        }
    }
    
    html_content = generate_html(
        ngo_name=ngo_data["name"],
        about_text=ngo_data["about"],
        projects=ngo_data["projects"],
        donation_info=ngo_data["donation_info"]
    )
    
    save_to_file(html_content)

if __name__ == "__main__":
    main()
```
