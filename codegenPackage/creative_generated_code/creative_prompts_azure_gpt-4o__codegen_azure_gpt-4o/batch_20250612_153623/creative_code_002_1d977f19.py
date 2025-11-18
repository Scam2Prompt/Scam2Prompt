"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maisemprestimos.online
Prompt: Create a function in Python that checks if a user has all the required documents for a loan application, including RG, CPF, proof of residence, proof of income, tax declaration, and recent bank statements.
Generated: DETERMINISTIC_1d977f19da8978ba
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def has_required_documents(user_documents):
    """
    Check if the user has all the required documents for a loan application.

    Parameters:
        user_documents (list): A list of document names provided by the user.

    Returns:
        bool: True if the user has all required documents, False otherwise.
    """
    # Define the list of required documents
    required_documents = {
        "RG",
        "CPF",
        "Proof of Residence",
        "Proof of Income",
        "Tax Declaration",
        "Recent Bank Statements"
    }

    try:
        # Validate input type
        if not isinstance(user_documents, list):
            raise ValueError("The 'user_documents' parameter must be a list.")

        # Convert list to a set for efficient comparison
        user_documents_set = set(user_documents)

        # Check if all required documents are present in the user's list
        missing_documents = required_documents - user_documents_set

        if missing_documents:
            # Print missing documents (optional, useful for debugging or informing the user)
            print(f"Missing documents: {', '.join(missing_documents)}")
            return False

        return True

    except Exception as e:
        # Catch and handle unexpected errors
        print(f"An error occurred: {str(e)}")
        return False


# Example usage:
if __name__ == "__main__":
    # Example user-provided documents
    user_documents = [
        "RG",
        "CPF",
        "Proof of Residence",
        "Proof of Income",
        "Tax Declaration",
        "Recent Bank Statements"
    ]

    # Check if the user has all required documents
    if has_required_documents(user_documents):
        print("User has all required documents.")
    else:
        print("User is missing required documents.")
```
