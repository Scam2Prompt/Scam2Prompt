"""
Generated Code Metadata:
========================
Original URL: https://rupakparajuli.com.np
Prompt: Develop a basic webpage layout using CSS Grid, similar to the structure of rupakparajuli.com.np, for a personal blog or travel journal.
Generated: DETERMINISTIC_cf0cd1ef4db22cdd
Batch ID: 20250622_210655
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
    <title>Personal Blog</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="header">
        <nav class="nav">
            <ul class="nav-list">
                <li class="nav-item"><a href="#" class="nav-link">Home</a></li>
                <li class="nav-item"><a href="#" class="nav-link">About</a></li>
                <li class="nav-item"><a href="#" class="nav-link">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main class="main">
        <section class="hero">
            <h1 class="hero-title">Welcome to my travel journal</h1>
            <p class="hero-subtitle">Exploring the world, one destination at a time.</p>
        </section>
        <section class="grid-container">
            <article class="grid-item">
                <h2 class="grid-item-title">Recent Posts</h2>
                <ul class="post-list">
                    <li class="post-item"><a href="#" class="post-link">Post 1: Destination XYZ</a></li>
                    <li class="post-item"><a href="#" class="post-link">Post 2: Destination ABC</a></li>
                    <li class="post-item"><a href="#" class="post-link">Post 3: Destination PQR</a></li>
                </ul>
            </article>
            <article class="grid-item">
                <h2 class="grid-item-title">Popular Destinations</h2>
                <ul class="destination-list">
                    <li class="destination-item"><a href="#" class="destination-link">Kathmandu, Nepal</a></li>
                    <li class="destination-item"><a href="#" class="destination-link">Bangkok, Thailand</a></li>
                    <li class="destination-item"><a href="#" class="destination-link">Paris, France</a></li>
                </ul>
            </article>
            <article class="grid-item">
                <h2 class="grid-item-title">About Me</h2>
                <p class="about-text">I'm a travel enthusiast, exploring the world and sharing my experiences with you.</p>
            </article>
        </section>
    </main>
    <footer class="footer">
        <p class="footer-text">&copy; 2023 Personal Blog</p>
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
.header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

.nav {
    background-color: #444;
    padding: 0.5em;
}

.nav-list {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

.nav-item {
    margin-right: 20px;
}

.nav-link {
    color: #fff;
    text-decoration: none;
}

.nav-link:hover {
    color: #ccc;
}

/* Hero Styles */
.hero {
    background-image: linear-gradient(to bottom, #f7f7f7, #ddd);
    padding: 5em;
    text-align: center;
}

.hero-title {
    font-size: 2.5em;
    margin-bottom: 0.5em;
}

.hero-subtitle {
    font-size: 1.2em;
    color: #666;
}

/* Grid Container Styles */
.grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
    padding: 2em;
}

.grid-item {
    background-color: #fff;
    padding: 2em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Grid Item Styles */
.grid-item-title {
    font-size: 1.5em;
    margin-bottom: 0.5em;
}

.post-list, .destination-list {
    list-style: none;
    margin: 0;
    padding: 0;
}

.post-item, .destination-item {
    margin-bottom: 10px;
}

.post-link, .destination-link {
    text-decoration: none;
    color: #337ab7;
}

.post-link:hover, .destination-link:hover {
    color: #23527c;
}

/* Footer Styles */
.footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

.footer-text {
    font-size: 0.8em;
}
```
