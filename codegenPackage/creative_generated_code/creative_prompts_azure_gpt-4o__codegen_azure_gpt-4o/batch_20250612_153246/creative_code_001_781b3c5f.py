"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upjobsead.com.br
Prompt: Generate a JavaScript function to display course details dynamically, including course name, duration, total lessons, and quizzes, as seen in the "Especialização em Elétrica Naval" course on the website.
Generated: DETERMINISTIC_781b3c5f313cad54
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to dynamically display course details
 * @param {Object} courseDetails - Object containing details of the course
 * @param {string} courseDetails.name - Name of the course
 * @param {string} courseDetails.duration - Duration of the course (e.g., "6 months")
 * @param {number} courseDetails.totalLessons - Total number of lessons in the course
 * @param {number} courseDetails.quizzes - Total number of quizzes in the course
 * @param {string} containerId - ID of the HTML container where details should be displayed
 */
function displayCourseDetails(courseDetails, containerId) {
  try {
    // Validate input parameters
    if (!courseDetails || typeof courseDetails !== 'object') {
      throw new Error("Invalid course details provided");
    }
    if (!containerId || typeof containerId !== 'string') {
      throw new Error("Invalid container ID provided");
    }

    // Get the container element by ID
    const container = document.getElementById(containerId);
    if (!container) {
      throw new Error(`Container with ID '${containerId}' not found`);
    }

    // Clear any existing content in the container
    container.innerHTML = '';

    // Create and append elements for course details dynamically
    const courseNameElem = document.createElement('h1');
    courseNameElem.textContent = courseDetails.name;
    container.appendChild(courseNameElem);

    const durationElem = document.createElement('p');
    durationElem.textContent = `Duration: ${courseDetails.duration}`;
    container.appendChild(durationElem);

    const lessonsElem = document.createElement('p');
    lessonsElem.textContent = `Total Lessons: ${courseDetails.totalLessons}`;
    container.appendChild(lessonsElem);

    const quizzesElem = document.createElement('p');
    quizzesElem.textContent = `Quizzes: ${courseDetails.quizzes}`;
    container.appendChild(quizzesElem);
  } catch (error) {
    console.error("Error displaying course details:", error.message);
  }
}

// Example usage:
const exampleCourse = {
  name: "Especialização em Elétrica Naval",
  duration: "6 months",
  totalLessons: 30,
  quizzes: 10,
};

displayCourseDetails(exampleCourse, "course-details-container");
```

Make sure to have a container with the ID `course-details-container` in your HTML for this function to work. Example:

```html
<div id="course-details-container"></div>
```
