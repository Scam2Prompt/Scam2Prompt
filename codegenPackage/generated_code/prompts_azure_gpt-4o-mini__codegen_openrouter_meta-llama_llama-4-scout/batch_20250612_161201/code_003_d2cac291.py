"""
Generated Code Metadata:
========================
Original URL: https://www.dexodoor.com
Prompt: Create a JavaScript function that dynamically displays different UPVC window styles based on user selection, as seen in the DEXODOOR product offerings.
Generated: DETERMINISTIC_d2cac291411f6085
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// window-styles.js

/**
 * Window Styles Manager
 * 
 * Dynamically displays different UPVC window styles based on user selection.
 */

// Define window styles data
const windowStyles = [
  {
    id: 1,
    name: "Casement Window",
    description: "A traditional style with a hinged sash that opens outwards.",
    image: "casement-window.jpg"
  },
  {
    id: 2,
    name: "Sliding Window",
    description: "A modern style with sashes that slide horizontally.",
    image: "sliding-window.jpg"
  },
  {
    id: 3,
    name: "Tilt and Turn Window",
    description: "A versatile style that can be tilted inwards for ventilation or turned for easy cleaning.",
    image: "tilt-and-turn-window.jpg"
  },
  // Add more window styles as needed
];

/**
 * Displays the window style selection menu.
 * 
 * @param {HTMLElement} container - The container element to render the menu in.
 */
function renderWindowStyleMenu(container) {
  // Create the menu element
  const menuElement = document.createElement("select");
  menuElement.id = "window-style-menu";

  // Populate the menu with window styles
  windowStyles.forEach((style) => {
    const optionElement = document.createElement("option");
    optionElement.value = style.id;
    optionElement.textContent = style.name;
    menuElement.appendChild(optionElement);
  });

  // Add event listener for menu changes
  menuElement.addEventListener("change", (event) => {
    const selectedStyleId = parseInt(event.target.value);
    renderWindowStyleDetails(selectedStyleId);
  });

  // Append the menu to the container
  container.appendChild(menuElement);
}

/**
 * Displays the details of the selected window style.
 * 
 * @param {number} styleId - The ID of the selected window style.
 */
function renderWindowStyleDetails(styleId) {
  // Find the selected window style
  const selectedStyle = windowStyles.find((style) => style.id === styleId);

  // Check if the style exists
  if (!selectedStyle) {
    console.error(`Window style with ID ${styleId} not found.`);
    return;
  }

  // Create the details element
  const detailsElement = document.getElementById("window-style-details");

  // Check if the details element exists
  if (!detailsElement) {
    console.error("Window style details element not found.");
    return;
  }

  // Update the details element with the selected style's information
  detailsElement.innerHTML = `
    <h2>${selectedStyle.name}</h2>
    <p>${selectedStyle.description}</p>
    <img src="${selectedStyle.image}" alt="${selectedStyle.name}">
  `;
}

// Initialize the window style menu
document.addEventListener("DOMContentLoaded", () => {
  const menuContainer = document.getElementById("window-style-menu-container");
  if (menuContainer) {
    renderWindowStyleMenu(menuContainer);
    renderWindowStyleDetails(1); // Default to the first window style
  } else {
    console.error("Window style menu container not found.");
  }
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DEXODOOR Window Styles</title>
  <style>
    /* Add some basic styling */
    body {
      font-family: Arial, sans-serif;
    }
    #window-style-menu-container {
      margin-bottom: 20px;
    }
    #window-style-details {
      margin-top: 20px;
    }
    #window-style-details img {
      width: 100%;
      height: 200px;
      object-fit: cover;
      border-radius: 10px;
    }
  </style>
</head>
<body>
  <div id="window-style-menu-container"></div>
  <div id="window-style-details"></div>

  <script src="window-styles.js"></script>
</body>
</html>
```
