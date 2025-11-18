"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghmc.edu.au
Prompt: Create a script in JavaScript to automate the admission process for vocational training programs, incorporating unique course details such as duration (e.g., 76 weeks for Graduate Diploma of Management) and fees (e.g., $18,000).
Generated: DETERMINISTIC_86b382b44d709914
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Admission Automation Script for Vocational Training Programs
 * This script automates the admission process, including course details such as duration and fees.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

/**
 * Course details structure
 * Each course has a name, duration (in weeks), and fees (in USD).
 */
const courses = [
  {
    id: 1,
    name: "Graduate Diploma of Management",
    duration: 76, // in weeks
    fees: 18000 // in USD
  },
  {
    id: 2,
    name: "Certificate IV in Information Technology",
    duration: 52, // in weeks
    fees: 12000 // in USD
  },
  {
    id: 3,
    name: "Diploma of Nursing",
    duration: 104, // in weeks
    fees: 24000 // in USD
  }
];

/**
 * Function to display available courses
 */
function displayCourses() {
  console.log("Available Courses:");
  courses.forEach(course => {
    console.log(`ID: ${course.id}, Name: ${course.name}, Duration: ${course.duration} weeks, Fees: $${course.fees}`);
  });
}

/**
 * Function to handle admissions
 * @param {number} courseId - ID of the course selected by the applicant
 * @param {string} applicantName - Name of the applicant
 */
function processAdmission(courseId, applicantName) {
  // Validate the course ID
  const course = courses.find(c => c.id === courseId);
  if (!course) {
    console.error("Invalid course ID. Please select a valid course.");
    return;
  }

  // Process the admission
  console.log(`Processing admission for ${applicantName}...`);
  console.log(`Course Selected: ${course.name}`);
  console.log(`Duration: ${course.duration} weeks`);
  console.log(`Fees: $${course.fees}`);
  console.log(`Admission successfully processed for ${applicantName}!`);
}

/**
 * Main function to execute the script
 * Replace the hard-coded inputs with actual user inputs if integrating with a web form or UI.
 */
function main() {
  try {
    displayCourses();

    const applicantName = "John Doe"; // Example applicant name
    const selectedCourseId = 1; // Example selected course ID

    console.log(`Applicant Name: ${applicantName}`);
    console.log(`Selected Course ID: ${selectedCourseId}`);

    processAdmission(selectedCourseId, applicantName);
  } catch (error) {
    console.error("An unexpected error occurred:", error.message);
  }
}

// Run the script
main();
```
