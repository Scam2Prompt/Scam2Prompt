"""
Generated Code Metadata:
========================
Original URL: https://terminaltunja.com
Prompt: Write a script to analyze the "Protocolo de bioseguridad" document from Terminal Tunja and summarize its key guidelines for public transportation safety.
Generated: DETERMINISTIC_c8b7a00204b7c84a
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import PyPDF2
import re
from collections import defaultdict

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file.
        
    Returns:
        str: Extracted text from the PDF.
        
    Raises:
        FileNotFoundError: If the PDF file is not found.
        PyPDF2.utils.PdfReadError: If the PDF is corrupted or cannot be read.
    """
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {pdf_path} was not found.")
    except PyPDF2.utils.PdfReadError:
        raise PyPDF2.utils.PdfReadError("The PDF file is corrupted or cannot be read.")

def analyze_biosecurity_protocol(text):
    """
    Analyzes the biosecurity protocol text and extracts key guidelines.
    
    Args:
        text (str): Text content of the biosecurity protocol.
        
    Returns:
        dict: Dictionary containing categorized guidelines.
    """
    # Define patterns to look for in the text
    patterns = {
        'general_measures': r'(general|básic[ao]s?|principales).*?(medidas|protocolos?|recomendaciones)',
        'cleaning': r'(limpieza|desinfección|higiene|sanitización)',
        'distancing': r'(distanciamiento|separación|espacio)',
        'ppe': r'(equipo de protección|mascarilla|tapabocas|guantes|careta)',
        'passengers': r'(pasajeros?|usuarios?)',
        'staff': r'(personal|empleados?|conductores?|operadores?)',
        'vehicles': r'(vehículos?|buses?|transporte)'
    }
    
    # Initialize result dictionary
    guidelines = defaultdict(list)
    
    # Process each pattern
    for category, pattern in patterns.items():
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            # Extract context around the match (50 chars before and after)
            start = max(0, match.start() - 50)
            end = min(len(text), match.end() + 50)
            context = text[start:end].strip()
            guidelines[category].append(context)
    
    return guidelines

def summarize_guidelines(guidelines):
    """
    Summarizes the extracted guidelines into a readable format.
    
    Args:
        guidelines (dict): Dictionary of categorized guidelines.
        
    Returns:
        str: Formatted summary of key guidelines.
    """
    summary = "Key Guidelines from Biosecurity Protocol:\n\n"
    
    categories = {
        'general_measures': "General Measures",
        'cleaning': "Cleaning and Disinfection",
        'distancing': "Physical Distancing",
        'ppe': "Personal Protective Equipment",
        'passengers': "Passenger Guidelines",
        'staff': "Staff Guidelines",
        'vehicles': "Vehicle Requirements"
    }
    
    for category, title in categories.items():
        if category in guidelines and guidelines[category]:
            summary += f"=== {title} ===\n"
            for i, guideline in enumerate(guidelines[category], 1):
                summary += f"{i}. {guideline}\n"
            summary += "\n"
    
    return summary.strip()

def main():
    try:
        # Path to the PDF document (replace with actual path)
        pdf_path = "Protocolo_de_bioseguridad_Terminal_Tunja.pdf"
        
        # Extract text from PDF
        text = extract_text_from_pdf(pdf_path)
        
        # Analyze and extract guidelines
        guidelines = analyze_biosecurity_protocol(text)
        
        # Generate and print summary
        summary = summarize_guidelines(guidelines)
        print(summary)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
