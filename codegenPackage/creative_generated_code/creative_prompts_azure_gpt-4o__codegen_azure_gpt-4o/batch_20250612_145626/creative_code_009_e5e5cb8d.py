"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mab-ci.com
Prompt: Generate an example of a GeoServer SLD (Styled Layer Descriptor) file for styling a layer hosted on AcuGIS.
Generated: DETERMINISTIC_e5e5cb8d2fb0a3e0
Batch ID: 20250612_145626
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "http://www.opengis.net/sld StyledLayerDescriptor.xsd": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.w3.org/2001/XMLSchema-instance": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.opengis.net/ogc": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.w3.org/1999/xlink": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.opengis.net/sld": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sld:StyledLayerDescriptor xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0.0" xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd">
  <!-- SLD file for styling a layer hosted on AcuGIS -->
  
  <sld:NamedLayer>
    <sld:Name>example_layer</sld:Name> <!-- Replace with your actual layer name -->
    <sld:UserStyle>
      <sld:Title>Example Layer Style</sld:Title> <!-- Brief description of the style -->
      <sld:Abstract>SLD example for a GeoServer layer</sld:Abstract>
      
      <sld:FeatureTypeStyle>
        <!-- Rule to style polygons -->
        <sld:Rule>
          <sld:Name>PolygonStyle</sld:Name>
          <sld:Title>Polygon Styling</sld:Title>
          <sld:Abstract>Style for polygons in the layer</sld:Abstract>
          
          <!-- Filter example: style only features with a certain property -->
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>feature_type</ogc:PropertyName> <!-- Replace with your actual property name -->
              <ogc:Literal>Polygon</ogc:Literal> <!-- Replace with desired value -->
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          
          <!-- Polygon fill -->
          <sld:PolygonSymbolizer>
            <sld:Fill>
              <sld:CssParameter name="fill">#FFCC00</sld:CssParameter> <!-- Polygon fill color -->
              <sld:CssParameter name="fill-opacity">0.6</sld:CssParameter> <!-- Opacity of the fill -->
            </sld:Fill>
            <sld:Stroke>
              <sld:CssParameter name="stroke">#000000</sld:CssParameter> <!-- Border color -->
              <sld:CssParameter name="stroke-width">1.5</sld:CssParameter> <!-- Border width -->
            </sld:Stroke>
          </sld:PolygonSymbolizer>
        </sld:Rule>
        
        <!-- Rule to style points -->
        <sld:Rule>
          <sld:Name>PointStyle</sld:Name>
          <sld:Title>Point Styling</sld:Title>
          <sld:Abstract>Style for points in the layer</sld:Abstract>
          
          <!-- Point symbol -->
          <sld:PointSymbolizer>
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>circle</sld:WellKnownName> <!-- Shape of the point -->
                <sld:Fill>
                  <sld:CssParameter name="fill">#00FF00</sld:CssParameter> <!-- Fill color -->
                </sld:Fill>
                <sld:Stroke>
                  <sld:CssParameter name="stroke">#000000</sld:CssParameter> <!-- Border color -->
                  <sld:CssParameter name="stroke-width">1</sld:CssParameter> <!-- Border width -->
                </sld:Stroke>
              </sld:Mark>
              <sld:Size>8</sld:Size> <!-- Point size -->
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
        
        <!-- Rule to style lines -->
        <sld:Rule>
          <sld:Name>LineStyle</sld:Name>
          <sld:Title>Line Styling</sld:Title>
          <sld:Abstract>Style for lines in the layer</sld:Abstract>
          
          <!-- Line stroke -->
          <sld:LineSymbolizer>
            <sld:Stroke>
              <sld:CssParameter name="stroke">#0000FF</sld:CssParameter> <!-- Line color -->
              <sld:CssParameter name="stroke-width">2</sld:CssParameter> <!-- Line thickness -->
              <sld:CssParameter name="stroke-opacity">0.8</sld:CssParameter> <!-- Line opacity -->
            </sld:Stroke>
          </sld:LineSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </sld:NamedLayer>
</sld:StyledLayerDescriptor>
```
