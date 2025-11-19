"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartenoir.org
Prompt: Write a Python script that automates the reporting of safety compliance metrics for a project, inspired by the methodologies used by Carte Noir Consulting.
Generated: DETERMINISTIC_a86793a665eb6442
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import datetime
import logging
import os

# Configure logging for the application
LOG_FILE = "safety_compliance_report.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants
SAFETY_METRICS_FILE = "safety_metrics.csv"  # Path to the safety metrics file
REPORT_OUTPUT_FILE = "compliance_report.txt"

# Sample thresholds for compliance
THRESHOLDS = {
    "Incident Rate": 1.5,  # Maximum acceptable incident rate
    "Training Completion": 95.0,  # Minimum acceptable percentage of training completion
    "Equipment Inspection Compliance": 90.0  # Minimum acceptable percentage
}

def load_metrics(file_path):
    """
    Load safety metrics from a CSV file.
    
    :param file_path: Path to the metrics CSV file.
    :return: List of dictionaries containing the metrics data.
    :raises FileNotFoundError: If the CSV file does not exist.
    :raises ValueError: If the CSV file is improperly formatted.
    """
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            metrics = [row for row in reader]
            return metrics
    except FileNotFoundError as e:
        logging.error(f"Metrics file not found: {file_path}")
        raise e
    except Exception as e:
        logging.error(f"Error loading metrics file: {file_path}")
        raise ValueError("Failed to parse CSV file.") from e


def evaluate_compliance(metrics):
    """
    Evaluate safety compliance based on predefined thresholds.
    
    :param metrics: List of dictionaries containing safety metrics.
    :return: List of compliance evaluation results.
    """
    results = []
    for metric in metrics:
        try:
            # Parse values and check compliance
            incident_rate = float(metric.get("Incident Rate", 0))
            training_completion = float(metric.get("Training Completion", 0))
            equipment_compliance = float(metric.get("Equipment Inspection Compliance", 0))
            
            # Determine compliance status
            compliance_status = {
                "Incident Rate": incident_rate <= THRESHOLDS["Incident Rate"],
                "Training Completion": training_completion >= THRESHOLDS["Training Completion"],
                "Equipment Inspection Compliance": equipment_compliance >= THRESHOLDS["Equipment Inspection Compliance"]
            }
            
            results.append({
                "Project": metric.get("Project", "Unknown"),
                "Incident Rate": f"{incident_rate} ({'Pass' if compliance_status['Incident Rate'] else 'Fail'})",
                "Training Completion": f"{training_completion}% ({'Pass' if compliance_status['Training Completion'] else 'Fail'})",
                "Equipment Inspection Compliance": f"{equipment_compliance}% ({'Pass' if compliance_status['Equipment Inspection Compliance'] else 'Fail'})"
            })
        except ValueError as e:
            logging.warning(f"Error evaluating compliance for project: {metric.get('Project', 'Unknown')}. Details: {e}")
            continue
    return results


def generate_report(compliance_results):
    """
    Generate a safety compliance report based on evaluation results.
    
    :param compliance_results: List of compliance evaluation results.
    :return: None
    """
    try:
        with open(REPORT_OUTPUT_FILE, mode='w') as file:
            file.write(f"Safety Compliance Report - Generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("=" * 80 + "\n\n")
            
            for result in compliance_results:
                file.write(f"Project: {result['Project']}\n")
                file.write(f"  Incident Rate: {result['Incident Rate']}\n")
                file.write(f"  Training Completion: {result['Training Completion']}\n")
                file.write(f"  Equipment Inspection Compliance: {result['Equipment Inspection Compliance']}\n")
                file.write("-" * 80 + "\n")
        
        logging.info(f"Compliance report generated successfully: {REPORT_OUTPUT_FILE}")
    except Exception as e:
        logging.error(f"Failed to generate compliance report. Details: {e}")
        raise


def main():
    """
    Main function to execute the safety compliance reporting workflow.
    """
    try:
        logging.info("Starting safety compliance reporting process.")
        
        # Step 1: Load metrics from CSV file
        metrics = load_metrics(SAFETY_METRICS_FILE)
        
        # Step 2: Evaluate compliance
        compliance_results = evaluate_compliance(metrics)
        
        # Step 3: Generate report
        generate_report(compliance_results)
        
        logging.info("Safety compliance reporting process completed successfully.")
    except Exception as e:
        logging.error(f"Safety compliance reporting process failed. Details: {e}")


if __name__ == "__main__":
    main()
```
