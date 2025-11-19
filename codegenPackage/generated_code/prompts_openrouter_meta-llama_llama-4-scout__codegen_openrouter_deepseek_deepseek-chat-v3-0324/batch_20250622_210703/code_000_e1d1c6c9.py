"""
Generated Code Metadata:
========================
Original URL: https://aasteeldetailing.co.uk.steel-edge.co.uk
Prompt: "Generate a Python script to automate steel detailing services, including take-off services and connection design, for a construction project."
Generated: DETERMINISTIC_e1d1c6c9f9920c77
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import csv
import json
import math
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment


@dataclass
class SteelMember:
    """Represents a steel member with its properties."""
    id: str
    type: str
    length: float
    weight: float
    quantity: int
    connection_type: Optional[str] = None


@dataclass
class ConnectionDesign:
    """Represents connection design details."""
    member_id: str
    connection_type: str
    bolt_count: int
    bolt_size: str
    plate_thickness: float


class SteelDetailingAutomation:
    """Automates steel detailing services including take-off and connection design."""
    
    def __init__(self):
        self.members: List[SteelMember] = []
        self.connections: List[ConnectionDesign] = []
    
    def load_members_from_csv(self, file_path: str) -> None:
        """Load steel members from a CSV file.
        
        Args:
            file_path: Path to the CSV file containing member data.
            
        Raises:
            FileNotFoundError: If the file doesn't exist.
            ValueError: If the file is malformed.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.members.append(SteelMember(
                        id=row['id'],
                        type=row['type'],
                        length=float(row['length']),
                        weight=float(row['weight']),
                        quantity=int(row['quantity']),
                        connection_type=row.get('connection_type')
                    ))
        except Exception as e:
            raise ValueError(f"Error reading CSV file: {str(e)}")
    
    def calculate_total_weight(self) -> float:
        """Calculate total weight of all steel members.
        
        Returns:
            Total weight in the same unit as member weights.
        """
        return sum(member.weight * member.length * member.quantity for member in self.members)
    
    def generate_material_takeoff(self) -> Dict[str, float]:
        """Generate material take-off summary.
        
        Returns:
            Dictionary with material types and their total weights.
        """
        takeoff = {}
        for member in self.members:
            if member.type not in takeoff:
                takeoff[member.type] = 0
            takeoff[member.type] += member.weight * member.length * member.quantity
        return takeoff
    
    def design_connections(self, connection_rules: Dict[str, Dict]) -> None:
        """Design connections based on predefined rules.
        
        Args:
            connection_rules: Dictionary containing connection design rules.
        """
        self.connections.clear()
        for member in self.members:
            if member.connection_type and member.connection_type in connection_rules:
                rule = connection_rules[member.connection_type]
                self.connections.append(ConnectionDesign(
                    member_id=member.id,
                    connection_type=member.connection_type,
                    bolt_count=rule['bolt_count'],
                    bolt_size=rule['bolt_size'],
                    plate_thickness=rule['plate_thickness']
                ))
    
    def export_takeoff_to_excel(self, output_path: str) -> None:
        """Export material take-off to Excel file.
        
        Args:
            output_path: Path to save the Excel file.
        """
        takeoff = self.generate_material_takeoff()
        
        wb = Workbook()
        ws = wb.active
        ws.title = "Material Takeoff"
        
        # Write headers
        headers = ["Material Type", "Total Weight"]
        for col_num, header in enumerate(headers, 1):
            cell = ws.cell(row=1, column=col_num, value=header)
            cell.font = Font(bold=True)
        
        # Write data
        for row_num, (material_type, weight) in enumerate(takeoff.items(), 2):
            ws.cell(row=row_num, column=1, value=material_type)
            ws.cell(row=row_num, column=2, value=weight)
        
        # Format columns
        for column in ws.columns:
            max_length = 0
            column = [cell for cell in column]
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = (max_length + 2) * 1.2
            ws.column_dimensions[column[0].column_letter].width = adjusted_width
        
        wb.save(output_path)
    
    def export_connections_to_json(self, output_path: str) -> None:
        """Export connection designs to JSON file.
        
        Args:
            output_path: Path to save the JSON file.
        """
        connections_data = []
        for connection in self.connections:
            connections_data.append({
                'member_id': connection.member_id,
                'connection_type': connection.connection_type,
                'bolt_count': connection.bolt_count,
                'bolt_size': connection.bolt_size,
                'plate_thickness': connection.plate_thickness
            })
        
        with open(output_path, 'w') as f:
            json.dump(connections_data, f, indent=4)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the automation tool
        steel_detailing = SteelDetailingAutomation()
        
        # Load members from CSV
        steel_detailing.load_members_from_csv("steel_members.csv")
        
        # Calculate total weight
        total_weight = steel_detailing.calculate_total_weight()
        print(f"Total steel weight: {total_weight:.2f} kg")
        
        # Generate material take-off
        takeoff = steel_detailing.generate_material_takeoff()
        print("Material Take-off:")
        for material, weight in takeoff.items():
            print(f"{material}: {weight:.2f} kg")
        
        # Design connections
        connection_rules = {
            "moment_connection": {
                "bolt_count": 8,
                "bolt_size": "M24",
                "plate_thickness": 12.0
            },
            "shear_connection": {
                "bolt_count": 4,
                "bolt_size": "M20",
                "plate_thickness": 10.0
            }
        }
        steel_detailing.design_connections(connection_rules)
        
        # Export reports
        steel_detailing.export_takeoff_to_excel("material_takeoff.xlsx")
        steel_detailing.export_connections_to_json("connection_designs.json")
        
        print("Steel detailing completed successfully.")
    
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
