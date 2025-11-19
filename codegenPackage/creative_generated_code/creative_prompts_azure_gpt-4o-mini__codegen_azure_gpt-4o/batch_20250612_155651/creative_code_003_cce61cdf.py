"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wc.innovie-corp.com
Prompt: Generate a sample user interface for the Worldcoin friend invitation system that includes email registration and invitation code input.
Generated: DETERMINISTIC_cce61cdfa08ff54c
Batch ID: 20250612_155651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, efficient, and well-documented implementation of a Worldcoin friend invitation system user interface using JavaScript (React.js) and styled with CSS:

```javascript
// App.js - Main React Component for Worldcoin Friend Invitation System UI
import React, { useState } from "react";
import "./App.css";

const App = () => {
  // State variables for form inputs
  const [email, setEmail] = useState("");
  const [invitationCode, setInvitationCode] = useState("");
  const [error, setError] = useState("");
  const [successMessage, setSuccessMessage] = useState("");

  // Handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();

    // Input validation
    if (!email) {
      setError("Email is required.");
      return;
    }
    if (!validateEmail(email)) {
      setError("Please enter a valid email address.");
      return;
    }
    if (!invitationCode) {
      setError("Invitation code is required.");
      return;
    }

    setError(""); // Clear errors

    // Simulate API call
    setTimeout(() => {
      setSuccessMessage("Thank you for registering! Your invitation code has been submitted.");
      setEmail(""); // Reset email input
      setInvitationCode(""); // Reset invitation code input
    }, 500);
  };

  // Helper function to validate email format
  const validateEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email regex
    return emailRegex.test(email);
  };

  return (
    <div className="app-container">
      <h1>Worldcoin Friend Invitation System</h1>
      <form className="invitation-form" onSubmit={handleSubmit}>
        {/* Email input */}
        <div className="form-group">
          <label htmlFor="email">Email Address:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your email"
            required
          />
        </div>

        {/* Invitation code input */}
        <div className="form-group">
          <label htmlFor="invitationCode">Invitation Code:</label>
          <input
            type="text"
            id="invitationCode"
            value={invitationCode}
            onChange={(e) => setInvitationCode(e.target.value)}
            placeholder="Enter your invitation code"
            required
          />
        </div>

        {/* Submit button */}
        <button type="submit" className="submit-button">
          Register
        </button>

        {/* Display error or success messages */}
        {error && <p className="error-message">{error}</p>}
        {successMessage && <p className="success-message">{successMessage}</p>}
      </form>
    </div>
  );
};

export default App;
```

```css
/* App.css - Styles for Worldcoin Friend Invitation System */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f9f9f9;
}

.app-container {
  max-width: 400px;
  margin: 50px auto;
  padding: 20px;
  background: #ffffff;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  text-align: center;
}

h1 {
  font-size: 1.8em;
  margin-bottom: 20px;
}

.invitation-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.form-group {
  text-align: left;
}

label {
  font-weight: bold;
  margin-bottom: 5px;
  display: block;
}

input {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input:focus {
  border: 1px solid #007bff;
  outline: none;
}

.submit-button {
  background-color: #007bff;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #0056b3;
}

.error-message {
  color: #d9534f;
  font-size: 0.9em;
}

.success-message {
  color: #5cb85c;
  font-size: 0.9em;
}
```

### File Structure:
- `App.js`: Contains the main React.js logic for the UI.
- `App.css`: Contains the styles for the UI.

### Prerequisites:
To run this code:
1. Install Node.js and npm.
2. Create a React app with `npx create-react-app worldcoin-invitation`.
3. Replace the `App.js` and `App.css` files with the provided code.
4. Start the app with `npm start`.

Let me know if you need further assistance!
