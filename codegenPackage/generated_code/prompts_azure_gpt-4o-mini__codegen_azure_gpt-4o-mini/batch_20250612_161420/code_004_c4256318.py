"""
Generated Code Metadata:
========================
Original URL: https://tolaandtola.com
Prompt: Outline a program that helps clients understand their rights in criminal litigation, drawing on Tola and Tola's emphasis on strong advocacy in criminal law.
Generated: DETERMINISTIC_c425631878de1646
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# criminal_rights_advisor.py

class Client:
    """
    A class to represent a client in a criminal litigation scenario.
    """

    def __init__(self, name, case_type):
        """
        Initializes a new client with a name and type of case.

        :param name: str - The name of the client
        :param case_type: str - The type of criminal case
        """
        self.name = name
        self.case_type = case_type
        self.rights = self.get_rights()

    def get_rights(self):
        """
        Retrieves the rights associated with the client's case type.

        :return: list - A list of rights
        """
        rights_dict = {
            "felony": [
                "Right to an attorney",
                "Right to a fair trial",
                "Right to remain silent",
                "Right to confront witnesses"
            ],
            "misdemeanor": [
                "Right to an attorney",
                "Right to a fair trial",
                "Right to remain silent"
            ],
            "summary": [
                "Right to remain silent",
                "Right to a fair trial"
            ]
        }
        return rights_dict.get(self.case_type, ["No specific rights found."])

    def display_rights(self):
        """
        Displays the rights of the client in a user-friendly format.
        """
        print(f"Client Name: {self.name}")
        print(f"Case Type: {self.case_type.capitalize()}")
        print("Client Rights:")
        for right in self.rights:
            print(f"- {right}")


def main():
    """
    Main function to run the criminal rights advisor program.
    """
    try:
        # Input client details
        client_name = input("Enter the client's name: ")
        case_type = input("Enter the type of case (felony, misdemeanor, summary): ").lower()

        # Validate case type
        if case_type not in ["felony", "misdemeanor", "summary"]:
            raise ValueError("Invalid case type. Please enter 'felony', 'misdemeanor', or 'summary'.")

        # Create a Client instance
        client = Client(client_name, case_type)

        # Display the client's rights
        client.display_rights()

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
