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

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Second City Comedy Shows & Classes</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to The Second City</h1>
        <p>Your destination for comedy shows and classes!</p>
    </header>

    <nav>
        <ul>
            <li><a href="#shows">Comedy Shows</a></li>
            <li><a href="#classes">Comedy Classes</a></li>
        </ul>
    </nav>

    <main>
        <section id="shows">
            <h2>Upcoming Comedy Shows</h2>
            <div class="show-finder">
                <input type="text" id="showSearch" placeholder="Search for a show...">
                <button onclick="searchShows()">Search</button>
            </div>
            <ul id="showList">
                <li>Show 1: The Comedy Hour</li>
                <li>Show 2: Laugh Out Loud</li>
                <li>Show 3: Improv Night</li>
                <li>Show 4: Stand-Up Spectacular</li>
            </ul>
        </section>

        <section id="classes">
            <h2>Comedy Classes</h2>
            <div class="class-search">
                <input type="text" id="classSearch" placeholder="Search for a class...">
                <button onclick="searchClasses()">Search</button>
            </div>
            <ul id="classList">
                <li>Class 1: Intro to Improv</li>
                <li>Class 2: Stand-Up Comedy Basics</li>
                <li>Class 3: Sketch Writing Workshop</li>
                <li>Class 4: Advanced Improv Techniques</li>
            </ul>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 The Second City. All rights reserved.</p>
    </footer>

    <script>
        // Function to search for shows based on user input
        function searchShows() {
            const input = document.getElementById('showSearch').value.toLowerCase();
            const showList = document.getElementById('showList');
            const shows = showList.getElementsByTagName('li');

            // Loop through shows and hide those that don't match the search
            for (let i = 0; i < shows.length; i++) {
                const show = shows[i].textContent.toLowerCase();
                shows[i].style.display = show.includes(input) ? '' : 'none';
            }
        }

        // Function to search for classes based on user input
        function searchClasses() {
            const input = document.getElementById('classSearch').value.toLowerCase();
            const classList = document.getElementById('classList');
            const classes = classList.getElementsByTagName('li');

            // Loop through classes and hide those that don't match the search
            for (let i = 0; i < classes.length; i++) {
                const className = classes[i].textContent.toLowerCase();
                classes[i].style.display = className.includes(input) ? '' : 'none';
            }
        }
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p, ul {
    margin: 0;
    padding: 0;
}

/* Basic styling for the body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styling */
header {
    background: #333;
    color: #fff;
    padding: 20px 0;
    text-align: center;
}

/* Navigation styling */
nav {
    background: #444;
    color: #fff;
    padding: 10px 0;
}

nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Main content styling */
main {
    padding: 20px;
}

/* Section styling */
section {
    margin-bottom: 40px;
}

/* Search input and button styling */
.show-finder, .class-search {
    margin-bottom: 20px;
}

input[type="text"] {
    padding: 10px;
    width: 200px;
}

button {
    padding: 10px 15px;
    background: #333;
    color: #fff;
    border: none;
    cursor: pointer;
}

button:hover {
    background: #555;
}

/* Footer styling */
footer {
    text-align: center;
    padding: 20px 0;
    background: #333;
    color: #fff;
}
```
