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
 * Displays course details dynamically on a webpage.
 * @param {Object} course - Course details object.
 * @param {string} course.name - Name of the course.
 * @param {string} course.duration - Duration of the course.
 * @param {number} course.totalLessons - Total number of lessons.
 * @param {number} course.totalQuizzes - Total number of quizzes.
 * @param {string} targetElementId - ID of the HTML element where details will be displayed.
 */
function displayCourseDetails(course, targetElementId) {
    try {
        // Validate input parameters
        if (!course || typeof course !== 'object') {
            throw new Error('Invalid course object provided');
        }

        if (!targetElementId || typeof targetElementId !== 'string') {
            throw new Error('Invalid target element ID provided');
        }

        const requiredFields = ['name', 'duration', 'totalLessons', 'totalQuizzes'];
        for (const field of requiredFields) {
            if (!(field in course)) {
                throw new Error(`Missing required field: ${field}`);
            }
        }

        // Get the target element
        const targetElement = document.getElementById(targetElementId);
        if (!targetElement) {
            throw new Error(`Element with ID '${targetElementId}' not found`);
        }

        // Create HTML for course details
        const courseHTML = `
            <div class="course-details">
                <h2 class="course-title">${course.name}</h2>
                <div class="course-meta">
                    <div class="meta-item">
                        <span class="meta-label">Duração:</span>
                        <span class="meta-value">${course.duration}</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label">Total de Aulas:</span>
                        <span class="meta-value">${course.totalLessons}</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label">Questionários:</span>
                        <span class="meta-value">${course.totalQuizzes}</span>
                    </div>
                </div>
            </div>
        `;

        // Insert the HTML into the target element
        targetElement.innerHTML = courseHTML;

    } catch (error) {
        console.error('Error displaying course details:', error.message);
        // Optionally display error to user
        const errorElement = document.getElementById(targetElementId);
        if (errorElement) {
            errorElement.innerHTML = `<div class="error">Failed to load course details. Please try again later.</div>`;
        }
    }
}

// Example usage:
/*
const courseData = {
    name: "Especialização em Elétrica Naval",
    duration: "6 meses",
    totalLessons: 42,
    totalQuizzes: 8
};

displayCourseDetails(courseData, 'course-details-container');
*/
```
