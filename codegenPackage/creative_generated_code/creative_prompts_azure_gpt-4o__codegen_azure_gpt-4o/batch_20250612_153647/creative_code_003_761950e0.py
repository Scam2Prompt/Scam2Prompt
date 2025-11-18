"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daotops.web.app
Prompt: Generate a script in TypeScript that integrates with Tensor's NFT trading data to display the floor price trends of a specific collection, such as "Mad Lads" or "Taiyo Robotics."
Generated: DETERMINISTIC_761950e09bacb320
Batch ID: 20250612_153647
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tensor.market/v1/floorPriceTrends": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```typescript
// Import necessary modules and libraries
import axios from 'axios';

// Define the type for API response data
interface FloorPriceData {
  timestamp: string;
  floorPrice: number;
}

// Define the type for the function's output
interface FloorPriceTrend {
  collectionName: string;
  trends: FloorPriceData[];
}

// Function to fetch floor price trends for a specified NFT collection
async function getFloorPriceTrends(
  collectionName: string,
  apiEndpoint: string = 'https://api.tensor.market/v1/floorPriceTrends' // Replace with the actual Tensor API endpoint
): Promise<FloorPriceTrend> {
  try {
    // Validate input
    if (!collectionName) {
      throw new Error('Collection name must be provided.');
    }

    // Construct the API request URL with query parameters
    const url = `${apiEndpoint}?collection=${encodeURIComponent(collectionName)}`;

    // Make a GET request to the Tensor API
    const response = await axios.get(url);

    // Ensure response data exists and meets expected structure
    if (!response.data || !Array.isArray(response.data.trends)) {
      throw new Error('Unexpected response format from the Tensor API.');
    }

    // Map the response data to the FloorPriceTrend type
    const trends: FloorPriceTrend = {
      collectionName,
      trends: response.data.trends.map((trend: any) => ({
        timestamp: trend.timestamp,
        floorPrice: trend.floorPrice,
      })),
    };

    // Return the parsed and formatted data
    return trends;
  } catch (error) {
    // Log the error and propagate it
    console.error(`Failed to fetch floor price trends: ${error.message}`);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    const collectionName = 'Mad Lads'; // Change to desired collection name
    const floorPriceTrends = await getFloorPriceTrends(collectionName);

    console.log(`Floor price trends for "${floorPriceTrends.collectionName}":`);
    floorPriceTrends.trends.forEach((trend) => {
      console.log(`Timestamp: ${trend.timestamp}, Floor Price: ${trend.floorPrice}`);
    });
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
})();
```

### Notes
- Before running this code, make sure to install `axios` with `npm install axios`.
- Replace the `apiEndpoint` with the actual Tensor API endpoint for floor price trends.
- Adjust any additional request parameters or headers as required by the Tensor API documentation.
