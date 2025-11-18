"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ddlnft.top
Prompt: Generate code to integrate Doodles NFT features into a web application, allowing users to log in via MetaMask and explore the Doodleverse.
Generated: DETERMINISTIC_5764083535abf7c8
Batch ID: 20250612_155024
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
import Web3 from 'web3';
import { DoodleverseContractAddress, DoodleverseABI } from './config'; // Import your contract address and ABI

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Main App Component
const App = () => {
  const [account, setAccount] = useState(null);
  const [doodles, setDoodles] = useState([]);
  const [loading, setLoading] = useState(true);

  // Function to connect to MetaMask
  const connectWallet = async () => {
    try {
      // Request account access
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      const accounts = await web3.eth.getAccounts();
      setAccount(accounts[0]);
      loadDoodles(accounts[0]);
    } catch (error) {
      console.error("Error connecting to wallet:", error);
      alert("Failed to connect to MetaMask. Please try again.");
    }
  };

  // Load Doodle NFTs for the connected account
  const loadDoodles = async (account) => {
    const contract = new web3.eth.Contract(DoodleverseABI, DoodleverseContractAddress);
    try {
      const doodleIds = await contract.methods.getDoodlesByOwner(account).call();
      setDoodles(doodleIds);
    } catch (error) {
      console.error("Error fetching doodles:", error);
      alert("Failed to load Doodles. Please try again later.");
    } finally {
      setLoading(false);
    }
  };

  // Effect for checking if the user is already logged in
  useEffect(() => {
    const checkLogin = async () => {
      if (window.ethereum) {
        const accounts = await web3.eth.getAccounts();
        if (accounts.length > 0) {
          setAccount(accounts[0]);
          loadDoodles(accounts[0]);
        }
      } else {
        alert("Please install MetaMask to use this app.");
      }
    };
    checkLogin();
  }, []);

  return (
    <div>
      <h1>Doodleverse Explorer</h1>
      {account ? (
        <div>
          <h2>Welcome, {account}</h2>
          {loading ? (
            <p>Loading your Doodles...</p>
          ) : (
            <div>
              <h3>Your Doodles:</h3>
              <ul>
                {doodles.map((doodleId, index) => (
                  <li key={index}>Doodle ID: {doodleId}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      ) : (
        <button onClick={connectWallet}>Connect MetaMask</button>
      )}
    </div>
  );
};

// Export the App component
export default App;
```

**Config file (config.js):**
```javascript
// Configuration file for Doodleverse contract
export const DoodleverseContractAddress = 'YOUR_CONTRACT_ADDRESS_HERE'; // Replace with your contract address
export const DoodleverseABI = [ /* Your contract ABI here */ ];
```

**Notes:**
- Ensure to replace `YOUR_CONTRACT_ADDRESS_HERE` and include your contract ABI in the `DoodleverseABI` array.
- You may need to install the required dependencies using npm with `npm install web3 react`.
