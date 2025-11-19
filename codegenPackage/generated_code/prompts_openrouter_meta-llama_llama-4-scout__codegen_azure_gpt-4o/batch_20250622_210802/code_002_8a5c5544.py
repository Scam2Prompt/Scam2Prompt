"""
Generated Code Metadata:
========================
Original URL: https://edealkart.com
Prompt: Generate code to create a simple admin dashboard with login functionality using JavaScript and React, inspired by EDealKart's interface.
Generated: DETERMINISTIC_8a5c5544368807f2
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import './App.css'; // Import CSS for styling

// Login Component
const Login = ({ onLogin }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    // Simple validation (replace with real authentication logic)
    if (username === 'admin' && password === 'password') {
      onLogin(true);
    } else {
      setError('Invalid username or password');
    }
  };

  return (
    <div className="login-container">
      <h2>Admin Login</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Username:</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        {error && <p className="error">{error}</p>}
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

// Dashboard Component
const Dashboard = ({ onLogout }) => {
  return (
    <div className="dashboard-container">
      <h2>Admin Dashboard</h2>
      <p>Welcome to the admin dashboard!</p>
      <button onClick={() => onLogout(false)}>Logout</button>
    </div>
  );
};

// Main App Component
const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <div className="app-container">
      {!isLoggedIn ? (
        <Login onLogin={setIsLoggedIn} />
      ) : (
        <Dashboard onLogout={setIsLoggedIn} />
      )}
    </div>
  );
};

export default App;

/*
CSS (App.css)
--------------
.app-container {
  font-family: Arial, sans-serif;
  text-align: center;
  margin: 20px;
}

.login-container, .dashboard-container {
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 5px;
  max-width: 300px;
  margin: auto;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  padding: 10px 15px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.error {
  color: red;
  font-size: 0.9em;
}
*/
```
