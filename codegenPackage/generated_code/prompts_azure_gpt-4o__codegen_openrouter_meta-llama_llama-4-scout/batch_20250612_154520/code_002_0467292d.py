"""
Generated Code Metadata:
========================
Original URL: https://danceanatolia.com
Prompt: Generate HTML and CSS code for a webpage showcasing Turkish folk dance traditions, with sections for adult and children's dance courses, inspired by the structure of danceanatolia.com.
Generated: DETERMINISTIC_0467292dead0ba61
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Turkish Folk Dance Traditions</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#adult-courses">Adult Courses</a></li>
                <li><a href="#child-courses">Children's Courses</a></li>
                <li><a href="#">About Us</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Turkish Folk Dance Traditions</h1>
        <p>Discover the rich cultural heritage of Turkey through our dance courses</p>
        <button>Learn More</button>
    </section>

    <!-- Adult Courses Section -->
    <section id="adult-courses" class="courses">
        <h2>Adult Dance Courses</h2>
        <div class="course-cards">
            <div class="course-card">
                <h3>Turkish Folk Dance</h3>
                <p>Learn traditional Turkish dances like Halay, Horon, and more</p>
                <button>Enroll Now</button>
            </div>
            <div class="course-card">
                <h3>Whirling Dervishes</h3>
                <p>Experience the spiritual dance of the Whirling Dervishes</p>
                <button>Enroll Now</button>
            </div>
            <div class="course-card">
                <h3>Turkish Wedding Dances</h3>
                <p>Learn the traditional dances performed at Turkish weddings</p>
                <button>Enroll Now</button>
            </div>
        </div>
    </section>

    <!-- Children's Courses Section -->
    <section id="child-courses" class="courses">
        <h2>Children's Dance Courses</h2>
        <div class="course-cards">
            <div class="course-card">
                <h3>Kids' Turkish Folk Dance</h3>
                <p>Introduce your child to traditional Turkish dances in a fun and interactive way</p>
                <button>Enroll Now</button>
            </div>
            <div class="course-card">
                <h3>Children's Whirling Dervishes</h3>
                <p>Let your child experience the joy of spinning and dancing</p>
                <button>Enroll Now</button>
            </div>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Turkish Folk Dance Traditions</p>
        <ul>
            <li><a href="#" target="_blank">Facebook</a></li>
            <li><a href="#" target="_blank">Instagram</a></li>
            <li><a href="#" target="_blank">Twitter</a></li>
        </ul>
    </footer>
</body>
</html>
```

**styles.css**
```css
/* Global Styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Header Styles */
header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

header nav ul li {
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

/* Hero Styles */
.hero {
    background-image: linear-gradient(to bottom, #f7f7f7, #ddd);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #333;
}

.hero h1 {
    font-size: 48px;
}

/* Courses Styles */
.courses {
    padding: 2em;
}

.course-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.course-card {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin: 20px;
    width: calc(33.33% - 20px);
}

.course-card h3 {
    font-size: 18px;
    margin-bottom: 10px;
}

.course-card p {
    font-size: 14px;
    margin-bottom: 20px;
}

.course-card button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 14px;
    cursor: pointer;
}

/* Footer Styles */
footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

footer ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

footer ul li {
    display: inline-block;
    margin-right: 20px;
}

footer a {
    color: #fff;
    text-decoration: none;
}
```
