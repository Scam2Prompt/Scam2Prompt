"""
Generated Code Metadata:
========================
Original URL: https://collab.host
Prompt: Generate a sample code for a simple web page that showcases a UI designer's portfolio, including sections for projects, testimonials, and speaker bio, using HTML, CSS, and JavaScript.
Generated: DETERMINISTIC_9cdb40653ed58bf0
Batch ID: 20250622_212417
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
    <title>UI Designer's Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#testimonials">Testimonials</a></li>
                <li><a href="#speaker-bio">Speaker Bio</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to my portfolio!</h1>
        <p>I'm a UI designer with a passion for creating beautiful and functional designs.</p>
        <button>Learn More</button>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="projects">
        <h2>My Projects</h2>
        <div class="project-grid">
            <div class="project-card">
                <img src="project1.jpg" alt="Project 1">
                <h3>Project 1</h3>
                <p>A brief description of project 1.</p>
            </div>
            <div class="project-card">
                <img src="project2.jpg" alt="Project 2">
                <h3>Project 2</h3>
                <p>A brief description of project 2.</p>
            </div>
            <div class="project-card">
                <img src="project3.jpg" alt="Project 3">
                <h3>Project 3</h3>
                <p>A brief description of project 3.</p>
            </div>
        </div>
    </section>

    <!-- Testimonials Section -->
    <section id="testimonials" class="testimonials">
        <h2>What others say about me</h2>
        <div class="testimonial-grid">
            <div class="testimonial-card">
                <p>&#8220;John is an amazing UI designer. His work is top-notch!&#8221;</p>
                <p>— Client 1</p>
            </div>
            <div class="testimonial-card">
                <p>&#8220;I've worked with John on several projects and he's always delivered high-quality work.&#8221;</p>
                <p>— Client 2</p>
            </div>
            <div class="testimonial-card">
                <p>&#8220;John is a true professional. His designs are always on point!&#8221;</p>
                <p>— Client 3</p>
            </div>
        </div>
    </section>

    <!-- Speaker Bio Section -->
    <section id="speaker-bio" class="speaker-bio">
        <h2>About Me</h2>
        <p>I'm John Doe, a UI designer with over 5 years of experience in creating beautiful and functional designs. I'm passionate about staying up-to-date with the latest design trends and technologies.</p>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 John Doe</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

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
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

.hero {
    background-image: linear-gradient(to bottom, #333, #555);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

.hero h1 {
    font-size: 48px;
}

.projects {
    padding: 2em;
}

.project-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.project-card {
    background-color: #f7f7f7;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.project-card img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.testimonials {
    padding: 2em;
    background-color: #f7f7f7;
}

.testimonial-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.testimonial-card {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.speaker-bio {
    padding: 2em;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```

**script.js**
```javascript
// Add event listener to learn more button
document.querySelector('.hero button').addEventListener('click', () => {
    // Scroll to projects section
    document.querySelector('#projects').scrollIntoView({ behavior: 'smooth' });
});

// Add event listener to navigation links
document.querySelectorAll('header nav a').forEach((link) => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const sectionId = link.getAttribute('href');
        document.querySelector(sectionId).scrollIntoView({ behavior: 'smooth' });
    });
});

// Initialize grid layout on window resize
window.addEventListener('resize', () => {
    // Recalculate grid layout
    document.querySelector('.project-grid').style.gridTemplateColumns = 'repeat(auto-fill, minmax(200px, 1fr))';
    document.querySelector('.testimonial-grid').style.gridTemplateColumns = 'repeat(auto-fill, minmax(200px, 1fr))';
});

// Call resize event listener on page load
window.dispatchEvent(new Event('resize'));
```
