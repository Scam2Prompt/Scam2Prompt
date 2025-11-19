"""
Generated Code Metadata:
========================
Original URL: https://xeluudong.com
Prompt: Create a sample HTML structure for a webpage that features articles on interior design, including sections for kitchen layouts and Feng Shui tips.
Generated: DETERMINISTIC_4588c7b3badcf39c
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interior Design Articles</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#kitchen-layouts">Kitchen Layouts</a></li>
                <li><a href="#feng-shui-tips">Feng Shui Tips</a></li>
                <li><a href="#latest-articles">Latest Articles</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to Interior Design Insights</h1>
        <p>Explore the latest trends and tips in interior design</p>
    </section>

    <!-- Main Content Section -->
    <main>
        <!-- Kitchen Layouts Section -->
        <section id="kitchen-layouts">
            <h2>Kitchen Layouts</h2>
            <article>
                <h3>Modern Kitchen Design</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                <img src="modern-kitchen.jpg" alt="Modern Kitchen Design">
            </article>
            <article>
                <h3>Small Kitchen Solutions</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                <img src="small-kitchen.jpg" alt="Small Kitchen Solutions">
            </article>
        </section>

        <!-- Feng Shui Tips Section -->
        <section id="feng-shui-tips">
            <h2>Feng Shui Tips</h2>
            <article>
                <h3>Creating a Balanced Space</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                <img src="feng-shui-tips.jpg" alt="Feng Shui Tips">
            </article>
            <article>
                <h3>Using Colors in Feng Shui</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                <img src="feng-shui-colors.jpg" alt="Feng Shui Colors">
            </article>
        </section>

        <!-- Latest Articles Section -->
        <section id="latest-articles">
            <h2>Latest Articles</h2>
            <article>
                <h3>5 Interior Design Trends to Watch</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                <img src="interior-design-trends.jpg" alt="Interior Design Trends">
            </article>
            <article>
                <h3>How to Create a Home Office</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                <img src="home-office.jpg" alt="Home Office">
            </article>
        </section>
    </main>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Interior Design Insights</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

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

h2 {
    margin-top: 0;
}

article {
    margin-bottom: 20px;
}

img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```

```javascript
// script.js

// Add event listener to nav links
document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('header nav a');

    navLinks.forEach((link) => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            targetSection.scrollIntoView({ behavior: 'smooth' });
        });
    });
});
```
