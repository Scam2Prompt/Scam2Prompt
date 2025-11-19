"""
Generated Code Metadata:
========================
Original URL: https://bernynovias.com
Prompt: "Generate a JavaScript code snippet to implement a discount system for an online store selling wedding dresses and accessories, with discounts up to 10% off all products."
Generated: DETERMINISTIC_c31b17751894deac
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Discount System for an Online Store Selling Wedding Dresses and Accessories

// Function to calculate the discounted price
function calculateDiscountedPrice(originalPrice, discountPercentage) {
  // Validate inputs
  if (typeof originalPrice !== 'number' || originalPrice <= 0) {
    throw new Error("Invalid original price. Must be a positive number.");
  }
  if (typeof discountPercentage !== 'number' || discountPercentage < 0 || discountPercentage > 10) {
    throw new Error("Invalid discount percentage. Must be between 0 and 10.");
  }

  // Calculate the discounted price
  const discountAmount = (originalPrice * discountPercentage) / 100;
  const discountedPrice = originalPrice - discountAmount;

  return discountedPrice.toFixed(2); // Return price rounded to 2 decimal places
}

// Function to apply discount to a list of products
function applyDiscountToProducts(products, discountPercentage) {
  // Validate inputs
  if (!Array.isArray(products)) {
    throw new Error("Invalid products list. Must be an array.");
  }

  return products.map((product) => {
    if (!product.name || typeof product.price !== 'number' || product.price <= 0) {
      throw new Error("Invalid product object. Each product must have a name and a positive price.");
    }

    // Apply discount to each product
    const discountedPrice = calculateDiscountedPrice(product.price, discountPercentage);
    return {
      ...product,
      discountedPrice: parseFloat(discountedPrice), // Add discounted price to product object
    };
  });
}

// Example usage
try {
  const products = [
    { name: "Wedding Dress A", price: 500 },
    { name: "Wedding Dress B", price: 800 },
    { name: "Accessory A", price: 50 },
    { name: "Accessory B", price: 100 },
  ];

  const discountPercentage = 10; // Maximum discount is 10%
  const discountedProducts = applyDiscountToProducts(products, discountPercentage);

  console.log("Discounted Products:", discountedProducts);
} catch (error) {
  console.error("Error:", error.message);
}
```
