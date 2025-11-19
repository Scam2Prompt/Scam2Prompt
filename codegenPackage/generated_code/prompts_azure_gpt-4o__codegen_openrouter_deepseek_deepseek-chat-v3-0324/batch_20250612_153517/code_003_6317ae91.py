"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Create a script to automate the process of managing raw material inventory for high-performance cosmetic production, based on Fabricare Cosméticos' emphasis on advanced technology and rich active ingredients.
Generated: DETERMINISTIC_6317ae913246c583
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fabricare Cosméticos - Raw Material Inventory Management System

This script automates the process of managing raw material inventory for
high-performance cosmetic production, with emphasis on tracking advanced
technology ingredients and rich active compounds.
"""

import csv
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Union

import pandas as pd
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill


class RawMaterialInventory:
    """Core class for managing raw material inventory."""

    def __init__(self, inventory_file: str = "inventory.xlsx"):
        """
        Initialize inventory system.
        
        Args:
            inventory_file: Path to Excel inventory file (default: inventory.xlsx)
        """
        self.inventory_file = inventory_file
        self.required_columns = [
            "Material ID",
            "Name",
            "Category",
            "Supplier",
            "Quantity",
            "Unit",
            "Cost Per Unit",
            "Active Ingredient %",
            "Technology Type",
            "Last Updated",
            "Minimum Stock Level",
            "Lead Time (days)"
        ]
        self._initialize_inventory()

    def _initialize_inventory(self) -> None:
        """Create inventory file with required structure if it doesn't exist."""
        if not os.path.exists(self.inventory_file):
            wb = Workbook()
            ws = wb.active
            ws.title = "Raw Materials"
            
            # Add headers with styling
            header_font = Font(bold=True)
            header_fill = PatternFill(start_color="FFD700", end_color="FFD700", fill_type="solid")
            
            for col_num, header in enumerate(self.required_columns, 1):
                cell = ws.cell(row=1, column=col_num, value=header)
                cell.font = header_font
                cell.fill = header_fill
            
            wb.save(self.inventory_file)

    def _validate_material_data(self, material_data: Dict) -> bool:
        """Validate material data against required schema."""
        required_fields = {
            "Material ID": str,
            "Name": str,
            "Category": str,
            "Supplier": str,
            "Quantity": (int, float),
            "Unit": str,
            "Cost Per Unit": (int, float),
            "Active Ingredient %": (int, float),
            "Technology Type": str,
            "Minimum Stock Level": (int, float),
            "Lead Time (days)": int
        }
        
        for field, field_type in required_fields.items():
            if field not in material_data:
                print(f"Error: Missing required field '{field}'")
                return False
            
            if not isinstance(material_data[field], field_type):
                print(f"Error: Field '{field}' must be of type {field_type}")
                return False
        
        return True

    def add_material(self, material_data: Dict) -> bool:
        """
        Add new raw material to inventory.
        
        Args:
            material_data: Dictionary containing material information
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not self._validate_material_data(material_data):
            return False
            
        try:
            wb = load_workbook(self.inventory_file)
            ws = wb["Raw Materials"]
            
            # Check if material ID already exists
            for row in ws.iter_rows(min_row=2, max_col=1):
                if row[0].value == material_data["Material ID"]:
                    print(f"Error: Material ID {material_data['Material ID']} already exists")
                    return False
            
            # Add current timestamp
            material_data["Last Updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Append new row
            new_row = [material_data.get(col, "") for col in self.required_columns]
            ws.append(new_row)
            
            wb.save(self.inventory_file)
            return True
            
        except Exception as e:
            print(f"Error adding material: {str(e)}")
            return False

    def update_material(self, material_id: str, updates: Dict) -> bool:
        """
        Update existing material in inventory.
        
        Args:
            material_id: ID of material to update
            updates: Dictionary of fields to update
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            wb = load_workbook(self.inventory_file)
            ws = wb["Raw Materials"]
            
            found = False
            for row_idx, row in enumerate(ws.iter_rows(min_row=2), start=2):
                if row[0].value == material_id:
                    found = True
                    for col_idx, header in enumerate(self.required_columns, start=1):
                        if header in updates:
                            ws.cell(row=row_idx, column=col_idx, value=updates[header])
                    
                    # Update timestamp
                    ws.cell(row=row_idx, column=self.required_columns.index("Last Updated") + 1, 
                           value=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    break
            
            if not found:
                print(f"Error: Material ID {material_id} not found")
                return False
                
            wb.save(self.inventory_file)
            return True
            
        except Exception as e:
            print(f"Error updating material: {str(e)}")
            return False

    def get_material(self, material_id: str) -> Optional[Dict]:
        """
        Retrieve material information by ID.
        
        Args:
            material_id: ID of material to retrieve
            
        Returns:
            Optional[Dict]: Material data if found, None otherwise
        """
        try:
            wb = load_workbook(self.inventory_file)
            ws = wb["Raw Materials"]
            
            headers = [cell.value for cell in ws[1]]
            
            for row in ws.iter_rows(min_row=2):
                if row[0].value == material_id:
                    return {headers[i]: cell.value for i, cell in enumerate(row)}
            
            return None
            
        except Exception as e:
            print(f"Error retrieving material: {str(e)}")
            return None

    def list_materials(self, filter_criteria: Optional[Dict] = None) -> List[Dict]:
        """
        List all materials with optional filtering.
        
        Args:
            filter_criteria: Dictionary of field:value pairs to filter by
            
        Returns:
            List[Dict]: List of material dictionaries
        """
        try:
            wb = load_workbook(self.inventory_file)
            ws = wb["Raw Materials"]
            
            headers = [cell.value for cell in ws[1]]
            materials = []
            
            for row in ws.iter_rows(min_row=2):
                material = {headers[i]: cell.value for i, cell in enumerate(row)}
                
                if filter_criteria:
                    match = True
                    for field, value in filter_criteria.items():
                        if field not in material or material[field] != value:
                            match = False
                            break
                    if match:
                        materials.append(material)
                else:
                    materials.append(material)
            
            return materials
            
        except Exception as e:
            print(f"Error listing materials: {str(e)}")
            return []

    def check_low_stock(self) -> List[Dict]:
        """
        Check for materials below minimum stock level.
        
        Returns:
            List[Dict]: List of materials below minimum stock
        """
        try:
            materials = self.list_materials()
            low_stock = []
            
            for material in materials:
                if material["Quantity"] < material["Minimum Stock Level"]:
                    low_stock.append(material)
            
            return low_stock
            
        except Exception as e:
            print(f"Error checking stock levels: {str(e)}")
            return []

    def generate_report(self, report_type: str = "stock") -> bool:
        """
        Generate inventory reports.
        
        Args:
            report_type: Type of report to generate ('stock', 'active_ingredients', 'technology')
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            materials = self.list_materials()
            df = pd.DataFrame(materials)
            
            if report_type == "stock":
                report_df = df[["Material ID", "Name", "Quantity", "Minimum Stock Level", "Unit"]]
                report_df["Status"] = report_df.apply(
                    lambda x: "Low" if x["Quantity"] < x["Minimum Stock Level"] else "OK", axis=1
                )
                report_file = "inventory_stock_report.xlsx"
                
            elif report_type == "active_ingredients":
                report_df = df[["Material ID", "Name", "Active Ingredient %", "Category"]]
                report_df = report_df.sort_values("Active Ingredient %", ascending=False)
                report_file = "active_ingredients_report.xlsx"
                
            elif report_type == "technology":
                report_df = df[["Material ID", "Name", "Technology Type", "Supplier"]]
                report_df = report_df.groupby(["Technology Type", "Supplier"]).size().reset_index(name="Count")
                report_file =
