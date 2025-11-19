"""
Generated Code Metadata:
========================
Original URL: https://carvalhocr.com
Prompt: "Generate a simple webpage layout using HTML and CSS for a personal portfolio site like carvalhocr.com."
Generated: DETERMINISTIC_4354ed63f3c00aab
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
    <title>Personal Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#about">About</a></li>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="about">
            <h1>About Me</h1>
            <p>Welcome to my personal portfolio site. I'm a software developer with a passion for building clean and efficient code.</p>
            <img src="profile-picture.jpg" alt="Profile Picture">
        </section>
        <section id="projects">
            <h1>My Projects</h1>
            <ul>
                <li>
                    <h2>Project 1</h2>
                    <p>Description of project 1.</p>
                    <a href="#" target="_blank">View Project</a>
                </li>
                <li>
                    <h2>Project 2</h2>
                    <p>Description of project 2.</p>
                    <a href="#" target="_blank">View Project</a>
                </li>
            </ul>
        </section>
        <section id="contact">
            <h1>Get in Touch</h1>
            <p>Feel free to reach out to me through social media or email.</p>
            <ul>
                <li><a href="#" target="_blank">LinkedIn</a></li>
                <li><a href="#" target="_blank">GitHub</a></li>
                <li><a href="mailto:example@example.com">Email</a></li>
            </ul>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Personal Portfolio</p>
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

/* Main Styles */
main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #fff;
    padding: 2em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    margin-bottom: 10px;
}

#about img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    margin: 20px;
}

/* Project Styles */
#projects ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

#projects li {
    margin-bottom: 20px;
}

#projects h2 {
    margin-bottom: 10px;
}

#projects a {
    text-decoration: none;
    color: #337ab7;
}

/* Contact Styles */
#contact ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

#contact li {
    margin-bottom: 10px;
}

#contact a {
    text-decoration: none;
    color: #337ab7;
}

/* Footer Styles */
footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```
