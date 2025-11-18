"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-humanizedai.web.app
Prompt: Develop a web application interface using React that mimics the HumanizedAi staking platform, including features like HMZ balance display, lock duration selection, and calculated earnings preview.
Generated: DETERMINISTIC_c680cd44f0df60ec
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import './App.css'; // Import CSS for styling

// Main App component
const App = () => {
  // State variables
  const [hmzBalance, setHmzBalance] = useState(0); // HMZ balance
  const [lockDuration, setLockDuration] = useState(30); // Lock duration in days
  const [earnings, setEarnings] = useState(0); // Calculated earnings

  // Mock function to simulate fetching HMZ balance from an API
  const fetchHmzBalance = async () => {
    try {
      // Here you would typically fetch data from an API
      const balance = await new Promise((resolve) => setTimeout(() => resolve(1200), 1000));
      setHmzBalance(balance);
    } catch (error) {
      console.error("Error fetching HMZ balance:", error);
    }
  };

  // Effect to fetch HMZ balance on component mount
  useEffect(() => {
    fetchHmzBalance();
  }, []);

  // Function to calculate earnings based on lock duration
  const calculateEarnings = () => {
    const earningsRate = 0.05; // Earnings rate per day
    const calculatedEarnings = hmzBalance * earningsRate * lockDuration;
    setEarnings(calculatedEarnings);
  };

  // Effect to calculate earnings whenever lock duration or balance changes
  useEffect(() => {
    calculateEarnings();
  }, [lockDuration, hmzBalance]);

  return (
    <div className="App">
      <header className="App-header">
        <h1>HumanizedAi Staking Platform</h1>
        <div className="balance-display">
          <h2>HMZ Balance: {hmzBalance} HMZ</h2>
        </div>
        <div className="lock-duration">
          <label htmlFor="lockDuration">Select Lock Duration (days): </label>
          <select
            id="lockDuration"
            value={lockDuration}
            onChange={(e) => setLockDuration(Number(e.target.value))}
          >
            {[30, 60, 90, 120].map((duration) => (
              <option key={duration} value={duration}>
                {duration} days
              </option>
            ))}
          </select>
        </div>
        <div className="earnings-preview">
          <h3>Estimated Earnings: {earnings.toFixed(2)} HMZ</h3>
        </div>
      </header>
    </div>
  );
};

export default App;
```

```css
/* App.css */

.App {
  text-align: center;
  font-family: Arial, sans-serif;
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: white;
}

.balance-display {
  margin: 20px;
}

.lock-duration {
  margin: 20px;
}

.earnings-preview {
  margin: 20px;
}
```
