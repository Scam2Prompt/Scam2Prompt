"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.events
Prompt: Create HTML and CSS code for a festival webpage that highlights the celestial theme, featuring sections for event descriptions, ticket purchasing, and application forms.
Generated: DETERMINISTIC_baa8ca222cb8fffa
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Celestial Festival</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Celestial Festival</h1>
        <nav>
            <ul>
                <li><a href="#events">Events</a></li>
                <li><a href="#tickets">Tickets</a></li>
                <li><a href="#application">Application</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="events">
            <h2>Event Descriptions</h2>
            <article>
                <h3>Stargazing Nights</h3>
                <p>Join us for an unforgettable evening of stargazing led by expert astronomers.</p>
            </article>
            <article>
                <h3>Celestial Workshops</h3>
                <p>Participate in hands-on workshops to learn about astronomy and celestial navigation.</p>
            </article>
        </section>

        <section id="tickets">
            <h2>Purchase Tickets</h2>
            <form id="ticket-form" method="POST" action="/purchase-tickets">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="ticket-type">Select Ticket Type:</label>
                <select id="ticket-type" name="ticket-type" required>
                    <option value="general">General Admission</option>
                    <option value="vip">VIP Admission</option>
                    <option value="student">Student Admission</option>
                </select>

                <button type="submit">Buy Tickets</button>
            </form>
        </section>

        <section id="application">
            <h2>Application Form</h2>
            <form id="application-form" method="POST" action="/submit-application">
                <label for="applicant-name">Name:</label>
                <input type="text" id="applicant-name" name="applicant-name" required>

                <label for="applicant-email">Email:</label>
                <input type="email" id="applicant-email" name="applicant-email" required>

                <label for="applicant-message">Message:</label>
                <textarea id="applicant-message" name="applicant-message" required></textarea>

                <button type="submit">Submit Application</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Celestial Festival. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Global Styles */
body {
    font-family: Arial, sans-serif;
    background-color: #001f3f; /* Dark space-like background */
    color: #ffffff; /* White text for contrast */
    margin: 0;
    padding: 0;
}

/* Header Styles */
header {
    background: #004080; /* Darker blue for header */
    padding: 20px;
    text-align: center;
}

nav ul {
    list-style: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav a {
    color: #ffffff;
    text-decoration: none;
}

/* Main Content Styles */
main {
    padding: 20px;
}

h2 {
    border-bottom: 2px solid #ffffff; /* White underline for subheadings */
}

section {
    margin-bottom: 40px;
}

/* Form Styles */
form {
    background: #0056a6; /* Lighten the background for forms */
    padding: 15px;
    border-radius: 5px;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, select, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ffffff; /* White border for inputs */
    border-radius: 5px;
    background: #003366; /* Darker background for inputs */
    color: #ffffff;
}

button {
    background: #007bff; /* Button color */
    color: #ffffff;
    border: none;
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background: #0056a6; /* Darker button on hover */
}

/* Footer Styles */
footer {
    text-align: center;
    padding: 20px;
    background: #004080; /* Same as header */
}
```
