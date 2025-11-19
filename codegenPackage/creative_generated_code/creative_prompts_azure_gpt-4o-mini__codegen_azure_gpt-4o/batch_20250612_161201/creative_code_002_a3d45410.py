"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.maxevent.pro
Prompt: Create a JavaScript function that allows users to select and customize their IPTV package from MaxEvent's offerings.
Generated: DETERMINISTIC_a3d4541058a35d72
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Allows users to select and customize their IPTV package from MaxEvent's offerings.
 * Users can choose from predefined packages and add additional channels or features.
 * This function assumes the presence of MaxEvent's offerings in a predefined format.
 */

// Sample data representing MaxEvent's offerings
const maxEventPackages = [
  {
    id: 1,
    name: "Basic Package",
    price: 20,
    channels: ["News", "Sports", "Entertainment"]
  },
  {
    id: 2,
    name: "Premium Package",
    price: 50,
    channels: ["News", "Sports", "Entertainment", "Movies", "Kids"]
  },
  {
    id: 3,
    name: "Ultra Package",
    price: 80,
    channels: [
      "News",
      "Sports",
      "Entertainment",
      "Movies",
      "Kids",
      "Documentary",
      "Music"
    ]
  }
];

// Sample data representing additional features
const additionalFeatures = [
  { id: 101, name: "HD Streaming", price: 10 },
  { id: 102, name: "Cloud DVR", price: 15 },
  { id: 103, name: "4K Streaming", price: 20 }
];

/**
 * Function to customize and select an IPTV package.
 * @param {number} packageId - The ID of the base package.
 * @param {number[]} featureIds - Array of IDs representing additional features.
 * @returns {object} - A summary of the customized IPTV package.
 */
function selectIPTVPackage(packageId, featureIds) {
  try {
    // Find the selected package
    const selectedPackage = maxEventPackages.find(
      (pkg) => pkg.id === packageId
    );

    if (!selectedPackage) {
      throw new Error("Invalid package ID provided.");
    }

    // Calculate the base price
    let totalPrice = selectedPackage.price;
    const selectedFeatures = [];

    // Add selected features
    featureIds.forEach((featureId) => {
      const feature = additionalFeatures.find((f) => f.id === featureId);
      if (feature) {
        selectedFeatures.push(feature);
        totalPrice += feature.price;
      } else {
        console.warn(`Feature ID ${featureId} is invalid and was ignored.`);
      }
    });

    // Return a summary object
    return {
      basePackage: selectedPackage.name,
      baseChannels: selectedPackage.channels,
      selectedFeatures: selectedFeatures.map((f) => f.name),
      totalPrice: totalPrice
    };
  } catch (error) {
    console.error("An error occurred while selecting the package:", error.message);
    return null;
  }
}

// Example Usage:
// User selects the 'Premium Package' and adds 'HD Streaming' and 'Cloud DVR'
const userSelection = selectIPTVPackage(2, [101, 102]);
console.log("Customized IPTV Package:", userSelection);
```
