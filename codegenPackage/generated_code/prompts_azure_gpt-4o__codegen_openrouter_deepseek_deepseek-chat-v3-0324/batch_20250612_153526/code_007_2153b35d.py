"""
Generated Code Metadata:
========================
Original URL: https://kiberahamlets.org
Prompt: Create a chatbot using natural language processing that answers questions about Kibera Hamlets' programs, such as education initiatives ("Somesha") or environmental conservation efforts.
Generated: DETERMINISTIC_2153b35d7ed82cb0
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
import spacy
from spacy.matcher import PhraseMatcher
from flask import Flask, request, jsonify

# Load the NLP model
nlp = spacy.load("en_core_web_sm")

# Initialize Flask app
app = Flask(__name__)

# Knowledge base for Kibera Hamlets programs
PROGRAMS_KB = {
    "education": {
        "name": "Somesha Education Initiative",
        "description": "Provides quality education to underprivileged children in Kibera through school sponsorships, teacher training, and learning materials.",
        "impact": "Over 500 children enrolled in schools annually with improved academic performance.",
        "contact": "education@kiberahamlets.org"
    },
    "environment": {
        "name": "Green Kibera Initiative",
        "description": "Focuses on environmental conservation through waste management, tree planting, and community awareness programs.",
        "impact": "Planted over 10,000 trees and established 20 community waste collection points.",
        "contact": "environment@kiberahamlets.org"
    },
    "health": {
        "name": "Afya Bora Health Program",
        "description": "Improves community health through medical camps, hygiene education, and disease prevention programs.",
        "impact": "Conducts monthly medical camps serving 200+ residents.",
        "contact": "health@kiberahamlets.org"
    }
}

# Initialize phrase matcher for program names
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
program_patterns = [nlp.make_doc(program) for program in ["somesha", "education", "environment", "health", "green kibera", "afya bora"]]
matcher.add("PROGRAMS", program_patterns)

def extract_program_key(query: str) -> Optional[str]:
    """
    Extract the most relevant program key from user query.
    """
    doc = nlp(query.lower())
    matches = matcher(doc)
    
    if not matches:
        return None
    
    # Get the matched span and determine program
    matched_span = doc[matches[0][1]:matches[0][2]]
    matched_text = matched_span.text.lower()
    
    if "somesha" in matched_text or "education" in matched_text:
        return "education"
    elif "environment" in matched_text or "green" in matched_text:
        return "environment"
    elif "health" in matched_text or "afya" in matched_text:
        return "health"
    return None

def generate_response(program_key: Optional[str], query: str) -> Dict[str, str]:
    """
    Generate appropriate response based on detected program and query intent.
    """
    if not program_key:
        return {
            "response": "I can provide information about Kibera Hamlets' programs including education (Somesha), environmental conservation, and health initiatives. Could you specify which program you're interested in?",
            "suggestions": ["Tell me about Somesha", "What environmental programs exist?", "How does the health program work?"]
        }
    
    program = PROGRAMS_KB[program_key]
    doc = nlp(query.lower())
    
    # Check for specific information requests
    if any(token.text in ["impact", "result", "achievement"] for token in doc):
        return {
            "response": f"The {program['name']} has achieved: {program['impact']}",
            "contact": program["contact"]
        }
    elif any(token.text in ["contact", "email", "reach"] for token in doc):
        return {
            "response": f"For more information about {program['name']}, please contact: {program['contact']}"
        }
    else:
        return {
            "response": f"{program['name']}: {program['description']}",
            "more_info": f"Impact: {program['impact']}",
            "contact": program["contact"]
        }

@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint to handle chat requests.
    """
    try:
        data = request.get_json()
        if not data or 'query' not in data:
            return jsonify({"error": "Invalid request format"}), 400
        
        query = data['query']
        program_key = extract_program_key(query)
        response = generate_response(program_key, query)
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```
