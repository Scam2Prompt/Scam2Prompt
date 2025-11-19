"""
Generated Code Metadata:
========================
Original URL: https://colegiodepsicologosoruro.org
Prompt: Create a data visualization dashboard using Tableau or Power BI to showcase the activities and events organized by the Colegio de Psicologos de Oruro.
Generated: DETERMINISTIC_d688658faa33811a
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Since you're requesting code for a data visualization dashboard in Tableau or Power BI, I'll provide a Python script that prepares and processes the data for such a dashboard. This script assumes you'll export the processed data to CSV/Excel for use in Tableau/Power BI.

```python
import pandas as pd
import numpy as np
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='dashboard_data_prep.log'
)

class DashboardDataProcessor:
    """
    Processes raw event data for Colegio de Psicologos de Oruro dashboard.
    Outputs cleaned data ready for visualization in Tableau/Power BI.
    """
    
    def __init__(self, raw_data_path):
        """
        Initialize with path to raw data file.
        
        Args:
            raw_data_path (str): Path to Excel/CSV file containing raw event data
        """
        self.raw_data_path = raw_data_path
        self.df = None
        self.processed_data = None
        
    def load_data(self):
        """
        Load raw data from file with error handling.
        """
        try:
            if self.raw_data_path.endswith('.xlsx'):
                self.df = pd.read_excel(self.raw_data_path)
            elif self.raw_data_path.endswith('.csv'):
                self.df = pd.read_csv(self.raw_data_path)
            else:
                raise ValueError("Unsupported file format. Please provide .xlsx or .csv")
                
            logging.info(f"Successfully loaded data from {self.raw_data_path}")
            return True
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            return False
    
    def clean_data(self):
        """
        Clean and transform raw data into analysis-ready format.
        """
        try:
            # Standardize column names
            self.df.columns = self.df.columns.str.strip().str.lower().str.replace(' ', '_')
            
            # Convert date columns to datetime
            if 'fecha' in self.df.columns:
                self.df['fecha'] = pd.to_datetime(self.df['fecha'], errors='coerce')
            
            # Fill missing values
            self.df.fillna({
                'participantes': 0,
                'duracion_horas': 0,
                'costo': 0
            }, inplace=True)
            
            # Add derived columns
            self.df['año'] = self.df['fecha'].dt.year
            self.df['mes'] = self.df['fecha'].dt.month_name()
            self.df['trimestre'] = self.df['fecha'].dt.quarter
            
            logging.info("Data cleaning completed successfully")
            return True
        except Exception as e:
            logging.error(f"Error cleaning data: {str(e)}")
            return False
    
    def calculate_metrics(self):
        """
        Calculate key metrics for dashboard visualization.
        """
        try:
            metrics = {
                'total_eventos': len(self.df),
                'total_participantes': self.df['participantes'].sum(),
                'total_horas': self.df['duracion_horas'].sum(),
                'eventos_por_tipo': self.df['tipo_evento'].value_counts().to_dict(),
                'participantes_por_tipo': self.df.groupby('tipo_evento')['participantes'].sum().to_dict(),
                'eventos_por_mes': self.df.groupby(['año', 'mes']).size().reset_index(name='count'),
                'participantes_por_mes': self.df.groupby(['año', 'mes'])['participantes'].sum().reset_index()
            }
            
            self.processed_data = {
                'raw_data': self.df,
                'metrics': metrics
            }
            
            logging.info("Metrics calculation completed")
            return True
        except Exception as e:
            logging.error(f"Error calculating metrics: {str(e)}")
            return False
    
    def export_data(self, output_path):
        """
        Export processed data to CSV/Excel for dashboard consumption.
        
        Args:
            output_path (str): Path to save processed data
        """
        try:
            if output_path.endswith('.xlsx'):
                with pd.ExcelWriter(output_path) as writer:
                    self.df.to_excel(writer, sheet_name='Eventos', index=False)
                    pd.DataFrame.from_dict(self.processed_data['metrics']['eventos_por_mes']).to_excel(
                        writer, sheet_name='EventosPorMes', index=False
                    )
                    pd.DataFrame.from_dict(self.processed_data['metrics']['participantes_por_mes']).to_excel(
                        writer, sheet_name='ParticipantesPorMes', index=False
                    )
            elif output_path.endswith('.csv'):
                self.df.to_csv(output_path.replace('.csv', '_eventos.csv'), index=False)
                pd.DataFrame.from_dict(self.processed_data['metrics']['eventos_por_mes']).to_csv(
                    output_path.replace('.csv', '_eventos_mes.csv'), index=False
                )
                pd.DataFrame.from_dict(self.processed_data['metrics']['participantes_por_mes']).to_csv(
                    output_path.replace('.csv', '_participantes_mes.csv'), index=False
                )
            
            logging.info(f"Data exported successfully to {output_path}")
            return True
        except Exception as e:
            logging.error(f"Error exporting data: {str(e)}")
            return False
    
    def process(self, output_path):
        """
        Complete data processing pipeline.
        
        Args:
            output_path (str): Path to save processed data
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.load_data():
            return False
        if not self.clean_data():
            return False
        if not self.calculate_metrics():
            return False
        if not self.export_data(output_path):
            return False
        return True


if __name__ == "__main__":
    # Example usage
    processor = DashboardDataProcessor('datos_crudos_eventos.xlsx')
    if processor.process('datos_procesados_dashboard.xlsx'):
        print("Data processing completed successfully")
    else:
        print("Data processing failed. Check logs for details.")
```
