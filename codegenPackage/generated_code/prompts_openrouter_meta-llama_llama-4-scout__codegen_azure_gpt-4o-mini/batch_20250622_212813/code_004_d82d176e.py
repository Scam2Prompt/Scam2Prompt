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
from qgis.core import (
    QgsProcessingAlgorithm,
    QgsProcessingParameterFile,
    QgsProcessingParameterFeatureSink,
    QgsProcessingParameterString,
    QgsProcessingParameterBoolean,
    QgsFeature,
    QgsGeometry,
    QgsProject,
    QgsVectorLayer
)
from qgis.PyQt.QtCore import QVariant
import os

class LoadDTDictData(QgsProcessingAlgorithm):
    """
    A QGIS Processing Algorithm to load and work with DT-DICT data.
    """

    INPUT_FILE = 'INPUT_FILE'
    OUTPUT_LAYER = 'OUTPUT_LAYER'
    USE_GEOMETRY = 'USE_GEOMETRY'

    def initAlgorithm(self, self):
        """
        Define the parameters of the algorithm.
        """
        self.addParameter(QgsProcessingParameterFile(
            self.INPUT_FILE,
            'Input DT-DICT File',
            extension='txt'
        ))

        self.addParameter(QgsProcessingParameterBoolean(
            self.USE_GEOMETRY,
            'Use Geometry from DT-DICT',
            defaultValue=True
        ))

        self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT_LAYER,
            'Output Layer'
        ))

    def processAlgorithm(self, parameters, context, feedback):
        """
        The main processing method of the algorithm.
        """
        input_file = self.parameterAsFile(parameters, self.INPUT_FILE, context)
        use_geometry = self.parameterAsBool(parameters, self.USE_GEOMETRY, context)

        if not os.path.exists(input_file):
            raise ValueError(f"Input file does not exist: {input_file}")

        # Create a new vector layer for the output
        output_layer = QgsVectorLayer("Point?crs=EPSG:4326", "DT-DICT Data", "memory")
        provider = output_layer.dataProvider()

        # Add fields to the layer
        provider.addAttributes([
            QgsField("ID", QVariant.String),
            QgsField("Description", QVariant.String)
        ])
        output_layer.updateFields()

        # Read the DT-DICT file and populate the layer
        try:
            with open(input_file, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) < 2:
                        continue  # Skip malformed lines

                    feature = QgsFeature()
                    feature.setAttributes([parts[0], parts[1]])

                    if use_geometry:
                        # Assuming the geometry is provided in the file as "lat,lon"
                        if len(parts) >= 4:
                            lat = float(parts[2])
                            lon = float(parts[3])
                            feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(lon, lat)))

                    provider.addFeature(feature)

            output_layer.updateExtents()

            # Add the layer to the project
            QgsProject.instance().addMapLayer(output_layer)

            # Return the output layer
            return {self.OUTPUT_LAYER: output_layer.id()}

        except Exception as e:
            feedback.reportError(f"Error processing file: {str(e)}")
            return {}

    def name(self):
        return "LoadDTDictData"

    def displayName(self):
        return "Load DT-DICT Data"

    def group(self):
        return "Custom Tools"

    def groupId(self):
        return "custom_tools"

    def createInstance(self):
        return LoadDTDictData()
```
