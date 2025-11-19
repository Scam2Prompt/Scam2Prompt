"""
Generated Code Metadata:
========================
Original URL: https://ullivis.blogspot.com
Prompt: Design a basic Blogger theme similar to the one on illuvis, including a section for articles and a search function, using only HTML and CSS.
Generated: DETERMINISTIC_8acb3840172f846e
Batch ID: 20250622_205158
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
    <title>Illuvis-inspired Blogger Theme</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
        <div class="search-bar">
            <input type="text" id="search-input" placeholder="Search...">
            <button id="search-button">Search</button>
        </div>
    </header>

    <!-- Main Content Section -->
    <main>
        <section class="articles">
            <h1>Recent Articles</h1>
            <div class="article-grid">
                <article>
                    <h2><a href="#">Article Title 1</a></h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                </article>
                <article>
                    <h2><a href="#">Article Title 2</a></h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                </article>
                <article>
                    <h2><a href="#">Article Title 3</a></h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                </article>
            </div>
        </section>
    </main>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Illuvis-inspired Blogger Theme</p>
    </footer>

    <script>
        // Basic search functionality
        const searchInput = document.getElementById('search-input');
        const searchButton = document.getElementById('search-button');

        searchButton.addEventListener('click', () => {
            const searchTerm = searchInput.value.trim();
            if (searchTerm !== '') {
                // Implement search logic here (e.g., send request to server)
                console.log(`Searching for: ${searchTerm}`);
            }
        });
    </script>
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

.search-bar {
    margin-top: 10px;
}

#search-input {
    padding: 10px;
    font-size: 16px;
    border: none;
    border-radius: 5px 0 0 5px;
}

#search-button {
    padding: 10px;
    font-size: 16px;
    border: none;
    border-radius: 0 5px 5px 0;
    background-color: #444;
    color: #fff;
    cursor: pointer;
}

/* Main Content Styles */
main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.articles {
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.article-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

article {
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
}

article h2 {
    margin-top: 0;
}

article a {
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
