"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://salesstudios.com
Prompt: Create a Python script to calculate ROI for email marketing campaigns, using metrics like open rates and sales revenue increases, similar to Sales Studios' case studies.
Generated: DETERMINISTIC_4de12088785f91e4
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to handle unexpected errors and track runtime behavior
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("email_marketing_roi.log"), logging.StreamHandler()]
)

def calculate_roi(email_campaign_cost, total_sales_revenue, email_open_rate):
    """
    Calculate the Return on Investment (ROI) for an email marketing campaign.

    Args:
        email_campaign_cost (float): Total cost of the email marketing campaign.
        total_sales_revenue (float): The total sales revenue generated from the campaign.
        email_open_rate (float): Percentage of recipients who opened the email (0-100).

    Returns:
        dict: A dictionary containing ROI percentage and other calculated metrics.
    """
    try:
        # Validate input
        if email_campaign_cost <= 0:
            raise ValueError("Email campaign cost must be greater than zero.")
        if total_sales_revenue < 0:
            raise ValueError("Total sales revenue cannot be negative.")
        if not (0 <= email_open_rate <= 100):
            raise ValueError("Email open rate must be between 0 and 100.")
        
        # Calculate ROI percentage
        roi_percentage = ((total_sales_revenue - email_campaign_cost) / email_campaign_cost) * 100

        metrics = {
            "email_campaign_cost": email_campaign_cost,
            "total_sales_revenue": total_sales_revenue,
            "email_open_rate": email_open_rate,
            "roi_percentage": roi_percentage
        }

        return metrics
    
    except Exception as e:
        logging.error(f"Error calculating ROI: {e}")
        raise


def main():
    """
    Main function to collect user input, calculate ROI, and display results.
    """
    logging.info("Starting the email marketing ROI calculator.")

    try:
        # Collecting input from the user
        email_campaign_cost = float(input("Enter the total cost of the email campaign: "))
        total_sales_revenue = float(input("Enter the total sales revenue generated from the campaign: "))
        email_open_rate = float(input("Enter the email open rate (in %): "))

        # Calculate ROI
        roi_metrics = calculate_roi(email_campaign_cost, total_sales_revenue, email_open_rate)

        # Display results
        print("\n--- ROI Calculation Results ---")
        print(f"Email Campaign Cost: ${roi_metrics['email_campaign_cost']:.2f}")
        print(f"Total Sales Revenue: ${roi_metrics['total_sales_revenue']:.2f}")
        print(f"Email Open Rate: {roi_metrics['email_open_rate']:.2f}%")
        print(f"ROI Percentage: {roi_metrics['roi_percentage']:.2f}%")
        logging.info("ROI calculation completed successfully.")
    
    except ValueError as ve:
        logging.error(f"Invalid input: {ve}")
        print(f"Input Error: {ve}")
    except Exception as e:
        logging.critical(f"Unexpected error: {e}")
        print("An unexpected error occurred. Please check the logs for more details.")
    finally:
        logging.info("Program execution finished.")


if __name__ == "__main__":
    main()
```
