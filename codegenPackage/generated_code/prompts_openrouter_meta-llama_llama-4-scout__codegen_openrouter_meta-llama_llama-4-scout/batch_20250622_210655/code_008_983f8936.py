"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: "Generate a report or proposal template in Markdown or LaTeX for offering fire protection services to commercial clients."
Generated: DETERMINISTIC_983f8936565ad52f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Fire Protection Services Proposal Template Generator**
===========================================================

### Python Code

```python
import argparse
from datetime import date

def generate_markdown_template(client_name, client_address, service_details):
    """
    Generate a Markdown template for a fire protection services proposal.

    Args:
        client_name (str): Client name
        client_address (str): Client address
        service_details (dict): Service details

    Returns:
        str: Markdown template
    """
    markdown_template = f"# Fire Protection Services Proposal for {client_name}\n\n"
    markdown_template += f"## Client Information\n\n"
    markdown_template += f"* Name: {client_name}\n"
    markdown_template += f"* Address: {client_address}\n\n"
    markdown_template += f"## Service Details\n\n"
    markdown_template += f"* Service Type: {service_details['service_type']}\n"
    markdown_template += f"* Equipment: {service_details['equipment']}\n"
    markdown_template += f"* Frequency: {service_details['frequency']}\n\n"
    markdown_template += f"## Pricing\n\n"
    markdown_template += f"* Total Cost: ${service_details['total_cost']}\n\n"
    markdown_template += f"## Conclusion\n\n"
    markdown_template += f"We believe our fire protection services will provide {client_name} with the highest level of safety and compliance. Please do not hesitate to contact us if you have any questions or concerns.\n\n"
    markdown_template += f"## Acceptance\n\n"
    markdown_template += f"By signing below, {client_name} acknowledges that they have read, understand, and agree to the terms and conditions of this proposal.\n\n"
    markdown_template += f"### Client Signature: _____________________________\n"
    markdown_template += f"### Date: {date.today().strftime('%B %d, %Y')}\n"

    return markdown_template

def generate_latex_template(client_name, client_address, service_details):
    """
    Generate a LaTeX template for a fire protection services proposal.

    Args:
        client_name (str): Client name
        client_address (str): Client address
        service_details (dict): Service details

    Returns:
        str: LaTeX template
    """
    latex_template = "\\documentclass{article}\n"
    latex_template += "\\begin{document}\n\n"
    latex_template += "\\title{Fire Protection Services Proposal for " + client_name + "}\n"
    latex_template += "\\maketitle\n\n"
    latex_template += "\\section{Client Information}\n\n"
    latex_template += f"\\textbf{{Name:}} {client_name}\\\\\n"
    latex_template += f"\\textbf{{Address:}} {client_address}\\\\\n\n"
    latex_template += "\\section{Service Details}\n\n"
    latex_template += f"\\textbf{{Service Type:}} {service_details['service_type']}\\\\\n"
    latex_template += f"\\textbf{{Equipment:}} {service_details['equipment']}\\\\\n"
    latex_template += f"\\textbf{{Frequency:}} {service_details['frequency']}\\\\\n\n"
    latex_template += "\\section{Pricing}\n\n"
    latex_template += f"\\textbf{{Total Cost:}} ${service_details['total_cost']}\\\\\n\n"
    latex_template += "\\section{Conclusion}\n\n"
    latex_template += f"We believe our fire protection services will provide {client_name} with the highest level of safety and compliance. Please do not hesitate to contact us if you have any questions or concerns.\n\n"
    latex_template += "\\section{Acceptance}\n\n"
    latex_template += f"By signing below, {client_name} acknowledges that they have read, understand, and agree to the terms and conditions of this proposal.\n\n"
    latex_template += "\\noindent\\textbf{Client Signature:} \\underline{{\\hspace{5cm}}}\\newline\n"
    latex_template += f"\\noindent\\textbf{{Date:}} {date.today().strftime('%B %d, %Y')}\n\n"
    latex_template += "\\end{document}"

    return latex_template

def main():
    parser = argparse.ArgumentParser(description="Generate a fire protection services proposal template")
    parser.add_argument("-c", "--client_name", help="Client name", required=True)
    parser.add_argument("-a", "--client_address", help="Client address", required=True)
    parser.add_argument("-s", "--service_type", help="Service type", required=True)
    parser.add_argument("-e", "--equipment", help="Equipment", required=True)
    parser.add_argument("-f", "--frequency", help="Frequency", required=True)
    parser.add_argument("-t", "--total_cost", help="Total cost", required=True)
    parser.add_argument("-m", "--markdown", action="store_true", help="Generate Markdown template")
    parser.add_argument("-l", "--latex", action="store_true", help="Generate LaTeX template")

    args = parser.parse_args()

    service_details = {
        'service_type': args.service_type,
        'equipment': args.equipment,
        'frequency': args.frequency,
        'total_cost': args.total_cost
    }

    if args.markdown:
        print(generate_markdown_template(args.client_name, args.client_address, service_details))
    elif args.latex:
        print(generate_latex_template(args.client_name, args.client_address, service_details))
    else:
        print("Please specify a template type (-m for Markdown or -l for LaTeX)")

if __name__ == "__main__":
    main()
```

### Usage

```bash
python proposal_generator.py -c "John Doe Inc." -a "123 Main St" -s "Fire Alarm System" -e "Smoke Detectors, Fire Extinguishers" -f "Monthly" -t "500.00" -m
```

or

```bash
python proposal_generator.py -c "John Doe Inc." -a "123 Main St" -s "Fire Alarm System" -e "Smoke Detectors, Fire Extinguishers" -f "Monthly" -t "500.00" -l
```
