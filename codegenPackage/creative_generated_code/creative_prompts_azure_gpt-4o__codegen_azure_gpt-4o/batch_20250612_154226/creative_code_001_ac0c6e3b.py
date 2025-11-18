"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sunsystems.hk
Prompt: Generate code to create a custom financial report using Infor SunSystems advanced reporting capabilities, tailored for Hong Kong businesses.
Generated: DETERMINISTIC_ac0c6e3bb2054cfb
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import datetime
import logging
import pymssql  # Database driver for MS SQL Server

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

# Constants for database connection
DB_HOST = "your_database_host"
DB_PORT = 1433
DB_USER = "your_db_user"
DB_PASSWORD = "your_db_password"
DB_NAME = "your_db_name"

# Report configuration
REPORT_OUTPUT_DIR = "./reports"
REPORT_NAME = f"Financial_Report_HongKong_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.json"

def fetch_financial_data(cursor):
    """
    Fetch financial data tailored for Hong Kong businesses.
    :param cursor: Database cursor object
    :return: List of rows containing financial data
    """
    query = """
    SELECT 
        AccountNumber, 
        AccountName, 
        TransactionDate, 
        Amount, 
        Currency, 
        Location 
    FROM FinancialRecords
    WHERE Location = 'Hong Kong'
    ORDER BY TransactionDate DESC;
    """
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        logging.error(f"Error fetching financial data: {str(e)}")
        return []

def generate_report(data):
    """
    Generate a JSON financial report based on data.
    :param data: List of rows containing financial data
    :return: Filepath of the generated report
    """
    try:
        # Ensure output directory exists
        os.makedirs(REPORT_OUTPUT_DIR, exist_ok=True)
        report_path = os.path.join(REPORT_OUTPUT_DIR, REPORT_NAME)

        # Transform data into the desired format
        report_data = [
            {
                "AccountNumber": row[0],
                "AccountName": row[1],
                "TransactionDate": row[2].strftime("%Y-%m-%d"),
                "Amount": row[3],
                "Currency": row[4],
                "Location": row[5],
            }
            for row in data
        ]

        # Write to JSON file
        with open(report_path, "w", encoding="utf-8") as report_file:
            json.dump(report_data, report_file, ensure_ascii=False, indent=4)

        logging.info(f"Report generated successfully: {report_path}")
        return report_path
    except Exception as e:
        logging.error(f"Error generating report: {str(e)}")
        return None

def main():
    """
    Main function to fetch financial data and generate a report.
    """
    try:
        # Connect to the database
        connection = pymssql.connect(
            server=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT
        )
        cursor = connection.cursor()

        logging.info("Fetching financial data...")
        financial_data = fetch_financial_data(cursor)

        if not financial_data:
            logging.warning("No financial data found for Hong Kong businesses.")
            return

        logging.info("Generating report...")
        report_path = generate_report(financial_data)

        if report_path:
            logging.info(f"Report available at: {report_path}")
        else:
            logging.error("Failed to generate the report.")

    except pymssql.DatabaseError as db_error:
        logging.error(f"Database connection error: {str(db_error)}")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
    finally:
        # Ensure connection is closed properly
        try:
            if connection:
                connection.close()
                logging.info("Database connection closed.")
        except Exception as e:
            logging.error(f"Error closing database connection: {str(e)}")

if __name__ == "__main__":
    main()
```
