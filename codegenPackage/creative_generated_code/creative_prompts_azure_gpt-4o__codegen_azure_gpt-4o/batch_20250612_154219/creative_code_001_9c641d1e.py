"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aplanet.in
Prompt: Generate a script using JavaScript to create a dropdown menu for selecting product variants (e.g., storage options) as described on the APlanet website.
Generated: DETERMINISTIC_9c641d1ea5e263e0
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Create a dropdown menu for selecting product variants (e.g., storage options)

// Function to dynamically create the dropdown menu
function createDropdownMenu(containerId, variants) {
  // Validate input
  if (!Array.isArray(variants) || variants.length === 0) {
    console.error("Variants must be a non-empty array.");
    return;
  }

  // Get the container element where the menu will be appended
  const container = document.getElementById(containerId);
  if (!container) {
    console.error(`Container element with ID '${containerId}' not found.`);
    return;
  }

  // Create the dropdown <select> element
  const dropdown = document.createElement("select");
  dropdown.setAttribute("id", `${containerId}-dropdown`);
  dropdown.setAttribute("class", "product-variants-dropdown");

  // Add an initial disabled option as a prompt
  const defaultOption = document.createElement("option");
  defaultOption.setAttribute("disabled", true);
  defaultOption.setAttribute("selected", true);
  defaultOption.textContent = "Select a variant";
  dropdown.appendChild(defaultOption);

  // Populate the dropdown with product variant options
  variants.forEach((variant) => {
    const option = document.createElement("option");
    option.setAttribute("value", variant.value || variant.name); // Set value for the option
    option.textContent = variant.name; // Set visible name
    dropdown.appendChild(option);
  });

  // Append the dropdown menu to the container
  container.appendChild(dropdown);

  // Add an event listener to handle user selection
  dropdown.addEventListener("change", (event) => {
    console.log(`Selected Variant: ${event.target.value}`);
    // Additional handling for variant selection can be added here
  });
}

// Example usage: Populate a dropdown menu
document.addEventListener("DOMContentLoaded", () => {
  const containerId = "product-variants-container";
  const variants = [
    { name: "64GB Storage", value: "64gb" },
    { name: "128GB Storage", value: "128gb" },
    { name: "256GB Storage", value: "256gb" },
    { name: "512GB Storage", value: "512gb" },
  ];

  createDropdownMenu(containerId, variants);
});
```

HTML to accompany the JavaScript:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Product Variants Dropdown</title>
  <style>
    /* Styling for the dropdown menu */
    .product-variants-dropdown {
      width: 200px;
      padding: 10px;
      font-size: 16px;
    }
  </style>
</head>
<body>
  <!-- Container for the dropdown menu -->
  <div id="product-variants-container"></div>

  <!-- Include the script -->
  <script src="dropdownMenu.js"></script>
</body>
</html>
```
