"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiha7aew6cnrfx323nbkbwheqhy7qp4rdsogs3bqahgzfex7vgmlya.ipfs.dweb.link
Prompt: Develop a frontend form using React that allows users to participate in the BCKR presale by entering their ETH amount and displaying the equivalent BCKR tokens.
Generated: DETERMINISTIC_15b11dea5557e454
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary libraries
import React, { useState } from 'react';

// Constants
const TOKEN_EXCHANGE_RATE = 1000; // 1 ETH = 1000 BCKR tokens

/**
 * PresaleForm Component
 * This component renders a form for users to participate in the BCKR presale.
 */
const PresaleForm = () => {
  // State for form data and error messages
  const [ethAmount, setEthAmount] = useState('');
  const [bckrTokens, setBckrTokens] = useState(0);
  const [error, setError] = useState('');

  /**
   * Handles changes to the ETH input field.
   * Validates that the input is a valid number.
   */
  const handleEthChange = (e) => {
    const value = e.target.value;

    // Reset error state
    setError('');

    // Validate input
    if (!isNaN(value) && Number(value) >= 0) {
      setEthAmount(value);
      setBckrTokens(value * TOKEN_EXCHANGE_RATE); // Calculate equivalent tokens
    } else {
      setError('Please enter a valid ETH amount.');
      setEthAmount('');
      setBckrTokens(0);
    }
  };

  /**
   * Handles form submission.
   * Prevents default behavior and logs the ETH and token amounts.
   */
  const handleSubmit = (e) => {
    e.preventDefault();

    // Ensure valid ETH amount is entered
    if (ethAmount === '' || isNaN(ethAmount) || ethAmount <= 0) {
      setError('Please enter a valid ETH amount before submitting.');
      return;
    }

    // Log or process data as needed in production apps
    alert(`You are purchasing ${bckrTokens} BCKR tokens for ${ethAmount} ETH.`);
  };

  return (
    <div style={styles.container}>
      <h1>BCKR Presale</h1>
      <form onSubmit={handleSubmit} style={styles.form}>
        <div style={styles.inputGroup}>
          <label htmlFor="ethAmount" style={styles.label}>
            Enter ETH Amount:
          </label>
          <input
            type="text"
            id="ethAmount"
            value={ethAmount}
            onChange={handleEthChange}
            placeholder="e.g., 0.5"
            style={styles.input}
          />
          {error && <p style={styles.error}>{error}</p>}
        </div>
        <div style={styles.result}>
          <p>
            Equivalent BCKR Tokens: <strong>{bckrTokens}</strong>
          </p>
        </div>
        <button type="submit" style={styles.button}>
          Participate in Presale
        </button>
      </form>
    </div>
  );
};

// Inline styles for the component
const styles = {
  container: {
    textAlign: 'center',
    margin: '20px auto',
    maxWidth: '400px',
    fontFamily: 'Arial, sans-serif',
  },
  form: {
    border: '1px solid #ccc',
    borderRadius: '8px',
    padding: '20px',
    backgroundColor: '#f9f9f9',
  },
  inputGroup: {
    marginBottom: '15px',
  },
  label: {
    display: 'block',
    fontWeight: 'bold',
    marginBottom: '5px',
  },
  input: {
    width: '100%',
    padding: '10px',
    fontSize: '16px',
    borderRadius: '4px',
    border: '1px solid #ccc',
  },
  error: {
    color: 'red',
    fontSize: '12px',
  },
  result: {
    marginTop: '15px',
    fontSize: '18px',
  },
  button: {
    padding: '10px 15px',
    fontSize: '16px',
    color: '#fff',
    backgroundColor: '#007bff',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
  },
};

// Export the component
export default PresaleForm;
```
