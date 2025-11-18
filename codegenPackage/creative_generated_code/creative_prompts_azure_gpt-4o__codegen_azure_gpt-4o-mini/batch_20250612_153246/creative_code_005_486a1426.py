"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upjobsead.com.br
Prompt: Develop HTML and CSS code for a course catalog page that includes course names, prices, durations, and student counts, similar to the layout on the website.
Generated: DETERMINISTIC_486a1426bb034124
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Catalog</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Course Catalog</h1>
        <p>Explore our wide range of courses to enhance your skills!</p>
    </header>

    <main>
        <section class="course-list">
            <article class="course">
                <h2>Web Development Bootcamp</h2>
                <p class="price">$499</p>
                <p class="duration">Duration: 12 weeks</p>
                <p class="students">Students Enrolled: 250</p>
            </article>
            <article class="course">
                <h2>Data Science Masterclass</h2>
                <p class="price">$599</p>
                <p class="duration">Duration: 10 weeks</p>
                <p class="students">Students Enrolled: 150</p>
            </article>
            <article class="course">
                <h2>Digital Marketing Essentials</h2>
                <p class="price">$399</p>
                <p class="duration">Duration: 8 weeks</p>
                <p class="students">Students Enrolled: 300</p>
            </article>
            <article class="course">
                <h2>UI/UX Design Fundamentals</h2>
                <p class="price">$450</p>
                <p class="duration">Duration: 6 weeks</p>
                <p class="students">Students Enrolled: 200</p>
            </article>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Course Catalog. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General styles for the body */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

/* Styling for the header */
header {
    background-color: #007BFF;
    color: white;
    padding: 20px;
    text-align: center;
}

/* Main content styling */
main {
    padding: 20px;
}

/* Course list styling */
.course-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}

/* Individual course card styling */
.course {
    background-color: white;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin: 10px;
    padding: 15px;
    width: calc(25% - 40px); /* Responsive design */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Course title styling */
.course h2 {
    font-size: 1.5em;
    color: #333;
}

/* Price, duration, and student count styling */
.price, .duration, .students {
    font-size: 1.1em;
    margin: 5px 0;
}

/* Footer styling */
footer {
    background-color: #007BFF;
    color: white;
    text-align: center;
    padding: 10px 0;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
