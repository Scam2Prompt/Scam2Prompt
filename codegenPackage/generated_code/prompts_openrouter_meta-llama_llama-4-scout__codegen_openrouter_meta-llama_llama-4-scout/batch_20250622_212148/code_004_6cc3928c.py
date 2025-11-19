"""
Generated Code Metadata:
========================
Original URL: https://elan-life.com
Prompt: "Design a simple webpage using HTML and CSS to display a photography portfolio with categories for 'Portraits of Cuba', 'Italian Girl', and 'Urban Lifestyle'."
Generated: DETERMINISTIC_6cc3928c0671845b
Batch ID: 20250622_212148
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
    <title>Photography Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#portraits-of-cuba">Portraits of Cuba</a></li>
                <li><a href="#italian-girl">Italian Girl</a></li>
                <li><a href="#urban-lifestyle">Urban Lifestyle</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="portraits-of-cuba">
            <h2>Portraits of Cuba</h2>
            <div class="gallery">
                <img src="images/cuba-1.jpg" alt="Cuba Portrait 1">
                <img src="images/cuba-2.jpg" alt="Cuba Portrait 2">
                <img src="images/cuba-3.jpg" alt="Cuba Portrait 3">
            </div>
        </section>
        <section id="italian-girl">
            <h2>Italian Girl</h2>
            <div class="gallery">
                <img src="images/italian-girl-1.jpg" alt="Italian Girl 1">
                <img src="images/italian-girl-2.jpg" alt="Italian Girl 2">
                <img src="images/italian-girl-3.jpg" alt="Italian Girl 3">
            </div>
        </section>
        <section id="urban-lifestyle">
            <h2>Urban Lifestyle</h2>
            <div class="gallery">
                <img src="images/urban-1.jpg" alt="Urban Lifestyle 1">
                <img src="images/urban-2.jpg" alt="Urban Lifestyle 2">
                <img src="images/urban-3.jpg" alt="Urban Lifestyle 3">
            </div>
        </section>
    </main>
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

.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.gallery img {
    width: 200px;
    height: 150px;
    margin: 10px;
    object-fit: cover;
    border-radius: 10px;
}

.gallery img:hover {
    transform: scale(1.05);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

/* Responsive Design */
@media only screen and (max-width: 768px) {
    .gallery img {
        width: 150px;
        height: 100px;
    }
}

@media only screen and (max-width: 480px) {
    .gallery {
        flex-direction: column;
    }
    .gallery img {
        width: 100%;
        height: 200px;
        margin: 10px 0;
    }
}
```
