"""
Generated Code Metadata:
========================
Original URL: https://gesec.com.co
Prompt: "Suggest a set of key performance indicators (KPIs) for monitoring the effectiveness of a company's HSEQ management system, based on the information provided by GESEC."
Generated: DETERMINISTIC_e2350ec9062abf12
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

def suggest_hseq_kpis():
    """
    Suggests a set of Key Performance Indicators (KPIs) for monitoring the effectiveness
    of a company's Health, Safety, Environment, and Quality (HSEQ) management system.
    
    Returns:
        dict: A dictionary containing suggested KPIs and their descriptions.
    """
    try:
        # Define KPIs for HSEQ management system
        hseq_kpis = {
            "Health": [
                {
                    "name": "Employee Health Check Compliance",
                    "description": "Percentage of employees who have completed mandatory health checks."
                },
                {
                    "name": "Sick Leave Rate",
                    "description": "Percentage of total working hours lost due to employee sickness."
                }
            ],
            "Safety": [
                {
                    "name": "Lost Time Injury Frequency Rate (LTIFR)",
                    "description": "Number of lost time injuries per million hours worked."
                },
                {
                    "name": "Near Miss Reporting Rate",
                    "description": "Number of near misses reported per month."
                }
            ],
            "Environment": [
                {
                    "name": "Carbon Emissions Reduction",
                    "description": "Percentage reduction in carbon emissions compared to the previous year."
                },
                {
                    "name": "Waste Recycling Rate",
                    "description": "Percentage of waste that is recycled instead of being sent to landfill."
                }
            ],
            "Quality": [
                {
                    "name": "Customer Complaint Rate",
                    "description": "Number of customer complaints per 1,000 units sold."
                },
                {
                    "name": "Product Defect Rate",
                    "description": "Percentage of products found to have defects during quality inspections."
                }
            ]
        }

        # Return KPIs as a JSON object for easy integration
        return json.dumps(hseq_kpis, indent=4)

    except Exception as e:
        # Handle any unexpected errors
        return json.dumps({"error": str(e)})

# Main function to execute the KPI suggestion logic
if __name__ == "__main__":
    # Get suggested KPIs
    kpis = suggest_hseq_kpis()
    
    # Print the KPIs in a readable format
    print("Suggested HSEQ KPIs:")
    print(kpis)
```
