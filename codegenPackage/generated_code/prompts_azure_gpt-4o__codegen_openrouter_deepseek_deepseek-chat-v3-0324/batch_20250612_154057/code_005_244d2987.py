"""
Generated Code Metadata:
========================
Original URL: https://openstar.fr
Prompt: Write a Python function for QGIS that utilizes geomatics standards to process electrical network data, inspired by the OpenStaR-Elec toolbox on https://openstar.fr.
Generated: DETERMINISTIC_244d298717d5e039
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import processing
from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsFeature,
    QgsGeometry,
    QgsField,
    QgsWkbTypes,
    QgsProcessingFeedback,
    QgsProcessingException
)
from PyQt5.QtCore import QVariant

def process_electrical_network(input_layer_path, output_path, voltage_level=None, max_distance=100):
    """
    Processes electrical network data according to geomatics standards.
    
    Args:
        input_layer_path (str): Path to the input vector layer (shapefile or GeoPackage)
        output_path (str): Path to save the processed output layer
        voltage_level (float, optional): Filter for specific voltage level (kV). Defaults to None.
        max_distance (float, optional): Maximum snapping distance for network connectivity (meters). Defaults to 100.
    
    Returns:
        str: Path to the processed output layer if successful, None otherwise
    
    Raises:
        QgsProcessingException: If processing fails
    """
    try:
        # Load input layer
        input_layer = QgsVectorLayer(input_layer_path, "input_network", "ogr")
        if not input_layer.isValid():
            raise QgsProcessingException("Invalid input layer")
        
        # Create output layer
        fields = input_layer.fields()
        if fields.indexOf("voltage") == -1:
            fields.append(QgsField("voltage", QVariant.Double))
        if fields.indexOf("length") == -1:
            fields.append(QgsField("length", QVariant.Double))
        
        output_layer = QgsVectorLayer(
            "LineString?crs={}".format(input_layer.crs().authid()),
            "processed_network",
            "memory"
        )
        output_layer.dataProvider().addAttributes(fields)
        output_layer.updateFields()
        
        # Process features
        feedback = QgsProcessingFeedback()
        parameters = {
            'INPUT': input_layer,
            'OUTPUT': 'memory:'
        }
        
        # Filter by voltage if specified
        if voltage_level is not None:
            parameters['EXPRESSION'] = f'"voltage" = {voltage_level}'
            result = processing.run("qgis:extractbyexpression", parameters, feedback=feedback)
            filtered_layer = result['OUTPUT']
        else:
            filtered_layer = input_layer
        
        # Snap geometries to ensure network connectivity
        snap_params = {
            'INPUT': filtered_layer,
            'REFERENCE_LAYER': filtered_layer,
            'TOLERANCE': max_distance,
            'BEHAVIOR': 0,  # Prefer aligning nodes
            'OUTPUT': 'memory:'
        }
        snapped_result = processing.run("qgis:snapgeometries", snap_params, feedback=feedback)
        snapped_layer = snapped_result['OUTPUT']
        
        # Calculate line lengths
        length_params = {
            'INPUT': snapped_layer,
            'OUTPUT': 'memory:'
        }
        length_result = processing.run("qgis:exportaddgeometrycolumns", length_params, feedback=feedback)
        length_layer = length_result['OUTPUT']
        
        # Save final output
        save_params = {
            'INPUT': length_layer,
            'OUTPUT': output_path,
            'LAYER_NAME': 'processed_network',
            'DATASOURCE_OPTIONS': 'OVERWRITE=YES'
        }
        
        if output_path.lower().endswith('.shp'):
            processing.run("qgis:exporttoshapefile", save_params, feedback=feedback)
        elif output_path.lower().endswith('.gpkg'):
            processing.run("qgis:package", {
                'LAYERS': [length_layer],
                'OUTPUT': output_path,
                'OVERWRITE': True
            }, feedback=feedback)
        else:
            raise QgsProcessingException("Unsupported output format")
        
        # Add layer to project
        QgsProject.instance().addMapLayer(QgsVectorLayer(output_path, "Processed Electrical Network", "ogr"))
        
        return output_path
    
    except Exception as e:
        raise QgsProcessingException(f"Error processing electrical network: {str(e)}")
```
