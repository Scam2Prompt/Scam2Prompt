"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: Write JavaScript code for a dynamic webpage that showcases Virtual5's monthly events, testimonials, and course offerings, with interactive elements for user engagement.
Generated: DETERMINISTIC_8d3cacf630e8b16d
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Virtual5 Events and Courses</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>Welcome to Virtual5</h1>
        <nav>
            <ul>
                <li><a href="#events">Monthly Events</a></li>
                <li><a href="#testimonials">Testimonials</a></li>
                <li><a href="#courses">Course Offerings</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="events">
            <h2>Monthly Events</h2>
            <div id="event-list"></div>
            <button id="load-events">Load Events</button>
        </section>

        <section id="testimonials">
            <h2>Testimonials</h2>
            <div id="testimonial-list"></div>
        </section>

        <section id="courses">
            <h2>Course Offerings</h2>
            <div id="course-list"></div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Virtual5. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

header {
    background: #35424a;
    color: #ffffff;
    padding: 10px 0;
    text-align: center;
}

nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav a {
    color: #ffffff;
    text-decoration: none;
}

section {
    padding: 20px;
    margin: 20px;
    background: #ffffff;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

footer {
    text-align: center;
    padding: 10px 0;
    background: #35424a;
    color: #ffffff;
}
```

```javascript
// script.js

// Sample data for events, testimonials, and courses
const events = [
    { date: '2023-11-01', title: 'Web Development Workshop' },
    { date: '2023-11-15', title: 'AI in Business Seminar' },
    { date: '2023-11-30', title: 'Networking Event' }
];

const testimonials = [
    { name: 'Alice', feedback: 'Virtual5 has transformed my career!' },
    { name: 'Bob', feedback: 'The courses are top-notch and very engaging.' },
    { name: 'Charlie', feedback: 'I love the community and support!' }
];

const courses = [
    { title: 'JavaScript for Beginners', duration: '4 weeks' },
    { title: 'Advanced CSS Techniques', duration: '3 weeks' },
    { title: 'Data Science with Python', duration: '6 weeks' }
];

// Function to load events dynamically
function loadEvents() {
    const eventList = document.getElementById('event-list');
    eventList.innerHTML = ''; // Clear previous events

    events.forEach(event => {
        const eventItem = document.createElement('div');
        eventItem.classList.add('event-item');
        eventItem.innerHTML = `<strong>${event.date}</strong>: ${event.title}`;
        eventList.appendChild(eventItem);
    });
}

// Function to display testimonials
function displayTestimonials() {
    const testimonialList = document.getElementById('testimonial-list');
    testimonialList.innerHTML = ''; // Clear previous testimonials

    testimonials.forEach(testimonial => {
        const testimonialItem = document.createElement('div');
        testimonialItem.classList.add('testimonial-item');
        testimonialItem.innerHTML = `<strong>${testimonial.name}</strong>: "${testimonial.feedback}"`;
        testimonialList.appendChild(testimonialItem);
    });
}

// Function to display courses
function displayCourses() {
    const courseList = document.getElementById('course-list');
    courseList.innerHTML = ''; // Clear previous courses

    courses.forEach(course => {
        const courseItem = document.createElement('div');
        courseItem.classList.add('course-item');
        courseItem.innerHTML = `<strong>${course.title}</strong> - Duration: ${course.duration}`;
        courseList.appendChild(courseItem);
    });
}

// Event listeners for interactive elements
document.getElementById('load-events').addEventListener('click', loadEvents);

// Initial display of testimonials and courses
displayTestimonials();
displayCourses();
```

This code creates a dynamic webpage for Virtual5, showcasing monthly events, testimonials, and course offerings with interactive elements for user engagement.
