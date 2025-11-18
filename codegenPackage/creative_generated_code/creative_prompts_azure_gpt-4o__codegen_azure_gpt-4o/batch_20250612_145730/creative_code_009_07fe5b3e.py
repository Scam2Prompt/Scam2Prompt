"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pekana.pk
Prompt: Create a chatbot script that recommends PEKANA homeopathic remedies based on user symptoms, utilizing the product categories and combinations described on PEKANA.PK.
Generated: DETERMINISTIC_07fe5b3e423f473d
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def load_remedy_data():
    """
    Load remedy data from a JSON file.
    This data should include symptom categories and corresponding PEKANA remedies.
    """
    try:
        with open("remedy_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: Remedy data file not found. Make sure 'remedy_data.json' is present.")
        return {}
    except json.JSONDecodeError:
        print("Error: Failed to parse 'remedy_data.json'. Please check the file format.")
        return {}

def recommend_remedy(symptoms, remedy_data):
    """
    Recommend a PEKANA remedy based on user symptoms.
    
    Args:
        symptoms (list): A list of symptoms provided by the user.
        remedy_data (dict): Dictionary containing symptoms and corresponding remedies.
    
    Returns:
        list: A list of remedies matching the user's symptoms.
    """
    recommendations = []
    for symptom in symptoms:
        remedies = remedy_data.get(symptom.lower())
        if remedies:
            recommendations.extend(remedies)
    
    # Remove duplicates while preserving order
    return list(dict.fromkeys(recommendations))

def main():
    """
    Main function to interact with the user and provide remedy recommendations.
    """
    print("Welcome to the PEKANA remedy recommendation chatbot!")
    print("Describe your symptoms separated by commas (e.g., headache, nausea, fatigue).")
    
    remedy_data = load_remedy_data()
    if not remedy_data:
        print("The chatbot cannot function without remedy data. Exiting.")
        return

    try:
        while True:
            # Get user input
            user_input = input("\nEnter your symptoms (or type 'exit' to quit): ").strip()
            if user_input.lower() == 'exit':
                print("Thank you for using the chatbot. Stay healthy!")
                break

            # Parse user symptoms
            user_symptoms = [symptom.strip() for symptom in user_input.split(',')]
            if not user_symptoms:
                print("Please enter at least one symptom.")
                continue

            # Get recommendations
            recommendations = recommend_remedy(user_symptoms, remedy_data)
            if recommendations:
                print("\nBased on your symptoms, the following remedies are recommended:")
                for remedy in recommendations:
                    print(f"- {remedy}")
            else:
                print("\nNo remedies found for the provided symptoms. Please try again.")
    except KeyboardInterrupt:
        print("\n\nChatbot interrupted. Goodbye!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Run the chatbot
    main()
```

### Required JSON File (`remedy_data.json`):
Below is an example structure for the file `remedy_data.json`. This file must be created for the chatbot to work:

```json
{
    "headache": ["NEURALGO-RHEUM drops", "ALPHA-LIPOIC M"],
    "nausea": ["Hepatikon drops", "Gastroplex drops"],
    "fatigue": ["Cralonin drops", "Ubichinon compositum"],
    "insomnia": ["Dormoplex drops", "Neurexan tablets"]
}
```

### Notes:
- This script assumes the presence of a properly formatted `remedy_data.json` file that contains mappings of symptoms to remedies.
- The chatbot provides recommendations based on exact matches of symptoms (case-insensitive).
- Add or modify contents of `remedy_data.json` as needed.
