"""
Generated Code Metadata:
========================
Original URL: https://phantomslens.com
Prompt: Generate HTML/CSS code for a simple portfolio website with a navigation menu featuring sections for music, horror, and other creative projects, like PhantomsLens.
Generated: DETERMINISTIC_fffbf3e1b5972445
Batch ID: 20250622_212817
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
    <title>PhantomsLens Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <nav>
        <ul>
            <li><a href="#music" class="active">Music</a></li>
            <li><a href="#horror">Horror</a></li>
            <li><a href="#other-projects">Other Projects</a></li>
        </ul>
    </nav>
    <main>
        <section id="music">
            <h1>Music Projects</h1>
            <p>Explore my music endeavors, from compositions to performances.</p>
            <div class="project-grid">
                <!-- Music project cards will be generated here -->
            </div>
        </section>
        <section id="horror">
            <h1>Horror Projects</h1>
            <p>Delve into my horror creations, including stories, films, and more.</p>
            <div class="project-grid">
                <!-- Horror project cards will be generated here -->
            </div>
        </section>
        <section id="other-projects">
            <h1>Other Creative Projects</h1>
            <p>Discover my other creative ventures, including PhantomsLens.</p>
            <div class="project-grid">
                <div class="project-card">
                    <h2>PhantomsLens</h2>
                    <p>A brief description of PhantomsLens.</p>
                    <a href="#" class="project-link">Learn More</a>
                </div>
                <!-- Other project cards will be generated here -->
            </div>
        </section>
    </main>
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

nav {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

nav li {
    display: inline-block;
    margin-right: 20px;
}

nav a {
    color: #fff;
    text-decoration: none;
}

nav a.active {
    color: #ccc;
}

nav a:hover {
    color: #ccc;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 2em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    margin-top: 0;
}

.project-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

.project-card {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.project-link {
    text-decoration: none;
    color: #337ab7;
}

.project-link:hover {
    color: #23527c;
}
```

**script.js**
```javascript
// Generate project cards dynamically
const musicSection = document.querySelector('#music .project-grid');
const horrorSection = document.querySelector('#horror .project-grid');
const otherProjectsSection = document.querySelector('#other-projects .project-grid');

// Example project data
const projects = [
    { id: 1, title: 'Music Project 1', description: 'A brief description of music project 1.' },
    { id: 2, title: 'Horror Project 1', description: 'A brief description of horror project 1.' },
    { id: 3, title: 'PhantomsLens', description: 'A brief description of PhantomsLens.' },
    // Add more project data here...
];

// Function to generate project cards
function generateProjectCards(section, projects) {
    projects.forEach((project) => {
        const projectCard = document.createElement('div');
        projectCard.classList.add('project-card');
        projectCard.innerHTML = `
            <h2>${project.title}</h2>
            <p>${project.description}</p>
            <a href="#" class="project-link">Learn More</a>
        `;
        section.appendChild(projectCard);
    });
}

// Generate project cards for each section
generateProjectCards(musicSection, projects.filter((project) => project.id === 1));
generateProjectCards(horrorSection, projects.filter((project) => project.id === 2));
generateProjectCards(otherProjectsSection, projects.filter((project) => project.id === 3));

// Add event listener to navigation menu
const navLinks = document.querySelectorAll('nav a');
navLinks.forEach((link) => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const sectionId = link.getAttribute('href');
        document.querySelector(sectionId).scrollIntoView({ behavior: 'smooth' });
    });
});
```
