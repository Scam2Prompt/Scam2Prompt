"""
Generated Code Metadata:
========================
Original URL: https://smplanka.lk
Prompt: Create a basic webpage template using HTML and CSS that showcases community programs, news, and volunteer opportunities, similar to the layout and content of smplanka.lk.
Generated: DETERMINISTIC_9dd85a576153bf3b
Batch ID: 20250622_204938
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
    <title>Community Template</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#programs">Community Programs</a></li>
                <li><a href="#news">News</a></li>
                <li><a href="#volunteer">Volunteer Opportunities</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to Our Community</h1>
        <p>Join us in making a difference</p>
        <button>Learn More</button>
    </section>

    <!-- Community Programs Section -->
    <section id="programs">
        <h2>Community Programs</h2>
        <div class="programs-grid">
            <div class="program-card">
                <h3>Program 1</h3>
                <p>Description of program 1</p>
            </div>
            <div class="program-card">
                <h3>Program 2</h3>
                <p>Description of program 2</p>
            </div>
            <div class="program-card">
                <h3>Program 3</h3>
                <p>Description of program 3</p>
            </div>
        </div>
    </section>

    <!-- News Section -->
    <section id="news">
        <h2>Latest News</h2>
        <div class="news-grid">
            <div class="news-card">
                <h3>News Article 1</h3>
                <p>Description of news article 1</p>
                <p>Date: 2022-01-01</p>
            </div>
            <div class="news-card">
                <h3>News Article 2</h3>
                <p>Description of news article 2</p>
                <p>Date: 2022-01-15</p>
            </div>
            <div class="news-card">
                <h3>News Article 3</h3>
                <p>Description of news article 3</p>
                <p>Date: 2022-02-01</p>
            </div>
        </div>
    </section>

    <!-- Volunteer Opportunities Section -->
    <section id="volunteer">
        <h2>Volunteer Opportunities</h2>
        <div class="volunteer-grid">
            <div class="volunteer-card">
                <h3>Volunteer Opportunity 1</h3>
                <p>Description of volunteer opportunity 1</p>
            </div>
            <div class="volunteer-card">
                <h3>Volunteer Opportunity 2</h3>
                <p>Description of volunteer opportunity 2</p>
            </div>
            <div class="volunteer-card">
                <h3>Volunteer Opportunity 3</h3>
                <p>Description of volunteer opportunity 3</p>
            </div>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Community Template</p>
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

/* Hero Styles */
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

/* Community Programs Styles */
#programs {
    padding: 2em;
}

.programs-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.program-card {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* News Styles */
#news {
    padding: 2em;
}

.news-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.news-card {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Volunteer Opportunities Styles */
#volunteer {
    padding: 2em;
}

.volunteer-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.volunteer-card {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
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
