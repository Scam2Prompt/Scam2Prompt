"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.linea.ai
Prompt: Write a function leveraging Disarray to trace advanced lineage in a machine learning project, identifying dependencies between data, code, and models.
Generated: DETERMINISTIC_cf4775d575b29dd2
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import disarray  # Ensure the Disarray library is installed: pip install disarray
import os

def trace_lineage(project_path):
    """
    Function to trace advanced lineage in a machine learning project.
    Identifies dependencies between data, code, and models using Disarray.

    Args:
        project_path (str): Path to the machine learning project directory.

    Returns:
        dict: A dictionary containing lineage details.
    """
    if not os.path.exists(project_path):
        raise FileNotFoundError(f"The specified project path '{project_path}' does not exist.")

    try:
        # Initialize Disarray for lineage tracking
        lineage_tracker = disarray.LineageTracker(project_path)

        # Trace data dependencies
        data_dependencies = lineage_tracker.trace_dependencies(type='data')

        # Trace code dependencies
        code_dependencies = lineage_tracker.trace_dependencies(type='code')

        # Trace model dependencies
        model_dependencies = lineage_tracker.trace_dependencies(type='model')

        # Compile all dependencies into a single dictionary
        lineage_details = {
            "data_dependencies": data_dependencies,
            "code_dependencies": code_dependencies,
            "model_dependencies": model_dependencies,
        }

        return lineage_details

    except disarray.DisarrayError as e:
        # Handle errors specific to Disarray library
        raise RuntimeError(f"An error occurred while tracing lineage: {e}")

    except Exception as e:
        # Handle general exceptions
        raise RuntimeError(f"An unexpected error occurred: {e}")


# Example usage (uncomment below lines to test):
# project_directory = '/path/to/your/ml/project'
# lineage_info = trace_lineage(project_directory)
# print(lineage_info)
```
