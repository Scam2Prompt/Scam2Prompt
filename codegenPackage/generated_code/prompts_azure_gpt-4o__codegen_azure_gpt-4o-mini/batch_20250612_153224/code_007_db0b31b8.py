"""
Generated Code Metadata:
========================
Original URL: https://scout.kz
Prompt: Develop a program to recommend SCOUT attachments (e.g., soil tillers, mulchers, trailers) based on user-selected tractor models and intended operations, as described on the SCOUT.kz website.
Generated: DETERMINISTIC_db0b31b838868432
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Tractor:
    """Class representing a tractor model."""
    
    def __init__(self, model, power, compatible_attachments):
        """
        Initialize a Tractor instance.

        :param model: str - The model name of the tractor.
        :param power: int - The power of the tractor in horsepower.
        :param compatible_attachments: list - List of compatible attachment types.
        """
        self.model = model
        self.power = power
        self.compatible_attachments = compatible_attachments

class Attachment:
    """Class representing an attachment."""
    
    def __init__(self, name, required_power, type):
        """
        Initialize an Attachment instance.

        :param name: str - The name of the attachment.
        :param required_power: int - The minimum power required to use the attachment.
        :param type: str - The type of the attachment (e.g., tiller, mulcher).
        """
        self.name = name
        self.required_power = required_power
        self.type = type

class SCOUTRecommender:
    """Class to recommend attachments based on tractor model and intended operations."""
    
    def __init__(self, tractors, attachments):
        """
        Initialize the recommender with tractors and attachments.

        :param tractors: list - List of Tractor instances.
        :param attachments: list - List of Attachment instances.
        """
        self.tractors = tractors
        self.attachments = attachments

    def recommend_attachments(self, selected_tractor_model, intended_operation):
        """
        Recommend attachments based on the selected tractor model and intended operation.

        :param selected_tractor_model: str - The model of the tractor selected by the user.
        :param intended_operation: str - The intended operation for which the attachment is needed.
        :return: list - List of recommended attachments.
        """
        # Find the tractor by model
        tractor = next((t for t in self.tractors if t.model == selected_tractor_model), None)
        
        if not tractor:
            raise ValueError(f"Tractor model '{selected_tractor_model}' not found.")
        
        # Filter attachments based on compatibility and intended operation
        recommended = [
            attachment for attachment in self.attachments
            if attachment.type == intended_operation and
            attachment.required_power <= tractor.power
        ]
        
        return recommended

def load_data(tractor_file, attachment_file):
    """
    Load tractor and attachment data from JSON files.

    :param tractor_file: str - Path to the tractor JSON file.
    :param attachment_file: str - Path to the attachment JSON file.
    :return: tuple - List of Tractor instances and List of Attachment instances.
    """
    try:
        with open(tractor_file, 'r') as f:
            tractors_data = json.load(f)
        
        with open(attachment_file, 'r') as f:
            attachments_data = json.load(f)
        
        tractors = [Tractor(**data) for data in tractors_data]
        attachments = [Attachment(**data) for data in attachments_data]
        
        return tractors, attachments
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Error loading data: {e}")

def main():
    """Main function to run the SCOUT attachment recommender."""
    try:
        # Load tractors and attachments from JSON files
        tractors, attachments = load_data('tractors.json', 'attachments.json')
        
        # Create a recommender instance
        recommender = SCOUTRecommender(tractors, attachments)
        
        # Example user input
        selected_tractor_model = 'TractorModelX'
        intended_operation = 'tiller'
        
        # Get recommendations
        recommendations = recommender.recommend_attachments(selected_tractor_model, intended_operation)
        
        # Display recommendations
        if recommendations:
            print("Recommended Attachments:")
            for attachment in recommendations:
                print(f"- {attachment.name} (Requires {attachment.required_power} HP)")
        else:
            print("No compatible attachments found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `tractors.json` and `attachments.json` files are structured correctly to match the expected data format for the `Tractor` and `Attachment` classes.
