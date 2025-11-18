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
 * Course class represents a course with details such as name, duration, total lessons, and quizzes.
 */
class Course {
    constructor(name, duration, totalLessons, quizzes) {
        this.name = name; // Course name
        this.duration = duration; // Duration in hours
        this.totalLessons = totalLessons; // Total number of lessons
        this.quizzes = quizzes; // Total number of quizzes
    }

    /**
     * Renders the course details in a specified HTML element.
     * @param {HTMLElement} container - The container element to display course details.
     */
    displayCourseDetails(container) {
        // Validate the container element
        if (!(container instanceof HTMLElement)) {
            throw new Error("Invalid container element provided.");
        }

        // Clear previous contents
        container.innerHTML = '';

        // Create course details elements
        const courseNameElement = document.createElement('h2');
        courseNameElement.textContent = this.name;

        const courseDurationElement = document.createElement('p');
        courseDurationElement.textContent = `Duration: ${this.duration} hours`;

        const courseLessonsElement = document.createElement('p');
        courseLessonsElement.textContent = `Total Lessons: ${this.totalLessons}`;

        const courseQuizzesElement = document.createElement('p');
        courseQuizzesElement.textContent = `Total Quizzes: ${this.quizzes}`;

        // Append elements to the container
        container.appendChild(courseNameElement);
        container.appendChild(courseDurationElement);
        container.appendChild(courseLessonsElement);
        container.appendChild(courseQuizzesElement);
    }
}

// Sample usage

// Create an instance of Course
const electricalEngineeringCourse = new Course(
    "Especialização em Elétrica Naval",
    60, // Duration in hours
    12, // Total lessons
    5   // Total quizzes
);

// Select the container element
const courseContainer = document.getElementById('course-details');

// Display course details
try {
    electricalEngineeringCourse.displayCourseDetails(courseContainer);
} catch (error) {
    console.error("Error displaying course details:", error.message);
}
```

**HTML structure to use this JavaScript code:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Details</title>
</head>
<body>
    <div id="course-details"></div>
    <script src="path/to/your/javascript/file.js"></script>
</body>
</html>
```
