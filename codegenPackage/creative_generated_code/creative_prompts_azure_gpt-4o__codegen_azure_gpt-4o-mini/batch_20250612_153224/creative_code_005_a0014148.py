"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digistrategy.in
Prompt: Write HTML and CSS code for a "Get A Quote" form, like the one featured on digistrategy.in, with a modern and professional design.
Generated: DETERMINISTIC_a001414804152df2
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
    <title>Get A Quote</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="quote-form-container">
        <h1>Get A Quote</h1>
        <form id="quoteForm" action="/submit-quote" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required placeholder="Your Name">

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="Your Email">

            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone" required placeholder="Your Phone Number">

            <label for="service">Service Required:</label>
            <select id="service" name="service" required>
                <option value="">--Select a Service--</option>
                <option value="web-development">Web Development</option>
                <option value="graphic-design">Graphic Design</option>
                <option value="digital-marketing">Digital Marketing</option>
                <option value="seo">SEO</option>
            </select>

            <label for="message">Additional Information:</label>
            <textarea id="message" name="message" rows="4" placeholder="Any additional details..."></textarea>

            <button type="submit">Request a Quote</button>
        </form>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margin and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

/* Container for the quote form */
.quote-form-container {
    max-width: 500px;
    margin: 50px auto;
    padding: 20px;
    background: white;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
}

/* Header styling */
h1 {
    text-align: center;
    margin-bottom: 20px;
    color: #007BFF;
}

/* Form element styling */
form {
    display: flex;
    flex-direction: column;
}

/* Label styling */
label {
    margin-bottom: 5px;
    font-weight: bold;
}

/* Input styling */
input, select, textarea {
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
}

/* Focus state for inputs */
input:focus, select:focus, textarea:focus {
    border-color: #007BFF;
    outline: none;
}

/* Button styling */
button {
    padding: 10px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
}

/* Button hover effect */
button:hover {
    background-color: #0056b3;
}
```
