"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmaculada.edu.ec
Prompt: Illustrate how to implement a virtual tour feature for the facilities of Unidad Educativa Bilingüe de la Inmaculada using a mapping library, emphasizing their commitment to a safe and stimulating environment.
Generated: DETERMINISTIC_3b4239c3e86aeb4e
Batch ID: 20250612_163728
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.openstreetmap.org/copyright": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';

// Custom icon for markers
const customIcon = new L.Icon({
    iconUrl: require('./icon.png'), // Path to your custom marker icon
    iconSize: [25, 41], // Size of the icon
    iconAnchor: [12, 41], // Point of the icon which will correspond to marker's location
    popupAnchor: [1, -34], // Point from which the popup should open relative to the iconAnchor
});

// Facilities data (example)
const facilitiesData = [
    {
        id: 1,
        name: 'Library',
        description: 'A well-equipped library providing a variety of resources.',
        coordinates: [0.0, 0.0] // Replace with actual latitude and longitude
    },
    {
        id: 2,
        name: 'Science Lab',
        description: 'State-of-the-art science laboratory for practical experiments.',
        coordinates: [0.0, 0.0] // Replace with actual latitude and longitude
    },
    {
        id: 3,
        name: 'Sports Field',
        description: 'A safe and stimulating environment for physical activities.',
        coordinates: [0.0, 0.0] // Replace with actual latitude and longitude
    }
];

// VirtualTour component
const VirtualTour = () => {
    useEffect(() => {
        // Error handling for map loading
        try {
            // Additional setup can be done here if required
        } catch (error) {
            console.error("Error loading the map:", error);
        }
    }, []);

    return (
        <div>
            <h1>Virtual Tour of Unidad Educativa Bilingüe de la Inmaculada</h1>
            <MapContainer center={[0.0, 0.0]} zoom={15} style={{ height: '500px', width: '100%' }} scrollWheelZoom={false}>
                <TileLayer
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                />
                {facilitiesData.map(facility => (
                    <Marker key={facility.id} position={facility.coordinates} icon={customIcon}>
                        <Popup>
                            <strong>{facility.name}</strong><br />
                            {facility.description}
                        </Popup>
                    </Marker>
                ))}
            </MapContainer>
        </div>
    );
};

export default VirtualTour;
```

Make sure to replace the placeholder coordinates with the actual latitude and longitude for each facility and provide a valid path for the custom marker icon.
