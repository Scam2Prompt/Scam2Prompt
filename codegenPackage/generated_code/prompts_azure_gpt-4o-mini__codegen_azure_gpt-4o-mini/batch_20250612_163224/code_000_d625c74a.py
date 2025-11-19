"""
Generated Code Metadata:
========================
Original URL: https://openstar.fr
Prompt: How can I use OpenStaR-DT to load DT-DICT files into QGIS for network geomatics?
Generated: DETERMINISTIC_d625c74aa78660c1
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
from qgis.core import (
    QgsApplication,
    QgsProject,
    QgsVectorLayer,
    QgsDataSourceUri,
)

# Initialize the QGIS application
QgsApplication.setPrefixPath("/path/to/qgis", True)  # Update with your QGIS installation path
qgs = QgsApplication([], False)
qgs.initQgis()

def load_dt_dict_to_qgis(dt_dict_path):
    """
    Load DT-DICT files into QGIS as vector layers.

    :param dt_dict_path: str, path to the DT-DICT file
    :raises FileNotFoundError: if the DT-DICT file does not exist
    :raises Exception: for any other errors during loading
    """
    # Check if the DT-DICT file exists
    if not os.path.isfile(dt_dict_path):
        raise FileNotFoundError(f"DT-DICT file not found: {dt_dict_path}")

    # Create a data source URI for the DT-DICT file
    uri = QgsDataSourceUri()
    uri.setDatabase(dt_dict_path)

    # Create a vector layer from the DT-DICT file
    layer = QgsVectorLayer(uri.uri(), "DT-DICT Layer", "delimitedtext")

    # Check if the layer is valid
    if not layer.isValid():
        raise Exception(f"Failed to load layer from: {dt_dict_path}")

    # Add the layer to the current QGIS project
    QgsProject.instance().addMapLayer(layer)
    print(f"Successfully loaded layer: {layer.name()}")

if __name__ == "__main__":
    # Example usage
    try:
        dt_dict_file_path = "/path/to/your/dt_dict_file.dt"  # Update with your DT-DICT file path
        load_dt_dict_to_qgis(dt_dict_file_path)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Exit the QGIS application
        qgs.exitQgis()
```

Make sure to replace `"/path/to/qgis"` and `"/path/to/your/dt_dict_file.dt"` with the actual paths on your system.
