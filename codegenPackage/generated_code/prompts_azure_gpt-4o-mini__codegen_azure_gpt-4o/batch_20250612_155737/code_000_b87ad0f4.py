"""
Generated Code Metadata:
========================
Original URL: https://legend-of-jimmy.nfts2.me
Prompt: Generate a code snippet to create a report system for users to flag potential scams in NFT collections, similar to the process described on the NFTs 2 Me website.
Generated: DETERMINISTIC_b87ad0f4ded5a136
Batch ID: 20250612_155737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

# Define a class to handle the report system
class NFTScamReportSystem:
    def __init__(self):
        # Initialize an empty list to store reports
        self.reports = []

    def submit_report(self, user_id, nft_collection_name, reason):
        """
        Submit a report for a potential scam in an NFT collection.

        Args:
            user_id (str): The ID of the user submitting the report.
            nft_collection_name (str): The name of the NFT collection being flagged.
            reason (str): The reason for flagging the collection.

        Returns:
            dict: A confirmation message with the report details.
        """
        try:
            # Validate inputs
            if not user_id or not nft_collection_name or not reason:
                raise ValueError("All fields (user_id, nft_collection_name, reason) are required.")

            # Create a report object
            report = {
                "report_id": len(self.reports) + 1,
                "user_id": user_id,
                "nft_collection_name": nft_collection_name,
                "reason": reason,
                "timestamp": datetime.now().isoformat()
            }

            # Add the report to the list
            self.reports.append(report)

            # Return a confirmation message
            return {
                "status": "success",
                "message": "Report submitted successfully.",
                "report": report
            }
        except ValueError as ve:
            return {
                "status": "error",
                "message": str(ve)
            }
        except Exception as e:
            return {
                "status": "error",
                "message": "An unexpected error occurred: " + str(e)
            }

    def get_reports(self):
        """
        Retrieve all submitted reports.

        Returns:
            list: A list of all reports.
        """
        return self.reports

    def save_reports_to_file(self, file_path):
        """
        Save all reports to a JSON file.

        Args:
            file_path (str): The path to the file where reports will be saved.

        Returns:
            dict: A confirmation message indicating success or failure.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.reports, file, indent=4)
            return {
                "status": "success",
                "message": f"Reports saved to {file_path} successfully."
            }
        except Exception as e:
            return {
                "status": "error",
                "message": "Failed to save reports: " + str(e)
            }

# Example usage
if __name__ == "__main__":
    # Initialize the report system
    report_system = NFTScamReportSystem()

    # Submit a report
    response = report_system.submit_report(
        user_id="user123",
        nft_collection_name="FakeNFTCollection",
        reason="Suspicious activity detected"
    )
    print(response)

    # Retrieve all reports
    all_reports = report_system.get_reports()
    print("All Reports:", all_reports)

    # Save reports to a file
    save_response = report_system.save_reports_to_file("reports.json")
    print(save_response)
```
