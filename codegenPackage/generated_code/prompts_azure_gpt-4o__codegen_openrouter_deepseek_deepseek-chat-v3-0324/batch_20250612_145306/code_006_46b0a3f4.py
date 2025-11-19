"""
Generated Code Metadata:
========================
Original URL: https://lbicgroup.com
Prompt: Develop a program to track and visualize the supply chain for critical forgings and fabrication items for Indian Railways, leveraging the manufacturing expertise of Lalbaba Industrial Corporation Pvt. Ltd.
Generated: DETERMINISTIC_46b0a3f4e14fb42d
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from datetime import datetime
import logging
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='supply_chain_tracker.log'
)
logger = logging.getLogger(__name__)

class SupplyChainTracker:
    """
    A class to track and visualize the supply chain for critical forgings and fabrication items.
    """
    
    def __init__(self):
        """
        Initialize the supply chain tracker with empty data structures.
        """
        self.supply_chain_data = pd.DataFrame(columns=[
            'item_id', 'item_name', 'supplier', 'manufacturer', 
            'current_stage', 'quantity', 'target_date', 'status'
        ])
        self.suppliers = set()
        self.manufacturers = set()
        self.stages = ['Raw Material', 'Forging', 'Fabrication', 'Quality Check', 'Delivery']
        
    def add_item(
        self,
        item_id: str,
        item_name: str,
        supplier: str,
        manufacturer: str,
        quantity: int,
        target_date: str
    ) -> None:
        """
        Add a new item to the supply chain tracker.
        
        Args:
            item_id: Unique identifier for the item
            item_name: Name/description of the item
            supplier: Supplier name
            manufacturer: Manufacturer name
            quantity: Quantity of items
            target_date: Target completion date (YYYY-MM-DD)
        """
        try:
            # Validate date format
            datetime.strptime(target_date, '%Y-%m-%d')
            
            new_item = {
                'item_id': item_id,
                'item_name': item_name,
                'supplier': supplier,
                'manufacturer': manufacturer,
                'current_stage': 'Raw Material',
                'quantity': quantity,
                'target_date': target_date,
                'status': 'On Track'
            }
            
            self.supply_chain_data = pd.concat(
                [self.supply_chain_data, pd.DataFrame([new_item])],
                ignore_index=True
            )
            
            self.suppliers.add(supplier)
            self.manufacturers.add(manufacturer)
            
            logger.info(f"Added new item: {item_id} - {item_name}")
            
        except ValueError as e:
            logger.error(f"Invalid date format for item {item_id}: {e}")
            raise ValueError("Date must be in YYYY-MM-DD format")
        except Exception as e:
            logger.error(f"Error adding item {item_id}: {e}")
            raise

    def update_stage(self, item_id: str, new_stage: str) -> None:
        """
        Update the current stage of an item in the supply chain.
        
        Args:
            item_id: ID of the item to update
            new_stage: New stage to move the item to
        """
        try:
            if new_stage not in self.stages:
                raise ValueError(f"Invalid stage. Must be one of: {', '.join(self.stages)}")
                
            mask = self.supply_chain_data['item_id'] == item_id
            if not any(mask):
                raise ValueError(f"Item {item_id} not found in supply chain")
                
            self.supply_chain_data.loc[mask, 'current_stage'] = new_stage
            
            # Update status based on target date
            item = self.supply_chain_data[mask].iloc[0]
            target_date = datetime.strptime(item['target_date'], '%Y-%m-%d')
            days_remaining = (target_date - datetime.now()).days
            
            if new_stage == 'Delivery':
                self.supply_chain_data.loc[mask, 'status'] = 'Completed'
            elif days_remaining < 0:
                self.supply_chain_data.loc[mask, 'status'] = 'Delayed'
            elif days_remaining < 7 and new_stage != 'Delivery':
                self.supply_chain_data.loc[mask, 'status'] = 'At Risk'
                
            logger.info(f"Updated item {item_id} to stage: {new_stage}")
            
        except Exception as e:
            logger.error(f"Error updating stage for item {item_id}: {e}")
            raise

    def get_supply_chain_status(self) -> pd.DataFrame:
        """
        Get the current status of all items in the supply chain.
        
        Returns:
            DataFrame containing the current status of all items
        """
        return self.supply_chain_data.copy()

    def visualize_supply_chain(self, output_file: str = 'supply_chain.png') -> None:
        """
        Generate a visualization of the supply chain network.
        
        Args:
            output_file: Path to save the visualization image
        """
        try:
            plt.figure(figsize=(12, 8))
            
            # Create a directed graph
            G = nx.DiGraph()
            
            # Add nodes for each stage
            for stage in self.stages:
                G.add_node(stage, color='lightblue', shape='box')
                
            # Add edges between stages
            for i in range(len(self.stages)-1):
                G.add_edge(self.stages[i], self.stages[i+1])
                
            # Add supplier and manufacturer nodes
            for supplier in self.suppliers:
                G.add_node(supplier, color='lightgreen', shape='ellipse')
                G.add_edge(supplier, 'Raw Material')
                
            for manufacturer in self.manufacturers:
                G.add_node(manufacturer, color='orange', shape='ellipse')
                G.add_edge('Fabrication', manufacturer)
                
            # Node colors and shapes
            colors = [G.nodes[node]['color'] for node in G.nodes()]
            shapes = [G.nodes[node]['shape'] for node in G.nodes()]
            
            # Draw the graph
            pos = nx.spring_layout(G, seed=42)
            nx.draw(
                G, pos, with_labels=True, 
                node_color=colors, node_size=2000,
                font_size=10, font_weight='bold',
                arrowsize=20
            )
            
            plt.title("Indian Railways Critical Forgings Supply Chain")
            plt.tight_layout()
            plt.savefig(output_file)
            plt.close()
            
            logger.info(f"Supply chain visualization saved to {output_file}")
            
        except Exception as e:
            logger.error(f"Error generating supply chain visualization: {e}")
            raise

    def generate_status_report(self, output_file: str = 'status_report.xlsx') -> None:
        """
        Generate an Excel report with the current status of all items.
        
        Args:
            output_file: Path to save the Excel report
        """
        try:
            # Create a Pandas Excel writer
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                # Overall status
                status_summary = self.supply_chain_data.groupby('status').size().reset_index(name='count')
                status_summary.to_excel(writer, sheet_name='Status Summary', index=False)
                
                # Detailed view
                self.supply_chain_data.to_excel(writer, sheet_name='Detailed View', index=False)
                
                # Items by stage
                stage_summary = self.supply_chain_data.groupby('current_stage').size().reset_index(name='count')
                stage_summary.to_excel(writer, sheet_name='Stage Summary', index=False)
                
            logger.info(f"Status report generated at {output_file}")
            
        except Exception as e:
            logger.error(f"Error generating status report: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        tracker = SupplyChainTracker()
        
        # Add sample items
        tracker.add_item(
            item_id="IR-FG-001",
            item_name="Bogie Frame Forgings",
            supplier="Steel India Ltd.",
            manufacturer="Lalbaba Industrial Corporation Pvt. Ltd.",
            quantity=50,
            target_date="2023-12-15"
        )
        
        tracker.add_item(
            item_id="IR-FG-002",
            item_name="Coupler Forgings",
            supplier="Metallica Steels",
            manufacturer="Lalbaba Industrial Corporation Pvt. Ltd.",
            quantity=100,
            target_date="2023-11-30"
        )
        
        # Update stages
        tracker.update_stage("IR-FG-001", "Forging")
        tracker.update_stage("IR-FG-002", "Fabrication")
        
        # Generate outputs
        print(tracker.get_supply_chain_status())
        tracker.visualize_supply_chain()
        tracker.generate_status_report()
        
    except Exception as e:
        logger.error(f"Error in main execution: {e}")
        raise
```
