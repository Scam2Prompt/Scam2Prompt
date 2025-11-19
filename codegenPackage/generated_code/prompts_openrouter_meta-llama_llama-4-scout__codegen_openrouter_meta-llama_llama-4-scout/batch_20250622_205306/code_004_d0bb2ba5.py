"""
Generated Code Metadata:
========================
Original URL: https://secondcitysummers.com
Prompt: Design a simple web page using HTML and CSS to promote The Second City's comedy shows and classes, including a show finder and class search feature.
Generated: DETERMINISTIC_d0bb2ba5346eae69
Batch ID: 20250622_205306
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
    <title>The Second City</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#shows">Shows</a></li>
                <li><a href="#classes">Classes</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="hero">
            <h1>Laugh Out Loud with The Second City</h1>
            <p>Find comedy shows and classes in Chicago</p>
        </section>
        <section id="show-finder">
            <h2>Find a Show</h2>
            <form id="show-form">
                <label for="location">Location:</label>
                <select id="location" name="location">
                    <option value="">Select a location</option>
                    <option value="Chicago">Chicago</option>
                    <option value="Toronto">Toronto</option>
                    <option value="New York">New York</option>
                </select>
                <label for="date">Date:</label>
                <input type="date" id="date" name="date">
                <button id="show-search">Search</button>
            </form>
            <div id="show-results"></div>
        </section>
        <section id="class-search">
            <h2>Search Classes</h2>
            <form id="class-form">
                <label for="class-type">Class Type:</label>
                <select id="class-type" name="class-type">
                    <option value="">Select a class type</option>
                    <option value="improv">Improv</option>
                    <option value="stand-up">Stand-up</option>
                    <option value="writing">Writing</option>
                </select>
                <label for="class-level">Class Level:</label>
                <select id="class-level" name="class-level">
                    <option value="">Select a class level</option>
                    <option value="beginner">Beginner</option>
                    <option value="intermediate">Intermediate</option>
                    <option value="advanced">Advanced</option>
                </select>
                <button id="class-search">Search</button>
            </form>
            <div id="class-results"></div>
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

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2 {
    color: #333;
    margin-bottom: 10px;
}

#show-finder, #class-search {
    width: 80%;
}

label {
    display: block;
    margin-bottom: 10px;
}

input, select {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

button {
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #444;
}

#show-results, #class-results {
    margin-top: 20px;
}

.show {
    background-color: #fff;
    padding: 10px;
    border: 1px solid #ddd;
    margin-bottom: 10px;
}

.show h3 {
    margin-top: 0;
}

.class {
    background-color: #fff;
    padding: 10px;
    border: 1px solid #ddd;
    margin-bottom: 10px;
}

.class h3 {
    margin-top: 0;
}
```

**script.js**
```javascript
// Mock API data
const shows = [
    { id: 1, name: 'The Second City', location: 'Chicago', date: '2024-09-20' },
    { id: 2, name: 'The Second City', location: 'Toronto', date: '2024-09-22' },
    { id: 3, name: 'The Second City', location: 'New York', date: '2024-09-25' },
];

const classes = [
    { id: 1, name: 'Improv 101', type: 'improv', level: 'beginner' },
    { id: 2, name: 'Stand-up Comedy', type: 'stand-up', level: 'intermediate' },
    { id: 3, name: 'Writing for Comedy', type: 'writing', level: 'advanced' },
];

// Get DOM elements
const showForm = document.getElementById('show-form');
const showResults = document.getElementById('show-results');
const classForm = document.getElementById('class-form');
const classResults = document.getElementById('class-results');

// Add event listeners
showForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const location = document.getElementById('location').value;
    const date = document.getElementById('date').value;
    const filteredShows = shows.filter((show) => show.location === location && show.date === date);
    renderShowResults(filteredShows);
});

classForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const classType = document.getElementById('class-type').value;
    const classLevel = document.getElementById('class-level').value;
    const filteredClasses = classes.filter((cls) => cls.type === classType && cls.level === classLevel);
    renderClassResults(filteredClasses);
});

// Render show results
function renderShowResults(shows) {
    showResults.innerHTML = '';
    if (shows.length === 0) {
        const noResults = document.createElement('p');
        noResults.textContent = 'No shows found';
        showResults.appendChild(noResults);
    } else {
        shows.forEach((show) => {
            const showElement = document.createElement('div');
            showElement.classList.add('show');
            showElement.innerHTML = `
                <h3>${show.name}</h3>
                <p>Location: ${show.location}</p>
                <p>Date: ${show.date}</p>
            `;
            showResults.appendChild(showElement);
        });
    }
}

// Render class results
function renderClassResults(classes) {
    classResults.innerHTML = '';
    if (classes.length === 0) {
        const noResults = document.createElement('p');
        noResults.textContent = 'No classes found';
        classResults.appendChild(noResults);
    } else {
        classes.forEach((cls) => {
            const classElement = document.createElement('div');
            classElement.classList.add('class');
            classElement.innerHTML = `
                <h3>${cls.name}</h3>
                <p>Type: ${cls.type}</p>
                <p>Level: ${cls.level}</p>
            `;
            classResults.appendChild(classElement);
        });
    }
}
```
