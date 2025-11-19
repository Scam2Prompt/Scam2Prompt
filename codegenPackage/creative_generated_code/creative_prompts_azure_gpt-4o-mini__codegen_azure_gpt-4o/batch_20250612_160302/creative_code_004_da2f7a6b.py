"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://viysrbyrrsvrirsinylfyudluyxkyrzxyrgvulyhgxryskftdryk.pages.dev
Prompt: Develop a simple web application that allows users to track their betting history and earnings on BetFury using JavaScript and the platform's API.
Generated: DETERMINISTIC_da2f7a6ba31fd842
Batch ID: 20250612_160302
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.betfury.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Betting Tracker Web Application for BetFury
// This script uses JavaScript and connects to the BetFury API
// Please ensure you have proper API credentials to use this application

// Check if the window is loaded
document.addEventListener('DOMContentLoaded', () => {
  // DOM elements
  const form = document.querySelector('#betForm');
  const bettingHistoryContainer = document.querySelector('#bettingHistory');
  const errorContainer = document.querySelector('#errorContainer');

  // Mock API base URL (replace with the actual BetFury API URL)
  const API_BASE_URL = 'https://api.betfury.io';

  // Function to handle errors
  const handleError = (error) => {
    console.error(error);
    errorContainer.innerHTML = `<p>An error occurred: ${error.message}</p>`;
  };

  // Function to fetch betting history
  const fetchBettingHistory = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/bet-history`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('token')}`, // JWT token for authentication
        },
      });

      // Handle HTTP errors
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      updateBettingHistoryUI(data.bets);
    } catch (error) {
      handleError(error);
    }
  };

  // Function to update the UI with betting history
  const updateBettingHistoryUI = (bets) => {
    bettingHistoryContainer.innerHTML = ''; // Clear previous content

    if (bets.length === 0) {
      bettingHistoryContainer.innerHTML = '<p>No betting history found.</p>';
      return;
    }

    const table = document.createElement('table');
    table.innerHTML = `
      <thead>
        <tr>
          <th>Date</th>
          <th>Amount</th>
          <th>Result</th>
          <th>Earnings</th>
        </tr>
      </thead>
    `;
    const tbody = document.createElement('tbody');

    bets.forEach((bet) => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${new Date(bet.date).toLocaleString()}</td>
        <td>${bet.amount}</td>
        <td>${bet.result}</td>
        <td>${bet.earnings}</td>
      `;
      tbody.appendChild(row);
    });

    table.appendChild(tbody);
    bettingHistoryContainer.appendChild(table);
  };

  // Function to submit a new bet
  const submitBet = async (betData) => {
    try {
      const response = await fetch(`${API_BASE_URL}/place-bet`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('token')}`, // JWT token for authentication
        },
        body: JSON.stringify(betData),
      });

      // Handle HTTP errors
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      alert(`Bet placed successfully! Bet ID: ${data.betId}`);
      fetchBettingHistory(); // Refresh betting history
    } catch (error) {
      handleError(error);
    }
  };

  // Event listener for bet submission form
  form.addEventListener('submit', (event) => {
    event.preventDefault();

    const betAmount = parseFloat(event.target.elements.amount.value);
    if (isNaN(betAmount) || betAmount <= 0) {
      alert('Please enter a valid betting amount.');
      return;
    }

    const betData = {
      amount: betAmount,
      userId: localStorage.getItem('userId'), // Assuming userId is stored in localStorage
    };

    submitBet(betData);
  });

  // Initial fetch of betting history
  fetchBettingHistory();
});
```

Here is the accompanying HTML for the above JavaScript code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BetFury Betting Tracker</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
    }
    th, td {
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }
    th {
      background-color: #f4f4f4;
    }
  </style>
</head>
<body>
  <h1>BetFury Betting Tracker</h1>

  <form id="betForm">
    <label for="amount">Bet Amount:</label>
    <input type="number" id="amount" name="amount" required>
    <button type="submit">Place Bet</button>
  </form>

  <div id="errorContainer" style="color: red; margin-top: 20px;"></div>

  <div id="bettingHistory">
    <h2>Betting History</h2>
  </div>

  <script src="betTracker.js"></script>
</body>
</html>
```
