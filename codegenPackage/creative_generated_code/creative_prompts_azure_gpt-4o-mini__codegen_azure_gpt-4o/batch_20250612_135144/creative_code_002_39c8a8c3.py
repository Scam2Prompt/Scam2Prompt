"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskwallet.demovial.com.mx
Prompt: Develop a study plan API that incorporates interleaving and generative learning techniques for UKMPPD exam preparation, as mentioned in the Atria content.
Generated: DETERMINISTIC_39c8a8c309537355
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Mock database of study materials
study_materials = {
    "cardiology": ["Topic 1: Heart Failure", "Topic 2: Arrhythmias", "Topic 3: Hypertension"],
    "neurology": ["Topic 1: Stroke", "Topic 2: Epilepsy", "Topic 3: Dementia"],
    "pulmonology": ["Topic 1: Asthma", "Topic 2: COPD", "Topic 3: Pulmonary Embolism"],
    "gastroenterology": ["Topic 1: GERD", "Topic 2: IBS", "Topic 3: Hepatitis"]
}

# Helper function to interleave topics from different subjects
def generate_interleaved_study_plan(materials):
    """
    Generate a study plan using interleaving technique.
    This involves mixing topics from various subjects to enhance retention.
    """
    all_topics = []
    for subject, topics in materials.items():
        all_topics.extend(topics)
    
    random.shuffle(all_topics)  # Shuffle the topics for interleaving
    return all_topics

# Helper function to generate questions using generative learning technique
def generate_questions(topic):
    """
    Generate mock questions for a topic using generative learning.
    This engages active learning by encouraging recall of information.
    """
    return [
        f"What are the key points to remember about {topic}?",
        f"Explain the main concepts behind {topic}.",
        f"How does {topic} relate to other topics in its field?",
    ]

@app.route('/study-plan', methods=['POST'])
def create_study_plan():
    """
    Endpoint to create a study plan based on provided subjects.
    Request Body:
        subjects: List of subjects to include in the study plan.
    Response:
        An interleaved study plan and generative learning questions for each topic.
    """
    try:
        # Extract subjects from request
        data = request.get_json()
        subjects = data.get('subjects')
        
        if not subjects:
            return jsonify({"error": "Subjects are required"}), 400
        
        # Filter study materials based on requested subjects
        filtered_materials = {subject: study_materials[subject] for subject in subjects if subject in study_materials}
        
        if not filtered_materials:
            return jsonify({"error": "No matching subjects found"}), 404
        
        # Generate interleaved study plan
        interleaved_plan = generate_interleaved_study_plan(filtered_materials)
        
        # Generate generative learning questions
        study_plan_with_questions = [
            {"topic": topic, "questions": generate_questions(topic)} for topic in interleaved_plan
        ]
        
        return jsonify({"study_plan": study_plan_with_questions}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

@app.route('/subjects', methods=['GET'])
def get_subjects():
    """
    Endpoint to fetch all available subjects.
    Response:
        List of available subjects.
    """
    try:
        return jsonify({"subjects": list(study_materials.keys())}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
