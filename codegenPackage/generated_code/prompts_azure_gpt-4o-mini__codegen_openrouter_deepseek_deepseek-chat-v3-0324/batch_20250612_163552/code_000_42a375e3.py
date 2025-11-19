"""
Generated Code Metadata:
========================
Original URL: https://sandiegosleepandtmjcenter.com
Prompt: Generate a Python function that suggests non-surgical treatments for sleep apnea based on the unique services offered by the San Diego Sleep and TMJ Center.
Generated: DETERMINISTIC_42a375e398fe38c8
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def suggest_non_surgical_treatments(symptoms, preferences=None):
    """
    Suggests non-surgical treatments for sleep apnea based on symptoms and patient preferences.
    Treatments are modeled after the unique services offered by the San Diego Sleep and TMJ Center.

    Args:
        symptoms (dict): A dictionary containing the patient's symptoms. Expected keys:
            - 'apnea_severity': str, one of ['mild', 'moderate', 'severe']
            - 'tmj_pain': bool, whether the patient experiences TMJ pain
            - 'claustrophobia': bool, whether the patient has claustrophobia
            - 'bruxism': bool, whether the patient grinds teeth
        preferences (dict, optional): Patient preferences. Expected keys:
            - 'comfort': str, one of ['high', 'medium', 'low']
            - 'lifestyle': list, e.g., ['travel_friendly', 'minimal_maintenance']

    Returns:
        dict: A dictionary of recommended treatments with their descriptions.
              Returns None if no treatments are suitable.
    """
    
    # Define available treatments and their criteria
    treatments = {
        'oral_appliance_therapy': {
            'description': 'Custom-fitted oral appliance that repositions the jaw to keep the airway open.',
            'criteria': {
                'apnea_severity': ['mild', 'moderate'],
                'tmj_pain': False,
                'claustrophobia': None,  # No relevance
                'bruxism': None,  # Can be managed with additional features
            },
            'comfort': 'high',
            'lifestyle': ['travel_friendly', 'minimal_maintenance']
        },
        'cpap_alternative_therapy': {
            'description': 'Non-CPAP pressure therapy devices that are less intrusive than traditional CPAP.',
            'criteria': {
                'apnea_severity': ['moderate', 'severe'],
                'tmj_pain': None,
                'claustrophobia': False,
                'bruxism': None,
            },
            'comfort': 'medium',
            'lifestyle': ['travel_friendly']
        },
        'positional_therapy': {
            'description': 'Devices or techniques to encourage side-sleeping to reduce apnea events.',
            'criteria': {
                'apnea_severity': ['mild'],
                'tmj_pain': None,
                'claustrophobia': None,
                'bruxism': None,
            },
            'comfort': 'high',
            'lifestyle': ['travel_friendly', 'minimal_maintenance']
        },
        'tmj_sleep_appliance': {
            'description': 'Specialized oral appliance that addresses both sleep apnea and TMJ pain.',
            'criteria': {
                'apnea_severity': ['mild', 'moderate'],
                'tmj_pain': True,
                'claustrophobia': None,
                'bruxism': True,
            },
            'comfort': 'high',
            'lifestyle': ['travel_friendly']
        },
        'combination_therapy': {
            'description': 'Combination of oral appliance and positional therapy for enhanced results.',
            'criteria': {
                'apnea_severity': ['moderate', 'severe'],
                'tmj_pain': None,
                'claustrophobia': None,
                'bruxism': None,
            },
            'comfort': 'medium',
            'lifestyle': ['travel_friendly']
        }
    }

    # Validate input symptoms
    required_symptoms = ['apnea_severity', 'tmj_pain', 'claustrophobia', 'bruxism']
    if not all(key in symptoms for key in required_symptoms):
        raise ValueError(f"Missing required symptoms. Expected: {required_symptoms}")

    if symptoms['apnea_severity'] not in ['mild', 'moderate', 'severe']:
        raise ValueError("apnea_severity must be one of: 'mild', 'moderate', 'severe'")

    # Filter treatments based on symptoms
    recommended = {}
    for name, treatment in treatments.items():
        criteria = treatment['criteria']
        match = True

        # Check symptom criteria
        if (criteria['apnea_severity'] is not None and 
            symptoms['apnea_severity'] not in criteria['apnea_severity']):
            match = False
        if (criteria['tmj_pain'] is not None and 
            symptoms['tmj_pain'] != criteria['tmj_pain']):
            match = False
        if (criteria['claustrophobia'] is not None and 
            symptoms['claustrophobia'] != criteria['claustrophobia']):
            match = False
        if (criteria['bruxism'] is not None and 
            symptoms['bruxism'] != criteria['bruxism']):
            match = False

        if match:
            recommended[name] = {
                'description': treatment['description'],
                'comfort': treatment['comfort'],
                'lifestyle': treatment['lifestyle']
            }

    # Further filter by preferences if provided
    if preferences:
        filtered_recommended = {}
        for name, treatment in recommended.items():
            pref_match = True

            if 'comfort' in preferences:
                if preferences['comfort'] == 'high' and treatment['comfort'] != 'high':
                    pref_match = False
                elif preferences['comfort'] == 'medium' and treatment['comfort'] == 'low':
                    pref_match = False

            if 'lifestyle' in preferences:
                if not all(pref in treatment['lifestyle'] for pref in preferences['lifestyle']):
                    pref_match = False

            if pref_match:
                filtered_recommended[name] = treatment

        recommended = filtered_recommended

    return recommended if recommended else None
```
