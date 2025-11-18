"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yobugo.com
Prompt: Write JavaScript code to dynamically display Yobugo's product categories (e.g., "Cremas," "Piscos Afrutados," "Jarabes") on a webpage.
Generated: DETERMINISTIC_3d1c52a868382cc1
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Define a function to dynamically display product categories
function displayProductCategories(categories) {
    // Check if the input is an array
    if (!Array.isArray(categories)) {
        console.error("Invalid input: categories should be an array.");
        return;
    }

    // Get the container element where categories will be displayed
    const container = document.getElementById('product-categories');
    
    // Check if the container element exists
    if (!container) {
        console.error("Container element with id 'product-categories' not found.");
        return;
    }

    // Clear any existing content in the container
    container.innerHTML = '';

    // Create a list to hold the categories
    const list = document.createElement('ul');

    // Loop through each category and create a list item
    categories.forEach(category => {
        // Create a new list item
        const listItem = document.createElement('li');
        // Set the text content to the category name
        listItem.textContent = category;
        // Append the list item to the list
        list.appendChild(listItem);
    });

    // Append the list to the container
    container.appendChild(list);
}

// Sample product categories
const productCategories = ["Cremas", "Piscos Afrutados", "Jarabes"];

// Execute the function to display product categories on page load
document.addEventListener('DOMContentLoaded', () => {
    displayProductCategories(productCategories);
});
```

```html
<!-- HTML structure for displaying product categories -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yobugo Product Categories</title>
    <script src="path/to/your/script.js" defer></script> <!-- Ensure the JS file is loaded -->
</head>
<body>
    <h1>Yobugo Product Categories</h1>
    <div id="product-categories"></div> <!-- Container for product categories -->
</body>
</html>
```
