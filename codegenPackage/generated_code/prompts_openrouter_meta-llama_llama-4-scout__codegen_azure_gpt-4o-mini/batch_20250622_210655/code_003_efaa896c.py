"""
Generated Code Metadata:
========================
Original URL: https://ibcaj.org
Prompt: "Design a simple web page for announcing cultural events, including sections for upcoming and past events, using HTML and CSS."
Generated: DETERMINISTIC_efaa896cb59eddd6
Batch ID: 20250622_210655
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
    <title>Cultural Events Announcement</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Cultural Events Announcement</h1>
        <nav>
            <ul>
                <li><a href="#upcoming">Upcoming Events</a></li>
                <li><a href="#past">Past Events</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="upcoming">
            <h2>Upcoming Events</h2>
            <article class="event">
                <h3>Art Exhibition</h3>
                <p>Date: March 15, 2024</p>
                <p>Location: City Art Gallery</p>
                <p>Description: Join us for an exhibition showcasing local artists.</p>
            </article>
            <article class="event">
                <h3>Music Festival</h3>
                <p>Date: April 20, 2024</p>
                <p>Location: Central Park</p>
                <p>Description: A day filled with music from various genres.</p>
            </article>
        </section>

        <section id="past">
            <h2>Past Events</h2>
            <article class="event">
                <h3>Theater Play</h3>
                <p>Date: January 10, 2024</p>
                <p>Location: Downtown Theater</p>
                <p>Description: A captivating play performed by local actors.</p>
            </article>
            <article class="event">
                <h3>Food Festival</h3>
                <p>Date: February 5, 2024</p>
                <p>Location: Riverside Park</p>
                <p>Description: A celebration of culinary delights from around the world.</p>
            </article>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Cultural Events. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, p {
    margin: 0;
    padding: 0;
}

/* Set a basic font and background color */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

/* Style the header */
header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
    text-align: center;
}

/* Navigation styles */
nav ul {
    list-style: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #ffffff;
    text-decoration: none;
}

/* Main content styles */
main {
    padding: 20px;
}

/* Section styles */
section {
    margin-bottom: 40px;
}

/* Event article styles */
.event {
    background: #ffffff;
    border: 1px solid #dddddd;
    border-radius: 5px;
    padding: 15px;
    margin-bottom: 20px;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #35424a;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
