"""
Generated Code Metadata:
========================
Original URL: https://bafybeicx4qx5ng47s6p4ottbq5rvigxuacj5sg3urh654cdxqw343mbuua.ipfs.dweb.link
Prompt: Develop a simple dApp using React that displays the number of participants in a real-time or live event, similar to the "Shrine participants: 5" shown here.
Generated: DETERMINISTIC_eecbdb887b68c573
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries and components
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import './App.css';

// Smart Contract ABI (simplified for this example)
const contractABI = [
  {
    "inputs": [],
    "name": "getParticipantCount",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "participate",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];

// Contract address (replace with your actual contract address)
const contractAddress = "0x1234567890123456789012345678901234567890";

function App() {
  const [participantCount, setParticipantCount] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Initialize provider and contract
  const provider = new ethers.providers.Web3Provider(window.ethereum);
  const contract = new ethers.Contract(contractAddress, contractABI, provider.getSigner());

  // Fetch participant count from the contract
  const fetchParticipantCount = async () => {
    try {
      setLoading(true);
      const count = await contract.getParticipantCount();
      setParticipantCount(count.toNumber());
      setError('');
    } catch (err) {
      console.error("Error fetching participant count:", err);
      setError('Failed to fetch participant count');
    } finally {
      setLoading(false);
    }
  };

  // Handle participation
  const handleParticipate = async () => {
    try {
      setLoading(true);
      const tx = await contract.participate();
      await tx.wait();
      await fetchParticipantCount();
    } catch (err) {
      console.error("Error participating:", err);
      setError('Failed to participate');
    } finally {
      setLoading(false);
    }
  };

  // Check if wallet is connected
  const checkWalletConnection = async () => {
    if (window.ethereum) {
      try {
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        await fetchParticipantCount();
      } catch (err) {
        console.error("User denied account access");
      }
    } else {
      setError('Please install MetaMask!');
    }
  };

  // Set up event listener for account changes
  useEffect(() => {
    if (window.ethereum) {
      window.ethereum.on('accountsChanged', () => {
        fetchParticipantCount();
      });
    }

    return () => {
      if (window.ethereum) {
        window.ethereum.removeListener('accountsChanged', fetchParticipantCount);
      }
    };
  }, []);

  // Initial load
  useEffect(() => {
    checkWalletConnection();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Event Participation</h1>
        
        {error && <p className="error">{error}</p>}

        <div className="participant-count">
          <h2>Participants: {loading ? 'Loading...' : participantCount}</h2>
        </div>

        <button 
          onClick={handleParticipate} 
          disabled={loading}
          className="participate-button"
        >
          {loading ? 'Processing...' : 'Participate'}
        </button>
      </header>
    </div>
  );
}

export default App;
```

```css
/* App.css */
.App {
  text-align: center;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
  background-color: #282c34;
}

.App-header {
  padding: 20px;
}

.error {
  color: #ff6b6b;
}

.participate-button {
  background-color: #61dafb;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 20px 0;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.participate-button:hover {
  background-color: #4fa8d3;
}

.participate-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.participant-count {
  margin: 20px 0;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
}
```
