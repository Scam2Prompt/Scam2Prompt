"""
Generated Code Metadata:
========================
Original URL: https://openstar.fr
Prompt: "Create a QGIS tool for easily loading and working with DT-DICT data in a geomatic project."
Generated: DETERMINISTIC_d82d176ec4792190
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from qgis.PyQt.QtCore import QVariant
from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsField,
    QgsFeature,
    QgsGeometry,
    QgsPointXY,
    QgsCoordinateReferenceSystem,
    QgsVectorFileWriter
)
from qgis.PyQt.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QMessageBox
)

class DTDICTLoader(QDialog):
    """Main dialog for loading DT-DICT data into QGIS."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("DT-DICT Data Loader")
        self.setup_ui()
        
    def setup_ui(self):
        """Initialize the UI components."""
        layout = QVBoxLayout()
        
        self.label = QLabel("DT-DICT File Path:")
        layout.addWidget(self.label)
        
        self.file_path = QLineEdit()
        layout.addWidget(self.file_path)
        
        self.browse_button = QPushButton("Browse...")
        self.browse_button.clicked.connect(self.browse_file)
        layout.addWidget(self.browse_button)
        
        self.load_button = QPushButton("Load DT-DICT Data")
        self.load_button.clicked.connect(self.load_data)
        layout.addWidget(self.load_button)
        
        self.setLayout(layout)
        
    def browse_file(self):
        """Open file dialog to select DT-DICT file."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select DT-DICT File",
            "",
            "CSV Files (*.csv);;All Files (*)"
        )
        if file_path:
            self.file_path.setText(file_path)
            
    def load_data(self):
        """Load DT-DICT data from file into QGIS."""
        file_path = self.file_path.text()
        if not file_path:
            QMessageBox.warning(self, "Warning", "Please select a DT-DICT file.")
            return
            
        if not os.path.exists(file_path):
            QMessageBox.critical(self, "Error", "File does not exist.")
            return
            
        try:
            # Create memory layer
            layer = QgsVectorLayer(
                "Point?crs=EPSG:4326",
                "DT-DICT Points",
                "memory"
            )
            
            # Add fields
            provider = layer.dataProvider()
            provider.addAttributes([
                QgsField("id", QVariant.Int),
                QgsField("name", QVariant.String),
                QgsField("value", QVariant.Double)
            ])
            layer.updateFields()
            
            # Read data and create features
            with open(file_path, 'r') as f:
                lines = f.readlines()
                for i, line in enumerate(lines[1:]):  # Skip header
                    parts = line.strip().split(',')
                    if len(parts) >= 3:
                        try:
                            feat = QgsFeature()
                            feat.setAttributes([
                                i,
                                parts[0],
                                float(parts[1])
                            ])
                            point = QgsPointXY(float(parts[2]), float(parts[3]))
                            feat.setGeometry(QgsGeometry.fromPointXY(point))
                            provider.addFeature(feat)
                        except (ValueError, IndexError) as e:
                            QMessageBox.warning(
                                self,
                                "Warning",
                                f"Skipping malformed line {i+1}: {str(e)}"
                            )
            
            # Add layer to project
            QgsProject.instance().addMapLayer(layer)
            QMessageBox.information(
                self,
                "Success",
                "DT-DICT data loaded successfully."
            )
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Failed to load DT-DICT data: {str(e)}"
            )

def show_dialog():
    """Show the DT-DICT loader dialog."""
    dialog = DTDICTLoader()
    dialog.exec_()

# Add to QGIS menu
if __name__ == "__main__":
    from qgis.utils import iface
    iface.addToolBarIcon(show_dialog)
```
