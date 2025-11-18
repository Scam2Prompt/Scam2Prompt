"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Write code in JavaScript to create an interactive map that divides a city into regions of approximately 4,500 residents, as described in the Programa Saúde da Família, and assigns healthcare teams to each region.
Generated: DETERMINISTIC_dd5a90c5146d84eb
Batch ID: 20250612_152358
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png": {
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
/**
 * Interactive map application to divide a city into regions with approximately 4,500 residents
 * and assign healthcare teams to each region based on the Programa Saúde da Família guidelines.
 *
 * Author: [Your Name]
 * Date: [Current Date]
 */

// Import necessary libraries (assuming you are using Leaflet.js for mapping)
import L from 'leaflet';

// Simulated city data (population per block)
const cityData = [
  { name: "Block A", population: 2000, coordinates: [40.7128, -74.0060] },
  { name: "Block B", population: 2500, coordinates: [40.7138, -74.0050] },
  { name: "Block C", population: 3000, coordinates: [40.7148, -74.0040] },
  { name: "Block D", population: 1500, coordinates: [40.7158, -74.0030] },
  { name: "Block E", population: 4000, coordinates: [40.7168, -74.0020] },
  // Add more blocks as needed
];

// Constants
const REGION_POPULATION_LIMIT = 4500; // Max population per region
const mapContainerId = "map"; // ID of the HTML container for the map

// Initialize the map
const map = L.map(mapContainerId).setView([40.7128, -74.0060], 13); // Default view centered on the first block

// Add base map layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Function to divide blocks into regions
function divideIntoRegions(data, populationLimit) {
  const regions = [];
  let currentRegion = { population: 0, blocks: [] };

  data.forEach(block => {
    if (currentRegion.population + block.population <= populationLimit) {
      // Add block to the current region
      currentRegion.blocks.push(block);
      currentRegion.population += block.population;
    } else {
      // Save the current region and start a new one
      regions.push(currentRegion);
      currentRegion = { population: block.population, blocks: [block] };
    }
  });

  // Add the last region if it contains blocks
  if (currentRegion.blocks.length > 0) {
    regions.push(currentRegion);
  }

  return regions;
}

// Divide the city into regions
const regions = divideIntoRegions(cityData, REGION_POPULATION_LIMIT);

// Assign healthcare teams to regions
regions.forEach((region, index) => {
  region.team = `Healthcare Team ${index + 1}`;
});

// Display regions on the map
regions.forEach(region => {
  const regionCoordinates = region.blocks.map(block => block.coordinates);

  // Create a polygon for the region
  const polygon = L.polygon(regionCoordinates, {
    color: 'blue',
    weight: 2,
    fillOpacity: 0.3
  }).addTo(map);

  // Add a popup to display region information
  polygon.bindPopup(`
    <strong>${region.team}</strong><br>
    Population: ${region.population}<br>
    Blocks: ${region.blocks.map(block => block.name).join(", ")}
  `);
});

// Error handling for map initialization
try {
  if (!map) {
    throw new Error("Failed to initialize the map.");
  }
} catch (error) {
  console.error("Error initializing map:", error.message);
}

// Ensure the map container exists
try {
  const mapContainer = document.getElementById(mapContainerId);
  if (!mapContainer) {
    throw new Error(`Map container with ID "${mapContainerId}" not found.`);
  }
} catch (error) {
  console.error("Error:", error.message);
}
```

**Note:** This code assumes the use of the Leaflet.js library, which is a popular JavaScript library for interactive mapping. You would need to include the appropriate script and style tags in your HTML to use Leaflet, as well as create a `div` with the `id="map"` for the map container.
