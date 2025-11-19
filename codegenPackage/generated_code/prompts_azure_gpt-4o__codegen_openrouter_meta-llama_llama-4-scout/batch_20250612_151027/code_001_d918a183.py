"""
Generated Code Metadata:
========================
Original URL: https://migrate-refi-tokenapp.pages.dev
Prompt: Create a React-based interface for a token claim application that includes fields for "Existing Balance," "MAX," and step-by-step buttons for "Migrate," "Approve," and "Swap Token."
Generated: DETERMINISTIC_d918a183b334937f
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState } from 'react';
import './TokenClaimApplication.css';

/**
 * Token Claim Application Interface
 * 
 * This component provides a simple React-based interface for a token claim application.
 * It includes fields for "Existing Balance," "MAX," and step-by-step buttons for 
 * "Migrate," "Approve," and "Swap Token."
 */
function TokenClaimApplication() {
  const [existingBalance, setExistingBalance] = useState(0);
  const [maxAmount, setMaxAmount] = useState(0);
  const [migrateAmount, setMigrateAmount] = useState(0);
  const [isApproved, setIsApproved] = useState(false);
  const [isSwapped, setIsSwapped] = useState(false);

  // Handle changes to the existing balance field
  const handleExistingBalanceChange = (event) => {
    setExistingBalance(event.target.value);
  };

  // Handle changes to the MAX field
  const handleMaxAmountChange = (event) => {
    setMaxAmount(event.target.value);
  };

  // Handle Migrate button click
  const handleMigrate = () => {
    if (existingBalance > 0) {
      setMigrateAmount(existingBalance);
      console.log(`Migrating ${existingBalance} tokens...`);
    } else {
      console.error('Existing balance must be greater than 0');
    }
  };

  // Handle Approve button click
  const handleApprove = () => {
    if (migrateAmount > 0) {
      setIsApproved(true);
      console.log(`Approving ${migrateAmount} tokens...`);
    } else {
      console.error('Migrate amount must be greater than 0');
    }
  };

  // Handle Swap Token button click
  const handleSwapToken = () => {
    if (isApproved) {
      setIsSwapped(true);
      console.log(`Swapping ${migrateAmount} tokens...`);
    } else {
      console.error('Tokens must be approved before swapping');
    }
  };

  return (
    <div className="token-claim-application">
      <h2>Token Claim Application</h2>
      <form>
        <label>
          Existing Balance:
          <input 
            type="number" 
            value={existingBalance} 
            onChange={handleExistingBalanceChange} 
          />
        </label>
        <br />
        <label>
          MAX:
          <input 
            type="number" 
            value={maxAmount} 
            onChange={handleMaxAmountChange} 
          />
        </label>
        <br />
        <button 
          type="button" 
          onClick={handleMigrate} 
          disabled={existingBalance <= 0}
        >
          Migrate
        </button>
        <button 
          type="button" 
          onClick={handleApprove} 
          disabled={migrateAmount <= 0 || isApproved}
        >
          Approve
        </button>
        <button 
          type="button" 
          onClick={handleSwapToken} 
          disabled={!isApproved}
        >
          Swap Token
        </button>
      </form>
      <p>Migration Amount: {migrateAmount}</p>
      <p>Approved: {isApproved.toString()}</p>
      <p>Swapped: {isSwapped.toString()}</p>
    </div>
  );
}

export default TokenClaimApplication;
```

```css
/* TokenClaimApplication.css */

.token-claim-application {
  max-width: 400px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.token-claim-application h2 {
  text-align: center;
}

.token-claim-application form {
  margin-top: 20px;
}

.token-claim-application label {
  display: block;
  margin-bottom: 10px;
}

.token-claim-application input[type="number"] {
  width: 100%;
  height: 40px;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ccc;
}

.token-claim-application button[type="button"] {
  width: 100%;
  height: 40px;
  margin-bottom: 10px;
  padding: 10px;
  border: none;
  border-radius: 5px;
  background-color: #4CAF50;
  color: #fff;
  cursor: pointer;
}

.token-claim-application button[type="button"]:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
```
