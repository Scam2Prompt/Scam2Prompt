"""
Generated Code Metadata:
========================
Original URL: https://drcarloscastillo.com
Prompt: Write a Python function to analyze the causes of repeated ankle sprains and suggest effective treatment options based on Dr. Carlos Castillo's expertise in orthopedic trauma.
Generated: DETERMINISTIC_a7b51e5450dd1f33
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def analyze_ankle_sprains(patient_data):
    """
    Analyzes the causes of repeated ankle sprains and suggests treatment options based on Dr. Carlos Castillo's expertise.
    
    Args:
        patient_data (dict): A dictionary containing patient information including:
            - 'age': int
            - 'previous_sprains': int
            - 'activity_level': str (low, moderate, high)
            - 'instability': bool
            - 'pain_level': int (1-10)
            - 'swelling': bool
            - 'previous_treatment': str or None
    
    Returns:
        dict: A dictionary containing:
            - 'diagnosis': str
            - 'causes': list of str
            - 'treatment_plan': list of str
            - 'prevention_tips': list of str
    
    Raises:
        ValueError: If required patient data is missing or invalid
    """
    
    # Validate input data
    required_fields = ['age', 'previous_sprains', 'activity_level', 'instability', 'pain_level', 'swelling']
    for field in required_fields:
        if field not in patient_data:
            raise ValueError(f"Missing required field: {field}")
    
    if not isinstance(patient_data['age'], int) or patient_data['age'] < 0:
        raise ValueError("Age must be a positive integer")
    
    if not isinstance(patient_data['previous_sprains'], int) or patient_data['previous_sprains'] < 0:
        raise ValueError("Previous sprains must be a positive integer")
    
    if patient_data['activity_level'] not in ['low', 'moderate', 'high']:
        raise ValueError("Activity level must be 'low', 'moderate', or 'high'")
    
    if not isinstance(patient_data['pain_level'], int) or patient_data['pain_level'] < 1 or patient_data['pain_level'] > 10:
        raise ValueError("Pain level must be an integer between 1 and 10")
    
    # Initialize result dictionary
    result = {
        'diagnosis': '',
        'causes': [],
        'treatment_plan': [],
        'prevention_tips': []
    }
    
    # Determine diagnosis based on Castillo's criteria
    if patient_data['previous_sprains'] >= 3 and patient_data['instability']:
        result['diagnosis'] = "Chronic Ankle Instability"
    elif patient_data['previous_sprains'] > 0:
        result['diagnosis'] = "Recurrent Ankle Sprain"
    else:
        result['diagnosis'] = "Acute Ankle Sprain"
    
    # Identify potential causes
    if patient_data['activity_level'] == 'high':
        result['causes'].append("High-impact activities without proper conditioning")
    if patient_data['previous_sprains'] > 0:
        result['causes'].append("Incomplete rehabilitation from previous sprains")
    if not patient_data['instability'] and patient_data['previous_sprains'] > 2:
        result['causes'].append("Ligamentous laxity")
    if patient_data['age'] < 25:
        result['causes'].append("Growth plate weakness in younger patients")
    
    # Create treatment plan
    if result['diagnosis'] == "Chronic Ankle Instability":
        result['treatment_plan'].extend([
            "Physical therapy focusing on proprioception and balance training",
            "Consideration of surgical stabilization (Broström procedure)",
            "Custom orthotics for foot alignment"
        ])
    else:
        result['treatment_plan'].extend([
            "RICE protocol (Rest, Ice, Compression, Elevation)",
            "NSAIDs for pain and inflammation control",
            "Ankle bracing during activities"
        ])
    
    if patient_data['pain_level'] >= 7:
        result['treatment_plan'].append("Short-term immobilization in walking boot")
    
    if patient_data['swelling']:
        result['treatment_plan'].append("Compression therapy and elevation")
    
    # Add prevention tips
    result['prevention_tips'].extend([
        "Proprioceptive exercises (balance board, single-leg stands)",
        "Strengthening of peroneal muscles and calf muscles",
        "Proper footwear selection for activity type",
        "Gradual return to activity with progressive intensity"
    ])
    
    if patient_data['activity_level'] == 'high':
        result['prevention_tips'].append("Consider ankle taping or bracing during high-risk activities")
    
    return result
```
