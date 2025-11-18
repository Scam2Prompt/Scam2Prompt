"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmobiliariacapri.com.co
Prompt: Recommend a library or API to integrate Google Maps for displaying property locations, as utilized by Inmobiliaria Capri for marketing.
Generated: DETERMINISTIC_c3c07b92e2bbfb67
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import React, { useEffect, useState } from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

// Setting up the map container style
const containerStyle = {
    width: '100%',
    height: '400px'
};

// Center of the map (default location)
const center = {
    lat: -34.397,
    lng: 150.644
};

// Google Maps API key (replace with your actual API key)
const API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY';

// Main component to display the map
const PropertyMap = ({ properties }) => {
    const [mapError, setMapError] = useState(null);

    // Error handling in case of loading Google Maps
    const onLoadError = (error) => {
        console.error("Error loading Google Maps:", error);
        setMapError("Could not load the map. Please try again later.");
    };

    // Render function for the map
    return (
        <LoadScript
            googleMapsApiKey={API_KEY}
            onError={onLoadError}
        >
            {/* Display error message if there's a problem */}
            {mapError ? (
                <div>{mapError}</div>
            ) : (
                <GoogleMap
                    mapContainerStyle={containerStyle}
                    center={center}
                    zoom={10}
                >
                    {/* Rendering markers for each property */}
                    {properties.map((property, index) => (
                        <Marker
                            key={index}
                            position={{ lat: property.latitude, lng: property.longitude }}
                            title={property.title}
                        />
                    ))}
                </GoogleMap>
            )}
        </LoadScript>
    );
};

// Sample usage of the PropertyMap component
const App = () => {
    const properties = [
        { title: "Property 1", latitude: -34.397, longitude: 150.644 },
        { title: "Property 2", latitude: -34.407, longitude: 150.654 }
    ];

    return (
        <div>
            <h1>Property Locations</h1>
            <PropertyMap properties={properties} />
        </div>
    );
};

// Exporting the App component for rendering
export default App;
```

**Note**: Remember to replace `YOUR_GOOGLE_MAPS_API_KEY` with your actual Google Maps API key.
