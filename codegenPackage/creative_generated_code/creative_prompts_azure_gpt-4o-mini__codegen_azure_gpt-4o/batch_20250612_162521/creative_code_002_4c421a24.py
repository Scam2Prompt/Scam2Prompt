"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pif-presale-staging.vercel.app
Prompt: Generate a code snippet for a user interface that allows users to join a presale, referencing the layout seen on Fwen.io.
Generated: DETERMINISTIC_4c421a24081095cf
Batch ID: 20250612_162521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- Presale Join Interface - HTML -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Presale Join Interface</title>
  <link rel="stylesheet" href="styles.css"> <!-- External stylesheet -->
  <script src="script.js" defer></script> <!-- External JavaScript -->
</head>
<body>
  <header class="header">
    <h1>Join the Presale</h1>
  </header>

  <main class="main-content">
    <section class="presale-form">
      <h2>Secure Your Spot</h2>
      <form id="presaleForm">
        <!-- Email Input -->
        <div class="form-group">
          <label for="email">Email Address:</label>
          <input 
            type="email" 
            id="email" 
            name="email" 
            placeholder="Enter your email" 
            required
          />
        </div>

        <!-- Quantity Input -->
        <div class="form-group">
          <label for="quantity">Quantity:</label>
          <input 
            type="number" 
            id="quantity" 
            name="quantity" 
            placeholder="Enter quantity" 
            min="1" 
            max="10" 
            required
          />
        </div>

        <!-- Submit Button -->
        <button type="submit" class="btn-submit">Join Presale</button>

        <!-- Error Message -->
        <p id="errorMessage" class="error-message hidden">
          Please fill out both fields correctly.
        </p>

        <!-- Confirmation Message -->
        <p id="confirmationMessage" class="confirmation-message hidden">
          Thank you for joining the presale!
        </p>
      </form>
    </section>
  </main>

  <footer class="footer">
    <p>&copy; 2023 Example Company. All rights reserved.</p>
  </footer>
</body>
</html>
```

```css
/* styles.css - Presale UI styling */

/* General reset */
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f7f7f7;
  color: #333;
}

/* Header styles */
.header {
  text-align: center;
  background-color: #4CAF50;
  color: white;
  padding: 1rem 0;
}

/* Main content styles */
.main-content {
  max-width: 500px;
  margin: 2rem auto 0;
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
}

/* Form styles */
.presale-form h2 {
  text-align: center;
  margin-bottom: 1rem;
}

.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
}

input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.btn-submit {
  display: block;
  width: 100%;
  padding: 0.75rem;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-submit:hover {
  background-color: #45a049;
}

/* Error and confirmation messages */
.error-message,
.confirmation-message {
  text-align: center;
  margin-top: 1rem;
}

.hidden {
  display: none;
}

.error-message {
  color: red;
}

.confirmation-message {
  color: green;
}

/* Footer styles */
.footer {
  text-align: center;
  margin: 2rem 0;
  color: #666;
}
```

```javascript
// script.js - Presale Join Logic

// Wait for DOM to load
document.addEventListener("DOMContentLoaded", () => {
  // Get form elements
  const presaleForm = document.getElementById("presaleForm");
  const errorMessage = document.getElementById("errorMessage");
  const confirmationMessage = document.getElementById("confirmationMessage");

  // Form submission event listener
  presaleForm.addEventListener("submit", (event) => {
    event.preventDefault(); // Prevent default form submission

    // Get input values
    const email = document.getElementById("email").value.trim();
    const quantity = parseInt(document.getElementById("quantity").value, 10);

    // Basic validation
    if (!email || isNaN(quantity) || quantity < 1 || quantity > 10) {
      errorMessage.classList.remove("hidden");
      confirmationMessage.classList.add("hidden");
      return;
    }

    // Simulate successful form submission
    errorMessage.classList.add("hidden");
    confirmationMessage.classList.remove("hidden");

    // Clear form fields
    presaleForm.reset();
  });
});
```
