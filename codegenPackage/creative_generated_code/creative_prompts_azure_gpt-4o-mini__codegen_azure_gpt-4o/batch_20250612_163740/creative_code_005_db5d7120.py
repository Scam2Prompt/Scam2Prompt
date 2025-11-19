"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tcs-campaigns.com
Prompt: Create a guided development prompt using the pre-built prompt library from TCS AI Catapult Forward for a new software project.
Generated: DETERMINISTIC_db5d71208c374e3c
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries from TCS AI Catapult Forward framework
from tcs_ai_catapult.prompt_library import PromptLibrary, PromptBuilder
import logging

# Initialize logging for better error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_guided_development_prompt(project_name, requirements, use_cases):
    """
    Function to generate a guided development prompt using TCS AI Catapult's pre-built prompt library.
    
    Args:
        project_name (str): The name of the software project.
        requirements (list): A list of high-level requirements for the project.
        use_cases (list): A list of specific business or technical use cases for the project.
    
    Returns:
        str: A customized guided development prompt.
    """
    try:
        # Validate input parameters
        if not project_name or not isinstance(project_name, str):
            raise ValueError("Project name must be a non-empty string.")
        if not requirements or not isinstance(requirements, list):
            raise ValueError("Requirements must be a non-empty list.")
        if not use_cases or not isinstance(use_cases, list):
            raise ValueError("Use cases must be a non-empty list.")
        
        # Initialize PromptLibrary to access pre-built templates
        prompt_library = PromptLibrary()

        # Use PromptBuilder to start constructing the guided development prompt
        builder = PromptBuilder()

        # Add project name to the prompt context
        builder.add_context(f"Project Name: {project_name}")

        # Add requirements to the prompt context
        builder.add_context("High-Level Requirements:")
        for req in requirements:
            builder.add_context(f"- {req}")

        # Add use cases to the prompt context
        builder.add_context("Key Use Cases:")
        for use_case in use_cases:
            builder.add_context(f"- {use_case}")

        # Add instructional note for guided development
        instructional_note = (
            "Using the above context, generate a step-by-step plan for "
            "developing the project. Provide a system architecture design, "
            "a list of technologies to be used, and a timeline for implementation."
        )
        builder.add_instructions(instructional_note)

        # Generate the final prompt using TCS AI Catapult
        final_prompt = builder.build_prompt(prebuilt_template="guided_development")

        # Log the generated prompt for reference
        logging.info("Guided development prompt successfully generated.")
        
        return final_prompt

    except Exception as e:
        # Log errors and re-raise the exception for further handling if needed
        logging.error(f"An error occurred while generating the guided development prompt: {e}")
        raise

# Example usage (can be commented out before deployment in production)
if __name__ == "__main__":
    project_name = "E-Commerce Platform"
    requirements = [
        "User authentication and authorization",
        "Product catalog management",
        "Secure payment gateway integration"
    ]
    use_cases = [
        "Allow users to browse and purchase products",
        "Enable admins to manage product inventory",
        "Provide order tracking functionality for customers"
    ]

    try:
        prompt = create_guided_development_prompt(project_name, requirements, use_cases)
        print("Generated Prompt:\n")
        print(prompt)
    except Exception as err:
        logging.error(f"Failed to create guided development prompt: {err}")
```
