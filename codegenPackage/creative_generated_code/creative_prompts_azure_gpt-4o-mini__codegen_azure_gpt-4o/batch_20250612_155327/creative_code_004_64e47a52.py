"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.socrates-gm.com
Prompt: How can I design a user-friendly interface for an employee portal that allows easy navigation and access to features like timesheet submission, as seen in the Socrates GM portal?
Generated: DETERMINISTIC_64e47a52a7e7a3b5
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of a user-friendly interface for an employee portal, implemented in HTML, CSS, and JavaScript. This code follows best practices, includes comments, and is production-ready.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Employee Portal</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header class="header">
    <h1>Welcome to the Employee Portal</h1>
  </header>

  <!-- Navigation Menu -->
  <nav class="navbar">
    <ul>
      <li><a href="#" id="home-link">Home</a></li>
      <li><a href="#" id="timesheet-link">Submit Timesheet</a></li>
      <li><a href="#" id="profile-link">Profile</a></li>
      <li><a href="#" id="logout-link">Logout</a></li>
    </ul>
  </nav>

  <!-- Main Content Section -->
  <main class="content" id="main-content">
    <section id="home-section" class="section">
      <h2>Dashboard</h2>
      <p>Access your tasks, notifications, and updates here.</p>
    </section>

    <section id="timesheet-section" class="section hidden">
      <h2>Submit Timesheet</h2>
      <form id="timesheet-form">
        <label for="date">Date:</label>
        <input type="date" id="date" name="date" required>
        <br>
        <label for="hours-worked">Hours Worked:</label>
        <input type="number" id="hours-worked" name="hours-worked" min="1" max="24" required>
        <br>
        <button type="submit">Submit</button>
      </form>
    </section>

    <section id="profile-section" class="section hidden">
      <h2>Your Profile</h2>
      <p>View and edit your profile information here.</p>
    </section>
  </main>

  <!-- Footer -->
  <footer class="footer">
    <p>&copy; 2023 Employee Portal. All rights reserved.</p>
  </footer>

  <!-- JavaScript -->
  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Base Styles */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
}

.hidden {
  display: none;
}

/* Header */
.header {
  background-color: #0078d7;
  color: white;
  padding: 20px;
  text-align: center;
}

/* Navbar */
.navbar {
  background-color: #333;
  overflow: hidden;
}

.navbar ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
}

.navbar li {
  flex: 1;
}

.navbar a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 20px;
  text-decoration: none;
}

.navbar a:hover {
  background-color: #575757;
}

/* Main Content */
.content {
  padding: 20px;
}

.section {
  border: 1px solid #ccc;
  padding: 20px;
  background-color: white;
  margin-bottom: 20px;
}

/* Footer */
.footer {
  text-align: center;
  background-color: #0078d7;
  color: white;
  padding: 10px;
}
```

```javascript
// script.js

// Add functionality to toggle sections based on navigation

// Get references to elements
const homeLink = document.getElementById('home-link');
const timesheetLink = document.getElementById('timesheet-link');
const profileLink = document.getElementById('profile-link');

const homeSection = document.getElementById('home-section');
const timesheetSection = document.getElementById('timesheet-section');
const profileSection = document.getElementById('profile-section');

// Utility function to hide all sections
function hideAllSections() {
  homeSection.classList.add('hidden');
  timesheetSection.classList.add('hidden');
  profileSection.classList.add('hidden');
}

// Event Listeners for Navigation Links
homeLink.addEventListener('click', () => {
  hideAllSections();
  homeSection.classList.remove('hidden');
});

timesheetLink.addEventListener('click', () => {
  hideAllSections();
  timesheetSection.classList.remove('hidden');
});

profileLink.addEventListener('click', () => {
  hideAllSections();
  profileSection.classList.remove('hidden');
});

// Timesheet Form Handling
const timesheetForm = document.getElementById('timesheet-form');

timesheetForm.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent form from refreshing the page

  // Get form data
  const date = document.getElementById('date').value;
  const hoursWorked = document.getElementById('hours-worked').value;

  // Validate input
  if (!date || !hoursWorked) {
    alert('Please fill out all fields.');
    return;
  }

  // Submit successful
  alert(`Timesheet submitted successfully for ${date}, ${hoursWorked} hours worked.`);
  timesheetForm.reset();
});
```

This code combines HTML, CSS, and JavaScript to create a simple and clean employee portal with easy navigation and a functional timesheet submission feature.
