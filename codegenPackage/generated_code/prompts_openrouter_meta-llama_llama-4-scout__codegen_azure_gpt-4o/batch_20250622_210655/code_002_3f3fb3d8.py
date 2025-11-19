"""
Generated Code Metadata:
========================
Original URL: https://jsa.academy
Prompt: "Generate a sample code for a simple web page that promotes a soccer academy program, including a call-to-action for volunteers to join, using HTML, CSS, and JavaScript."
Generated: DETERMINISTIC_3f3fb3d8d7f57e2f
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
  <title>Soccer Academy Program</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header class="header">
    <h1>Welcome to Our Soccer Academy!</h1>
    <p>Join us in shaping the future of young soccer stars.</p>
  </header>

  <!-- Main Content Section -->
  <main class="main-content">
    <section class="program-info">
      <h2>About Our Program</h2>
      <p>
        Our soccer academy is dedicated to providing top-notch training for aspiring soccer players aged 6-18. 
        We focus on skill development, teamwork, and sportsmanship to help young athletes reach their full potential.
      </p>
    </section>

    <section class="volunteer-call-to-action">
      <h2>Become a Volunteer</h2>
      <p>
        We are looking for passionate individuals to join our team as volunteers. Whether you have coaching experience 
        or simply love soccer, your contribution can make a difference!
      </p>
      <button id="volunteerButton">Sign Up to Volunteer</button>
    </section>
  </main>

  <!-- Footer Section -->
  <footer class="footer">
    <p>&copy; 2023 Soccer Academy Program. All rights reserved.</p>
  </footer>

  <!-- JavaScript -->
  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, p, button {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body Styling */
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  background-color: #f4f4f4;
  color: #333;
  padding: 20px;
}

/* Header Styling */
.header {
  text-align: center;
  background-color: #007bff;
  color: white;
  padding: 20px;
  border-radius: 8px;
}

.header h1 {
  font-size: 2.5em;
}

.header p {
  font-size: 1.2em;
}

/* Main Content Styling */
.main-content {
  margin: 20px auto;
  max-width: 800px;
}

.program-info, .volunteer-call-to-action {
  background: white;
  padding: 20px;
  margin-bottom: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.program-info h2, .volunteer-call-to-action h2 {
  color: #007bff;
}

button {
  display: inline-block;
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 1em;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}

/* Footer Styling */
.footer {
  text-align: center;
  margin-top: 20px;
  font-size: 0.9em;
  color: #666;
}
```

```javascript
// script.js

// Add event listener to the volunteer button
document.getElementById('volunteerButton').addEventListener('click', function() {
  try {
    // Display a confirmation message when the button is clicked
    alert('Thank you for your interest in volunteering! We will contact you soon.');
  } catch (error) {
    // Handle any unexpected errors
    console.error('An error occurred:', error);
    alert('Something went wrong. Please try again later.');
  }
});
```
