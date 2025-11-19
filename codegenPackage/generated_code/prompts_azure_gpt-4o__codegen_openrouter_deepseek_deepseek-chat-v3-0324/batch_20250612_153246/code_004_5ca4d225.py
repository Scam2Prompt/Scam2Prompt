"""
Generated Code Metadata:
========================
Original URL: https://jauconsulting.com
Prompt: Write code to integrate business intelligence tools for automating report generation in engineering projects, as highlighted by Jau Consulting.
Generated: DETERMINISTIC_5ca4d225c6d78325
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from datetime import datetime
from typing import List, Dict, Optional
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, text
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bi_report_generation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class BIReportGenerator:
    """
    Business Intelligence Report Generator for Engineering Projects.
    """
    
    def __init__(self, db_connection_string: str):
        """
        Initialize the report generator with database connection.
        
        Args:
            db_connection_string: Database connection string
        """
        self.db_connection_string = db_connection_string
        self.engine = None
        self._connect_to_db()
        
    def _connect_to_db(self) -> None:
        """
        Establish connection to the database.
        """
        try:
            self.engine = create_engine(self.db_connection_string)
            logger.info("Successfully connected to the database")
        except Exception as e:
            logger.error(f"Failed to connect to database: {str(e)}")
            raise
            
    def _execute_query(self, query: str) -> pd.DataFrame:
        """
        Execute SQL query and return results as DataFrame.
        
        Args:
            query: SQL query to execute
            
        Returns:
            DataFrame containing query results
        """
        try:
            with self.engine.connect() as connection:
                result = pd.read_sql(text(query), connection)
                logger.info(f"Query executed successfully. Returned {len(result)} rows")
                return result
        except Exception as e:
            logger.error(f"Query execution failed: {str(e)}")
            raise
            
    def generate_project_metrics_report(self, project_ids: List[str], output_path: str) -> None:
        """
        Generate a comprehensive PDF report with project metrics.
        
        Args:
            project_ids: List of project IDs to include in report
            output_path: Path to save the generated PDF report
        """
        try:
            # Get project data
            projects_query = f"""
                SELECT project_id, project_name, start_date, end_date, budget, status 
                FROM projects 
                WHERE project_id IN ({','.join([f"'{pid}'" for pid in project_ids])})
            """
            projects_df = self._execute_query(projects_query)
            
            # Get task data
            tasks_query = f"""
                SELECT t.project_id, t.task_id, t.task_name, t.assigned_to, 
                       t.due_date, t.status, t.completion_percentage
                FROM tasks t
                JOIN projects p ON t.project_id = p.project_id
                WHERE t.project_id IN ({','.join([f"'{pid}'" for pid in project_ids])})
            """
            tasks_df = self._execute_query(tasks_query)
            
            # Get resource allocation data
            resources_query = f"""
                SELECT r.project_id, r.resource_name, r.resource_type, 
                       r.allocation_start, r.allocation_end, r.cost
                FROM resources r
                JOIN projects p ON r.project_id = p.project_id
                WHERE r.project_id IN ({','.join([f"'{pid}'" for pid in project_ids])})
            """
            resources_df = self._execute_query(resources_query)
            
            # Generate visualizations
            self._generate_visualizations(projects_df, tasks_df, resources_df, output_path)
            
            # Generate PDF report
            self._generate_pdf_report(projects_df, tasks_df, resources_df, output_path)
            
            logger.info(f"Report successfully generated at {output_path}")
            
        except Exception as e:
            logger.error(f"Failed to generate report: {str(e)}")
            raise
            
    def _generate_visualizations(self, projects_df: pd.DataFrame, 
                               tasks_df: pd.DataFrame, 
                               resources_df: pd.DataFrame,
                               output_path: str) -> None:
        """
        Generate visualizations for the report.
        """
        try:
            # Create output directory if it doesn't exist
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Project status distribution
            plt.figure(figsize=(8, 6))
            sns.countplot(data=projects_df, x='status', palette='viridis')
            plt.title('Project Status Distribution')
            plt.savefig(f"{output_path}_status.png", bbox_inches='tight')
            plt.close()
            
            # Task completion by project
            plt.figure(figsize=(10, 6))
            sns.barplot(data=tasks_df, x='project_id', y='completion_percentage', 
                        estimator=sum, ci=None, palette='mako')
            plt.title('Task Completion by Project')
            plt.xticks(rotation=45)
            plt.savefig(f"{output_path}_task_completion.png", bbox_inches='tight')
            plt.close()
            
            # Resource allocation cost
            plt.figure(figsize=(10, 6))
            sns.barplot(data=resources_df, x='project_id', y='cost', 
                        hue='resource_type', estimator=sum, ci=None)
            plt.title('Resource Allocation Cost by Project')
            plt.xticks(rotation=45)
            plt.savefig(f"{output_path}_resource_cost.png", bbox_inches='tight')
            plt.close()
            
        except Exception as e:
            logger.error(f"Failed to generate visualizations: {str(e)}")
            raise
            
    def _generate_pdf_report(self, projects_df: pd.DataFrame, 
                           tasks_df: pd.DataFrame, 
                           resources_df: pd.DataFrame,
                           output_path: str) -> None:
        """
        Generate PDF report with project metrics.
        """
        try:
            doc = SimpleDocTemplate(output_path, pagesize=letter)
            elements = []
            styles = getSampleStyleSheet()
            
            # Add title
            elements.append(Paragraph("Engineering Projects Report", styles['Title']))
            elements.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 
                                    styles['Normal']))
            elements.append(Paragraph(" ", styles['Normal']))  # Spacer
            
            # Add project summary
            elements.append(Paragraph("Project Summary", styles['Heading2']))
            project_table_data = [list(projects_df.columns)] + projects_df.values.tolist()
            project_table = Table(project_table_data)
            project_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            elements.append(project_table)
            elements.append(Paragraph(" ", styles['Normal']))  # Spacer
            
            # Add task summary
            elements.append(Paragraph("Task Summary", styles['Heading2']))
            task_table_data = [list(tasks_df.columns)] + tasks_df.values.tolist()
            task_table = Table(task_table_data)
            task_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            elements.append(task_table)
            elements.append(Paragraph(" ", styles['Normal']))  # Spacer
            
            # Add resource summary
            elements.append(Paragraph("Resource Allocation Summary", styles['Heading2']))
            resource_table_data = [list(resources_df.columns)] + resources_df.values.tolist
