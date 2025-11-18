"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Generate a function in JavaScript that categorizes fabrics from Shaoxing Eagles Textile Co., Ltd. based on their use cases, such as swimwear, sportswear, or leggings, using fabric names like "polar fleece" and "single jersey."
Generated: DETERMINISTIC_672d5b4009297298
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to categorize fabrics based on their use cases.
 * 
 * @param {string} fabricName - The name of the fabric to categorize.
 * @returns {string} - The category of the fabric or an error message if the fabric is unknown.
 */
function categorizeFabric(fabricName) {
    // Define a mapping of fabric names to their respective categories
    const fabricCategories = {
        "polar fleece": "sportswear",
        "single jersey": "leggings",
        "lycra": "swimwear",
        "mesh": "sportswear",
        "cotton spandex": "leggings",
        "neoprene": "swimwear",
        "satin": "evening wear",
        "polyester": "activewear",
        "tulle": "dancewear",
        "denim": "casual wear"
    };

    // Normalize the input to lower case for case-insensitive comparison
    const normalizedFabricName = fabricName.trim().toLowerCase();

    // Check if the fabric name exists in the mapping
    if (fabricCategories.hasOwnProperty(normalizedFabricName)) {
        return `The fabric "${fabricName}" is categorized as: ${fabricCategories[normalizedFabricName]}.`;
    } else {
        return `Error: The fabric "${fabricName}" is not recognized. Please provide a valid fabric name.`;
    }
}

// Example usage
try {
    console.log(categorizeFabric("Polar Fleece")); // Expected output: sportswear
    console.log(categorizeFabric("Single Jersey")); // Expected output: leggings
    console.log(categorizeFabric("Unknown Fabric")); // Expected output: error message
} catch (error) {
    console.error("An error occurred while categorizing the fabric:", error);
}
```
