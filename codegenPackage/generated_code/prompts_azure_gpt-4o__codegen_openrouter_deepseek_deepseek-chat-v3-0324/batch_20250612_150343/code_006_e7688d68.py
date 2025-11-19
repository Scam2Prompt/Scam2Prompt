"""
Generated Code Metadata:
========================
Original URL: https://strk.site
Prompt: Write a Python script to generate a PDF report summarizing renovation project details, including design plans, cost estimates, and progress updates, inspired by the workflow described on the webpage.
Generated: DETERMINISTIC_e7688d68afa94e1f
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from datetime import datetime
from fpdf import FPDF
from typing import Dict, List, Optional

class RenovationProjectReport:
    """
    A class to generate a PDF report for a renovation project.
    """

    def __init__(self, project_name: str, client_name: str, report_date: Optional[str] = None):
        """
        Initialize the report with basic project information.
        
        Args:
            project_name: Name of the renovation project
            client_name: Name of the client
            report_date: Date of the report (defaults to current date)
        """
        self.project_name = project_name
        self.client_name = client_name
        self.report_date = report_date if report_date else datetime.now().strftime("%Y-%m-%d")
        self.pdf = FPDF()
        self.sections = []
        self.design_plans = []
        self.cost_estimates = []
        self.progress_updates = []

    def add_section(self, title: str, content: str):
        """
        Add a generic section to the report.
        
        Args:
            title: Title of the section
            content: Content of the section
        """
        self.sections.append({"title": title, "content": content})

    def add_design_plan(self, plan_name: str, description: str, image_path: Optional[str] = None):
        """
        Add a design plan to the report.
        
        Args:
            plan_name: Name of the design plan
            description: Description of the design
            image_path: Path to design image (optional)
        """
        self.design_plans.append({
            "plan_name": plan_name,
            "description": description,
            "image_path": image_path
        })

    def add_cost_estimate(self, item: str, description: str, cost: float):
        """
        Add a cost estimate item to the report.
        
        Args:
            item: Name of the item
            description: Description of the item
            cost: Estimated cost
        """
        self.cost_estimates.append({
            "item": item,
            "description": description,
            "cost": cost
        })

    def add_progress_update(self, date: str, update: str, completed: bool):
        """
        Add a progress update to the report.
        
        Args:
            date: Date of the update
            update: Description of the progress
            completed: Whether the task is completed
        """
        self.progress_updates.append({
            "date": date,
            "update": update,
            "completed": completed
        })

    def _add_header(self):
        """Add header to each page."""
        self.pdf.set_font("Arial", "B", 12)
        self.pdf.cell(0, 10, f"Renovation Project: {self.project_name}", 0, 1, "L")
        self.pdf.set_font("Arial", "", 10)
        self.pdf.cell(0, 10, f"Client: {self.client_name} | Report Date: {self.report_date}", 0, 1, "L")
        self.pdf.ln(5)

    def _add_footer(self):
        """Add footer to each page."""
        self.pdf.set_y(-15)
        self.pdf.set_font("Arial", "I", 8)
        self.pdf.cell(0, 10, f"Page {self.pdf.page_no()}", 0, 0, "C")

    def _add_section_content(self, title: str, content: str):
        """Add section content to the PDF."""
        self.pdf.set_font("Arial", "B", 12)
        self.pdf.cell(0, 10, title, 0, 1)
        self.pdf.set_font("Arial", "", 10)
        self.pdf.multi_cell(0, 8, content)
        self.pdf.ln(5)

    def _add_design_plans(self):
        """Add design plans section to the PDF."""
        self.pdf.set_font("Arial", "B", 14)
        self.pdf.cell(0, 10, "Design Plans", 0, 1)
        self.pdf.ln(5)

        for plan in self.design_plans:
            self.pdf.set_font("Arial", "B", 12)
            self.pdf.cell(0, 10, plan["plan_name"], 0, 1)
            self.pdf.set_font("Arial", "", 10)
            self.pdf.multi_cell(0, 8, plan["description"])
            
            if plan["image_path"] and os.path.exists(plan["image_path"]):
                try:
                    self.pdf.image(plan["image_path"], x=10, w=180)
                    self.pdf.ln(5)
                except Exception as e:
                    self.pdf.set_font("Arial", "I", 8)
                    self.pdf.cell(0, 8, f"Could not load image: {str(e)}", 0, 1)
                    self.pdf.set_font("Arial", "", 10)
            self.pdf.ln(5)

    def _add_cost_estimates(self):
        """Add cost estimates section to the PDF."""
        self.pdf.set_font("Arial", "B", 14)
        self.pdf.cell(0, 10, "Cost Estimates", 0, 1)
        self.pdf.ln(5)

        # Table header
        self.pdf.set_font("Arial", "B", 10)
        self.pdf.cell(60, 8, "Item", 1, 0)
        self.pdf.cell(80, 8, "Description", 1, 0)
        self.pdf.cell(30, 8, "Cost ($)", 1, 1)
        self.pdf.set_font("Arial", "", 10)

        total = 0
        for estimate in self.cost_estimates:
            self.pdf.cell(60, 8, estimate["item"], 1, 0)
            self.pdf.cell(80, 8, estimate["description"], 1, 0)
            self.pdf.cell(30, 8, f"{estimate['cost']:.2f}", 1, 1)
            total += estimate["cost"]

        # Total row
        self.pdf.set_font("Arial", "B", 10)
        self.pdf.cell(140, 8, "Total Estimated Cost", 1, 0)
        self.pdf.cell(30, 8, f"{total:.2f}", 1, 1)
        self.pdf.ln(5)

    def _add_progress_updates(self):
        """Add progress updates section to the PDF."""
        self.pdf.set_font("Arial", "B", 14)
        self.pdf.cell(0, 10, "Progress Updates", 0, 1)
        self.pdf.ln(5)

        for update in self.progress_updates:
            status = "Completed" if update["completed"] else "In Progress"
            self.pdf.set_font("Arial", "B", 10)
            self.pdf.cell(0, 8, f"{update['date']} - {status}", 0, 1)
            self.pdf.set_font("Arial", "", 10)
            self.pdf.multi_cell(0, 8, update["update"])
            self.pdf.ln(3)

    def generate_report(self, output_path: str):
        """
        Generate and save the PDF report.
        
        Args:
            output_path: Path to save the PDF file
            
        Raises:
            Exception: If PDF generation fails
        """
        try:
            self.pdf = FPDF()
            self.pdf.set_auto_page_break(auto=True, margin=15)
            self.pdf.add_page()
            
            # Set up header and footer
            self.pdf.alias_nb_pages()
            self._add_header()
            
            # Add project overview sections
            for section in self.sections:
                self._add_section_content(section["title"], section["content"])
            
            # Add specialized sections
            if self.design_plans:
                self._add_design_plans()
            
            if self.cost_estimates:
                self._add_cost_estimates()
            
            if self.progress_updates:
                self._add_progress_updates()
            
            # Add footer
            self._add_footer()
            
            # Save the PDF
            self.pdf.output(output_path)
            
        except Exception as e:
            raise Exception(f"Failed to generate PDF report: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a report instance
        report = RenovationProjectReport(
            project_name="Kitchen Remodel",
            client_name="John Smith",
            report_date="2023-11-15"
        )
        
        # Add project overview
        report.add_section(
            "Project Overview",
            "This project involves a complete kitchen remodel including new cabinets, countertops, and appliances."
        )
        
        # Add design plans
        report.add_design_plan(
            "Floor Plan",
            "Open concept layout with island and breakfast bar.",
