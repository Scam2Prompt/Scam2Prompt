"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Create a Python script to automate the generation of safety recommendations for accessing rooftops securely, inspired by AFCO's guidelines on preventing falls from heights.
Generated: DETERMINISTIC_ef3ba8022ad42fe3
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# safety_recommendations.py

"""
Generate safety recommendations for accessing rooftops securely based on AFCO's guidelines on preventing falls from heights.
"""

import argparse

def get_safety_recommendations(rooftop_type, access_method):
    """
    Returns a list of safety recommendations for accessing a rooftop.

    Args:
        rooftop_type (str): Type of rooftop (e.g., flat, sloping, irregular)
        access_method (str): Method of accessing the rooftop (e.g., ladder, stairs, scaffolding)

    Returns:
        list: List of safety recommendations
    """

    # Define safety recommendations based on rooftop type and access method
    recommendations = {
        'flat': {
            'ladder': [
                'Ensure the ladder is securely positioned and levelled.',
                'Use a ladder stabilizer or have someone hold the ladder for added stability.',
                'Always maintain three points of contact with the ladder (two hands and one foot, or two feet and one hand).'
            ],
            'stairs': [
                'Ensure stairs are well-maintained and free of obstacles.',
                'Use handrails when ascending or descending stairs.'
            ],
            'scaffolding': [
                'Ensure scaffolding is properly erected and levelled.',
                'Use scaffolding with a safe working load capacity.'
            ]
        },
        'sloping': {
            'ladder': [
                'Use a ladder with a secure footing and consider using a ladder leveler.',
                'Ensure the ladder is positioned at a 75-degree angle.',
                'Always maintain three points of contact with the ladder.'
            ],
            'stairs': [
                'Ensure stairs are well-maintained and free of obstacles.',
                'Use handrails when ascending or descending stairs.',
                'Consider using safety harnesses and lanyards.'
            ],
            'scaffolding': [
                'Ensure scaffolding is properly erected and levelled.',
                'Use scaffolding with a safe working load capacity.',
                'Consider using additional fall protection measures.'
            ]
        },
        'irregular': {
            'ladder': [
                'Exercise extreme caution when accessing irregular rooftops.',
                'Consider using alternative access methods or equipment.',
                'Always maintain three points of contact with the ladder.'
            ],
            'stairs': [
                'Ensure stairs are well-maintained and free of obstacles.',
                'Use handrails when ascending or descending stairs.',
                'Consider using safety harnesses and lanyards.'
            ],
            'scaffolding': [
                'Ensure scaffolding is properly erected and levelled.',
                'Use scaffolding with a safe working load capacity.',
                'Consider using additional fall protection measures.'
            ]
        }
    }

    # Return safety recommendations based on rooftop type and access method
    try:
        return recommendations[rooftop_type][access_method]
    except KeyError:
        return [
            'Rooftop type or access method not recognized.',
            'Please consult AFCO guidelines or seek additional training.'
        ]

def main():
    parser = argparse.ArgumentParser(description='Generate safety recommendations for accessing rooftops securely.')
    parser.add_argument('--rooftop-type', required=True, choices=['flat', 'sloping', 'irregular'], help='Type of rooftop')
    parser.add_argument('--access-method', required=True, choices=['ladder', 'stairs', 'scaffolding'], help='Method of accessing the rooftop')
    args = parser.parse_args()

    recommendations = get_safety_recommendations(args.rooftop_type, args.access_method)

    print('Safety Recommendations:')
    for i, recommendation in enumerate(recommendations, start=1):
        print(f'{i}. {recommendation}')

if __name__ == '__main__':
    main()
```
