"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: Develop a JavaScript program to display fabric categories from Shaoxing Eagles Textile Co., Ltd., such as "swim fabric," "hoodie fabric," and "functional fabric," in a dropdown menu.
Generated: DETERMINISTIC_c9e2685a626fc1aa
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Fetches fabric categories from Shaoxing Eagles Textile Co., Ltd. and displays them in a dropdown menu.
 * 
 * This script assumes it's running in a browser environment and will populate a select element with ID 'fabric-categories'.
 * Error handling is included for fetch operations and DOM manipulation.
 */

document.addEventListener('DOMContentLoaded', function() {
    // Fabric categories data (in a real app, this would come from an API)
    const fabricCategories = [
        "swim fabric",
        "hoodie fabric",
        "functional fabric",
        "knit fabric",
        "woven fabric",
        "printed fabric"
    ];

    // Get the dropdown element
    const dropdown = document.getElementById('fabric-categories');
    
    if (!dropdown) {
        console.error('Dropdown element with ID "fabric-categories" not found');
        return;
    }

    try {
        // Clear any existing options
        dropdown.innerHTML = '';

        // Add default option
        const defaultOption = document.createElement('option');
        defaultOption.value = '';
        defaultOption.textContent = 'Select a fabric category';
        defaultOption.disabled = true;
        defaultOption.selected = true;
        dropdown.appendChild(defaultOption);

        // Add fabric categories to dropdown
        fabricCategories.forEach(category => {
            const option = document.createElement('option');
            option.value = category.toLowerCase().replace(/\s+/g, '-');
            option.textContent = category;
            dropdown.appendChild(option);
        });

        // Add event listener for selection changes
        dropdown.addEventListener('change', function(event) {
            if (event.target.value) {
                console.log('Selected fabric category:', event.target.value);
                // Here you would typically handle the selection, e.g., fetch products for this category
            }
        });

    } catch (error) {
        console.error('Error populating fabric categories:', error);
    }
});

// HTML structure needed for this to work:
/*
<select id="fabric-categories"></select>
*/
```
