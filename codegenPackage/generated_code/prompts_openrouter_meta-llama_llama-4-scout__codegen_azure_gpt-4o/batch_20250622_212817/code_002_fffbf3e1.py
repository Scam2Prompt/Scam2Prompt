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

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Portfolio website showcasing music, horror, and creative projects like PhantomsLens.">
    <title>Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section with Navigation Menu -->
    <header>
        <nav class="navbar">
            <div class="logo">My Portfolio</div>
            <ul class="nav-links">
                <li><a href="#music">Music</a></li>
                <li><a href="#horror">Horror</a></li>
                <li><a href="#creative-projects">Creative Projects</a></li>
            </ul>
        </nav>
    </header>

    <!-- Main Content Sections -->
    <main>
        <!-- Music Section -->
        <section id="music" class="section">
            <h2>Music</h2>
            <p>Explore my music projects, compositions, and performances.</p>
        </section>

        <!-- Horror Section -->
        <section id="horror" class="section">
            <h2>Horror</h2>
            <p>Dive into my horror-themed creations, including stories and visuals.</p>
        </section>

        <!-- Creative Projects Section -->
        <section id="creative-projects" class="section">
            <h2>Creative Projects</h2>
            <p>Discover my other creative works, such as PhantomsLens and more.</p>
        </section>
    </main>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 My Portfolio. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Header and Navigation */
header {
    background-color: #222;
    color: #fff;
    padding: 1rem 0;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

.logo {
    font-size: 1.5rem;
    font-weight: bold;
}

.nav-links {
    list-style: none;
    display: flex;
}

.nav-links li {
    margin: 0 1rem;
}

.nav-links a {
    text-decoration: none;
    color: #fff;
    transition: color 0.3s ease;
}

.nav-links a:hover {
    color: #00bcd4;
}

/* Section Styling */
.section {
    padding: 2rem 1rem;
    max-width: 1200px;
    margin: 0 auto;
    background-color: #fff;
    margin-bottom: 1rem;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.section h2 {
    margin-bottom: 1rem;
    color: #222;
}

.section p {
    color: #555;
}

/* Footer Styling */
footer {
    text-align: center;
    padding: 1rem 0;
    background-color: #222;
    color: #fff;
    font-size: 0.9rem;
}
```
