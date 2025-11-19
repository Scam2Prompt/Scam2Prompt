"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openstar.fr
Prompt: How can I use OpenStaR-DT to load DT-DICT files into QGIS for network geomatics?
Generated: DETERMINISTIC_d625c74aa78660c1
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to use OpenStaR-DT to load DT-DICT files into QGIS
for network geomatics. Ensure you have OpenStaR-DT installed and configured
properly along with QGIS Python API (PyQGIS) available in your environment.

Author: [Your Name]
"""

import os
from qgis.core import (
    QgsApplication,
    QgsVectorLayer,
    QgsProject,
    QgsMessageLog
)
import star_dt  # OpenStaR-DT Python library

def load_dt_dict_to_qgis(dict_file_path, qgis_project_path):
    """
    Load a DT-DICT file into QGIS as a vector layer.

    Args:
        dict_file_path (str): Path to the DT-DICT file.
        qgis_project_path (str): Path to the QGIS project file (.qgz) to save the results.
    """
    try:
        # Verify DT-DICT file existence
        if not os.path.isfile(dict_file_path):
            raise FileNotFoundError(f"DT-DICT file not found: {dict_file_path}")

        # Initialize QGIS application
        qgs = QgsApplication([], False)
        qgs.initQgis()
        QgsMessageLog.logMessage("Initialized QGIS application.", tag="OpenStaR-DT")

        # Use OpenStaR-DT to load the DT-DICT file
        dt_layer = star_dt.load_dt_dict(dict_file_path)
        if dt_layer is None:
            raise ValueError("Failed to load DT-DICT file using OpenStaR-DT.")

        # Convert the loaded DT-DICT data into a QGIS-compatible layer
        vector_layer = QgsVectorLayer(dt_layer, "DT-DICT Layer", "memory")
        if not vector_layer.isValid():
            raise ValueError("The resulting vector layer is invalid.")

        # Add the vector layer to QGIS project
        QgsProject.instance().addMapLayer(vector_layer)
        QgsMessageLog.logMessage(f"Added layer: {vector_layer.name()}", tag="OpenStaR-DT")

        # Save QGIS project
        QgsProject.instance().write(qgis_project_path)
        QgsMessageLog.logMessage(f"Saved QGIS project: {qgis_project_path}", tag="OpenStaR-DT")

    except Exception as e:
        QgsMessageLog.logMessage(f"Error: {e}", level=Qgis.MessageLevel.Critical, tag="OpenStaR-DT")
    finally:
        # Clean up and exit QGIS application
        qgs.exitQgis()


# Example Usage
if __name__ == "__main__":
    # Path to DT-DICT file
    dt_dict_file = "/path/to/your/dt_dict_file.dict"
    
    # Path to save updated QGIS project
    qgis_project_file = "/path/to/your/project.qgz"

    # Load DT-DICT and add it to QGIS project
    load_dt_dict_to_qgis(dt_dict_file, qgis_project_file)
```

Note:
1. Replace `/path/to/your/dt_dict_file.dict` and `/path/to/your/project.qgz` with appropriate file paths.
2. Make sure OpenStaR-DT and PyQGIS are installed and configured in your environment.
3. Logging is done using `QgsMessageLog` for better integration into QGIS logs.
