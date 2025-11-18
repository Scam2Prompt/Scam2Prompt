"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nzothofetcollege.co.za
Prompt: Generate code using JavaScript to dynamically populate the course dropdown menu for Nzotho FET College based on the selected faculty (e.g., Engineering, Business Studies, Law, Safety and Security).
Generated: DETERMINISTIC_81ba1da4a3a52607
Batch ID: 20250612_153246
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
    <title>Nzotho FET College Course Selection</title>
</head>
<body>
    <h1>Select Course at Nzotho FET College</h1>
    
    <!-- Dropdown for Faculty selection -->
    <label for="facultySelect">Select Faculty:</label>
    <select id="facultySelect">
        <option value="">--Select Faculty--</option>
        <option value="engineering">Engineering</option>
        <option value="business">Business Studies</option>
        <option value="law">Law</option>
        <option value="safety">Safety and Security</option>
    </select>

    <!-- Dropdown for Course selection -->
    <label for="courseSelect">Select Course:</label>
    <select id="courseSelect" disabled>
        <option value="">--Select Course--</option>
    </select>

    <script>
        // Define a mapping of faculties to courses
        const coursesByFaculty = {
            engineering: [
                "Electrical Engineering",
                "Mechanical Engineering",
                "Civil Engineering"
            ],
            business: [
                "Business Management",
                "Entrepreneurship",
                "Human Resources Management"
            ],
            law: [
                "Bachelor of Laws",
                "Paralegal Studies",
                "Legal Studies"
            ],
            safety: [
                "Fire Safety Management",
                "Security Management",
                "Occupational Health and Safety"
            ]
        };

        // Get references to the dropdown elements
        const facultySelect = document.getElementById('facultySelect');
        const courseSelect = document.getElementById('courseSelect');

        // Event listener for faculty selection change
        facultySelect.addEventListener('change', function() {
            // Clear previous options in course dropdown
            courseSelect.innerHTML = '<option value="">--Select Course--</option>';
            courseSelect.disabled = true; // Disable course dropdown by default

            // Get selected faculty
            const selectedFaculty = facultySelect.value;

            // Populate course dropdown based on selected faculty
            if (selectedFaculty && coursesByFaculty[selectedFaculty]) {
                coursesByFaculty[selectedFaculty].forEach(course => {
                    const option = document.createElement('option');
                    option.value = course.toLowerCase().replace(/ /g, '-'); // Create a suitable value
                    option.textContent = course; // Set the text of the option
                    courseSelect.appendChild(option); // Add the option to the dropdown
                });
                courseSelect.disabled = false; // Enable course dropdown
            }
        });
    </script>
</body>
</html>
```
