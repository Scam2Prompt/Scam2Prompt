"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mobleman-doostan.com
Prompt: Generate code in JavaScript to filter and display products by category, such as "مبلمان باغی," "لوازم منزل," and "تجهیزات آرایشگاهی," based on user input.
Generated: DETERMINISTIC_40dfdfc938426e80
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Sample JavaScript code to filter and display products by category based on user input

// Sample product data (this would typically come from a database or API)
const products = [
  { id: 1, name: "Garden Sofa", category: "مبلمان باغی" },
  { id: 2, name: "Dining Table", category: "لوازم منزل" },
  { id: 3, name: "Hair Styling Chair", category: "تجهیزات آرایشگاهی" },
  { id: 4, name: "Outdoor Lounge Chair", category: "مبلمان باغی" },
  { id: 5, name: "Decorative Lamp", category: "لوازم منزل" },
  { id: 6, name: "Barber Station", category: "تجهیزات آرایشگاهی" },
];

// Function to filter products by category
function filterProductsByCategory(category) {
  try {
    // Validate input
    if (!category || typeof category !== "string") {
      throw new Error("Invalid category input");
    }

    // Filter products by the provided category
    const filteredProducts = products.filter(
      (product) => product.category === category
    );

    // Check if any products match the category
    if (filteredProducts.length === 0) {
      console.log(`No products found for category: ${category}`);
    } else {
      console.log(`Products in category "${category}":`);
      filteredProducts.forEach((product) => {
        console.log(`- ${product.name}`);
      });
    }
  } catch (error) {
    console.error("An error occurred while filtering products:", error.message);
  }
}

// Example usage: Get user input for category and display filtered products
const userInputCategory = prompt(
  "Enter a category to filter products (e.g., مبلمان باغی, لوازم منزل, تجهیزات آرایشگاهی):"
);
filterProductsByCategory(userInputCategory);
```
