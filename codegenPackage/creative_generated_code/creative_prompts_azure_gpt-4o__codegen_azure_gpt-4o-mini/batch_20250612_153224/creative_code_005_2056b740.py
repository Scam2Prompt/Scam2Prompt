"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.viviresconvivir.cl
Prompt: Write code in HTML and CSS to design a webpage for a virtual workshop on the value of participation, inspired by the educational resources provided by Fundación Patricio Aylwin.
Generated: DETERMINISTIC_2056b7409d3bae1e
Batch ID: 20250612_153224
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
    <meta name="description" content="Join us for a virtual workshop focused on the value of participation, inspired by Fundación Patricio Aylwin.">
    <title>Virtual Workshop: The Value of Participation</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <header>
        <h1>Virtual Workshop: The Value of Participation</h1>
        <p>Hosted by Fundación Patricio Aylwin</p>
    </header>

    <main>
        <section id="intro">
            <h2>Welcome!</h2>
            <p>This workshop aims to explore the importance of participation in society and its impact on democracy.</p>
        </section>

        <section id="workshop-details">
            <h2>Workshop Details</h2>
            <ul>
                <li><strong>Date:</strong> April 15, 2024</li>
                <li><strong>Time:</strong> 10:00 AM - 12:00 PM (GMT)</li>
                <li><strong>Location:</strong> Online (Zoom link will be provided upon registration)</li>
            </ul>
        </section>

        <section id="registration">
            <h2>Registration</h2>
            <form action="submit_registration.php" method="POST" id="registration-form">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <button type="submit">Register Now</button>
            </form>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <p>If you have any questions, please email us at <a href="mailto:info@fundacionaylwin.cl">info@fundacionaylwin.cl</a></p>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Fundación Patricio Aylwin. All rights reserved.</p>
    </footer>
</body>

</html>
```

```css
/* styles.css */

/* Reset some default browser styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styles */
header {
    background: #007bff; /* Primary color */
    color: white;
    padding: 20px;
    text-align: center;
}

/* Main content styles */
main {
    padding: 20px;
}

h2 {
    color: #007bff; /* Primary color */
    margin-top: 20px;
}

/* Form styles */
form {
    display: flex;
    flex-direction: column;
    max-width: 400px;
    margin: auto;
}

label {
    margin-bottom: 5px;
}

input {
    margin-bottom: 15px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    padding: 10px;
    background: #007bff; /* Primary color */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background: #0056b3; /* Darker shade for hover effect */
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #f1f1f1;
    position: relative;
    bottom: 0;
    width: 100%;
}
``` 

Make sure to create a file named `submit_registration.php` for handling form submissions appropriately.
