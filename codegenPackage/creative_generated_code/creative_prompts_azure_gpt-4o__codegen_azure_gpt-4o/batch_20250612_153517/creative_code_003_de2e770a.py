"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staking-paalai.pages.dev
Prompt: Develop a frontend interface using React that displays staking configurations (e.g., 35% APY for 14 days, 80% APY for 28 days, 105% APY for 56 days) and allows users to select and stake $PAAL tokens.
Generated: DETERMINISTIC_de2e770a23abc01c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// src/App.js
import React, { useState } from "react";
import "./App.css"; // Importing styles

// Staking configurations
const stakingOptions = [
  { id: 1, apy: "35%", duration: "14 days" },
  { id: 2, apy: "80%", duration: "28 days" },
  { id: 3, apy: "105%", duration: "56 days" },
];

function App() {
  // States for selected option and amount of $PAAL tokens
  const [selectedOption, setSelectedOption] = useState(null);
  const [stakeAmount, setStakeAmount] = useState("");
  const [message, setMessage] = useState("");

  // Handle staking form submission
  const handleStake = (event) => {
    event.preventDefault();
    
    // Simple input validation
    if (!selectedOption) {
      setMessage("Please select a staking option.");
      return;
    }

    if (!stakeAmount || isNaN(stakeAmount) || Number(stakeAmount) <= 0) {
      setMessage("Please enter a valid amount of $PAAL tokens.");
      return;
    }

    // Display success message
    setMessage(`You have successfully staked ${stakeAmount} $PAAL tokens for ${selectedOption.duration} at ${selectedOption.apy}.`);
  };

  return (
    <div className="app">
      <h1>Stake $PAAL Tokens</h1>
      <p>Select a staking configuration and enter the number of tokens to stake.</p>

      {/* Staking Options */}
      <div className="staking-options">
        {stakingOptions.map((option) => (
          <div
            key={option.id}
            className={`staking-option ${selectedOption?.id === option.id ? "selected" : ""}`}
            onClick={() => setSelectedOption(option)}
          >
            <p><strong>APY:</strong> {option.apy}</p>
            <p><strong>Duration:</strong> {option.duration}</p>
          </div>
        ))}
      </div>

      {/* Staking Form */}
      <form className="staking-form" onSubmit={handleStake}>
        <label>
          Amount to Stake ($PAAL):
          <input
            type="number"
            min="0"
            value={stakeAmount}
            onChange={(e) => setStakeAmount(e.target.value)}
            placeholder="Enter amount"
          />
        </label>
        <button type="submit">Stake</button>
      </form>

      {/* Message Display */}
      {message && <p className="message">{message}</p>}
    </div>
  );
}

export default App;
```

```css
/* src/App.css */
.app {
  font-family: Arial, sans-serif;
  text-align: center;
  padding: 20px;
}

.staking-options {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin: 20px 0;
}

.staking-option {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  width: 150px;
  cursor: pointer;
  transition: transform 0.3s, box-shadow 0.3s;
}

.staking-option.selected {
  border-color: #4caf50;
  box-shadow: 0 0 10px #4caf50;
  transform: scale(1.05);
}

.staking-option:hover {
  transform: scale(1.05);
}

.staking-form {
  margin: 20px 0;
}

.staking-form input {
  margin: 10px 0;
  padding: 5px;
}

.staking-form button {
  padding: 10px 20px;
  background-color: #4caf50;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

.staking-form button:hover {
  background-color: #45a049;
}

.message {
  margin-top: 20px;
  color: #4caf50;
  font-weight: bold;
}
```

```javascript
// index.js
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
```
