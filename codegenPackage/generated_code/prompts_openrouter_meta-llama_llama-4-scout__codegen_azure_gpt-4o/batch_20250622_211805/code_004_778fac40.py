"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: "Create a JavaScript code snippet to display a product portfolio for a packaging manufacturer, showcasing products like ABS Atlas trays, bakery and biscuit trays, and plastic cutlery."
Generated: DETERMINISTIC_778fac40cc88d769
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product Portfolio for a Packaging Manufacturer

// Define the product portfolio data
const productPortfolio = [
  {
    id: 1,
    name: "ABS Atlas Trays",
    description: "Durable and versatile trays for industrial packaging.",
    imageUrl: "images/abs-atlas-trays.jpg",
    category: "Industrial Packaging",
  },
  {
    id: 2,
    name: "Bakery and Biscuit Trays",
    description: "Specialized trays for bakery and biscuit products.",
    imageUrl: "images/bakery-biscuit-trays.jpg",
    category: "Food Packaging",
  },
  {
    id: 3,
    name: "Plastic Cutlery",
    description: "High-quality plastic cutlery for food service.",
    imageUrl: "images/plastic-cutlery.jpg",
    category: "Food Service",
  },
];

// Function to render the product portfolio
function renderProductPortfolio(products) {
  try {
    // Get the container element where the portfolio will be displayed
    const portfolioContainer = document.getElementById("product-portfolio");

    if (!portfolioContainer) {
      throw new Error("Portfolio container element not found.");
    }

    // Clear any existing content in the container
    portfolioContainer.innerHTML = "";

    // Loop through the products and create HTML for each
    products.forEach((product) => {
      // Create a product card element
      const productCard = document.createElement("div");
      productCard.className = "product-card";

      // Add product image
      const productImage = document.createElement("img");
      productImage.src = product.imageUrl;
      productImage.alt = product.name;
      productImage.className = "product-image";
      productCard.appendChild(productImage);

      // Add product name
      const productName = document.createElement("h3");
      productName.textContent = product.name;
      productName.className = "product-name";
      productCard.appendChild(productName);

      // Add product description
      const productDescription = document.createElement("p");
      productDescription.textContent = product.description;
      productDescription.className = "product-description";
      productCard.appendChild(productDescription);

      // Add product category
      const productCategory = document.createElement("span");
      productCategory.textContent = `Category: ${product.category}`;
      productCategory.className = "product-category";
      productCard.appendChild(productCategory);

      // Append the product card to the portfolio container
      portfolioContainer.appendChild(productCard);
    });
  } catch (error) {
    console.error("Error rendering product portfolio:", error.message);
    alert("An error occurred while displaying the product portfolio. Please try again later.");
  }
}

// Wait for the DOM to load before rendering the portfolio
document.addEventListener("DOMContentLoaded", () => {
  renderProductPortfolio(productPortfolio);
});
```

```html
<!-- HTML Structure -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Product Portfolio</title>
  <style>
    /* Basic styles for the product portfolio */
    #product-portfolio {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      padding: 20px;
    }
    .product-card {
      border: 1px solid #ccc;
      border-radius: 8px;
      padding: 16px;
      width: 300px;
      text-align: center;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .product-image {
      max-width: 100%;
      height: auto;
      border-radius: 4px;
    }
    .product-name {
      font-size: 1.5em;
      margin: 10px 0;
    }
    .product-description {
      font-size: 1em;
      margin: 10px 0;
    }
    .product-category {
      font-size: 0.9em;
      color: #555;
    }
  </style>
</head>
<body>
  <h1>Packaging Manufacturer Product Portfolio</h1>
  <div id="product-portfolio"></div>
  <script src="portfolio.js"></script>
</body>
</html>
```
