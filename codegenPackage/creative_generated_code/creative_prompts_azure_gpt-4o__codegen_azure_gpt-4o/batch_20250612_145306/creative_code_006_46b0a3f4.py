"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbicgroup.com
Prompt: Develop a program to track and visualize the supply chain for critical forgings and fabrication items for Indian Railways, leveraging the manufacturing expertise of Lalbaba Industrial Corporation Pvt. Ltd.
Generated: DETERMINISTIC_46b0a3f4e14fb42d
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Supply Chain Tracker and Visualizer for Indian Railways Forgings and Fabrications
# Developed leveraging manufacturing expertise of Lalbaba Industrial Corporation Pvt. Ltd.

import sqlite3  # For database management
import matplotlib.pyplot as plt  # For visualizing supply chain data
import logging  # For error handling and logging

# Configure logging
logging.basicConfig(filename='supply_chain.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Database Initialization
DATABASE_NAME = "supply_chain.db"

def initialize_database():
    """Initialize the SQLite database for storing supply chain data."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        # Create a table to store critical items
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS critical_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL,
                supplier_name TEXT NOT NULL,
                manufacturing_stage TEXT NOT NULL,
                delivery_date TEXT NOT NULL
            )
        """)
        conn.commit()
        logging.info("Database initialized successfully.")
    except sqlite3.Error as e:
        logging.error(f"Database initialization error: {e}")
    finally:
        conn.close()

def add_item(item_name, supplier_name, manufacturing_stage, delivery_date):
    """Add a new critical item to the database."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO critical_items (item_name, supplier_name, manufacturing_stage, delivery_date)
            VALUES (?, ?, ?, ?)
        """, (item_name, supplier_name, manufacturing_stage, delivery_date))
        conn.commit()
        logging.info(f"Item '{item_name}' added successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error adding item: {e}")
    finally:
        conn.close()

def get_all_items():
    """Retrieve all critical items from the database."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM critical_items")
        items = cursor.fetchall()
        logging.info("Fetched all items successfully.")
        return items
    except sqlite3.Error as e:
        logging.error(f"Error fetching items: {e}")
        return []
    finally:
        conn.close()

def visualize_supply_chain():
    """Visualize the supply chain data using a bar chart."""
    try:
        items = get_all_items()
        if not items:
            print("No data available for visualization.")
            return
        
        # Extracting data for visualization
        item_names = [item[1] for item in items]  # Item names
        stages = [item[3] for item in items]  # Manufacturing stages
        
        # Plotting
        plt.figure(figsize=(10, 6))
        plt.bar(item_names, range(len(item_names)), tick_label=stages, color='blue')
        plt.xlabel('Items', fontsize=12)
        plt.ylabel('Stages (Index)', fontsize=12)
        plt.title('Supply Chain Visualization', fontsize=14)
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.tight_layout()
        plt.show()
        logging.info("Visualization generated successfully.")
    except Exception as e:
        logging.error(f"Error generating visualization: {e}")

# Main Execution
if __name__ == "__main__":
    try:
        # Initialize the database
        initialize_database()

        # Add sample data (In production, this will come from user input or external systems)
        add_item("Forging Item A", "Supplier X", "Stage 1", "2023-11-15")
        add_item("Fabrication Item B", "Supplier Y", "Stage 2", "2023-12-01")

        # Display all items
        print("Supply Chain Inventory:")
        for item in get_all_items():
            print(item)
        
        # Visualize the supply chain
        visualize_supply_chain()

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
```
