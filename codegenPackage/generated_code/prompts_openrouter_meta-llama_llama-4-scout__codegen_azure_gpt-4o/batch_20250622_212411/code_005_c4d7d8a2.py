"""
Generated Code Metadata:
========================
Original URL: https://usual-app.vercel.app
Prompt: "Design a basic UI for an alternative DeFi platform inspired by Usual's galaxy theme."
Generated: DETERMINISTIC_c4d7d8a2dfc9a87c
Batch ID: 20250622_212411
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
  <title>Galaxy DeFi Platform</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header class="header">
    <div class="logo">
      <img src="logo.png" alt="Galaxy DeFi Logo">
      <h1>Galaxy DeFi</h1>
    </div>
    <nav class="nav">
      <ul>
        <li><a href="#dashboard">Dashboard</a></li>
        <li><a href="#swap">Swap</a></li>
        <li><a href="#stake">Stake</a></li>
        <li><a href="#about">About</a></li>
      </ul>
    </nav>
  </header>

  <!-- Main Content -->
  <main>
    <!-- Dashboard Section -->
    <section id="dashboard" class="section">
      <h2>Dashboard</h2>
      <p>Track your assets and portfolio performance in the galaxy.</p>
      <div class="dashboard-grid">
        <div class="card">
          <h3>Total Balance</h3>
          <p>$0.00</p>
        </div>
        <div class="card">
          <h3>Staked Assets</h3>
          <p>$0.00</p>
        </div>
        <div class="card">
          <h3>Rewards</h3>
          <p>$0.00</p>
        </div>
      </div>
    </section>

    <!-- Swap Section -->
    <section id="swap" class="section">
      <h2>Swap</h2>
      <p>Exchange tokens seamlessly across the galaxy.</p>
      <form class="swap-form">
        <label for="from-token">From:</label>
        <select id="from-token" name="from-token">
          <option value="eth">ETH</option>
          <option value="btc">BTC</option>
          <option value="usdt">USDT</option>
        </select>
        <input type="number" id="from-amount" name="from-amount" placeholder="Amount">
        
        <label for="to-token">To:</label>
        <select id="to-token" name="to-token">
          <option value="eth">ETH</option>
          <option value="btc">BTC</option>
          <option value="usdt">USDT</option>
        </select>
        <input type="number" id="to-amount" name="to-amount" placeholder="Amount" disabled>
        
        <button type="submit">Swap</button>
      </form>
    </section>

    <!-- Stake Section -->
    <section id="stake" class="section">
      <h2>Stake</h2>
      <p>Earn rewards by staking your assets in the galaxy.</p>
      <form class="stake-form">
        <label for="stake-token">Token:</label>
        <select id="stake-token" name="stake-token">
          <option value="eth">ETH</option>
          <option value="btc">BTC</option>
          <option value="usdt">USDT</option>
        </select>
        <input type="number" id="stake-amount" name="stake-amount" placeholder="Amount">
        <button type="submit">Stake</button>
      </form>
    </section>

    <!-- About Section -->
    <section id="about" class="section">
      <h2>About</h2>
      <p>Galaxy DeFi is a decentralized finance platform inspired by the vastness of the universe.</p>
    </section>
  </main>

  <!-- Footer Section -->
  <footer class="footer">
    <p>&copy; 2023 Galaxy DeFi. All rights reserved.</p>
  </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p, ul, li, a, input, button {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body Styling */
body {
  font-family: Arial, sans-serif;
  background: linear-gradient(to bottom, #0b0c1d, #1a1b3c);
  color: #ffffff;
  line-height: 1.6;
}

/* Header Styling */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: #1a1b3c;
}

.logo img {
  height: 40px;
  margin-right: 10px;
}

.nav ul {
  list-style: none;
  display: flex;
}

.nav ul li {
  margin: 0 10px;
}

.nav ul li a {
  text-decoration: none;
  color: #ffffff;
  font-weight: bold;
}

.nav ul li a:hover {
  color: #00bcd4;
}

/* Section Styling */
.section {
  padding: 2rem;
  margin: 2rem auto;
  max-width: 800px;
  background-color: #1a1b3c;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.section h2 {
  margin-bottom: 1rem;
  color: #00bcd4;
}

/* Dashboard Grid */
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.card {
  background-color: #0b0c1d;
  padding: 1rem;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* Forms */
form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

form label {
  font-weight: bold;
}

form input, form select, form button {
  padding: 0.5rem;
  border: none;
  border-radius: 5px;
}

form button {
  background-color: #00bcd4;
  color: #ffffff;
  font-weight: bold;
  cursor: pointer;
}

form button:hover {
  background-color: #008ba3;
}

/* Footer Styling */
.footer {
  text-align: center;
  padding: 1rem;
  background-color: #1a1b3c;
}
```
