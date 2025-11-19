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

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fabric Categories Dropdown</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        label {
            margin-right: 10px;
        }
    </style>
</head>
<body>

    <label for="fabric-categories">Select Fabric Category:</label>
    <select id="fabric-categories">
        <!-- Options will be populated by JavaScript -->
    </select>

    <script>
        // Fabric categories from Shaoxing Eagles Textile Co., Ltd.
        const fabricCategories = [
            "Swim Fabric",
            "Hoodie Fabric",
            "Functional Fabric"
        ];

        /**
         * Function to populate the dropdown menu with fabric categories.
         * @param {Array} categories - An array of fabric category strings.
         */
        function populateDropdown(categories) {
            const dropdown = document.getElementById('fabric-categories');

            // Check if the dropdown element exists
            if (!dropdown) {
                console.error('Dropdown element not found');
                return;
            }

            // Clear existing options
            dropdown.innerHTML = '';

            // Populate dropdown with fabric categories
            categories.forEach(category => {
                const option = document.createElement('option');
                option.value = category.toLowerCase().replace(/\s+/g, '-'); // Use a URL-friendly format
                option.textContent = category; // Set the display text
                dropdown.appendChild(option); // Add option to dropdown
            });
        }

        // Error handling for populating the dropdown
        try {
            populateDropdown(fabricCategories);
        } catch (error) {
            console.error('Error populating dropdown:', error);
        }
    </script>

</body>
</html>
```
