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
"""
OpenStaR-DT QGIS Plugin for loading DT-DICT files into QGIS for network geomatics.

This script provides functionality to load DT-DICT (Digital Twin - Digital Infrastructure for Cities and Territories)
files into QGIS as vector layers for network analysis and visualization.
"""

import os
from qgis.core import (
    QgsVectorLayer,
    QgsProject,
    QgsMessageLog,
    Qgis
)
from qgis.PyQt.QtWidgets import QMessageBox

def load_dt_dict_file(file_path, layer_name=None):
    """
    Load a DT-DICT file into QGIS as a vector layer.

    Args:
        file_path (str): Path to the DT-DICT file (GeoJSON, Shapefile, etc.)
        layer_name (str, optional): Name for the layer in QGIS. Defaults to basename of file.

    Returns:
        QgsVectorLayer: The loaded vector layer, or None if failed.
    """
    if not os.path.exists(file_path):
        QMessageBox.critical(
            None,
            "File Not Found",
            f"The specified file does not exist: {file_path}"
        )
        QgsMessageLog.logMessage(
            f"DT-DICT file not found: {file_path}",
            "OpenStaR-DT",
            Qgis.Critical
        )
        return None

    if layer_name is None:
        layer_name = os.path.splitext(os.path.basename(file_path))[0]

    # Supported file formats for DT-DICT
    supported_formats = {
        '.geojson': 'GeoJSON',
        '.shp': 'ESRI Shapefile',
        '.gpkg': 'GPKG'
    }

    file_ext = os.path.sitext(file_path)[1].lower()
    if file_ext not in supported_formats:
        QMessageBox.critical(
            None,
            "Unsupported Format",
            f"Unsupported file format: {file_ext}. Supported formats: {', '.join(supported_formats.keys())}"
        )
        return None

    provider_type = supported_formats[file_ext]
    layer = QgsVectorLayer(file_path, layer_name, 'ogr')

    if not layer.isValid():
        QMessageBox.critical(
            None,
            "Layer Error",
            f"Failed to load layer from {file_path}"
        )
        QgsMessageLog.logMessage(
            f"Failed to load DT-DICT layer from {file_path}. Error: {layer.error().message()}",
            "OpenStaR-DT",
            Qgis.Critical
        )
        return None

    QgsProject.instance().addMapLayer(layer)
    QgsMessageLog.logMessage(
        f"Successfully loaded DT-DICT layer: {layer_name} from {file_path}",
        "OpenStaR-DT",
        Qgis.Info
    )

    return layer

def load_dt_dict_files(file_paths):
    """
    Load multiple DT-DICT files into QGIS.

    Args:
        file_paths (list): List of file paths to load.

    Returns:
        list: List of successfully loaded layers.
    """
    loaded_layers = []
    for file_path in file_paths:
        layer = load_dt_dict_file(file_path)
        if layer:
            loaded_layers.append(layer)
    return loaded_layers

# Example usage (would typically be called from QGIS plugin UI)
if __name__ == "__test__":
    # Test loading a sample file
    test_file = "/path/to/your/dtdict_file.geojson"
    load_dt_dict_file(test_file, "Test DT-DICT Network")
```
