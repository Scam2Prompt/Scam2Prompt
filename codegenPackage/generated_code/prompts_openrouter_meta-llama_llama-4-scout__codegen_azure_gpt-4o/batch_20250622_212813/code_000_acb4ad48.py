"""
Generated Code Metadata:
========================
Original URL: https://openstar.fr
Prompt: "Write a QGIS plugin to load DT-DICT data for network analysis using geostandards."
Generated: DETERMINISTIC_acb4ad48a6e3dfea
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
"""
DT-DICT Loader Plugin for QGIS
This plugin loads DT-DICT data for network analysis using geostandards.
"""

from qgis.PyQt.QtCore import QCoreApplication, QVariant
from qgis.PyQt.QtWidgets import QAction, QMessageBox, QFileDialog
from qgis.core import (
    QgsVectorLayer,
    QgsField,
    QgsProject,
    QgsFeature,
    QgsGeometry,
    QgsMessageLog
)
import os
import csv

class DTDictLoaderPlugin:
    def __init__(self, iface):
        """
        Constructor for the plugin.
        :param iface: QGIS interface instance.
        """
        self.iface = iface
        self.plugin_menu_action = None

    def initGui(self):
        """
        Initialize the GUI components of the plugin.
        """
        self.plugin_menu_action = QAction("Load DT-DICT Data", self.iface.mainWindow())
        self.plugin_menu_action.triggered.connect(self.load_dt_dict_data)
        self.iface.addPluginToMenu("&DT-DICT Loader", self.plugin_menu_action)

    def unload(self):
        """
        Unload the plugin and remove its GUI components.
        """
        self.iface.removePluginMenu("&DT-DICT Loader", self.plugin_menu_action)

    def load_dt_dict_data(self):
        """
        Load DT-DICT data from a CSV file and create a vector layer for network analysis.
        """
        try:
            # Open file dialog to select the DT-DICT CSV file
            file_path, _ = QFileDialog.getOpenFileName(
                self.iface.mainWindow(),
                "Select DT-DICT CSV File",
                "",
                "CSV Files (*.csv)"
            )

            if not file_path:
                QMessageBox.warning(self.iface.mainWindow(), "No File Selected", "Please select a valid CSV file.")
                return

            # Create a new memory layer for the data
            layer = QgsVectorLayer("LineString?crs=EPSG:4326", "DT-DICT Network", "memory")
            if not layer.isValid():
                raise Exception("Failed to create memory layer.")

            # Define fields for the layer
            layer_data_provider = layer.dataProvider()
            layer_data_provider.addAttributes([
                QgsField("ID", QVariant.Int),
                QgsField("StartNode", QVariant.String),
                QgsField("EndNode", QVariant.String),
                QgsField("Length", QVariant.Double)
            ])
            layer.updateFields()

            # Read the CSV file and populate the layer
            with open(file_path, "r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    try:
                        # Extract data from the CSV row
                        feature_id = int(row["ID"])
                        start_node = row["StartNode"]
                        end_node = row["EndNode"]
                        length = float(row["Length"])
                        start_x = float(row["StartX"])
                        start_y = float(row["StartY"])
                        end_x = float(row["EndX"])
                        end_y = float(row["EndY"])

                        # Create a feature with geometry and attributes
                        feature = QgsFeature()
                        feature.setGeometry(QgsGeometry.fromPolylineXY([
                            QgsPointXY(start_x, start_y),
                            QgsPointXY(end_x, end_y)
                        ]))
                        feature.setAttributes([feature_id, start_node, end_node, length])

                        # Add the feature to the layer
                        layer_data_provider.addFeature(feature)
                    except Exception as e:
                        QgsMessageLog.logMessage(f"Error processing row: {e}", "DT-DICT Loader", level=QgsMessageLog.CRITICAL)

            # Add the layer to the QGIS project
            QgsProject.instance().addMapLayer(layer)
            QMessageBox.information(self.iface.mainWindow(), "Success", "DT-DICT data loaded successfully.")
        except Exception as e:
            QMessageBox.critical(self.iface.mainWindow(), "Error", f"An error occurred: {e}")

# Required QGIS plugin functions
def classFactory(iface):
    """
    Entry point for the plugin.
    :param iface: QGIS interface instance.
    :return: Plugin instance.
    """
    return DTDictLoaderPlugin(iface)
```
