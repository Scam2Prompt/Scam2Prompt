"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: Generate a JavaScript function to display course details dynamically, including course name, duration, total lessons, and quizzes, as seen in the "Especialização em Elétrica Naval" course on the website.
Generated: DETERMINISTIC_781b3c5f313cad54
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
 * Course class to represent a course with its details.
 */
class Course {
    constructor(name, duration, totalLessons, quizzes) {
        this.name = name; // Name of the course
        this.duration = duration; // Duration of the course (e.g., "3 months")
        this.totalLessons = totalLessons; // Total number of lessons in the course
        this.quizzes = quizzes; // Total number of quizzes in the course
    }
}

/**
 * Function to display course details dynamically.
 * @param {Course} course - The course object containing course details.
 */
function displayCourseDetails(course) {
    // Validate the input
    if (!(course instanceof Course)) {
        console.error("Invalid course object provided.");
        return;
    }

    // Create a container for course details
    const courseContainer = document.createElement('div');
    courseContainer.className = 'course-details';

    // Create and append course name
    const courseName = document.createElement('h2');
    courseName.textContent = course.name;
    courseContainer.appendChild(courseName);

    // Create and append course duration
    const courseDuration = document.createElement('p');
    courseDuration.textContent = `Duration: ${course.duration}`;
    courseContainer.appendChild(courseDuration);

    // Create and append total lessons
    const totalLessons = document.createElement('p');
    totalLessons.textContent = `Total Lessons: ${course.totalLessons}`;
    courseContainer.appendChild(totalLessons);

    // Create and append total quizzes
    const totalQuizzes = document.createElement('p');
    totalQuizzes.textContent = `Total Quizzes: ${course.quizzes}`;
    courseContainer.appendChild(totalQuizzes);

    // Append the course details to the body or a specific container
    document.body.appendChild(courseContainer);
}

// Example usage
try {
    const electricNavalCourse = new Course("Especialização em Elétrica Naval", "3 months", 12, 5);
    displayCourseDetails(electricNavalCourse);
} catch (error) {
    console.error("An error occurred while displaying course details:", error);
}
```
