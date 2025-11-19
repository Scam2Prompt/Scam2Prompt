"""
Generated Code Metadata:
========================
Original URL: https://aplanet.in
Prompt: Generate a script using JavaScript to create a dropdown menu for selecting product variants (e.g., storage options) as described on the APlanet website.
Generated: DETERMINISTIC_9c641d1ea5e263e0
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Variant Dropdown</title>
    <style>
        /* Basic styling for the dropdown */
        .variant-dropdown {
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

    <div class="variant-dropdown">
        <label for="storage-options">Select Storage Option:</label>
        <select id="storage-options">
            <option value="" disabled selected>Select a variant</option>
            <option value="64GB">64GB</option>
            <option value="128GB">128GB</option>
            <option value="256GB">256GB</option>
            <option value="512GB">512GB</option>
        </select>
        <p id="selected-variant"></p>
    </div>

    <script>
        // Function to handle the change event of the dropdown
        function handleVariantChange(event) {
            const selectedVariant = event.target.value;
            const displayElement = document.getElementById('selected-variant');

            // Check if a variant is selected
            if (selectedVariant) {
                displayElement.textContent = `You have selected: ${selectedVariant}`;
            } else {
                displayElement.textContent = '';
            }
        }

        // Get the dropdown element
        const storageDropdown = document.getElementById('storage-options');

        // Add event listener for change event
        storageDropdown.addEventListener('change', handleVariantChange);

        // Error handling for dropdown initialization
        try {
            if (!storageDropdown) {
                throw new Error('Dropdown element not found');
            }
        } catch (error) {
            console.error('Initialization Error:', error.message);
        }
    </script>

</body>
</html>
```
