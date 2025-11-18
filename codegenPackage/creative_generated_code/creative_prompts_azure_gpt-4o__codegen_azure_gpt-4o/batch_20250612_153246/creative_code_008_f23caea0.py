"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gkcritiques.com
Prompt: Write code to filter and target respondents in real-time for a healthcare survey, using the extensive network of panelists provided by GK Critique Services.
Generated: DETERMINISTIC_f23caea04012a0f9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HealthcareSurveyFilter:
    """
    Class to filter and target respondents in real-time for a healthcare survey.
    """
    def __init__(self, panelists):
        """
        Initialize with a network of panelists.
        
        Parameters:
        panelists (list of dict): List of panelists, where each panelist is a dictionary 
                                  containing respondent details.
        """
        self.panelists = panelists

    def filter_respondents(self, criteria):
        """
        Filter respondents based on given criteria.

        Parameters:
        criteria (dict): A dictionary specifying the filtering conditions.
                         Example: {"age": [30, 40], "location": "NY", "health_condition": "diabetic"}

        Returns:
        list of dict: Filtered respondents matching the criteria.
        """
        try:
            filtered_panelists = []
            for panelist in self.panelists:
                match = True
                for key, value in criteria.items():
                    if key in panelist:
                        # Handle range-based criteria (e.g., age range)
                        if isinstance(value, list) and len(value) == 2 and isinstance(panelist[key], (int, float)):
                            if not (value[0] <= panelist[key] <= value[1]):
                                match = False
                                break
                        # Handle exact matches
                        elif panelist[key] != value:
                            match = False
                            break
                    else:
                        match = False
                        break
                if match:
                    filtered_panelists.append(panelist)
            return filtered_panelists
        except Exception as e:
            logging.error(f"Error filtering respondents: {e}")
            return []

    def target_respondents(self, criteria, action):
        """
        Target respondents based on criteria and perform an action.

        Parameters:
        criteria (dict): A dictionary specifying the filtering conditions.
        action (function): A callback function to apply to each targeted respondent.
                           Example: action(resp) where resp is a respondent's data.

        Returns:
        None
        """
        try:
            # Filter respondents based on criteria
            targeted_panelists = self.filter_respondents(criteria)
            logging.info(f"Number of respondents targeted: {len(targeted_panelists)}")

            # Apply the action to each targeted respondent
            for respondent in targeted_panelists:
                try:
                    action(respondent)
                except Exception as e:
                    logging.warning(f"Error handling respondent {respondent.get('id', 'unknown')}: {e}")
        except Exception as e:
            logging.error(f"Error targeting respondents: {e}")


# Example usage
if __name__ == "__main__":
    # Mock list of panelists
    panelists_data = [
        {"id": 1, "name": "John Doe", "age": 35, "location": "NY", "health_condition": "diabetic"},
        {"id": 2, "name": "Jane Smith", "age": 28, "location": "CA", "health_condition": "healthy"},
        {"id": 3, "name": "Alice Johnson", "age": 40, "location": "NY", "health_condition": "diabetic"},
        {"id": 4, "name": "Bob Brown", "age": 50, "location": "TX", "health_condition": "hypertension"}
    ]

    # Initialize the filter class
    survey_filter = HealthcareSurveyFilter(panelists_data)

    # Define criteria for filtering
    filter_criteria = {"age": [30, 40], "location": "NY", "health_condition": "diabetic"}

    # Define an action function (example: sending a survey invitation)
    def send_survey_invitation(respondent):
        logging.info(f"Sending survey invitation to {respondent['name']} (ID: {respondent['id']})")

    # Target respondents and perform the action
    survey_filter.target_respondents(filter_criteria, send_survey_invitation)
```
