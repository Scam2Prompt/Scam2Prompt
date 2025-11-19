"""
Generated Code Metadata:
========================
Original URL: https://morpho-frontend.pages.dev
Prompt: How can I create a user interface that mimics the design of the Morpho app using JavaScript?
Generated: DETERMINISTIC_7f85cd9064a45148
Batch ID: 20250612_155436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import './styles.css';

// Define a functional component for the Morpho app UI
function MorphoApp() {
  // State to store the current theme (light or dark)
  const [theme, setTheme] = useState('light');

  // Function to toggle the theme
  const toggleTheme = () => {
    setTheme(theme === 'light' ? 'dark' : 'light');
  };

  // Class name based on the current theme
  const className = `morpho-app ${theme}`;

  // Render the Morpho app UI
  return (
    <div className={className}>
      <header className="header">
        <nav className="nav">
          <ul>
            <li>
              <button className="nav-button" onClick={toggleTheme}>
                Toggle Theme
              </button>
            </li>
          </ul>
        </nav>
      </header>
      <main className="main">
        <section className="balance">
          <h2>Balance</h2>
          <p className="balance-value">$0.00</p>
        </section>
        <section className="transactions">
          <h2>Transactions</h2>
          <ul>
            <li>
              <span className="transaction-date">2022-01-01</span>
              <span className="transaction-amount">$100.00</span>
            </li>
            <li>
              <span className="transaction-date">2022-01-02</span>
              <span className="transaction-amount">$200.00</span>
            </li>
          </ul>
        </section>
      </main>
      <footer className="footer">
        <p>&copy; 2024 Morpho App</p>
      </footer>
    </div>
  );
}

// Render the Morpho app UI to the DOM
ReactDOM.render(
  <React.StrictMode>
    <MorphoApp />
  </React.StrictMode>,
  document.getElementById('root')
);
```

```css
/* styles.css */

/* Global styles */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f9f9f9;
}

.morpho-app {
  max-width: 800px;
  margin: 40px auto;
  padding: 20px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.morpho-app.dark {
  background-color: #333;
  color: #fff;
}

.header {
  background-color: #333;
  color: #fff;
  padding: 10px;
  border-bottom: 1px solid #555;
}

.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav li {
  display: inline-block;
  margin-right: 20px;
}

.nav-button {
  background-color: #555;
  color: #fff;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

.nav-button:hover {
  background-color: #777;
}

.main {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

.balance {
  background-color: #f7f7f7;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 10px;
  margin-bottom: 20px;
}

.balance-value {
  font-size: 24px;
  font-weight: bold;
}

.transactions {
  background-color: #f7f7f7;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 10px;
}

.transactions ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.transactions li {
  padding: 10px;
  border-bottom: 1px solid #ddd;
}

.transactions li:last-child {
  border-bottom: none;
}

.transaction-date {
  font-size: 16px;
  color: #666;
}

.transaction-amount {
  font-size: 16px;
  font-weight: bold;
}

.footer {
  background-color: #333;
  color: #fff;
  padding: 10px;
  text-align: center;
  clear: both;
}

.morpho-app.dark .header {
  background-color: #555;
}

.morpho-app.dark .nav-button {
  background-color: #777;
}

.morpho-app.dark .nav-button:hover {
  background-color: #999;
}

.morpho-app.dark .balance {
  background-color: #555;
  color: #fff;
}

.morpho-app.dark .transactions {
  background-color: #555;
  color: #fff;
}

.morpho-app.dark .transaction-date {
  color: #ccc;
}

.morpho-app.dark .transaction-amount {
  color: #fff;
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Morpho App</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="root"></div>
  <script src="index.js"></script>
</body>
</html>
```
