"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://questn-rewards.web.app
Prompt: Create a Web3 application that connects to QuestN and displays a user's completed quests and rewards.
Generated: DETERMINISTIC_0768efea81140b28
Batch ID: 20250612_150435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the production-ready code for a Web3 application that connects to QuestN and displays a user's completed quests and rewards. This implementation uses React.js with ethers.js for interacting with the blockchain:

### `App.js`

```javascript
import React, { useEffect, useState } from "react";
import { ethers } from "ethers";
import "./App.css";

// ABI and Contract Address for QuestN (replace with actual contract details)
const questNAbi = [
  // Replace with actual ABI from QuestN
  {
    "constant": true,
    "inputs": [{ "name": "_user", "type": "address" }],
    "name": "getCompletedQuests",
    "outputs": [{ "name": "quests", "type": "string[]" }],
    "type": "function",
  },
  {
    "constant": true,
    "inputs": [{ "name": "_user", "type": "address" }],
    "name": "getRewards",
    "outputs": [{ "name": "rewards", "type": "string[]" }],
    "type": "function",
  },
];
const questNContractAddress = "0xYourQuestNContractAddressHere"; // Replace with actual contract address

function App() {
  const [userAddress, setUserAddress] = useState(null);
  const [completedQuests, setCompletedQuests] = useState([]);
  const [rewards, setRewards] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // Connect to MetaMask wallet
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        setError("MetaMask is not installed.");
        return;
      }
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const accounts = await provider.send("eth_requestAccounts", []);
      setUserAddress(accounts[0]);
    } catch (err) {
      setError("Failed to connect wallet: " + err.message);
    }
  };

  // Fetch completed quests and rewards from QuestN
  const fetchQuestData = async () => {
    if (!userAddress) {
      setError("Wallet is not connected.");
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const contract = new ethers.Contract(questNContractAddress, questNAbi, provider);

      const quests = await contract.getCompletedQuests(userAddress);
      const userRewards = await contract.getRewards(userAddress);

      setCompletedQuests(quests);
      setRewards(userRewards);
    } catch (err) {
      setError("Failed to fetch data: " + err.message);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    if (userAddress) {
      fetchQuestData();
    }
  }, [userAddress]);

  return (
    <div className="App">
      <header className="App-header">
        <h1>QuestN - Completed Quests & Rewards</h1>
        {!userAddress ? (
          <button onClick={connectWallet}>Connect Wallet</button>
        ) : (
          <div>
            <p>Connected Wallet: {userAddress}</p>
            <button onClick={fetchQuestData} disabled={isLoading}>
              {isLoading ? "Loading..." : "Refresh Data"}
            </button>
          </div>
        )}
        {error && <p className="error">{error}</p>}

        <div className="data-section">
          <h2>Completed Quests</h2>
          {completedQuests.length > 0 ? (
            <ul>
              {completedQuests.map((quest, index) => (
                <li key={index}>{quest}</li>
              ))}
            </ul>
          ) : (
            <p>No completed quests found.</p>
          )}

          <h2>Rewards</h2>
          {rewards.length > 0 ? (
            <ul>
              {rewards.map((reward, index) => (
                <li key={index}>{reward}</li>
              ))}
            </ul>
          ) : (
            <p>No rewards found.</p>
          )}
        </div>
      </header>
    </div>
  );
}

export default App;
```

### `App.css`

```css
.App {
  text-align: center;
  font-family: Arial, sans-serif;
  padding: 20px;
}

.App-header {
  margin: 20px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  margin: 10px;
}

button:disabled {
  cursor: not-allowed;
  background-color: #ccc;
}

.error {
  color: red;
  margin: 10px 0;
}

.data-section {
  margin-top: 20px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  margin: 5px 0;
}
```

### Notes:
1. Replace `questNAbi` and `questNContractAddress` with the actual ABI and contract address for QuestN.
2. Ensure the MetaMask wallet is installed in the browser.
3. Install necessary dependencies:
   ```bash
   npm install ethers react-scripts
   ```
4. Run the application using:
   ```bash
   npm start
   ```
