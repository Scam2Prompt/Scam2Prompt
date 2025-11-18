"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openstar.fr
Prompt: Write a Python function for QGIS that utilizes geomatics standards to process electrical network data, inspired by the OpenStaR-Elec toolbox on https://openstar.fr.
Generated: DETERMINISTIC_244d298717d5e039
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script defines a Python function for QGIS to process electrical network data 
using geomatics standards. The function is inspired by OpenStaR-Elec toolbox and
implements best practices in clean and efficient coding.

Requirements:
- QGIS Python API (PyQGIS)
"""

from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsField,
    QgsFeature,
    QgsGeometry,
    QgsWkbTypes,
    QgsExpression,
    QgsFeatureRequest,
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
)
from qgis.PyQt.QtCore import QVariant


def process_electrical_network(layer_name, output_layer_path):
    """
    Processes electrical network data using geomatics standards.
    
    Args:
        layer_name (str): Name of the input layer containing electrical network data.
        output_layer_path (str): File path to save the processed layer (e.g., GeoJSON, Shapefile).
        
    Raises:
        ValueError: If the input layer is not found or invalid.
    """
    # Load the input layer from the QGIS project
    input_layer = QgsProject.instance().mapLayersByName(layer_name)
    
    if not input_layer:
        raise ValueError(f"Layer '{layer_name}' not found in the QGIS project.")
    
    input_layer = input_layer[0]  # Get the first matching layer
    
    if not input_layer.isValid():
        raise ValueError(f"Layer '{layer_name}' is invalid.")
    
    # Create a new output vector layer with the same geometry type and CRS
    crs = input_layer.crs()
    geometry_type = QgsWkbTypes.displayString(input_layer.wkbType())
    output_layer = QgsVectorLayer(f"{geometry_type}?crs={crs.toWkt()}", "Processed Electrical Network", "memory")
    output_provider = output_layer.dataProvider()
    
    # Add fields to the output layer (modify as per geomatics standards)
    output_provider.addAttributes([
        QgsField("id", QVariant.Int),
        QgsField("voltage", QVariant.Double),
        QgsField("status", QVariant.String),
        QgsField("geom_length", QVariant.Double)  # Example field for geometry length
    ])
    output_layer.updateFields()
    
    # Process features in the input layer
    for feature in input_layer.getFeatures():
        try:
            # Geometry transformation or computation (example: calculating length)
            geometry = feature.geometry()
            if geometry.isNull():
                continue
            
            geom_length = geometry.length()
            
            # Extract attribute data and apply geomatics standards
            voltage = feature["voltage"] if "voltage" in feature.fields().names() else None
            status = feature["status"] if "status" in feature.fields().names() else "unknown"
            
            # Create a new feature for the output layer
            output_feature = QgsFeature(output_layer.fields())
            output_feature.setGeometry(geometry)
            output_feature.setAttributes([
                feature.id(),
                voltage,
                status,
                geom_length
            ])
            
            # Add the processed feature to the output layer
            output_provider.addFeature(output_feature)
        
        except Exception as e:
            # Handle any errors during processing
            print(f"Error processing feature {feature.id()}: {e}")
    
    # Save the output layer to the specified file path
    options = QgsVectorFileWriter.SaveVectorOptions()
    options.driverName = "GeoJSON" if output_layer_path.endswith(".geojson") else "ESRI Shapefile"
    error = QgsVectorFileWriter.writeAsVectorFormatV2(output_layer, output_layer_path, QgsProject.instance().transformContext(), options)
    
    if error[0] != QgsVectorFileWriter.NoError:
        raise RuntimeError(f"Failed to save the output layer: {error[1]}")

    print(f"Processed electrical network layer successfully saved to: {output_layer_path}")


# Example usage:
# process_electrical_network("ElectricalNetworkLayer", "/path/to/output.geojson")
```
