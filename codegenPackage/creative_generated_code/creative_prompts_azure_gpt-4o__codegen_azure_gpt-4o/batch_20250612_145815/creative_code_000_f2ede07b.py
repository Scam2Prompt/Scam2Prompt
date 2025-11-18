"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reddecomercio.com
Prompt: Write Python code to automate import/export logistics management using the strategies outlined by Red de Comercio, including customs documentation and operational optimization.
Generated: DETERMINISTIC_f2ede07b9320f66b
Batch ID: 20250612_145815
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import os

# Constants for file paths and configurations
DOCUMENTATION_PATH = "customs_documents/"
EXPORT_RECORDS_FILE = "export_records.json"
IMPORT_RECORDS_FILE = "import_records.json"

# Helper Functions
def load_records(file_path):
    """
    Load records from a JSON file.
    :param file_path: Path to the JSON file.
    :return: List of records (empty list if file does not exist).
    """
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print(f"Error reading file: {file_path}")
        return []

def save_records(file_path, records):
    """
    Save records to a JSON file.
    :param file_path: Path to the JSON file.
    :param records: List of records to save.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(records, file, indent=4)
    except IOError:
        print(f"Error writing to file: {file_path}")

def generate_customs_document(order_id, operation_type, items):
    """
    Generate customs documentation for an order.
    :param order_id: Unique ID of the order.
    :param operation_type: Type of operation ('import' or 'export').
    :param items: List of items in the order.
    :return: File path to the generated document.
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    document_name = f"{operation_type}_customs_{order_id}_{timestamp}.txt"
    document_path = os.path.join(DOCUMENTATION_PATH, document_name)

    if not os.path.exists(DOCUMENTATION_PATH):
        os.makedirs(DOCUMENTATION_PATH)

    try:
        with open(document_path, 'w') as doc:
            doc.write(f"Customs Documentation\n")
            doc.write(f"Timestamp: {timestamp}\n")
            doc.write(f"Order ID: {order_id}\n")
            doc.write(f"Operation Type: {operation_type}\n\n")
            doc.write("Items:\n")
            for item in items:
                doc.write(f"- {item}\n")
        return document_path
    except IOError:
        print(f"Error generating customs document: {document_path}")
        return None

def add_record(file_path, record):
    """
    Add a record to the appropriate file (import or export).
    :param file_path: Path to the file for storing records.
    :param record: Record to add.
    """
    records = load_records(file_path)
    records.append(record)
    save_records(file_path, records)

# Main Automation Function
def process_order(order_id, operation_type, items):
    """
    Process logistics order (import/export).
    :param order_id: Unique ID of the order.
    :param operation_type: Type of operation ('import' or 'export').
    :param items: List of items in the order.
    """
    if operation_type not in ['import', 'export']:
        raise ValueError("Invalid operation type. Must be 'import' or 'export'.")

    # Generate customs documentation
    document_path = generate_customs_document(order_id, operation_type, items)
    if not document_path:
        print(f"Failed to generate customs documentation for order: {order_id}")
        return

    # Record the transaction
    record = {
        "order_id": order_id,
        "operation_type": operation_type,
        "items": items,
        "document_path": document_path,
        "timestamp": datetime.datetime.now().isoformat()
    }
    if operation_type == 'import':
        add_record(IMPORT_RECORDS_FILE, record)
    elif operation_type == 'export':
        add_record(EXPORT_RECORDS_FILE, record)

    print(f"Order processed successfully. Documentation saved at: {document_path}")

# Example Usage
if __name__ == "__main__":
    try:
        process_order(
            order_id="ORD12345",
            operation_type="export",
            items=["ItemA", "ItemB", "ItemC"]
        )
    except Exception as e:
        print(f"Error processing order: {e}")
```
