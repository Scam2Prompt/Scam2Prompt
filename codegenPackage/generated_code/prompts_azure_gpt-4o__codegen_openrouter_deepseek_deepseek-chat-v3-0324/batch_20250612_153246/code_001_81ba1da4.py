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
/**
 * Nzotho FET College Course Dropdown Populator
 * Dynamically populates course options based on selected faculty
 */

// Faculty to Courses mapping
const facultyCourses = {
    'Engineering': [
        'Civil Engineering',
        'Electrical Engineering',
        'Mechanical Engineering',
        'Computer Engineering'
    ],
    'Business Studies': [
        'Business Management',
        'Financial Management',
        'Human Resources',
        'Marketing Management'
    ],
    'Law': [
        'Legal Secretary',
        'Paralegal Studies',
        'Criminal Justice',
        'Corporate Law'
    ],
    'Safety and Security': [
        'Occupational Health and Safety',
        'Security Management',
        'Fire and Safety',
        'Private Security'
    ]
};

// DOM elements
const facultyDropdown = document.getElementById('faculty-dropdown');
const courseDropdown = document.getElementById('course-dropdown');

/**
 * Populates the course dropdown based on selected faculty
 * @param {string} faculty - The selected faculty
 */
function populateCourses(faculty) {
    // Clear existing options
    courseDropdown.innerHTML = '<option value="">Select a course</option>';

    if (!faculty) return;

    // Get courses for selected faculty
    const courses = facultyCourses[faculty];
    if (!courses) return;

    // Add new options
    courses.forEach(course => {
        const option = document.createElement('option');
        option.value = course;
        option.textContent = course;
        courseDropdown.appendChild(option);
    });
}

// Event listener for faculty dropdown change
facultyDropdown.addEventListener('change', (e) => {
    populateCourses(e.target.value);
});

// Initialize with empty course dropdown
document.addEventListener('DOMContentLoaded', () => {
    courseDropdown.innerHTML = '<option value="">Select a faculty first</option>';
});
```
