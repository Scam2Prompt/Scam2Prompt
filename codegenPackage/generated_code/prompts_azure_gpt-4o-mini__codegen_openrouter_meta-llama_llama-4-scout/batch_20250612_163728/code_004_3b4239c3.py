"""
Generated Code Metadata:
========================
Original URL: https://inmaculada.edu.ec
Prompt: Illustrate how to implement a virtual tour feature for the facilities of Unidad Educativa Bilingüe de la Inmaculada using a mapping library, emphasizing their commitment to a safe and stimulating environment.
Generated: DETERMINISTIC_3b4239c3e86aeb4e
Batch ID: 20250612_163728
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://osm.org/copyright": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import { MapContainer, TileLayer, Marker, Polyline } from 'react-leaflet';
import L from 'leaflet';

// Define the facilities of Unidad Educativa Bilingüe de la Inmaculada
const facilities = [
  {
    id: 1,
    name: 'Main Building',
    lat: 0.2253,
    lng: -78.1242,
  },
  {
    id: 2,
    name: 'Library',
    lat: 0.2245,
    lng: -78.1235,
  },
  {
    id: 3,
    name: 'Sports Field',
    lat: 0.2261,
    lng: -78.1251,
  },
];

// Define the virtual tour feature
function VirtualTour() {
  const [currentFacility, setCurrentFacility] = useState(facilities[0]);
  const [mapCenter, setMapCenter] = useState([currentFacility.lat, currentFacility.lng]);
  const [polyline, setPolyline] = useState([]);

  // Function to handle facility navigation
  const navigateToFacility = (facility) => {
    setCurrentFacility(facility);
    setMapCenter([facility.lat, facility.lng]);
  };

  // Function to draw a polyline between facilities
  const drawPolyline = () => {
    const points = facilities.map((facility) => [facility.lat, facility.lng]);
    setPolyline(points);
  };

  useEffect(() => {
    drawPolyline();
  }, []);

  // Error handling for map loading
  const [mapError, setMapError] = useState(null);
  const handleMapError = (error) => {
    setMapError(error.message);
  };

  return (
    <div>
      <h1>Virtual Tour of Unidad Educativa Bilingüe de la Inmaculada</h1>
      {mapError && <p style={{ color: 'red' }}>{mapError}</p>}
      <MapContainer
        center={mapCenter}
        zoom={15}
        style={{ width: '800px', height: '600px' }}
        onError={handleMapError}
      >
        <TileLayer
          attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
        />
        {facilities.map((facility) => (
          <Marker
            key={facility.id}
            position={[facility.lat, facility.lng]}
            onClick={() => navigateToFacility(facility)}
          >
            <div>
              <h3>{facility.name}</h3>
              <p>Latitude: {facility.lat}</p>
              <p>Longitude: {facility.lng}</p>
            </div>
          </Marker>
        ))}
        {polyline.length > 0 && (
          <Polyline latLngs={polyline} color='blue' />
        )}
      </MapContainer>
      <ul>
        {facilities.map((facility) => (
          <li key={facility.id}>
            <button onClick={() => navigateToFacility(facility)}>
              {facility.name}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

// Render the virtual tour feature
ReactDOM.render(
  <React.StrictMode>
    <VirtualTour />
  </React.StrictMode>,
  document.getElementById('root')
);
```
