"""
Generated Code Metadata:
========================
Original URL: https://smartconnect.ng
Prompt: Create a simple webpage that allows users to sign up and buy data plans at reasonable prices as offered by SmartConnect.ng, focusing on user interface and user experience.
Generated: DETERMINISTIC_758fd8367f213812
Batch ID: 20250622_212836
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
  <title>SmartConnect.ng - Sign Up & Buy Data Plans</title>
  <link rel="stylesheet" href="styles.css">
  <script src="script.js" defer></script>
</head>
<body>
  <!-- Header Section -->
  <header>
    <div class="container">
      <h1>SmartConnect.ng</h1>
      <p>Your gateway to affordable data plans</p>
    </div>
  </header>

  <!-- Main Content -->
  <main>
    <div class="container">
      <!-- Sign-Up Form -->
      <section id="signup">
        <h2>Sign Up</h2>
        <form id="signupForm">
          <label for="name">Full Name:</label>
          <input type="text" id="name" name="name" required>
          
          <label for="email">Email Address:</label>
          <input type="email" id="email" name="email" required>
          
          <label for="password">Password:</label>
          <input type="password" id="password" name="password" required>
          
          <button type="submit">Sign Up</button>
        </form>
      </section>

      <!-- Data Plans Section -->
      <section id="dataPlans">
        <h2>Available Data Plans</h2>
        <div class="plans">
          <div class="plan">
            <h3>1GB Plan</h3>
            <p>Price: ₦500</p>
            <button class="buyButton" data-plan="1GB" data-price="500">Buy Now</button>
          </div>
          <div class="plan">
            <h3>5GB Plan</h3>
            <p>Price: ₦2000</p>
            <button class="buyButton" data-plan="5GB" data-price="2000">Buy Now</button>
          </div>
          <div class="plan">
            <h3>10GB Plan</h3>
            <p>Price: ₦3500</p>
            <button class="buyButton" data-plan="10GB" data-price="3500">Buy Now</button>
          </div>
        </div>
      </section>
    </div>
  </main>

  <!-- Footer Section -->
  <footer>
    <div class="container">
      <p>&copy; 2023 SmartConnect.ng. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p, form, input, button {
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
}

/* Container */
.container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
}

/* Header */
header {
  background: #007bff;
  color: #fff;
  padding: 20px 0;
  text-align: center;
}

/* Main Content */
main {
  padding: 20px 0;
}

/* Sign-Up Form */
#signup {
  margin-bottom: 40px;
}

form {
  background: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

form label {
  display: block;
  margin-bottom: 5px;
}

form input {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

form button {
  background: #007bff;
  color: #fff;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
}

form button:hover {
  background: #0056b3;
}

/* Data Plans */
.plans {
  display: flex;
  gap: 20px;
}

.plan {
  background: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  text-align: center;
  flex: 1;
}

.plan h3 {
  margin-bottom: 10px;
}

.plan p {
  margin-bottom: 15px;
}

.plan button {
  background: #28a745;
  color: #fff;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
}

.plan button:hover {
  background: #218838;
}

/* Footer */
footer {
  background: #333;
  color: #fff;
  text-align: center;
  padding: 10px 0;
}
```

```javascript
// script.js

// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', () => {
  // Handle Sign-Up Form Submission
  const signupForm = document.getElementById('signupForm');
  signupForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent form from refreshing the page

    // Collect form data
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();

    // Basic validation
    if (!name || !email || !password) {
      alert('Please fill out all fields.');
      return;
    }

    // Simulate form submission (replace with actual API call in production)
    alert(`Thank you for signing up, ${name}!`);
    signupForm.reset(); // Clear the form
  });

  // Handle Buy Button Clicks
  const buyButtons = document.querySelectorAll('.buyButton');
  buyButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const plan = button.getAttribute('data-plan');
      const price = button.getAttribute('data-price');

      // Simulate purchase (replace with actual API call in production)
      alert(`You have successfully purchased the ${plan} plan for ₦${price}.`);
    });
  });
});
```
