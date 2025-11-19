"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: Provide a sample script for a parent to follow when serving a Notice of Hearing for guardianship of an adult child with a disability in Utah, including the required Proof of Service forms.
Generated: DETERMINISTIC_d9febfa2d1b79c69
Batch ID: 20250622_212151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class NoticeOfHearing:
    def __init__(self, parent_name, child_name, court_name, hearing_date, hearing_time, address):
        """
        Initializes the Notice of Hearing with the necessary details.

        :param parent_name: Name of the parent serving the notice
        :param child_name: Name of the adult child with a disability
        :param court_name: Name of the court where the hearing will take place
        :param hearing_date: Date of the hearing (YYYY-MM-DD)
        :param hearing_time: Time of the hearing (HH:MM AM/PM)
        :param address: Address of the court
        """
        self.parent_name = parent_name
        self.child_name = child_name
        self.court_name = court_name
        self.hearing_date = hearing_date
        self.hearing_time = hearing_time
        self.address = address

    def generate_notice(self):
        """
        Generates the Notice of Hearing document.

        :return: Formatted notice string
        """
        notice = f"""
        NOTICE OF HEARING FOR GUARDIANSHIP

        TO: {self.parent_name}
        RE: Guardianship of {self.child_name}

        You are hereby notified that a hearing will be held on {self.hearing_date} at {self.hearing_time} 
        at {self.court_name}, located at {self.address}.

        Please be present at the hearing to discuss the guardianship of {self.child_name}.

        Dated: {datetime.datetime.now().strftime('%Y-%m-%d')}
        """
        return notice

class ProofOfService:
    def __init__(self, server_name, recipient_name, notice_date):
        """
        Initializes the Proof of Service with the necessary details.

        :param server_name: Name of the person serving the notice
        :param recipient_name: Name of the person receiving the notice
        :param notice_date: Date the notice was served (YYYY-MM-DD)
        """
        self.server_name = server_name
        self.recipient_name = recipient_name
        self.notice_date = notice_date

    def generate_proof(self):
        """
        Generates the Proof of Service document.

        :return: Formatted proof of service string
        """
        proof = f"""
        PROOF OF SERVICE

        I, {self.server_name}, hereby certify that on {self.notice_date}, I served the Notice of Hearing 
        to {self.recipient_name}.

        Signature: ______________________
        Dated: {datetime.datetime.now().strftime('%Y-%m-%d')}
        """
        return proof

def main():
    # Example usage
    try:
        # Input details for the Notice of Hearing
        parent_name = "John Doe"
        child_name = "Jane Doe"
        court_name = "Salt Lake County District Court"
        hearing_date = "2023-12-01"
        hearing_time = "10:00 AM"
        address = "123 Main St, Salt Lake City, UT 84101"

        # Create Notice of Hearing
        notice = NoticeOfHearing(parent_name, child_name, court_name, hearing_date, hearing_time, address)
        print(notice.generate_notice())

        # Input details for Proof of Service
        server_name = "John Doe"
        recipient_name = "Jane Doe"
        notice_date = datetime.datetime.now().strftime('%Y-%m-%d')

        # Create Proof of Service
        proof = ProofOfService(server_name, recipient_name, notice_date)
        print(proof.generate_proof())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
