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

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Community programs, news, and volunteer opportunities">
    <meta name="author" content="Your Organization Name">
    <title>Community Programs</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <h1>Community Programs</h1>
            <nav>
                <ul>
                    <li><a href="#programs">Programs</a></li>
                    <li><a href="#news">News</a></li>
                    <li><a href="#volunteer">Volunteer</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Main Content Section -->
    <main>
        <!-- Community Programs Section -->
        <section id="programs" class="section">
            <div class="container">
                <h2>Our Programs</h2>
                <p>Explore the various programs we offer to support the community.</p>
                <div class="grid">
                    <div class="card">
                        <h3>Education Program</h3>
                        <p>Providing educational resources and support for children and adults.</p>
                    </div>
                    <div class="card">
                        <h3>Health Initiative</h3>
                        <p>Promoting health and wellness through workshops and free clinics.</p>
                    </div>
                    <div class="card">
                        <h3>Environmental Awareness</h3>
                        <p>Encouraging sustainable practices and environmental conservation.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- News Section -->
        <section id="news" class="section">
            <div class="container">
                <h2>Latest News</h2>
                <p>Stay updated with the latest happenings in our community.</p>
                <ul class="news-list">
                    <li><a href="#">Community Clean-Up Drive Scheduled for Next Week</a></li>
                    <li><a href="#">New Volunteer Opportunities Announced</a></li>
                    <li><a href="#">Health Workshop Recap: Tips for a Healthy Lifestyle</a></li>
                </ul>
            </div>
        </section>

        <!-- Volunteer Opportunities Section -->
        <section id="volunteer" class="section">
            <div class="container">
                <h2>Volunteer Opportunities</h2>
                <p>Join us in making a difference. Sign up for volunteer opportunities today!</p>
                <div class="grid">
                    <div class="card">
                        <h3>Teaching Assistant</h3>
                        <p>Help children with their studies in our education program.</p>
                    </div>
                    <div class="card">
                        <h3>Event Organizer</h3>
                        <p>Assist in planning and organizing community events.</p>
                    </div>
                    <div class="card">
                        <h3>Environmental Advocate</h3>
                        <p>Participate in tree planting and awareness campaigns.</p>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer Section -->
    <footer>
        <div class="container">
            <p>&copy; 2023 Your Organization Name. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p, ul, li, a {
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

/* Container */
.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
}

/* Header */
header {
    background-color: #0073e6;
    color: #fff;
    padding: 1rem 0;
}

header h1 {
    text-align: center;
    margin-bottom: 0.5rem;
}

header nav ul {
    display: flex;
    justify-content: center;
    list-style: none;
}

header nav ul li {
    margin: 0 1rem;
}

header nav ul li a {
    color: #fff;
    text-decoration: none;
    font-weight: bold;
}

/* Section Styling */
.section {
    padding: 2rem 0;
    background-color: #fff;
    margin-bottom: 1rem;
}

.section h2 {
    text-align: center;
    margin-bottom: 1rem;
}

.section p {
    text-align: center;
    margin-bottom: 2rem;
}

/* Grid Layout */
.grid {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
}

.card {
    background-color: #f1f1f1;
    padding: 1rem;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    width: 300px;
    text-align: center;
}

.card h3 {
    margin-bottom: 0.5rem;
}

/* News List */
.news-list {
    list-style: none;
    padding: 0;
    text-align: center;
}

.news-list li {
    margin-bottom: 0.5rem;
}

.news-list li a {
    text-decoration: none;
    color: #0073e6;
}

.news-list li a:hover {
    text-decoration: underline;
}

/* Footer */
footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 1rem 0;
}
```
