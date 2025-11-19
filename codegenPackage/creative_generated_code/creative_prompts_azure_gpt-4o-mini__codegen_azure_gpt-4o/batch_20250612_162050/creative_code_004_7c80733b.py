"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyscholarsacademy.com
Prompt: Design a user interface for a childcare enrollment system that includes sections for parent testimonials and program details, reflecting the layout and content style of Happy Scholars Academy's website.
Generated: DETERMINISTIC_7c80733b3905792b
Batch ID: 20250612_162050
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
  <title>Childcare Enrollment System</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Navigation Bar -->
  <header>
    <nav class="navbar">
      <div class="logo">
        <a href="#">Happy Scholars Academy</a>
      </div>
      <ul class="nav-links">
        <li><a href="#program-details">Programs</a></li>
        <li><a href="#testimonials">Testimonials</a></li>
        <li><a href="#enrollment-form">Enroll</a></li>
      </ul>
    </nav>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <h1>Welcome to Happy Scholars Academy</h1>
    <p>Empowering young minds through innovative childcare programs.</p>
  </section>

  <!-- Program Details Section -->
  <section id="program-details" class="program-details">
    <h2>Our Programs</h2>
    <div class="program-card">
      <h3>Infant Care</h3>
      <p>Providing a nurturing environment for babies aged 6 weeks to 12 months.</p>
    </div>
    <div class="program-card">
      <h3>Toddler Exploration</h3>
      <p>Interactive learning experiences for toddlers aged 1 to 3 years.</p>
    </div>
    <div class="program-card">
      <h3>Preschool Readiness</h3>
      <p>Preparing children aged 3 to 5 years for school success.</p>
    </div>
  </section>

  <!-- Parent Testimonials Section -->
  <section id="testimonials" class="testimonials">
    <h2>Parent Testimonials</h2>
    <div class="testimonial">
      <blockquote>"Happy Scholars Academy has been the best decision for our child. The staff is caring and the programs are excellent."</blockquote>
      <p>– Jane Doe</p>
    </div>
    <div class="testimonial">
      <blockquote>"Our toddler has grown so much since enrolling in the program. Highly recommend Happy Scholars Academy!"</blockquote>
      <p>– John Smith</p>
    </div>
    <div class="testimonial">
      <blockquote>"The preschool readiness program prepared my child for kindergarten and beyond. Thank you!"</blockquote>
      <p>– Sarah Johnson</p>
    </div>
  </section>

  <!-- Enrollment Form Section -->
  <section id="enrollment-form" class="enrollment-form">
    <h2>Enroll Your Child</h2>
    <form action="/submit-enrollment" method="POST">
      <!-- Parent Information -->
      <fieldset>
        <legend>Parent Information</legend>
        <label for="parent-name">Name:</label>
        <input type="text" id="parent-name" name="parentName" required>

        <label for="parent-email">Email:</label>
        <input type="email" id="parent-email" name="parentEmail" required>

        <label for="parent-phone">Phone:</label>
        <input type="tel" id="parent-phone" name="parentPhone" required>
      </fieldset>

      <!-- Child Information -->
      <fieldset>
        <legend>Child Information</legend>
        <label for="child-name">Name:</label>
        <input type="text" id="child-name" name="childName" required>

        <label for="child-age">Age:</label>
        <input type="number" id="child-age" name="childAge" min="0" required>

        <label for="program-select">Select Program:</label>
        <select id="program-select" name="program" required>
          <option value="">--Choose a Program--</option>
          <option value="infant-care">Infant Care</option>
          <option value="toddler-exploration">Toddler Exploration</option>
          <option value="preschool-readiness">Preschool Readiness</option>
        </select>
      </fieldset>

      <!-- Submit Button -->
      <button type="submit">Submit Enrollment</button>
    </form>
  </section>

  <!-- Footer -->
  <footer>
    <p>&copy; 2023 Happy Scholars Academy. All rights reserved.</p>
  </footer>

</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body {
  margin: 0;
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
}

/* Navbar */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #4CAF50;
  padding: 1rem;
}

.navbar .logo a {
  color: white;
  text-decoration: none;
  font-size: 1.5rem;
}

.nav-links {
  list-style: none;
  display: flex;
}

.nav-links li {
  margin: 0 1rem;
}

.nav-links a {
  color: white;
  text-decoration: none;
}

/* Hero Section */
.hero {
  text-align: center;
  background-color: #f9f9f9;
  padding: 2rem 1rem;
}

.hero h1 {
  font-size: 2.5rem;
}

.hero p {
  font-size: 1.2rem;
}

/* Program Details Section */
.program-details {
  padding: 2rem 1rem;
  background-color: #fff;
}

.program-card {
  margin-bottom: 1.5rem;
}

.program-card h3 {
  color: #4CAF50;
}

/* Testimonials Section */
.testimonials {
  background-color: #f9f9f9;
  padding: 2rem 1rem;
  text-align: center;
}

.testimonial {
  margin-bottom: 1.5rem;
}

blockquote {
  font-style: italic;
  quotes: "“" "”";
}

blockquote:before {
  content: open-quote;
}

blockquote:after {
  content: close-quote;
}

/* Enrollment Form Section */
.enrollment-form {
  background-color: #fff;
  padding: 2rem 1rem;
}

form {
  max-width: 600px;
  margin: 0 auto;
}

fieldset {
  margin-bottom: 1.5rem;
  border: 1px solid #ddd;
  padding: 1rem;
}

legend {
  font-weight: bold;
}

label {
  display: block;
  margin-bottom: 0.5rem;
}

input,
select {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

/* Footer */
footer {
  text-align: center;
  padding: 1rem;
  background-color: #4CAF50;
  color: white;
}
```
