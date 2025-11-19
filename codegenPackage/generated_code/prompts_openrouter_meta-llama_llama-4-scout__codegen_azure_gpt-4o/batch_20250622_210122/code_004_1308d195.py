"""
Generated Code Metadata:
========================
Original URL: https://claims-thentwrk.pages.dev
Prompt: Create a simple webpage using HTML, CSS, and JavaScript that allows users to claim Pudgy Penguins collectibles on NTWRK.
Generated: DETERMINISTIC_1308d195ba53ceea
Batch ID: 20250622_210122
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
  <title>Pudgy Penguins Collectibles</title>
  <!-- Link to external CSS -->
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <h1>Pudgy Penguins Collectibles</h1>
    <p>Claim your exclusive Pudgy Penguins collectibles on NTWRK!</p>
  </header>

  <main>
    <!-- Form for claiming collectibles -->
    <form id="claimForm">
      <label for="username">Enter your NTWRK username:</label>
      <input type="text" id="username" name="username" required>
      
      <label for="email">Enter your email:</label>
      <input type="email" id="email" name="email" required>
      
      <button type="submit">Claim Collectible</button>
    </form>
    
    <!-- Success message container -->
    <div id="successMessage" class="hidden">
      <p>🎉 Congratulations! Your Pudgy Penguins collectible has been claimed successfully.</p>
    </div>
  </main>

  <footer>
    <p>&copy; 2023 Pudgy Penguins | NTWRK</p>
  </footer>

  <!-- Link to external JavaScript -->
  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General reset */
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f9f9f9;
  color: #333;
}

/* Header styling */
header {
  text-align: center;
  padding: 20px;
  background-color: #4caf50;
  color: white;
}

header h1 {
  margin: 0;
  font-size: 2rem;
}

header p {
  margin: 5px 0 0;
}

/* Main content styling */
main {
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

form {
  display: flex;
  flex-direction: column;
}

form label {
  margin-bottom: 5px;
  font-weight: bold;
}

form input {
  margin-bottom: 15px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

form button {
  padding: 10px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

form button:hover {
  background-color: #45a049;
}

/* Success message styling */
.hidden {
  display: none;
}

#successMessage {
  margin-top: 20px;
  padding: 15px;
  background-color: #dff0d8;
  color: #3c763d;
  border: 1px solid #d6e9c6;
  border-radius: 4px;
  text-align: center;
}

/* Footer styling */
footer {
  text-align: center;
  padding: 10px;
  background-color: #333;
  color: white;
}
```

```javascript
// script.js

// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", () => {
  const claimForm = document.getElementById("claimForm");
  const successMessage = document.getElementById("successMessage");

  // Handle form submission
  claimForm.addEventListener("submit", (event) => {
    event.preventDefault(); // Prevent default form submission behavior

    // Get form data
    const username = document.getElementById("username").value.trim();
    const email = document.getElementById("email").value.trim();

    // Basic validation
    if (!username || !email) {
      alert("Please fill out all fields.");
      return;
    }

    // Simulate claiming process (replace with actual API call if needed)
    try {
      // Simulate success response
      setTimeout(() => {
        // Hide the form and show the success message
        claimForm.style.display = "none";
        successMessage.classList.remove("hidden");
      }, 1000); // Simulate a delay for the process
    } catch (error) {
      console.error("Error claiming collectible:", error);
      alert("An error occurred while claiming your collectible. Please try again.");
    }
  });
});
```
