"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Create a JavaScript function to dynamically display product details for solid cosmetics, ensuring it highlights eco-friendly attributes as seen on C'est Moi Qui L'ai Fait Pour Vous.
Generated: DETERMINISTIC_f04f9101dafac560
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to dynamically display product details for solid cosmetics
// Highlights eco-friendly attributes

/**
 * Function to render product details on the webpage.
 * @param {Object} product - The product object containing details.
 * @param {string} product.name - The name of the product.
 * @param {string} product.description - A brief description of the product.
 * @param {number} product.price - The price of the product.
 * @param {Array<string>} product.ecoAttributes - List of eco-friendly attributes.
 * @param {string} containerId - The ID of the HTML container where details will be displayed.
 */
function displayProductDetails(product, containerId) {
  try {
    // Validate input
    if (!product || typeof product !== "object") {
      throw new Error("Invalid product data.");
    }
    if (!containerId || typeof containerId !== "string") {
      throw new Error("Invalid container ID.");
    }

    // Get the container element
    const container = document.getElementById(containerId);
    if (!container) {
      throw new Error("Container element not found.");
    }

    // Clear any existing content in the container
    container.innerHTML = "";

    // Create and append product name
    const nameElement = document.createElement("h2");
    nameElement.textContent = product.name;
    container.appendChild(nameElement);

    // Create and append product description
    const descriptionElement = document.createElement("p");
    descriptionElement.textContent = product.description;
    container.appendChild(descriptionElement);

    // Create and append product price
    const priceElement = document.createElement("p");
    priceElement.textContent = `Price: $${product.price.toFixed(2)}`;
    container.appendChild(priceElement);

    // Highlight eco-friendly attributes
    if (product.ecoAttributes && product.ecoAttributes.length > 0) {
      const ecoAttributesElement = document.createElement("ul");
      ecoAttributesElement.textContent = "Eco-Friendly Attributes:";
      product.ecoAttributes.forEach((attribute) => {
        const li = document.createElement("li");
        li.textContent = attribute;
        ecoAttributesElement.appendChild(li);
      });
      container.appendChild(ecoAttributesElement);
    } else {
      const noEcoAttributesElement = document.createElement("p");
      noEcoAttributesElement.textContent = "No eco-friendly attributes listed.";
      container.appendChild(noEcoAttributesElement);
    }
  } catch (error) {
    console.error("Error displaying product details:", error.message);
    // Optionally display a user-friendly message in the container
    const container = document.getElementById(containerId);
    if (container) {
      container.innerHTML = "<p>Unable to display product details. Please try again later.</p>";
    }
  }
}

// Example usage
const productData = {
  name: "Solid Shampoo Bar",
  description: "A nourishing solid shampoo bar for eco-conscious consumers.",
  price: 12.99,
  ecoAttributes: ["Plastic-free packaging", "Cruelty-free", "Sustainably sourced ingredients"]
};

displayProductDetails(productData, "product-container");
```
