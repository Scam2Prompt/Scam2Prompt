"""
Generated Code Metadata:
========================
Original URL: https://karlakarita.com.br
Prompt: "Generate a social media posting schedule for promoting a fashion brand's new collection, including discounts and sustainability features."
Generated: DETERMINISTIC_05588f09fd9801d3
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json

class SocialMediaScheduler:
    def __init__(self, brand_name, collection_name, start_date, end_date, discount, sustainability_features):
        """
        Initializes the SocialMediaScheduler with brand details and promotion parameters.

        :param brand_name: Name of the fashion brand
        :param collection_name: Name of the new collection
        :param start_date: Start date for the promotion (YYYY-MM-DD)
        :param end_date: End date for the promotion (YYYY-MM-DD)
        :param discount: Discount percentage for the promotion
        :param sustainability_features: List of sustainability features of the collection
        """
        self.brand_name = brand_name
        self.collection_name = collection_name
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        self.discount = discount
        self.sustainability_features = sustainability_features
        self.schedule = []

    def generate_schedule(self):
        """
        Generates a posting schedule for the social media campaign.
        Posts will be scheduled every 3 days from start_date to end_date.
        """
        current_date = self.start_date
        while current_date <= self.end_date:
            post = {
                "date": current_date.strftime("%Y-%m-%d"),
                "message": self.create_post_message(),
            }
            self.schedule.append(post)
            current_date += datetime.timedelta(days=3)

    def create_post_message(self):
        """
        Creates a message for the social media post.

        :return: A formatted string containing the post message
        """
        features = ', '.join(self.sustainability_features)
        return (f"🌟 Exciting news from {self.brand_name}! 🌟\n"
                f"Introducing our new collection: {self.collection_name}.\n"
                f"Enjoy a {self.discount}% discount!\n"
                f"Features: {features}\n"
                f"Shop now and embrace sustainable fashion!")

    def save_schedule_to_file(self, filename):
        """
        Saves the generated schedule to a JSON file.

        :param filename: Name of the file to save the schedule
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.schedule, file, indent=4)
            print(f"Schedule saved to {filename}")
        except IOError as e:
            print(f"Error saving schedule to file: {e}")

    def display_schedule(self):
        """Displays the generated posting schedule in the console."""
        for post in self.schedule:
            print(f"Date: {post['date']}, Message: {post['message']}")

# Example usage
if __name__ == "__main__":
    try:
        brand_name = "EcoFashion"
        collection_name = "Spring Collection 2023"
        start_date = "2023-04-01"
        end_date = "2023-04-30"
        discount = 20  # 20% discount
        sustainability_features = ["Recycled materials", "Ethically sourced", "Carbon neutral production"]

        scheduler = SocialMediaScheduler(brand_name, collection_name, start_date, end_date, discount, sustainability_features)
        scheduler.generate_schedule()
        scheduler.display_schedule()
        scheduler.save_schedule_to_file("social_media_schedule.json")
    except ValueError as e:
        print(f"Error in input data: {e}")
```
