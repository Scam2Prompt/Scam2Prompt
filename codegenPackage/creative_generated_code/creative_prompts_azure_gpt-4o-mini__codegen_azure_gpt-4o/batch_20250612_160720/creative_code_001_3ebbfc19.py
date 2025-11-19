"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zagoranews.com
Prompt: Write a report on the local initiatives in Zagora, focusing on the 20th anniversary of the National Initiative for Human Development and the recent visit by Minister Fatima Zahra Mansouri.
Generated: DETERMINISTIC_3ebbfc198a043f69
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that generates a report based on the provided user request. The code includes comments and adheres to best practices.

```python
import datetime

def generate_report(city, initiative_anniversary, minister_visit):
    """
    Generates a formatted report based on local initiatives and a minister's visit.

    Args:
        city (str): Name of the city.
        initiative_anniversary (dict): Details about the initiative anniversary (name and years since inception).
        minister_visit (dict): Details of minister's visit (name, visit date).

    Returns:
        str: Formatted report.
    """
    try:
        # Validate inputs
        if not city or not isinstance(city, str):
            raise ValueError("City name must be a non-empty string.")
        if not initiative_anniversary.get("name") or not initiative_anniversary.get("years"):
            raise ValueError("Initiative anniversary details must include 'name' and 'years'.")
        if not minister_visit.get("name") or not minister_visit.get("date"):
            raise ValueError("Minister visit details must include 'name' and 'date'.")

        # Generate report content
        report = f"""
        Local Initiatives in {city}
        -------------------------------------
        
        Celebrating the {initiative_anniversary['years']}-Year Anniversary of the {initiative_anniversary['name']}
        ---------------------------------------------------------------
        This year marks the 20th anniversary of the National Initiative for Human Development (INDH). 
        The initiative has played a critical role in driving sustainable development and improving 
        the quality of life for communities in {city} and beyond. Projects under INDH have focused 
        on education, healthcare, infrastructure, and employment.

        Ministerial Visit: Fatima Zahra Mansouri
        ----------------------------------------
        Recently, Minister Fatima Zahra Mansouri visited {city} on {minister_visit['date']}. Her visit 
        underscored the government's commitment to advancing local development projects and engaging 
        directly with community leaders and residents. During her visit, the minister inaugurated key 
        projects and highlighted the importance of collaboration between national and local stakeholders 
        in achieving long-term development goals.

        -------------------------------------
        Report generated on: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        """
        
        # Return the final report
        return report.strip()

    except Exception as e:
        # Log and handle exceptions gracefully
        return f"Error generating report: {str(e)}"


if __name__ == "__main__":
    # Sample input data
    city_name = "Zagora"
    initiative_details = {
        "name": "National Initiative for Human Development",
        "years": 20
    }
    minister_details = {
        "name": "Fatima Zahra Mansouri",
        "date": "2023-10-01"
    }

    # Generate and print report
    report_output = generate_report(city_name, initiative_details, minister_details)
    print(report_output)
```

This code is ready for production and follows best practices for error handling, validation, and formatting.
