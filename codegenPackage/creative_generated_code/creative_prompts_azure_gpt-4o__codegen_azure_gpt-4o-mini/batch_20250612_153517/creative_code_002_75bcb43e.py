"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plus.endeavorschools.com
Prompt: Generate JavaScript code to create a dynamic dropdown menu that lists all the schools offering Endeavor Plus programs, using the extensive school list provided on the Endeavor Schools site.
Generated: DETERMINISTIC_75bcb43ec57d2294
Batch ID: 20250612_153517
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
    <title>Endeavor Plus Programs Dropdown</title>
    <style>
        body {
            font-family: Arial, sans-serif;
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

    <label for="schoolDropdown">Select a School Offering Endeavor Plus:</label>
    <select id="schoolDropdown">
        <option value="">--Please choose a school--</option>
    </select>

    <script>
        // Sample data representing schools offering Endeavor Plus programs.
        // In a real-world scenario, this data might come from an API or database.
        const schools = [
            { id: 1, name: "Springfield Elementary" },
            { id: 2, name: "Shelbyville High School" },
            { id: 3, name: "Capital City Academy" },
            { id: 4, name: "Ogden Community School" },
            // Add more schools as needed
        ];

        // Function to populate the dropdown with school names
        function populateSchoolDropdown(schoolList) {
            const dropdown = document.getElementById('schoolDropdown');

            // Clear existing options
            dropdown.innerHTML = '<option value="">--Please choose a school--</option>';

            // Check if school list is valid
            if (!Array.isArray(schoolList) || schoolList.length === 0) {
                console.error('Invalid school list provided.');
                return;
            }

            // Iterate over the school list and create option elements
            schoolList.forEach(school => {
                if (school.id && school.name) {
                    const option = document.createElement('option');
                    option.value = school.id;
                    option.textContent = school.name;
                    dropdown.appendChild(option);
                } else {
                    console.warn('School data is missing id or name:', school);
                }
            });
        }

        // Error handling for DOMContentLoaded event
        document.addEventListener('DOMContentLoaded', () => {
            try {
                populateSchoolDropdown(schools);
            } catch (error) {
                console.error('An error occurred while populating the dropdown:', error);
            }
        });
    </script>

</body>
</html>
```
