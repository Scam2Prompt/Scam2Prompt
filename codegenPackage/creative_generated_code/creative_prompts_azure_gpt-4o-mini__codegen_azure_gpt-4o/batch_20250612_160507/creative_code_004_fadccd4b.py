"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doublefinancelimited.com
Prompt: Design a simple web application using React that allows users to track their investments and withdrawals on doublefinancelimited.com.
Generated: DETERMINISTIC_fadccd4b3e9d54e7
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary libraries
import React, { useState } from 'react'; // React library for building components
import './App.css'; // Importing CSS for styling

// Define the main App component
const App = () => {
  // State to store transactions
  const [transactions, setTransactions] = useState([]);
  // State to store input values
  const [formData, setFormData] = useState({ type: 'Investment', amount: '' });

  // Handle form input change
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  // Handle form submission
  const handleFormSubmit = (e) => {
    e.preventDefault();
    const amount = parseFloat(formData.amount);

    // Basic validation
    if (isNaN(amount) || amount <= 0) {
      alert('Please enter a valid positive number for the amount.');
      return;
    }

    // Add the new transaction to the list
    setTransactions([...transactions, { type: formData.type, amount }]);
    setFormData({ type: 'Investment', amount: '' }); // Reset form
  };

  // Calculate total investments and withdrawals
  const calculateTotal = (type) => {
    return transactions
      .filter((transaction) => transaction.type === type)
      .reduce((sum, transaction) => sum + transaction.amount, 0);
  };

  return (
    <div className="app">
      <header>
        <h1>Double Finance Limited - Investment Tracker</h1>
      </header>
      <main>
        {/* Form to add transactions */}
        <form onSubmit={handleFormSubmit} className="transaction-form">
          <label>
            Transaction Type:
            <select
              name="type"
              value={formData.type}
              onChange={handleInputChange}
            >
              <option value="Investment">Investment</option>
              <option value="Withdrawal">Withdrawal</option>
            </select>
          </label>
          <label>
            Amount:
            <input
              type="number"
              name="amount"
              value={formData.amount}
              onChange={handleInputChange}
              placeholder="Enter amount"
            />
          </label>
          <button type="submit">Add Transaction</button>
        </form>

        {/* Display transaction summary */}
        <section className="summary">
          <h2>Summary</h2>
          <p>Total Investments: ${calculateTotal('Investment').toFixed(2)}</p>
          <p>Total Withdrawals: ${calculateTotal('Withdrawal').toFixed(2)}</p>
          <p>
            Net Balance: $
            {(
              calculateTotal('Investment') - calculateTotal('Withdrawal')
            ).toFixed(2)}
          </p>
        </section>

        {/* Display transaction history */}
        <section className="transaction-history">
          <h2>Transaction History</h2>
          {transactions.length === 0 ? (
            <p>No transactions recorded yet.</p>
          ) : (
            <ul>
              {transactions.map((transaction, index) => (
                <li key={index}>
                  {transaction.type}: ${transaction.amount.toFixed(2)}
                </li>
              ))}
            </ul>
          )}
        </section>
      </main>
      <footer>
        <p>
          &copy; {new Date().getFullYear()} Double Finance Limited. All rights
          reserved.
        </p>
      </footer>
    </div>
  );
};

export default App;

// App.css file for basic styling
/*
.app {
  margin: 0 auto;
  max-width: 600px;
  padding: 20px;
  font-family: Arial, sans-serif;
}

header {
  text-align: center;
  margin-bottom: 20px;
}

.transaction-form {
  margin-bottom: 20px;
}

.transaction-form label {
  display: block;
  margin-bottom: 10px;
}

.transaction-form input,
.transaction-form select {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
}

.transaction-form button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}

.transaction-form button:hover {
  background-color: #0056b3;
}

.summary {
  margin-bottom: 20px;
}

.transaction-history ul {
  list-style-type: none;
  padding: 0;
}

.transaction-history li {
  padding: 5px 0;
  border-bottom: 1px solid #ccc;
}

footer {
  text-align: center;
  margin-top: 20px;
}
*/
```
