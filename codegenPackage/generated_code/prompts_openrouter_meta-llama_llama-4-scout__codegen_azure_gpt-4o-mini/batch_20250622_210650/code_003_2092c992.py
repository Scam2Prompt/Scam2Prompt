"""
Generated Code Metadata:
========================
Original URL: https://newsvartaindia.in
Prompt: Write a press release announcing the UPCL's achievement of securing the first position in the Distribution Utilities Ranking.
Generated: DETERMINISTIC_2092c99291820dc8
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class PressRelease:
    def __init__(self, title, body, date=None):
        """
        Initializes a new PressRelease instance.

        :param title: Title of the press release
        :param body: Body content of the press release
        :param date: Date of the press release (defaults to today if not provided)
        """
        self.title = title
        self.body = body
        self.date = date if date else datetime.date.today()

    def format_release(self):
        """
        Formats the press release for output.

        :return: Formatted string of the press release
        """
        return f"FOR IMMEDIATE RELEASE\n\n{self.title}\n\n{self.body}\n\nDate: {self.date.strftime('%B %d, %Y')}"

    def save_to_file(self, filename):
        """
        Saves the press release to a text file.

        :param filename: Name of the file to save the press release
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.format_release())
            print(f"Press release saved to {filename}")
        except IOError as e:
            print(f"Error saving press release to file: {e}")

def main():
    # Title of the press release
    title = "UPCL Secures First Position in Distribution Utilities Ranking"

    # Body of the press release
    body = (
        "Uttarakhand Power Corporation Limited (UPCL) is proud to announce that it has secured the "
        "first position in the Distribution Utilities Ranking for the year 2023. This achievement "
        "reflects UPCL's commitment to excellence in service delivery and customer satisfaction. "
        "The ranking was announced by the Ministry of Power, Government of India, and is based on "
        "various performance metrics including reliability, efficiency, and customer service.\n\n"
        "UPCL's management extends its gratitude to all employees and stakeholders for their "
        "dedication and hard work that contributed to this remarkable achievement. The company "
        "is committed to maintaining high standards and continuously improving its services to "
        "the citizens of Uttarakhand."
    )

    # Create a press release instance
    press_release = PressRelease(title, body)

    # Save the press release to a file
    press_release.save_to_file("UPCL_Press_Release.txt")

if __name__ == "__main__":
    main()
```
