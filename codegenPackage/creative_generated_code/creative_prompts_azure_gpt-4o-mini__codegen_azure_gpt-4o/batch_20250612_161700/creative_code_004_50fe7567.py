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
import pytz

class PropertyAssessmentScheduler:
    """
    A class to manage scheduling of onsite property assessments.
    """

    def __init__(self):
        # Initialize the scheduler with a list to store scheduled assessments
        self.scheduled_assessments = []

    def schedule_assessment(self, property_id, customer_name, assessment_date, timezone="UTC"):
        """
        Schedule an onsite property assessment.
        
        Args:
            property_id (str): Unique ID for the property.
            customer_name (str): Name of the customer.
            assessment_date (str): Date and time for the assessment (format: 'YYYY-MM-DD HH:MM').
            timezone (str): Timezone for the assessment. Defaults to UTC.

        Returns:
            dict: Details of the scheduled assessment.

        Raises:
            ValueError: If the assessment date is in the past.
        """
        try:
            # Parse the input date and time
            local_tz = pytz.timezone(timezone)
            parsed_date = datetime.strptime(assessment_date, '%Y-%m-%d %H:%M')
            localized_date = local_tz.localize(parsed_date)

            # Check if the date is in the past
            current_time = datetime.now(pytz.UTC)
            if localized_date < current_time:
                raise ValueError("Assessment date cannot be in the past.")

            # Create the assessment entry
            assessment_entry = {
                "property_id": property_id,
                "customer_name": customer_name,
                "assessment_date": localized_date,
                "timezone": timezone
            }

            # Save the assessment
            self.scheduled_assessments.append(assessment_entry)
            return assessment_entry

        except Exception as e:
            # Log the error for debugging and rethrow it
            print(f"Error scheduling assessment: {e}")
            raise

    def list_scheduled_assessments(self):
        """
        Retrieve all scheduled assessments.

        Returns:
            list: List of scheduled assessments.
        """
        return self.scheduled_assessments

    def reschedule_assessment(self, property_id, new_date, timezone="UTC"):
        """
        Reschedule an existing property assessment.

        Args:
            property_id (str): Unique ID for the property.
            new_date (str): New date and time for the assessment (format: 'YYYY-MM-DD HH:MM').
            timezone (str): Timezone for the assessment. Defaults to UTC.

        Returns:
            dict: Updated assessment details.

        Raises:
            ValueError: If the property ID is not found.
        """
        try:
            # Find the assessment entry by property ID
            assessment = next(
                (a for a in self.scheduled_assessments if a["property_id"] == property_id), None
            )

            if not assessment:
                raise ValueError(f"No assessment found for property ID: {property_id}")

            # Parse the new date and time
            local_tz = pytz.timezone(timezone)
            new_parsed_date = datetime.strptime(new_date, '%Y-%m-%d %H:%M')
            new_localized_date = local_tz.localize(new_parsed_date)

            # Check if the new date is in the past
            current_time = datetime.now(pytz.UTC)
            if new_localized_date < current_time:
                raise ValueError("New assessment date cannot be in the past.")

            # Update the assessment entry
            assessment["assessment_date"] = new_localized_date
            assessment["timezone"] = timezone

            return assessment

        except Exception as e:
            # Log the error for debugging and rethrow it
            print(f"Error rescheduling assessment: {e}")
            raise

    def cancel_assessment(self, property_id):
        """
        Cancel a scheduled assessment.

        Args:
            property_id (str): Unique ID for the property.

        Returns:
            bool: True if the cancellation was successful, False otherwise.

        Raises:
            ValueError: If the property ID is not found.
        """
        try:
            # Find the assessment entry by property ID
            idx = next(
                (i for i, a in enumerate(self.scheduled_assessments) if a["property_id"] == property_id),
                None
            )

            if idx is None:
                raise ValueError(f"No assessment found for property ID: {property_id}")

            # Remove the assessment entry from the list
            del self.scheduled_assessments[idx]
            return True

        except Exception as e:
            # Log the error for debugging and rethrow it
            print(f"Error canceling assessment: {e}")
            raise


# Sample usage:
if __name__ == "__main__":
    scheduler = PropertyAssessmentScheduler()

    try:
        # Schedule a new assessment
        new_assessment = scheduler.schedule_assessment(
            property_id="PROP123",
            customer_name="John Doe",
            assessment_date="2023-11-25 14:00",
            timezone="America/New_York"
        )
        print("Assessment Scheduled:", new_assessment)

        # List all scheduled assessments
        print("Scheduled Assessments:", scheduler.list_scheduled_assessments())

        # Reschedule the assessment
        updated_assessment = scheduler.reschedule_assessment(
            property_id="PROP123",
            new_date="2023-11-26 16:00",
            timezone="America/New_York"
        )
        print("Updated Assessment:", updated_assessment)

        # Cancel the assessment
        if scheduler.cancel_assessment(property_id="PROP123"):
            print("Assessment canceled successfully.")

        # List all scheduled assessments after cancellation
        print("Scheduled Assessments:", scheduler.list_scheduled_assessments())

    except Exception as e:
        print(f"An error occurred: {e}")
```
