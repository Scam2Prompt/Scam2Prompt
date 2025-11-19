"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhonybarros.com.br
Prompt: Write a Python function that simulates the process of sending exam requests through a pre-attendance system, ensuring the user can select a preferred unit for collection.
Generated: DETERMINISTIC_aa5639485c6a811a
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error reporting and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_exam_request(student_name, exam_type, preferred_unit):
    """
    Simulates the process of sending exam requests through a pre-attendance system.

    Args:
        student_name (str): Name of the student requesting the exam.
        exam_type (str): Type of exam (e.g., "midterm", "final", "quiz").
        preferred_unit (str): Preferred unit for collection (e.g., "Unit A", "Unit B").

    Returns:
        dict: A dictionary with the confirmation status and details of the request.

    Raises:
        ValueError: If any of the input arguments are invalid.
    """
    # Validate input arguments
    if not student_name or not isinstance(student_name, str):
        raise ValueError("Invalid student name. It must be a non-empty string.")
    if not exam_type or not isinstance(exam_type, str):
        raise ValueError("Invalid exam type. It must be a non-empty string.")
    if not preferred_unit or not isinstance(preferred_unit, str):
        raise ValueError("Invalid preferred unit. It must be a non-empty string.")

    # List of available units for validation
    available_units = ["Unit A", "Unit B", "Unit C", "Unit D"]

    if preferred_unit not in available_units:
        raise ValueError(f"Preferred unit '{preferred_unit}' is not available. Choose from {available_units}.")

    try:
        # Simulate sending the request
        logging.info(f"Sending exam request for student '{student_name}'...")
        logging.info(f"Exam type: {exam_type}")
        logging.info(f"Preferred unit for collection: {preferred_unit}")

        # Mockup of an actual process (e.g., database update, notification, etc.)
        confirmation_id = f"REQ-{hash(student_name + exam_type + preferred_unit)}"

        # Successful response
        response = {
            "status": "success",
            "message": "Exam request sent successfully.",
            "confirmation_id": confirmation_id,
            "student_name": student_name,
            "exam_type": exam_type,
            "preferred_unit": preferred_unit,
        }
        logging.info("Exam request processed successfully.")
        return response
    except Exception as e:
        # Log and handle any unexpected errors
        logging.error(f"An error occurred while sending the exam request: {e}")
        return {
            "status": "error",
            "message": f"An error occurred: {str(e)}",
        }


# Example usage:
if __name__ == "__main__":
    try:
        # Request simulation
        result = send_exam_request(student_name="Alice Johnson",
                                   exam_type="midterm",
                                   preferred_unit="Unit A")
        print(result)
    except ValueError as ve:
        # Handle specific validation errors
        print(f"Validation Error: {ve}")
    except Exception as ex:
        # Handle any unexpected errors
        print(f"Unexpected Error: {ex}")
```
