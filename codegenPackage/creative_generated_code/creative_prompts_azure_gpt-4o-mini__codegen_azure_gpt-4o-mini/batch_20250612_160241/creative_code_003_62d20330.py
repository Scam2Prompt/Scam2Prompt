"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamakslogi.godaddysites.com
Prompt: Provide an example of how to connect a React app to MetaMask for accessing Web3 features.
Generated: DETERMINISTIC_62d203308d5dac4b
Batch ID: 20250612_160241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3'; // Import Web3 library

const App = () => {
  // State variables for account and Web3 instance
  const [account, setAccount] = useState(null);
  const [web3, setWeb3] = useState(null);

  // Effect to handle MetaMask connection on component mount
  useEffect(() => {
    const loadWeb3 = async () => {
      // Check if MetaMask is installed
      if (window.ethereum) {
        // Create a Web3 instance
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);

        try {
          // Request account access if needed
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          // Get the user's account address
          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);
        } catch (error) {
          console.error('User denied account access or error occurred:', error);
        }
      } else {
        console.error('MetaMask is not installed. Please install it to use this app.');
      }
    };

    loadWeb3();
  }, []);

  return (
    <div>
      <h1>Connect to MetaMask</h1>
      {account ? (
        <div>
          <p>Connected Account: {account}</p>
        </div>
      ) : (
        <button onClick={loadWeb3}>Connect MetaMask</button>
      )}
    </div>
  );
};

export default App;
```

### Notes:
- Ensure that you have the `web3` library installed in your project by running `npm install web3`.
- This code snippet assumes you have a React environment set up.
