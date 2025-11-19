"""
Generated Code Metadata:
========================
Original URL: https://haseebbaig.me
Prompt: Develop a web application using HTML/CSS, JavaScript, and PHP, with a focus on user experience and responsive design.
Generated: DETERMINISTIC_b440f89acfb410e3
Batch ID: 20250622_210718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### HTML (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Responsive Web Application</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header>
    <nav>
      <ul class="nav-links">
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  </header>

  <!-- Main Content Section -->
  <main>
    <section id="home">
      <h1>Welcome to Our Web Application</h1>
      <p>Experience a responsive and user-friendly design.</p>
    </section>

    <section id="about">
      <h2>About Us</h2>
      <p>We are dedicated to providing the best user experience.</p>
    </section>

    <section id="contact">
      <h2>Contact Us</h2>
      <form id="contactForm">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
        
        <button type="submit">Submit</button>
      </form>
      <p id="formResponse"></p>
    </section>
  </main>

  <!-- Footer Section -->
  <footer>
    <p>&copy; 2023 Responsive Web Application</p>
  </footer>

  <script src="script.js"></script>
</body>
</html>
```

### CSS (styles.css)
```css
/* General Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body Styling */
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f4f4f4;
}

/* Header Styling */
header {
  background: #333;
  color: #fff;
  padding: 1rem 0;
}

header nav ul {
  list-style: none;
  display: flex;
  justify-content: center;
}

header nav ul li {
  margin: 0 1rem;
}

header nav ul li a {
  color: #fff;
  text-decoration: none;
}

/* Main Content Styling */
main {
  padding: 2rem;
}

section {
  margin-bottom: 2rem;
}

h1, h2 {
  color: #333;
}

/* Form Styling */
form {
  max-width: 600px;
  margin: 0 auto;
  background: #fff;
  padding: 1rem;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

form label {
  display: block;
  margin-bottom: 0.5rem;
}

form input, form textarea, form button {
  width: 100%;
  margin-bottom: 1rem;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

form button {
  background: #333;
  color: #fff;
  border: none;
  cursor: pointer;
}

form button:hover {
  background: #555;
}

/* Footer Styling */
footer {
  text-align: center;
  padding: 1rem;
  background: #333;
  color: #fff;
}

/* Responsive Design */
@media (max-width: 768px) {
  header nav ul {
    flex-direction: column;
  }

  form {
    width: 90%;
  }
}
```

### JavaScript (script.js)
```javascript
// Handle form submission
document.getElementById('contactForm').addEventListener('submit', async function (event) {
  event.preventDefault(); // Prevent default form submission

  // Collect form data
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const message = document.getElementById('message').value;

  try {
    // Send data to the server using Fetch API
    const response = await fetch('submit.php', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name, email, message }),
    });

    // Parse server response
    const result = await response.json();

    // Display response message
    document.getElementById('formResponse').textContent = result.message;
  } catch (error) {
    // Handle errors
    document.getElementById('formResponse').textContent = 'An error occurred. Please try again.';
    console.error('Error:', error);
  }
});
```

### PHP (submit.php)
```php
<?php
// Enable error reporting for debugging (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Set response headers
header('Content-Type: application/json');

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Get the raw POST data
    $data = file_get_contents('php://input');
    $decodedData = json_decode($data, true);

    // Validate input data
    if (isset($decodedData['name'], $decodedData['email'], $decodedData['message'])) {
        $name = htmlspecialchars($decodedData['name']);
        $email = htmlspecialchars($decodedData['email']);
        $message = htmlspecialchars($decodedData['message']);

        // Simulate saving data (e.g., to a database)
        // In production, replace this with actual database logic
        $success = true; // Simulate success

        if ($success) {
            echo json_encode(['message' => 'Thank you for your message, ' . $name . '!']);
        } else {
            echo json_encode(['message' => 'Failed to save your message. Please try again.']);
        }
    } else {
        echo json_encode(['message' => 'Invalid input. Please fill out all fields.']);
    }
} else {
    echo json_encode(['message' => 'Invalid request method.']);
}
?>
```
