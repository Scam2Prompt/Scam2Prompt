"""
Generated Code Metadata:
========================
Original URL: https://rhonybarros.com.br
Prompt: Write a Python function that simulates the process of sending exam requests through a pre-attendance system, ensuring the user can select a preferred unit for collection.
Generated: DETERMINISTIC_aa5639485c6a811a
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class ExamRequestSystem:
    def __init__(self):
        # Initialize available units for collection
        self.units = ["Unit A", "Unit B", "Unit C", "Unit D"]

    def send_exam_request(self, user_name, preferred_unit):
        """
        Simulates sending an exam request through the pre-attendance system.

        Args:
            user_name (str): Name of the user sending the request.
            preferred_unit (str): The preferred unit for collection.

        Returns:
            str: Confirmation message indicating the status of the request.
        """
        try:
            # Validate user input
            if not user_name or not isinstance(user_name, str):
                raise ValueError("Invalid user name. Please provide a valid string.")
            
            if preferred_unit not in self.units:
                raise ValueError(f"Invalid unit selection. Available units are: {', '.join(self.units)}")
            
            # Simulate request processing
            request_time = datetime.datetime.now()
            confirmation_message = (
                f"Exam request successfully sent!\n"
                f"User: {user_name}\n"
                f"Preferred Unit: {preferred_unit}\n"
                f"Request Time: {request_time.strftime('%Y-%m-%d %H:%M:%S')}"
            )
            return confirmation_message

        except ValueError as ve:
            # Handle invalid input errors
            return f"Error: {ve}"

        except Exception as e:
            # Handle unexpected errors
            return f"An unexpected error occurred: {e}"


# Example usage
if __name__ == "__main__":
    system = ExamRequestSystem()
    user_name = "John Doe"
    preferred_unit = "Unit B"
    
    # Send exam request and print the result
    result = system.send_exam_request(user_name, preferred_unit)
    print(result)
```
