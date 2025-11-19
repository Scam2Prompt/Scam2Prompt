"""
Generated Code Metadata:
========================
Original URL: https://trysonicsolutions.com
Prompt: Generate a checklist for determining whether to use ultrasonic cleaning or jet washing for different types of industrial parts.
Generated: DETERMINISTIC_d561d6584816c80e
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CleaningMethodChecklist:
    """
    A checklist to determine whether to use ultrasonic cleaning or jet washing for industrial parts.
    """
    
    def __init__(self):
        self.questions = [
            {
                'question': 'Is the part delicate or have intricate geometries?',
                'yes': 'ultrasonic',
                'no': None
            },
            {
                'question': 'Does the part have blind holes or hard-to-reach areas?',
                'yes': 'ultrasonic',
                'no': None
            },
            {
                'question': 'Is the contamination light to moderate (e.g., oils, dust)?',
                'yes': 'ultrasonic',
                'no': None
            },
            {
                'question': 'Is the part large and bulky?',
                'yes': 'jet_washing',
                'no': None
            },
            {
                'question': 'Is the contamination heavy (e.g., grease, scale, rust)?',
                'yes': 'jet_washing',
                'no': None
            },
            {
                'question': 'Is the part made of sturdy material that can withstand high pressure?',
                'yes': 'jet_washing',
                'no': 'ultrasonic'
            },
            {
                'question': 'Is quick drying required after cleaning?',
                'yes': 'jet_washing',
                'no': None
            },
            {
                'question': 'Is the part sensitive to high temperatures?',
                'yes': 'ultrasonic',
                'no': None
            }
        ]
    
    def determine_cleaning_method(self):
        """
        Runs through the checklist to determine the appropriate cleaning method.
        
        Returns:
            str: Recommended cleaning method ('ultrasonic', 'jet_washing', or 'undetermined')
        """
        ultrasonic_score = 0
        jet_washing_score = 0
        
        for item in self.questions:
            print(f"\n{item['question']} (y/n)")
            while True:
                answer = input().strip().lower()
                if answer in ('y', 'n'):
                    break
                print("Please enter 'y' for yes or 'n' for no.")
            
            if answer == 'y' and item['yes']:
                if item['yes'] == 'ultrasonic':
                    ultrasonic_score += 1
                else:
                    jet_washing_score += 1
            elif answer == 'n' and item.get('no'):
                if item['no'] == 'ultrasonic':
                    ultrasonic_score += 1
                else:
                    jet_washing_score += 1
        
        if ultrasonic_score > jet_washing_score:
            return 'ultrasonic'
        elif jet_washing_score > ultrasonic_score:
            return 'jet_washing'
        else:
            return 'undetermined'
    
    def print_recommendation(self, method):
        """
        Prints the final recommendation based on the determined method.
        
        Args:
            method (str): The cleaning method determined by the checklist
        """
        recommendations = {
            'ultrasonic': "Recommended cleaning method: Ultrasonic Cleaning",
            'jet_washing': "Recommended cleaning method: Jet Washing",
            'undetermined': "Unable to determine clear recommendation. Consider both methods or consult an expert."
        }
        print("\n" + recommendations.get(method, "Invalid recommendation"))


if __name__ == "__main__":
    try:
        checklist = CleaningMethodChecklist()
        method = checklist.determine_cleaning_method()
        checklist.print_recommendation(method)
    except Exception as e:
        print(f"An error occurred: {e}")
```
