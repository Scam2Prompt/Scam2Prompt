"""
Generated Code Metadata:
========================
Original URL: https://trekk.com
Prompt: Provide a step-by-step guide to develop a portfolio website for showcasing historic building restorations, similar to Trekk's project example.
Generated: DETERMINISTIC_edbb17dda380f534
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Portfolio Website for Historic Building Restorations**
===========================================================

**Project Structure**
---------------------

* `index.html`
* `styles.css`
* `script.js`
* `images/` (folder for project images)
* `projects.json` (file for project data)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Historic Building Restorations Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="projects">
            <h1>Projects</h1>
            <div class="project-grid" id="project-grid"></div>
        </section>
        <section id="about">
            <h1>About</h1>
            <p>Welcome to our portfolio website showcasing historic building restorations.</p>
        </section>
        <section id="contact">
            <h1>Contact</h1>
            <p>Get in touch with us: <a href="mailto:info@example.com">info@example.com</a></p>
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

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

nav li {
    margin-right: 20px;
}

nav a {
    color: #fff;
    text-decoration: none;
}

.project-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
    padding: 20px;
}

.project {
    background-color: #f7f7f7;
    padding: 20px;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.project img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.project h2 {
    margin-top: 0;
}

.project p {
    margin-bottom: 20px;
}
```

**script.js**
```javascript
// Get project grid element
const projectGrid = document.getElementById('project-grid');

// Load project data from JSON file
fetch('projects.json')
    .then(response => response.json())
    .then(projects => {
        // Render project grid
        projects.forEach(project => {
            const projectHTML = `
                <div class="project">
                    <img src="${project.image}" alt="${project.name}">
                    <h2>${project.name}</h2>
                    <p>${project.description}</p>
                    <p>Location: ${project.location}</p>
                    <p>Year: ${project.year}</p>
                </div>
            `;
            projectGrid.insertAdjacentHTML('beforeend', projectHTML);
        });
    })
    .catch(error => console.error('Error loading project data:', error));
```

**projects.json**
```json
[
    {
        "name": "Restoration of Historic Town Hall",
        "image": "images/town-hall.jpg",
        "description": "A comprehensive restoration of the historic town hall, including repairs to the stone façade, replacement of the roof, and modernization of the interior.",
        "location": "Main St, Anytown, USA",
        "year": 2018
    },
    {
        "name": "Preservation of Old Church Building",
        "image": "images/old-church.jpg",
        "description": "A meticulous preservation project aimed at maintaining the original character of the old church building, including restoration of the stained glass windows and refinishing of the hardwood floors.",
        "location": "Elm St, Othertown, USA",
        "year": 2020
    },
    {
        "name": "Renovation of Historic Landmark Hotel",
        "image": "images/hotel.jpg",
        "description": "A major renovation of the historic landmark hotel, including upgrades to the plumbing, electrical, and HVAC systems, as well as restoration of the original lobby and rooms.",
        "location": "Park Ave, Bigcity, USA",
        "year": 2015
    }
]
```
