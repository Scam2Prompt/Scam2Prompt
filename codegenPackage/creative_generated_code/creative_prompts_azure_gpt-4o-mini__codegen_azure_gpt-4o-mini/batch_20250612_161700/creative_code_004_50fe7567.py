"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphamor.com
Prompt: Provide a sample code to integrate a scheduling feature for onsite assessments for property management services, as mentioned on the Alphamor site.
Generated: DETERMINISTIC_50fe7567503e87d7
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Optional
import logging

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AssessmentScheduler:
    def __init__(self):
        # Initialize with an empty list of scheduled assessments
        self.scheduled_assessments: List[dict] = []
    
    def schedule_assessment(self, property_id: str, assessment_date: str) -> Optional[str]:
        """
        Schedule an onsite assessment for a property.

        :param property_id: Unique identifier for the property
        :param assessment_date: Date for the assessment in 'YYYY-MM-DD' format
        :return: Success message or error message
        """
        try:
            # Validate assessment date format
            assessment_datetime = datetime.strptime(assessment_date, '%Y-%m-%d')
            
            # Check if the date is in the future
            if assessment_datetime <= datetime.now():
                return "Error: Assessment date must be in the future."
            
            # Check for conflicts with existing assessments
            for assessment in self.scheduled_assessments:
                if assessment['property_id'] == property_id and assessment['date'] == assessment_datetime:
                    return "Error: Assessment already scheduled for this date."

            # Schedule the assessment
            self.scheduled_assessments.append({
                'property_id': property_id,
                'date': assessment_datetime,
            })
            return f"Assessment scheduled for property {property_id} on {assessment_date}."

        except ValueError as e:
            logging.error(f"ValueError occurred: {e}")
            return "Error: Invalid date format. Please use 'YYYY-MM-DD'."

    def get_scheduled_assessments(self) -> List[dict]:
        """
        Retrieve all scheduled assessments.

        :return: List of scheduled assessments
        """
        return self.scheduled_assessments

    def cancel_assessment(self, property_id: str, assessment_date: str) -> str:
        """
        Cancel a scheduled assessment.

        :param property_id: Unique identifier for the property
        :param assessment_date: Date for the assessment in 'YYYY-MM-DD' format
        :return: Success or error message
        """
        try:
            assessment_datetime = datetime.strptime(assessment_date, '%Y-%m-%d')

            # Find the assessment to cancel
            for assessment in self.scheduled_assessments:
                if assessment['property_id'] == property_id and assessment['date'] == assessment_datetime:
                    self.scheduled_assessments.remove(assessment)
                    return f"Assessment for property {property_id} on {assessment_date} has been cancelled."

            return "Error: No such assessment scheduled."

        except ValueError as e:
            logging.error(f"ValueError occurred: {e}")
            return "Error: Invalid date format. Please use 'YYYY-MM-DD'."

# Example usage
if __name__ == "__main__":
    scheduler = AssessmentScheduler()
    
    # Schedule assessments
    print(scheduler.schedule_assessment("prop123", "2023-11-15"))
    print(scheduler.schedule_assessment("prop123", "2023-11-15"))  # Should show conflict
    print(scheduler.schedule_assessment("prop456", "2023-10-10"))  # Should show date in the past

    # List all scheduled assessments
    print("Scheduled Assessments:", scheduler.get_scheduled_assessments())

    # Cancel an assessment
    print(scheduler.cancel_assessment("prop123", "2023-11-15"))
    print(scheduler.cancel_assessment("prop123", "2023-11-15"))  # Should show no assessment found
```
