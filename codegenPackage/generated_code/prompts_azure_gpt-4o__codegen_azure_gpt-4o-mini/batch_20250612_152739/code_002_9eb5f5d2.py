"""
Generated Code Metadata:
========================
Original URL: https://araform.org
Prompt: Generate code using JavaScript to display a dynamic list of available vocational courses (IeFP, IFTS) on a website, pulling data from a JSON file structured similarly to the course offerings on Araform.
Generated: DETERMINISTIC_9eb5f5d2cdf89d29
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Define a function to fetch and display vocational courses
async function fetchAndDisplayCourses() {
    const coursesContainer = document.getElementById('courses-container');

    try {
        // Fetch the JSON data from the specified file
        const response = await fetch('courses.json');

        // Check if the response is ok (status in the range 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Parse the JSON data
        const courses = await response.json();

        // Clear the container before displaying new courses
        coursesContainer.innerHTML = '';

        // Check if courses are available
        if (courses.length === 0) {
            coursesContainer.innerHTML = '<p>No courses available at the moment.</p>';
            return;
        }

        // Iterate over the courses and create HTML elements for each
        courses.forEach(course => {
            const courseElement = document.createElement('div');
            courseElement.classList.add('course');

            // Create course title
            const titleElement = document.createElement('h3');
            titleElement.textContent = course.title;
            courseElement.appendChild(titleElement);

            // Create course description
            const descriptionElement = document.createElement('p');
            descriptionElement.textContent = course.description;
            courseElement.appendChild(descriptionElement);

            // Create course duration
            const durationElement = document.createElement('p');
            durationElement.textContent = `Duration: ${course.duration}`;
            courseElement.appendChild(durationElement);

            // Append the course element to the container
            coursesContainer.appendChild(courseElement);
        });
    } catch (error) {
        // Handle any errors that occur during the fetch
        console.error('Error fetching courses:', error);
        coursesContainer.innerHTML = '<p>Failed to load courses. Please try again later.</p>';
    }
}

// Call the function to fetch and display courses when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', fetchAndDisplayCourses);
```

```html
<!-- HTML structure for displaying courses -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vocational Courses</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
</head>
<body>
    <h1>Available Vocational Courses</h1>
    <div id="courses-container"></div> <!-- Container for courses -->
    <script src="script.js"></script> <!-- Link to your JavaScript file -->
</body>
</html>
```

```json
// Example JSON structure for courses.json
[
    {
        "title": "Course in Web Development",
        "description": "Learn to build modern web applications using HTML, CSS, and JavaScript.",
        "duration": "6 months"
    },
    {
        "title": "Course in Graphic Design",
        "description": "Explore the principles of design and create stunning visuals.",
        "duration": "4 months"
    },
    {
        "title": "Course in Data Analysis",
        "description": "Gain skills in data manipulation and visualization using Python.",
        "duration": "5 months"
    }
]
```
