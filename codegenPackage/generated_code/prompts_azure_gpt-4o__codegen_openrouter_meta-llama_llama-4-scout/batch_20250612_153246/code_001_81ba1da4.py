"""
Generated Code Metadata:
========================
Original URL: https://nzothofetcollege.co.za
Prompt: Generate code using JavaScript to dynamically populate the course dropdown menu for Nzotho FET College based on the selected faculty (e.g., Engineering, Business Studies, Law, Safety and Security).
Generated: DETERMINISTIC_81ba1da4a3a52607
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// course-dropdown.js

/**
 * Dynamically populates the course dropdown menu for Nzotho FET College based on the selected faculty.
 */

// Define the course data for each faculty
const courseData = {
  "Engineering": [
    { id: 1, name: "Electrical Engineering" },
    { id: 2, name: "Mechanical Engineering" },
    { id: 3, name: "Civil Engineering" },
  ],
  "Business Studies": [
    { id: 4, name: "Business Management" },
    { id: 5, name: "Accounting" },
    { id: 6, name: "Marketing" },
  ],
  "Law": [
    { id: 7, name: "Bachelor of Laws (LL.B)" },
    { id: 8, name: "Diploma in Law" },
  ],
  "Safety and Security": [
    { id: 9, name: "Safety and Security Management" },
    { id: 10, name: "Protection and Security Services" },
  ],
};

// Function to populate the course dropdown menu
function populateCourseDropdown(faculty) {
  try {
    // Get the course dropdown element
    const courseDropdown = document.getElementById("course-dropdown");

    // Clear existing options
    courseDropdown.innerHTML = "";

    // Check if faculty is valid
    if (!courseData[faculty]) {
      throw new Error(`Invalid faculty: ${faculty}`);
    }

    // Populate course options
    courseData[faculty].forEach((course) => {
      const option = document.createElement("option");
      option.value = course.id;
      option.text = course.name;
      courseDropdown.appendChild(option);
    });
  } catch (error) {
    console.error("Error populating course dropdown:", error);
    // Handle error, e.g., display error message to user
  }
}

// Example usage
document.addEventListener("DOMContentLoaded", () => {
  // Get the faculty dropdown element
  const facultyDropdown = document.getElementById("faculty-dropdown");

  // Add event listener to faculty dropdown
  facultyDropdown.addEventListener("change", (event) => {
    const selectedFaculty = event.target.value;
    populateCourseDropdown(selectedFaculty);
  });

  // Trigger initial population
  const initialFaculty = facultyDropdown.value;
  populateCourseDropdown(initialFaculty);
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nzotho FET College</title>
</head>
<body>
  <select id="faculty-dropdown">
    <option value="Engineering">Engineering</option>
    <option value="Business Studies">Business Studies</option>
    <option value="Law">Law</option>
    <option value="Safety and Security">Safety and Security</option>
  </select>

  <select id="course-dropdown"></select>

  <script src="course-dropdown.js"></script>
</body>
</html>
```
