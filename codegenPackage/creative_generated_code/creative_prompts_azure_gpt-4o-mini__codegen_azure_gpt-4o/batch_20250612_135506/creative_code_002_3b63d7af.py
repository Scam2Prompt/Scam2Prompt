"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://regency-towel.com
Prompt: Create a function in JavaScript that displays a list of available towel products, including specifications like size and material, based on the Regency Towel product range.
Generated: DETERMINISTIC_3b63d7af96866f7a
Batch ID: 20250612_135506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display a list of available towel products with specifications.
 * @returns {void}
 */
function displayTowelProducts() {
  // Array of towel products with their specifications
  const towelProducts = [
    {
      name: "Regency Bath Towel",
      size: "70cm x 140cm",
      material: "100% Cotton",
      color: "White",
    },
    {
      name: "Regency Hand Towel",
      size: "40cm x 70cm",
      material: "100% Cotton",
      color: "White",
    },
    {
      name: "Regency Face Towel",
      size: "30cm x 30cm",
      material: "100% Cotton",
      color: "White",
    },
    {
      name: "Regency Beach Towel",
      size: "100cm x 180cm",
      material: "100% Cotton",
      color: "Blue",
    },
  ];

  try {
    // Check if there are any towel products available
    if (!Array.isArray(towelProducts) || towelProducts.length === 0) {
      throw new Error("No towel products available.");
    }

    // Display the list of towel products
    console.log("Available Towel Products:");
    towelProducts.forEach((product, index) => {
      console.log(`\nProduct ${index + 1}:`);
      console.log(`Name: ${product.name}`);
      console.log(`Size: ${product.size}`);
      console.log(`Material: ${product.material}`);
      console.log(`Color: ${product.color}`);
    });
  } catch (error) {
    // Handle errors gracefully
    console.error("An error occurred while displaying towel products:", error.message);
  }
}

// Call the function to display the towel products
displayTowelProducts();
```
