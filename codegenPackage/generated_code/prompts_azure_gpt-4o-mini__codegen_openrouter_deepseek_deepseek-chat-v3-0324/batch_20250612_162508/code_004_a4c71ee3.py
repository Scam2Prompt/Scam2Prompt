"""
Generated Code Metadata:
========================
Original URL: https://chhatrapatitimes.com
Prompt: Summarize the findings of the transport department's recent inspection of school buses, including the number of buses checked and the revenue collected from fines.
Generated: DETERMINISTIC_a4c71ee3e09b88f0
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Tuple, Dict, Any

def get_inspection_summary(db_path: str) -> Dict[str, Any]:
    """
    Retrieves the summary of school bus inspections from the database.
    
    Args:
        db_path (str): Path to the SQLite database file.
        
    Returns:
        Dict[str, Any]: A dictionary containing:
            - 'total_buses_checked': Total number of buses inspected
            - 'total_revenue': Total revenue collected from fines
            - 'details': List of inspection details (bus_id, fine_amount, violation)
            
    Raises:
        sqlite3.Error: If there's an error accessing the database.
    """
    summary = {
        'total_buses_checked': 0,
        'total_revenue': 0.0,
        'details': []
    }
    
    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get total number of buses checked
        cursor.execute("SELECT COUNT(DISTINCT bus_id) FROM inspections")
        summary['total_buses_checked'] = cursor.fetchone()[0]
        
        # Get total revenue from fines
        cursor.execute("SELECT SUM(fine_amount) FROM inspections")
        total_revenue = cursor.fetchone()[0]
        summary['total_revenue'] = total_revenue if total_revenue else 0.0
        
        # Get inspection details
        cursor.execute("""
            SELECT bus_id, fine_amount, violation 
            FROM inspections 
            WHERE fine_amount > 0
            ORDER BY bus_id
        """)
        summary['details'] = [
            {'bus_id': row[0], 'fine_amount': row[1], 'violation': row[2]}
            for row in cursor.fetchall()
        ]
        
    except sqlite3.Error as e:
        raise sqlite3.Error(f"Database error: {e}")
    finally:
        if conn:
            conn.close()
    
    return summary

def generate_report(summary: Dict[str, Any]) -> str:
    """
    Generates a human-readable report from the inspection summary.
    
    Args:
        summary (Dict[str, Any]): The inspection summary dictionary
        
    Returns:
        str: Formatted report string
    """
    report = [
        "School Bus Inspection Report",
        "==========================",
        f"Total Buses Checked: {summary['total_buses_checked']}",
        f"Total Revenue from Fines: ${summary['total_revenue']:,.2f}",
        "\nDetailed Findings:"
    ]
    
    if not summary['details']:
        report.append("No fines were issued during this inspection period.")
    else:
        for detail in summary['details']:
            report.append(
                f"Bus {detail['bus_id']}: ${detail['fine_amount']:,.2f} "
                f"for {detail['violation']}"
            )
    
    return "\n".join(report)

def main():
    """Main function to generate and print the inspection report."""
    try:
        # In a real application, this would be a configurable path
        db_path = "transport_inspections.db"
        summary = get_inspection_summary(db_path)
        report = generate_report(summary)
        print(report)
    except sqlite3.Error as e:
        print(f"Error generating report: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
