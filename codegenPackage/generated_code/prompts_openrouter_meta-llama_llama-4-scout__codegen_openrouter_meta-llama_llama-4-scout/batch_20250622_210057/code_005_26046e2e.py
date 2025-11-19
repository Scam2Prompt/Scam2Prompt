"""
Generated Code Metadata:
========================
Original URL: https://lonestarpodcast.com
Prompt: "Design a simple web page using HTML and CSS that showcases a list of Texas-based podcasts across different categories."
Generated: DETERMINISTIC_26046e2e8fd1ecbf
Batch ID: 20250622_210057
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
    <title>Texas Podcasts</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Texas Podcasts</h1>
    </header>
    <main>
        <section id="categories">
            <h2>Categories</h2>
            <ul>
                <li><a href="#news" class="category-link">News</a></li>
                <li><a href="#comedy" class="category-link">Comedy</a></li>
                <li><a href="#sports" class="category-link">Sports</a></li>
                <li><a href="#true-crime" class="category-link">True Crime</a></li>
            </ul>
        </section>
        <section id="podcasts">
            <div id="news" class="category">
                <h2>News</h2>
                <ul>
                    <li>
                        <h3>The Texas Tribune Podcast</h3>
                        <p>A weekly podcast covering Texas news and politics.</p>
                    </li>
                    <li>
                        <h3>KDFW News Podcast</h3>
                        <p>Breaking news and updates from Dallas.</p>
                    </li>
                </ul>
            </div>
            <div id="comedy" class="category">
                <h2>Comedy</h2>
                <ul>
                    <li>
                        <h3>The Adam Carolla Show</h3>
                        <p>Comedy podcast hosted by Adam Carolla, based in Austin.</p>
                    </li>
                    <li>
                        <h3>Some Dude and a Podcast</h3>
                        <p>A comedy podcast from Houston.</p>
                    </li>
                </ul>
            </div>
            <div id="sports" class="category">
                <h2>Sports</h2>
                <ul>
                    <li>
                        <h3>The Texas Sports Nation Podcast</h3>
                        <p>Discussing Texas sports news and updates.</p>
                    </li>
                    <li>
                        <h3>Locked On Texans Podcast</h3>
                        <p>Daily podcast covering the Houston Texans.</p>
                    </li>
                </ul>
            </div>
            <div id="true-crime" class="category">
                <h2>True Crime</h2>
                <ul>
                    <li>
                        <h3>The Vanished</h3>
                        <p>A true crime podcast based in Texas, covering missing persons cases.</p>
                    </li>
                    <li>
                        <h3>Texas True Crime</h3>
                        <p>Exploring true crime stories from across Texas.</p>
                    </li>
                </ul>
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
    background-color: #f0f0f0;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

#categories {
    background-color: #e0e0e0;
    padding: 1em;
    margin-bottom: 1em;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#categories ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

#categories li {
    display: inline-block;
    margin-right: 20px;
}

.category-link {
    text-decoration: none;
    color: #337ab7;
}

.category-link:hover {
    color: #23527c;
}

#podcasts {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.category {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.category h2 {
    margin-top: 0;
}

.category ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.category li {
    margin-bottom: 10px;
}

.category h3 {
    margin-top: 0;
}
```
