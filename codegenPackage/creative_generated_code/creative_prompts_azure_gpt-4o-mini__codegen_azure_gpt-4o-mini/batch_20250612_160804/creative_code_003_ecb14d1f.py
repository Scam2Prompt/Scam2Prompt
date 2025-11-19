"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opennet.net
Prompt: Develop a JavaScript application that displays the OpenNet Initiative's social media filtering map, highlighting regions with significant restrictions.
Generated: DETERMINISTIC_ecb14d1fb0465224
Batch ID: 20250612_160804
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://opennetinitiative.github.io/filtering-map/data/countries.json": {
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
import React, { useEffect, useState } from 'react';

// Define a functional component for the Social Media Filtering Map
const SocialMediaFilteringMap = () => {
    // State to hold map data
    const [mapData, setMapData] = useState([]);
    const [error, setError] = useState(null);

    // Fetch map data from OpenNet Initiative API
    const fetchMapData = async () => {
        try {
            const response = await fetch('https://opennetinitiative.github.io/filtering-map/data/countries.json');
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const data = await response.json();
            setMapData(data);
        } catch (err) {
            setError(err.message);
        }
    };

    // Use useEffect for fetching the map data on component mount
    useEffect(() => {
        fetchMapData();
    }, []);

    // Render the map or error message if present
    return (
        <div>
            <h1>OpenNet Initiative Social Media Filtering Map</h1>
            {error ? (
                <div className="error">
                    <p>Error fetching data: {error}</p>
                </div>
            ) : (
                <div className="map-container">
                    {/* Here you can integrate a map library to visually represent mapData */}
                    <ul>
                        {mapData.map((region) => (
                            <li key={region.name}>
                                {region.name}: {region.restrictions}
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
};

// Export the component for use in other parts of the application
export default SocialMediaFilteringMap;

// Styles (Assuming CSS-in-JS or use of external stylesheet)
// .error { color: red; }
// .map-container { padding: 20px; }
```
