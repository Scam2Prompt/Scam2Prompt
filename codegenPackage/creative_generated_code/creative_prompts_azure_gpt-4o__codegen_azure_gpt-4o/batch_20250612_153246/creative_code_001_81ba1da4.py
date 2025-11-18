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

```javascript
// HTML Dropdowns for Faculty and Course Selection
// Make sure to include this HTML snippet in your webpage for the JavaScript to work.
// <select id="facultyDropdown">
//   <option value="" disabled selected>Select Faculty</option>
//   <option value="engineering">Engineering</option>
//   <option value="businessStudies">Business Studies</option>
//   <option value="law">Law</option>
//   <option value="safetyAndSecurity">Safety and Security</option>
// </select>
// <select id="courseDropdown">
//   <option value="" disabled selected>Select Course</option>
// </select>

document.addEventListener("DOMContentLoaded", () => {
  // Mapping of faculties to their respective courses
  const facultyCourses = {
    engineering: ["Civil Engineering", "Mechanical Engineering", "Electrical Engineering"],
    businessStudies: ["Accounting", "Marketing", "Human Resources Management"],
    law: ["Criminal Law", "Corporate Law", "Family Law"],
    safetyAndSecurity: ["Security Management", "Fire Safety", "Disaster Management"]
  };

  // Get references to the dropdown elements
  const facultyDropdown = document.getElementById("facultyDropdown");
  const courseDropdown = document.getElementById("courseDropdown");

  // Event listener for when the faculty dropdown changes
  facultyDropdown.addEventListener("change", (event) => {
    const selectedFaculty = event.target.value;

    // Clear any existing options in the course dropdown
    courseDropdown.innerHTML = '<option value="" disabled selected>Select Course</option>';

    // Check if the selected faculty has courses mapped
    if (facultyCourses[selectedFaculty]) {
      // Populate the course dropdown with courses for the selected faculty
      facultyCourses[selectedFaculty].forEach((course) => {
        const option = document.createElement("option");
        option.value = course;
        option.textContent = course;
        courseDropdown.appendChild(option);
      });
    } else {
      // Handle case where no courses are mapped to the selected faculty
      const option = document.createElement("option");
      option.value = "";
      option.textContent = "No courses available for this faculty";
      courseDropdown.appendChild(option);
    }
  });
});
```
