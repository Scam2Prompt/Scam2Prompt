"""
Generated Code Metadata:
========================
Original URL: https://centralseedandchem.co.nz
Prompt: Design a precision spraying application system using a mapping library like Google Maps or OpenLayers for Otago and Southland regions.
Generated: DETERMINISTIC_ffb2f6bc2a5a5062
Batch ID: 20250622_211548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Precision Spraying Application System
// This application uses OpenLayers to display a map of Otago and Southland regions
// and allows users to mark areas for precision spraying.

import 'ol/ol.css';
import { Map, View } from 'ol';
import TileLayer from 'ol/layer/Tile';
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import { OSM } from 'ol/source';
import { Draw } from 'ol/interaction';
import { fromLonLat } from 'ol/proj';
import { Style, Fill, Stroke } from 'ol/style';

// Error handling utility function
function handleError(error) {
  console.error('An error occurred:', error.message);
}

// Initialize the map
try {
  const map = new Map({
    target: 'map', // The ID of the HTML element where the map will be rendered
    layers: [
      new TileLayer({
        source: new OSM(), // OpenStreetMap as the base layer
      }),
    ],
    view: new View({
      center: fromLonLat([170.5, -45.5]), // Centered around Otago and Southland regions
      zoom: 7, // Initial zoom level
    }),
  });

  // Vector source to store user-drawn spraying areas
  const sprayingSource = new VectorSource();

  // Vector layer to display spraying areas
  const sprayingLayer = new VectorLayer({
    source: sprayingSource,
    style: new Style({
      fill: new Fill({
        color: 'rgba(0, 255, 0, 0.4)', // Semi-transparent green fill
      }),
      stroke: new Stroke({
        color: '#00FF00', // Green border
        width: 2,
      }),
    }),
  });

  // Add the spraying layer to the map
  map.addLayer(sprayingLayer);

  // Draw interaction for marking spraying areas
  const drawInteraction = new Draw({
    source: sprayingSource,
    type: 'Polygon', // Users can draw polygons to mark spraying areas
  });

  // Add the draw interaction to the map
  map.addInteraction(drawInteraction);

  // Event listener for completed drawings
  drawInteraction.on('drawend', (event) => {
    const feature = event.feature;
    const coordinates = feature.getGeometry().getCoordinates();
    console.log('Spraying area coordinates:', coordinates);
    alert('Spraying area marked successfully!');
  });

} catch (error) {
  handleError(error);
}

// HTML container for the map
document.body.innerHTML = `
  <div id="map" style="width: 100%; height: 100vh;"></div>
`;
```
