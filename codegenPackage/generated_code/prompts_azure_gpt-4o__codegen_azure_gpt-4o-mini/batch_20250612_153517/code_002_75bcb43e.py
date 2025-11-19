"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: Generate JavaScript code to create a dynamic dropdown menu that lists all the schools offering Endeavor Plus programs, using the extensive school list provided on the Endeavor Schools site.
Generated: DETERMINISTIC_75bcb43ec57d2294
Batch ID: 20250612_153517
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
    <title>Endeavor Plus Schools Dropdown</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        select {
            padding: 10px;
            font-size: 16px;
        }
    </style>
</head>
<body>

    <h1>Select a School Offering Endeavor Plus Programs</h1>
    <select id="schoolDropdown">
        <option value="">-- Select a School --</option>
    </select>

    <script>
        // Array of schools offering Endeavor Plus programs
        const schools = [
            { id: 1, name: "Endeavor Academy" },
            { id: 2, name: "Endeavor High School" },
            { id: 3, name: "Endeavor College" },
            // Add more schools as needed
        ];

        /**
         * Populates the dropdown menu with school options.
         * @param {Array} schoolList - The list of schools to populate.
         */
        function populateDropdown(schoolList) {
            const dropdown = document.getElementById('schoolDropdown');

            // Check if the dropdown element exists
            if (!dropdown) {
                console.error('Dropdown element not found');
                return;
            }

            // Clear existing options (if any)
            dropdown.innerHTML = '<option value="">-- Select a School --</option>';

            // Populate dropdown with school options
            schoolList.forEach(school => {
                const option = document.createElement('option');
                option.value = school.id; // Set the value to the school's ID
                option.textContent = school.name; // Set the display text to the school's name
                dropdown.appendChild(option); // Add the option to the dropdown
            });
        }

        // Error handling for populating the dropdown
        try {
            populateDropdown(schools);
        } catch (error) {
            console.error('Error populating dropdown:', error);
        }
    </script>

</body>
</html>
```
