"""
Generated Code Metadata:
========================
Original URL: https://plf3108.com
Prompt: Generate a JavaScript code example to create a user-friendly interface for an online betting platform, like 868, with easy navigation, accessible on both desktop and mobile devices.
Generated: DETERMINISTIC_fda8f845368b36c6
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import './styles.css';

// Define a functional component for the betting platform
function BettingPlatform() {
  // State to store the current page (desktop or mobile)
  const [currentPage, setCurrentPage] = useState('home');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [balance, setBalance] = useState(0.0);
  const [betAmount, setBetAmount] = useState(0.0);
  const [betType, setBetType] = useState('');
  const [odds, setOdds] = useState(0.0);

  // Function to handle navigation between pages
  const navigateToPage = (page) => {
    setCurrentPage(page);
  };

  // Function to handle user login
  const handleLogin = () => {
    // Simulate a login API call
    if (username === 'admin' && password === 'password') {
      setBalance(100.0);
      navigateToPage('dashboard');
    } else {
      alert('Invalid username or password');
    }
  };

  // Function to handle placing a bet
  const handlePlaceBet = () => {
    // Simulate a bet placement API call
    if (betAmount > 0 && betType !== '') {
      const winnings = betAmount * odds;
      setBalance(balance + winnings);
      alert(`Bet placed successfully! Your new balance is ${balance + winnings}`);
    } else {
      alert('Please enter a valid bet amount and type');
    }
  };

  // Render the current page
  switch (currentPage) {
    case 'home':
      return (
        <div className="container">
          <h1>Welcome to Like868</h1>
          <form>
            <label>Username:</label>
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
            <br />
            <label>Password:</label>
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
            <br />
            <button type="button" onClick={handleLogin}>
              Login
            </button>
          </form>
        </div>
      );
    case 'dashboard':
      return (
        <div className="container">
          <h1>Dashboard</h1>
          <p>Balance: ${balance}</p>
          <form>
            <label>Bet Amount:</label>
            <input type="number" value={betAmount} onChange={(e) => setBetAmount(parseFloat(e.target.value))} />
            <br />
            <label>Bet Type:</label>
            <select value={betType} onChange={(e) => setBetType(e.target.value)}>
              <option value="">Select a bet type</option>
              <option value="sports">Sports</option>
              <option value="casino">Casino</option>
            </select>
            <br />
            <label>Odds:</label>
            <input type="number" value={odds} onChange={(e) => setOdds(parseFloat(e.target.value))} />
            <br />
            <button type="button" onClick={handlePlaceBet}>
              Place Bet
            </button>
          </form>
          <button type="button" onClick={() => navigateToPage('home')}>
            Logout
          </button>
        </div>
      );
    default:
      return <div>Page not found</div>;
  }
}

// Render the betting platform component
ReactDOM.render(
  <React.StrictMode>
    <BettingPlatform />
  </React.StrictMode>,
  document.getElementById('root')
);
```

```css
/* styles.css */
body {
  font-family: Arial, sans-serif;
}

.container {
  max-width: 800px;
  margin: 40px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
  display: block;
  margin-bottom: 10px;
}

input[type="text"],
input[type="password"],
input[type="number"],
select {
  width: 100%;
  height: 40px;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ccc;
}

button[type="button"] {
  width: 100%;
  height: 40px;
  background-color: #4CAF50;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button[type="button"]:hover {
  background-color: #3e8e41;
}

@media only screen and (max-width: 768px) {
  .container {
    margin: 20px auto;
    padding: 10px;
  }
}
```
