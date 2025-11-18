"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trekk.com
Prompt: Write code to analyze customer data for personalized marketing campaigns, referencing Trekk's use of variable data publishing.
Generated: DETERMINISTIC_bc9c139428e1ad3e
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class CustomerDataAnalyzer:
    """
    A class to analyze customer data for personalized marketing campaigns.
    """

    def __init__(self, data_file):
        """
        Initializes the CustomerDataAnalyzer with customer data.

        :param data_file: str, path to the CSV file containing customer data
        """
        try:
            self.customer_data = pd.read_csv(data_file)
            self.validate_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The file is empty.")
        except pd.errors.ParserError:
            raise ValueError("Error parsing the file. Please check the format.")

    def validate_data(self):
        """
        Validates the customer data to ensure required columns are present.
        """
        required_columns = ['customer_id', 'name', 'email', 'purchase_history', 'preferences']
        for column in required_columns:
            if column not in self.customer_data.columns:
                raise ValueError(f"Missing required column: {column}")

    def segment_customers(self):
        """
        Segments customers based on their purchase history and preferences.

        :return: dict, segmented customer data
        """
        # Example segmentation logic based on purchase frequency
        self.customer_data['purchase_frequency'] = self.customer_data['purchase_history'].apply(lambda x: len(x.split(',')))
        segments = {
            'high_value': self.customer_data[self.customer_data['purchase_frequency'] > 5],
            'medium_value': self.customer_data[(self.customer_data['purchase_frequency'] <= 5) & (self.customer_data['purchase_frequency'] > 2)],
            'low_value': self.customer_data[self.customer_data['purchase_frequency'] <= 2],
        }
        return segments

    def generate_personalized_marketing_campaigns(self):
        """
        Generates personalized marketing campaigns based on customer segments.

        :return: dict, marketing campaign details for each segment
        """
        segments = self.segment_customers()
        campaigns = {}

        for segment_name, customers in segments.items():
            campaign_message = self.create_campaign_message(segment_name)
            campaigns[segment_name] = {
                'customer_count': len(customers),
                'campaign_message': campaign_message,
                'customers': customers[['customer_id', 'name', 'email']].to_dict(orient='records')
            }
        
        return campaigns

    def create_campaign_message(self, segment_name):
        """
        Creates a personalized message based on the customer segment.

        :param segment_name: str, the name of the customer segment
        :return: str, personalized campaign message
        """
        messages = {
            'high_value': "Thank you for being a loyal customer! Here's an exclusive offer just for you.",
            'medium_value': "We appreciate your business! Here's a special discount to encourage more purchases.",
            'low_value': "We miss you! Come back and enjoy a special offer on your next purchase."
        }
        return messages.get(segment_name, "We have a special offer for you!")

# Example usage:
if __name__ == "__main__":
    try:
        # Replace 'customer_data.csv' with the path to your CSV file.
        analyzer = CustomerDataAnalyzer('customer_data.csv')
        marketing_campaigns = analyzer.generate_personalized_marketing_campaigns()
        print(marketing_campaigns)
    except Exception as e:
        print(f"An error occurred: {e}")
```
