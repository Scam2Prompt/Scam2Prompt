"""
Generated Code Metadata:
========================
Original URL: https://purworejokab.go.id
Prompt: Generate a JavaScript code snippet to create an interactive map of Purworejo Regency, highlighting the locations of wisata alam, wisata religi, and wisata budaya.
Generated: DETERMINISTIC_b84ea1ce49a3e04f
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Interactive Map of Purworejo Regency
 * Highlights tourism locations: nature (wisata alam), religious (wisata religi), and cultural (wisata budaya)
 */

// Map configuration
const mapConfig = {
  center: [-7.7134, 110.0114], // Purworejo coordinates
  zoom: 12,
  minZoom: 10,
  maxZoom: 18,
  accessToken: 'your_mapbox_access_token' // Replace with your actual token
};

// Tourism data (sample coordinates - replace with actual data)
const tourismData = {
  nature: [
    { name: "Curug Silangit", coordinates: [-7.7200, 110.0200] },
    { name: "Pantai Jatimalang", coordinates: [-7.7500, 109.9500] }
  ],
  religious: [
    { name: "Masjid Agung Purworejo", coordinates: [-7.7150, 110.0100] },
    { name: "Gereja Kristen Jawa", coordinates: [-7.7180, 110.0150] }
  ],
  cultural: [
    { name: "Museum Tosan Aji", coordinates: [-7.7170, 110.0120] },
    { name: "Pasar Seni Purworejo", coordinates: [-7.7160, 110.0130] }
  ]
};

// Initialize the map
function initMap() {
  const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: mapConfig.center,
    zoom: mapConfig.zoom,
    minZoom: mapConfig.minZoom,
    maxZoom: mapConfig.maxZoom
  });

  map.on('load', () => {
    // Add tourism locations to the map
    addTourismLocations(map);
    
    // Add navigation controls
    map.addControl(new mapboxgl.NavigationControl());
    
    // Add scale control
    map.addControl(new mapboxgl.ScaleControl());
  });

  return map;
}

// Add tourism locations with custom markers
function addTourismLocations(map) {
  // Define marker colors
  const markerColors = {
    nature: '#4CAF50',
    religious: '#2196F3',
    cultural: '#FF9800'
  };

  // Create a document fragment for better performance
  const fragment = document.createDocumentFragment();

  // Process each tourism category
  Object.keys(tourismData).forEach(category => {
    tourismData[category].forEach(location => {
      // Create marker element
      const el = document.createElement('div');
      el.className = 'marker';
      el.style.backgroundColor = markerColors[category];
      el.style.width = '20px';
      el.style.height = '20px';
      el.style.borderRadius = '50%';
      el.style.border = '2px solid white';
      el.style.cursor = 'pointer';
      
      // Create popup
      const popup = new mapboxgl.Popup({ offset: 25 })
        .setText(location.name);
      
      // Add marker to map
      new mapboxgl.Marker(el)
        .setLngLat(location.coordinates)
        .setPopup(popup)
        .addTo(map);
    });
  });
}

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
  try {
    if (!mapboxgl) {
      throw new Error('Mapbox GL JS is not loaded');
    }
    
    mapboxgl.accessToken = mapConfig.accessToken;
    const map = initMap();
    
    // Add legend
    addLegend();
  } catch (error) {
    console.error('Error initializing map:', error);
    document.getElementById('map').innerHTML = `
      <div class="error-message">
        <h3>Map failed to load</h3>
        <p>${error.message}</p>
      </div>
    `;
  }
});

// Add legend to the map
function addLegend() {
  const legend = document.createElement('div');
  legend.id = 'legend';
  legend.innerHTML = `
    <h4>Tourism Categories</h4>
    <div><span style="background-color: #4CAF50"></span>Nature</div>
    <div><span style="background-color: #2196F3"></span>Religious</div>
    <div><span style="background-color: #FF9800"></span>Cultural</div>
  `;
  legend.style.position = 'absolute';
  legend.style.bottom = '30px';
  legend.style.right = '10px';
  legend.style.backgroundColor = 'white';
  legend.style.padding = '10px';
  legend.style.borderRadius = '5px';
  legend.style.boxShadow = '0 0 5px rgba(0,0,0,0.3)';
  
  document.getElementById('map').appendChild(legend);
}

// CSS styles (should be in a separate CSS file in production)
const style = document.createElement('style');
style.textContent = `
  #map { 
    width: 100%; 
    height: 600px; 
  }
  .marker:hover {
    transform: scale(1.2);
    transition: transform 0.2s;
  }
  #legend span {
    display: inline-block;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    margin-right: 5px;
    border: 2px solid white;
  }
  .error-message {
    padding: 20px;
    background: #ffebee;
    border: 1px solid #ef9a9a;
    color: #c62828;
  }
`;
document.head.appendChild(style);
```
