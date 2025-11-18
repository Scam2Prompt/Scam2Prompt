"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Develop a JavaScript program to display fabric categories from Shaoxing Eagles Textile Co., Ltd., such as "swim fabric," "hoodie fabric," and "functional fabric," in a dropdown menu.
Generated: DETERMINISTIC_c9e2685a626fc1aa
Batch ID: 20250612_154413
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
    <title>Fabric Categories Dropdown</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        label {
            margin-right: 10px;
        }
        select {
            padding: 5px;
            font-size: 16px;
        }
    </style>
</head>
<body>

    <label for="fabricCategories">Select Fabric Category:</label>
    <select id="fabricCategories">
        <!-- Options will be populated here via JavaScript -->
    </select>

    <script>
        // Define an array of fabric categories
        const fabricCategories = [
            "Swim Fabric",
            "Hoodie Fabric",
            "Functional Fabric"
        ];

        /**
         * Populates the dropdown menu with fabric categories.
         * @param {Array} categories - The array of fabric category names.
         */
        function populateDropdown(categories) {
            const dropdown = document.getElementById('fabricCategories');

            // Clear existing options
            dropdown.innerHTML = '';

            // Check if categories array is valid
            if (!Array.isArray(categories) || categories.length === 0) {
                console.error("Invalid categories array provided.");
                return;
            }

            // Create an option for each category
            categories.forEach(category => {
                const option = document.createElement('option');
                option.value = category.toLowerCase().replace(/\s+/g, '-'); // Convert to lowercase and replace spaces with dashes
                option.textContent = category; // Set the text content
                dropdown.appendChild(option); // Append the option to the dropdown
            });
        }

        // Call the function to populate the dropdown with fabric categories
        try {
            populateDropdown(fabricCategories);
        } catch (error) {
            console.error("An error occurred while populating the dropdown:", error);
        }
    </script>

</body>
</html>
```
