"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftbeerbox.com
Prompt: Write HTML and CSS code to design a landing page for a craft beer subscription service, featuring a "Contact Us" section with an email form.
Generated: DETERMINISTIC_f40721fcbb0ccc0e
Batch ID: 20250612_154954
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
  <meta name="description" content="Craft Beer Subscription Service">
  <title>Craft Beer Subscription</title>
  <link rel="stylesheet" href="styles.css">
</head>

<body>
  <!-- Header Section -->
  <header class="header">
    <div class="container">
      <h1>Craft Beer Subscription</h1>
      <p>Discover unique craft beers delivered to your doorstep every month.</p>
    </div>
  </header>

  <!-- Main Content Section -->
  <section class="main-content container">
    <h2>Why Choose Us?</h2>
    <p>We source the best craft beers from local breweries and deliver them to you, hassle-free.</p>
    <ul>
      <li>Exclusive selections from top breweries</li>
      <li>Flexible subscription plans</li>
      <li>Delivered fresh to your home</li>
    </ul>
  </section>

  <!-- Contact Us Section -->
  <section class="contact-us container">
    <h2>Contact Us</h2>
    <p>Have questions? Reach out to us below.</p>
    <form id="contact-form" action="/submit-form" method="post">
      <label for="name">Name:</label>
      <input type="text" id="name" name="name" required placeholder="Your Name">

      <label for="email">Email:</label>
      <input type="email" id="email" name="email" required placeholder="Your Email">

      <label for="message">Message:</label>
      <textarea id="message" name="message" rows="4" required placeholder="Your Message"></textarea>

      <button type="submit">Submit</button>
    </form>
  </section>

  <!-- Footer Section -->
  <footer class="footer container">
    <p>&copy; 2023 Craft Beer Subscription. All rights reserved.</p>
  </footer>
</body>

</html>
```

```css
/* styles.css */

/* Global Styles */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  line-height: 1.6;
}

.container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
}

/* Header Section */
.header {
  background-color: #f8b400;
  color: #fff;
  text-align: center;
  padding: 2rem 1rem;
}

.header h1 {
  font-size: 2.5rem;
}

.header p {
  font-size: 1.2rem;
}

/* Main Content Section */
.main-content {
  margin: 2rem 0;
}

.main-content h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #333;
}

.main-content ul {
  list-style-type: disc;
  margin-left: 1.5rem;
}

.main-content ul li {
  margin-bottom: 0.5rem;
}

/* Contact Us Section */
.contact-us {
  margin: 2rem 0;
}

.contact-us h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #333;
}

.contact-us form {
  display: flex;
  flex-direction: column;
}

.contact-us label {
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.contact-us input,
.contact-us textarea {
  margin-bottom: 1rem;
  padding: 0.5rem;
  font-size: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.contact-us button {
  background-color: #f8b400;
  color: #fff;
  padding: 0.7rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.contact-us button:hover {
  background-color: #e09e00;
}

/* Footer Section */
.footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 1rem 0;
}

.footer p {
  margin: 0;
  font-size: 0.9rem;
}
```
