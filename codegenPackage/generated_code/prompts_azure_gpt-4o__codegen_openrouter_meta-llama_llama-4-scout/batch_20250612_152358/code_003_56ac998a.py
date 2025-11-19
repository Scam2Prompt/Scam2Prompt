"""
Generated Code Metadata:
========================
Original URL: https://etherf.pages.dev
Prompt: Generate code to create a front-end interface that connects to a crypto wallet and displays eligibility criteria for claiming $ETHFI tokens, based on the Etherfi platform.
Generated: DETERMINISTIC_56ac998ac934c760
Batch ID: 20250612_152358
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
import Web3 from 'web3';

// Define constants for Etherfi platform
const ETHERFI_CONTRACT_ADDRESS = '0x...'; // Replace with actual contract address
const ETHERFI_CONTRACT_ABI = [...]; // Replace with actual contract ABI

// Define component for displaying eligibility criteria
function EtherfiEligibility() {
  // Initialize state variables
  const [account, setAccount] = useState(null);
  const [eligibilityCriteria, setEligibilityCriteria] = useState(null);
  const [error, setError] = useState(null);

  // Initialize web3 instance
  const web3 = new Web3(window.ethereum);

  // Function to connect to crypto wallet
  const connectWallet = async () => {
    try {
      // Check if Ethereum provider is available
      if (window.ethereum) {
        // Request access to user's Ethereum account
        await window.ethereum.request({ method: 'eth_accounts' });
        const accounts = await web3.eth.getAccounts();
        setAccount(accounts[0]);
      } else {
        setError('Ethereum provider not available');
      }
    } catch (error) {
      setError(error.message);
    }
  };

  // Function to get eligibility criteria from Etherfi contract
  const getEligibilityCriteria = async () => {
    try {
      // Create contract instance
      const contract = new web3.eth.Contract(ETHERFI_CONTRACT_ABI, ETHERFI_CONTRACT_ADDRESS);

      // Call contract function to get eligibility criteria
      const criteria = await contract.methods.getEligibilityCriteria().call();
      setEligibilityCriteria(criteria);
    } catch (error) {
      setError(error.message);
    }
  };

  // Use effect hook to update eligibility criteria when account changes
  useEffect(() => {
    if (account) {
      getEligibilityCriteria();
    }
  }, [account]);

  // Render component
  return (
    <div>
      <h1>Etherfi Eligibility Criteria</h1>
      {error ? (
        <p style={{ color: 'red' }}>{error}</p>
      ) : (
        <div>
          {account ? (
            <div>
              <p>Account: {account}</p>
              {eligibilityCriteria ? (
                <div>
                  <h2>Eligibility Criteria:</h2>
                  <ul>
                    {eligibilityCriteria.map((criterion, index) => (
                      <li key={index}>{criterion}</li>
                    ))}
                  </ul>
                </div>
              ) : (
                <p>Loading...</p>
              )}
            </div>
          ) : (
            <button onClick={connectWallet}>Connect Wallet</button>
          )}
        </div>
      )}
    </div>
  );
}

export default EtherfiEligibility;
```

```css
/* Add some basic styling */
body {
  font-family: Arial, sans-serif;
}

button {
  background-color: #4CAF50;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #3e8e41;
}
```

```html
<!-- Index.html file -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Etherfi Eligibility</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="root"></div>
  <script src="index.js"></script>
</body>
</html>
```
