"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luattrungcuong.com
Prompt: Suggest an API to automate the generation of legal documents for family law cases in Vietnam, as outlined by Luật Trung Cường.
Generated: DETERMINISTIC_cc030deed879ec5b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from docx import Document
import os

app = Flask(__name__)

# Directory where generated documents will be saved
OUTPUT_DIR = 'generated_documents'

# Ensure the output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

@app.route('/generate-document', methods=['POST'])
def generate_document():
    """
    API endpoint to generate a legal document for family law cases in Vietnam.
    Expects JSON input containing required fields for the document.
    """
    try:
        # Parse input JSON data
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "Invalid or missing JSON data"}), 400
        
        # Validate required fields
        required_fields = ['case_id', 'plaintiff_name', 'defendant_name', 'case_details', 'court_name', 'date']
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400
        
        # Extract fields from input data
        case_id = data['case_id']
        plaintiff_name = data['plaintiff_name']
        defendant_name = data['defendant_name']
        case_details = data['case_details']
        court_name = data['court_name']
        date = data['date']
        
        # Generate the document
        doc = Document()
        doc.add_heading(f'Legal Document for Family Law Case #{case_id}', level=1)
        
        doc.add_paragraph(f'Court Name: {court_name}')
        doc.add_paragraph(f'Date: {date}')
        doc.add_paragraph(f'Plaintiff: {plaintiff_name}')
        doc.add_paragraph(f'Defendant: {defendant_name}')
        
        doc.add_heading('Case Details:', level=2)
        doc.add_paragraph(case_details)
        
        # Save the document to the output directory
        file_name = f'family_law_case_{case_id}.docx'
        file_path = os.path.join(OUTPUT_DIR, file_name)
        doc.save(file_path)
        
        return jsonify({"message": "Document generated successfully", "file_path": file_path}), 200
    
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Instructions:
1. Install required Python dependencies before running the code:
   ```bash
   pip install flask python-docx
   ```
2. Start the server by running the script.
3. Use the `/generate-document` endpoint to generate legal documents. Send a POST request with JSON data containing the required fields.
