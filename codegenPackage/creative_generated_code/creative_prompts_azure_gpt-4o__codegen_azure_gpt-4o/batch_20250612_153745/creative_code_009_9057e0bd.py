"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-quest-fnjdubph5-lfglabs.vercel.app
Prompt: Develop a web application using Starknet libraries to allow users to connect their wallet, participate in quests, and view their earned rewards in real-time.
Generated: DETERMINISTIC_9057e0bd8ccc0cd4
Batch ID: 20250612_153745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready implementation using Starknet.js, assuming a modern JavaScript framework like React is used to build the frontend. The code includes wallet connection, quests participation, and reward tracking functionalities.

```javascript
// Import necessary libraries
import React, { useState, useEffect } from "react";
import { connect, disconnect, getStarknetWallet } from "starknet"; // Example Starknet wallet utilities
import { Contract } from "starknet"; // Starknet contract interaction
import toast from "react-hot-toast"; // Notification library for user feedback

// Example contract details (replace with actual address and ABI)
const QUEST_CONTRACT_ADDRESS = "0x123456789abcdef"; // Replace with your contract address
const QUEST_CONTRACT_ABI = [ /* Replace with your contract's ABI */ ];

function App() {
  // Application state
  const [walletAddress, setWalletAddress] = useState(null);
  const [contract, setContract] = useState(null);
  const [quests, setQuests] = useState([]);
  const [rewards, setRewards] = useState(0);

  // Connect wallet function
  const connectWallet = async () => {
    try {
      const wallet = await connect(); // Prompt user to connect their wallet
      if (wallet) {
        setWalletAddress(wallet.address);
        setContract(new Contract(QUEST_CONTRACT_ABI, QUEST_CONTRACT_ADDRESS, wallet)); // Initialize contract
        toast.success("Wallet connected successfully!");
      }
    } catch (error) {
      console.error("Failed to connect wallet:", error);
      toast.error("Wallet connection failed!");
    }
  };

  // Disconnect wallet function
  const disconnectWallet = () => {
    disconnect(); // Disconnect the wallet
    setWalletAddress(null);
    setContract(null);
    toast.success("Wallet disconnected.");
  };

  // Fetch quests from the contract
  const fetchQuests = async () => {
    if (!contract) return;
    try {
      const questsData = await contract.call("getQuests"); // Example method in your contract
      setQuests(questsData);
    } catch (error) {
      console.error("Failed to fetch quests:", error);
      toast.error("Error fetching quests!");
    }
  };

  // Participate in a quest
  const participateInQuest = async (questId) => {
    if (!contract || !walletAddress) {
      toast.error("Please connect your wallet first!");
      return;
    }
    try {
      await contract.invoke("participateInQuest", [questId]); // Example method in your contract
      toast.success("Quest participation successful!");
      fetchRewards(); // Refresh rewards after participation
    } catch (error) {
      console.error("Error participating in quest:", error);
      toast.error("Quest participation failed!");
    }
  };

  // Fetch rewards from the contract
  const fetchRewards = async () => {
    if (!contract) return;
    try {
      const rewardsData = await contract.call("getRewards", [walletAddress]); // Example method in your contract
      setRewards(rewardsData);
    } catch (error) {
      console.error("Failed to fetch rewards:", error);
      toast.error("Error fetching rewards!");
    }
  };

  // Fetch quests and rewards on wallet connection
  useEffect(() => {
    if (contract) {
      fetchQuests();
      fetchRewards();
    }
  }, [contract]);

  return (
    <div className="app">
      <header>
        <h1>Starknet Quests</h1>
        <div>
          {walletAddress ? (
            <>
              <span>Connected: {walletAddress}</span>
              <button onClick={disconnectWallet}>Disconnect</button>
            </>
          ) : (
            <button onClick={connectWallet}>Connect Wallet</button>
          )}
        </div>
      </header>

      <main>
        <section>
          <h2>Available Quests</h2>
          {quests.length ? (
            <ul>
              {quests.map((quest, index) => (
                <li key={index}>
                  <span>{quest.name}</span>
                  <button onClick={() => participateInQuest(quest.id)}>Join Quest</button>
                </li>
              ))}
            </ul>
          ) : (
            <p>No quests available.</p>
          )}
        </section>

        <section>
          <h2>Your Rewards</h2>
          <p>Total Rewards: {rewards}</p>
        </section>
      </main>
    </div>
  );
}

export default App;
```

### Notes:
- Replace `QUEST_CONTRACT_ABI` and `QUEST_CONTRACT_ADDRESS` with your actual Starknet contract details.
- Make sure your contract has the methods `getQuests`, `participateInQuest`, and `getRewards`.
- Ensure the Starknet wallet utilities (`connect`, `disconnect`, `getStarknetWallet`) work as expected for your environment.
- Additional styling and optimization can be applied based on your design requirements.
