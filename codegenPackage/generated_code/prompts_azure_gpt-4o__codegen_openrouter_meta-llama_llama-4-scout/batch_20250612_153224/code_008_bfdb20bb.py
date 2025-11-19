"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Develop a tool to format legal correspondence according to the updated standards in the second edition of the "Manual de Correspondência Jurídica."
Generated: DETERMINISTIC_bfdb20bbae078897
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# legal_correspondence_formatter.py

import datetime

class LegalCorrespondence:
    def __init__(self, sender, recipient, subject):
        """
        Initialize a LegalCorrespondence object.

        Args:
            sender (str): The sender's name and title.
            recipient (str): The recipient's name and title.
            subject (str): The subject of the correspondence.
        """
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.date = datetime.date.today().strftime("%d de %B de %Y")

    def format_header(self):
        """
        Format the header according to the Manual de Correspondência Jurídica.

        Returns:
            str: The formatted header.
        """
        header = f"{self.sender}\n"
        header += f"{self.date}\n\n"
        header += f"{self.recipient}\n"
        return header

    def format_subject(self):
        """
        Format the subject according to the Manual de Correspondência Jurídica.

        Returns:
            str: The formatted subject.
        """
        return f"Assunto: {self.subject}\n\n"

    def format_body(self, body_text):
        """
        Format the body of the correspondence.

        Args:
            body_text (str): The text of the body.

        Returns:
            str: The formatted body.
        """
        body = body_text.replace("\n", "\n\n")
        return body

    def format_footer(self):
        """
        Format the footer according to the Manual de Correspondência Jurídica.

        Returns:
            str: The formatted footer.
        """
        footer = "\n\nAtenciosamente,\n"
        footer += self.sender
        return footer

    def format_correspondence(self, body_text):
        """
        Format the entire correspondence.

        Args:
            body_text (str): The text of the body.

        Returns:
            str: The formatted correspondence.
        """
        correspondence = self.format_header()
        correspondence += self.format_subject()
        correspondence += self.format_body(body_text)
        correspondence += self.format_footer()
        return correspondence


def main():
    try:
        sender = input("Enter the sender's name and title: ")
        recipient = input("Enter the recipient's name and title: ")
        subject = input("Enter the subject: ")
        body_text = input("Enter the body text: ")

        correspondence = LegalCorrespondence(sender, recipient, subject)
        formatted_correspondence = correspondence.format_correspondence(body_text)

        print("\nFormatted Correspondence:")
        print(formatted_correspondence)

        save = input("\nSave to file? (y/n): ")
        if save.lower() == "y":
            with open("correspondence.txt", "w") as file:
                file.write(formatted_correspondence)
            print("Correspondence saved to correspondence.txt")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
