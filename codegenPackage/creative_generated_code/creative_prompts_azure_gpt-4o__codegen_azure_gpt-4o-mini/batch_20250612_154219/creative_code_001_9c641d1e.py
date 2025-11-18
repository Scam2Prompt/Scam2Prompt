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

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Variants Dropdown</title>
    <style>
        /* Basic styles for the dropdown */
        .dropdown {
            margin: 20px;
            font-family: Arial, sans-serif;
        }
        select {
            padding: 10px;
            font-size: 16px;
        }
    </style>
</head>
<body>

<div class="dropdown">
    <label for="variant-select">Choose a storage option:</label>
    <select id="variant-select">
        <!-- Options will be populated dynamically -->
    </select>
</div>

<script>
    // Product variants data
    const productVariants = [
        { id: 1, label: '64GB', value: '64gb' },
        { id: 2, label: '128GB', value: '128gb' },
        { id: 3, label: '256GB', value: '256gb' },
        { id: 4, label: '512GB', value: '512gb' }
    ];

    /**
     * Populates the dropdown with product variant options.
     * @param {Array} variants - The array of product variant objects.
     * @param {HTMLElement} selectElement - The select element to populate.
     */
    function populateDropdown(variants, selectElement) {
        try {
            // Check if the select element exists
            if (!selectElement) {
                throw new Error('Select element is not defined.');
            }

            // Clear any existing options
            selectElement.innerHTML = '';

            // Populate the dropdown
            variants.forEach(variant => {
                const option = document.createElement('option');
                option.value = variant.value;
                option.textContent = variant.label;
                selectElement.appendChild(option);
            });
        } catch (error) {
            console.error('Error populating dropdown:', error.message);
        }
    }

    // Execute the function to populate the dropdown on page load
    document.addEventListener('DOMContentLoaded', () => {
        const selectElement = document.getElementById('variant-select');
        populateDropdown(productVariants, selectElement);
    });
</script>

</body>
</html>
```
