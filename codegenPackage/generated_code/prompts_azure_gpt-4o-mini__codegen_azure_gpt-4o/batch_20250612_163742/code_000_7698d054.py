"""
Generated Code Metadata:
========================
Original URL: https://lineage-ai.vercel.app
Prompt: How can I create a model card for my machine learning model using the guidelines from Lineage AI?
Generated: DETERMINISTIC_7698d054e8a80992
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script generates a model card for a machine learning model following the guidelines from Lineage AI.
The model card provides essential information about the model, including its purpose, training data, evaluation metrics, and limitations.
"""

import json
import datetime

def generate_model_card(model_name, model_version, description, training_data, evaluation_metrics, limitations, authors):
    """
    Generates a model card in JSON format.

    Args:
        model_name (str): Name of the machine learning model.
        model_version (str): Version of the model.
        description (str): Brief description of the model's purpose and functionality.
        training_data (dict): Information about the training data (e.g., source, size, preprocessing).
        evaluation_metrics (dict): Metrics used to evaluate the model (e.g., accuracy, precision, recall).
        limitations (str): Known limitations or risks associated with the model.
        authors (list): List of authors or contributors to the model.

    Returns:
        str: JSON-formatted model card.
    """
    try:
        # Create a dictionary to store model card information
        model_card = {
            "model_name": model_name,
            "model_version": model_version,
            "description": description,
            "training_data": training_data,
            "evaluation_metrics": evaluation_metrics,
            "limitations": limitations,
            "authors": authors,
            "created_at": datetime.datetime.now().isoformat()  # Timestamp for when the model card was created
        }

        # Convert the dictionary to a JSON string
        model_card_json = json.dumps(model_card, indent=4)
        return model_card_json
    except Exception as e:
        # Handle any errors that occur during model card generation
        return f"Error generating model card: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define model card details
    model_name = "ImageClassifier"
    model_version = "1.0.0"
    description = "A convolutional neural network model for classifying images into predefined categories."
    training_data = {
        "source": "Open Images Dataset",
        "size": "500,000 images",
        "preprocessing": "Resized to 224x224, normalized pixel values"
    }
    evaluation_metrics = {
        "accuracy": "92%",
        "precision": "90%",
        "recall": "88%"
    }
    limitations = "The model may not perform well on images outside the training distribution or with significant noise."
    authors = ["Alice Smith", "Bob Johnson"]

    # Generate the model card
    model_card = generate_model_card(
        model_name=model_name,
        model_version=model_version,
        description=description,
        training_data=training_data,
        evaluation_metrics=evaluation_metrics,
        limitations=limitations,
        authors=authors
    )

    # Print the model card
    print(model_card)
```
