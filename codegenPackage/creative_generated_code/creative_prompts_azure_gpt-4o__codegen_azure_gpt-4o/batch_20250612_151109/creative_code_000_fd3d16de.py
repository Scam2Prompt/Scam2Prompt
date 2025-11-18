"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digital-hub.top
Prompt: Write Python code to calculate the digital carbon footprint of a user based on the guidelines for reducing digital impact described on Digital Hub.
Generated: DETERMINISTIC_fd3d16deae9265e7
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for tracking errors and events
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class DigitalCarbonFootprintCalculator:
    """
    Class to calculate digital carbon footprint of a user based on usage patterns.
    """

    def __init__(self):
        self.emission_factors = {
            "streaming_hours": 36,  # grams CO2e per hour of streaming video
            "email_sent": 4,        # grams CO2e per email sent
            "search_queries": 0.2,  # grams CO2e per web search query
            "cloud_storage_per_gb": 200  # grams CO2e per GB of cloud storage per year
        }

    def calculate_streaming_emissions(self, hours):
        """
        Calculate emissions from video streaming.
        :param hours: Number of hours streamed
        :return: Emissions in grams CO2e
        """
        if hours < 0:
            raise ValueError("Hours streamed must be a positive number.")
        return hours * self.emission_factors["streaming_hours"]

    def calculate_email_emissions(self, emails_sent):
        """
        Calculate emissions from sending emails.
        :param emails_sent: Number of emails sent
        :return: Emissions in grams CO2e
        """
        if emails_sent < 0:
            raise ValueError("Number of emails sent must be a positive number.")
        return emails_sent * self.emission_factors["email_sent"]

    def calculate_search_emissions(self, search_queries):
        """
        Calculate emissions from performing web searches.
        :param search_queries: Number of web search queries
        :return: Emissions in grams CO2e
        """
        if search_queries < 0:
            raise ValueError("Number of search queries must be a positive number.")
        return search_queries * self.emission_factors["search_queries"]

    def calculate_storage_emissions(self, gb_used):
        """
        Calculate emissions from cloud storage usage.
        :param gb_used: Amount of cloud storage used in GB
        :return: Emissions in grams CO2e
        """
        if gb_used < 0:
            raise ValueError("Cloud storage used must be a positive number.")
        return gb_used * self.emission_factors["cloud_storage_per_gb"]

    def calculate_total_emissions(self, streaming_hours, emails_sent, search_queries, gb_used):
        """
        Calculate total digital carbon footprint based on usage patterns.
        :param streaming_hours: Hours of video streaming
        :param emails_sent: Number of emails sent
        :param search_queries: Number of web search queries
        :param gb_used: Cloud storage used in GB
        :return: Total emissions in grams CO2e
        """
        try:
            streaming = self.calculate_streaming_emissions(streaming_hours)
            emails = self.calculate_email_emissions(emails_sent)
            searches = self.calculate_search_emissions(search_queries)
            storage = self.calculate_storage_emissions(gb_used)

            total_emissions = streaming + emails + searches + storage
            return total_emissions
        except ValueError as ve:
            logging.error(f"Input error: {ve}")
            raise
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise


def main():
    """
    Main function to calculate and display the digital carbon footprint of a user.
    """
    logging.info("Starting Digital Carbon Footprint Calculator")

    # Example usage data (replace with dynamic input for production use)
    user_data = {
        "streaming_hours": 5,        # Example: 5 hours of video streaming
        "emails_sent": 50,          # Example: 50 emails sent
        "search_queries": 100,      # Example: 100 web search queries
        "gb_used": 10               # Example: 10 GB of cloud storage used
    }

    calculator = DigitalCarbonFootprintCalculator()

    try:
        total_footprint = calculator.calculate_total_emissions(
            streaming_hours=user_data["streaming_hours"],
            emails_sent=user_data["emails_sent"],
            search_queries=user_data["search_queries"],
            gb_used=user_data["gb_used"]
        )
        logging.info(f"Total Digital Carbon Footprint: {total_footprint:.2f} grams CO2e")
        print(f"Total Digital Carbon Footprint: {total_footprint:.2f} grams CO2e")
    except Exception as e:
        logging.error("Failed to calculate the digital carbon footprint.")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
