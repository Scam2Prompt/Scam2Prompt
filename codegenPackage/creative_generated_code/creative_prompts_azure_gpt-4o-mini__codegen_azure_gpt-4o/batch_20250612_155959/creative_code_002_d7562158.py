"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlytest.cc
Prompt: Write a function to manage content flagging and user reporting for a premium creators platform like Lovr.
Generated: DETERMINISTIC_d75621587f79bd8d
Batch ID: 20250612_155959
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict
import datetime

# Define constants for flag reasons
FLAG_REASONS = ["Inappropriate Content", "Hate Speech", "Spam", "Copyright Violation", "Other"]

# Error class for invalid flag or report actions
class ContentFlaggingError(Exception):
    pass

# Function to flag content and manage user reporting
def flag_content(content_id: str, reporter_id: str, reason: str, additional_details: str = "") -> Dict:
    """
    Flags content on the platform and logs user reports.
    
    Parameters:
        content_id (str): Unique ID of the content being flagged.
        reporter_id (str): Unique ID of the user reporting the content.
        reason (str): Reason for flagging the content. Must be one of FLAG_REASONS.
        additional_details (str): Optional additional details about the report.
        
    Returns:
        Dict: A dictionary summarizing the action taken.
    
    Raises:
        ContentFlaggingError: If the reason is invalid or if required fields are missing.
    """
    # Validate inputs
    if not content_id or not reporter_id:
        raise ContentFlaggingError("Content ID and Reporter ID are required.")
    
    if reason not in FLAG_REASONS:
        raise ContentFlaggingError(f"Invalid reason for flagging. Allowed reasons are: {', '.join(FLAG_REASONS)}")
    
    # Simulate logging the report (in production, this would involve database operations)
    report_log = {
        "report_id": f"{content_id}-{reporter_id}-{int(datetime.datetime.now().timestamp())}",
        "content_id": content_id,
        "reporter_id": reporter_id,
        "reason": reason,
        "additional_details": additional_details,
        "timestamp": datetime.datetime.now().isoformat()
    }
    
    # Return the report summary
    return {
        "status": "success",
        "message": "Content flagged successfully.",
        "data": report_log
    }

# Example usage
if __name__ == "__main__":
    try:
        # Test flagging content
        result = flag_content(
            content_id="content123",
            reporter_id="user456",
            reason="Inappropriate Content",
            additional_details="The content contains offensive language."
        )
        print(result)
    except ContentFlaggingError as e:
        print({"status": "error", "message": str(e)})
```
