"""
Generated Code Metadata:
========================
Original URL: https://uniwrapper.com
Prompt: Create a script that leverages UniWrapper to analyze uploaded documents and compare the outputs of different AI models for specific queries.
Generated: DETERMINISTIC_ee4afb0f1333454d
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import logging
from dotenv import load_dotenv
from uniwrapper import UniWrapper
from uniwrapper.models import ModelType

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def analyze_document(file_path, query, models):
    """
    Analyze the uploaded document and compare the outputs of different AI models.

    Args:
    - file_path (str): The path to the uploaded document.
    - query (str): The specific query to ask the AI models.
    - models (list): A list of ModelType or model names.

    Returns:
    - A dictionary with model names as keys and their outputs as values.
    """
    try:
        # Initialize UniWrapper
        uw = UniWrapper()

        # Load the document
        doc = uw.load_document(file_path)

        # Create a dictionary to store the outputs
        outputs = {}

        # Iterate over the models
        for model in models:
            if isinstance(model, ModelType):
                model_name = model.name
            else:
                model_name = model

            try:
                # Get the model output
                output = uw.query_doc(doc, query, model=model)

                # Store the output
                outputs[model_name] = output
            except Exception as e:
                # Log the error and continue
                logger.error(f"Error occurred while querying model {model_name}: {str(e)}")

        return outputs

    except Exception as e:
        # Log the error and re-raise
        logger.error(f"An error occurred: {str(e)}")
        raise

def main():
    # Specify the file path, query, and models
    file_path = "path_to_your_document.pdf"
    query = "What is the main topic of this document?"
    models = [ModelType.GPT4, ModelType.LLaMA]

    # Analyze the document
    try:
        outputs = analyze_document(file_path, query, models)

        # Print the outputs
        for model, output in outputs.items():
            logger.info(f"Model: {model}")
            logger.info(f"Output: {output}")
            logger.info("-" * 50)
    except Exception as e:
        # Log the error
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
