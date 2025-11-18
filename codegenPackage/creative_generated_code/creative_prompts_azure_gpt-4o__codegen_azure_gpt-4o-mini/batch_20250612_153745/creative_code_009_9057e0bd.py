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

```javascript
// Importing required libraries
import React, { useEffect, useState } from 'react';
import { connect, isConnected, getAccount, onAccountChange } from 'starknet';
import { getQuests, submitQuest } from './api'; // Assume these are defined in api.js
import './App.css'; // Custom CSS for styling

// Main application component
const App = () => {
  const [account, setAccount] = useState(null);
  const [quests, setQuests] = useState([]);
  const [rewards, setRewards] = useState(0);
  const [error, setError] = useState(null);

  // Establishes connection to the wallet on component mount
  useEffect(() => {
    const initialize = async () => {
      try {
        // Check if the wallet is connected
        if (isConnected()) {
          const accountData = await getAccount();
          setAccount(accountData);
          fetchQuests();
        }
      } catch (err) {
        console.error('Error initializing wallet:', err);
        setError('Failed to connect to wallet. Please try again.');
      }
    };

    initialize();
    // Listening for account changes
    onAccountChange(() => {
      setAccount(getAccount());
    });
  }, []);

  // Function to fetch available quests
  const fetchQuests = async () => {
    try {
      const fetchedQuests = await getQuests(account);
      setQuests(fetchedQuests);
    } catch (err) {
      console.error('Error fetching quests:', err);
      setError('Failed to fetch quests. Please try again.');
    }
  };

  // Function to handle quest submission
  const handleQuestSubmission = async (questId) => {
    try {
      await submitQuest(account, questId);
      // Update rewards after successful submission
      setRewards((prev) => prev + 1); // Increment rewards
      fetchQuests(); // Refresh quests
    } catch (err) {
      console.error('Error submitting quest:', err);
      setError('Failed to submit quest. Please try again.');
    }
  };

  return (
    <div className="app">
      <h1>Starknet Quest Application</h1>
      {error && <div className="error">{error}</div>}
      {account ? (
        <div>
          <h2>Connected as: {account}</h2>
          <h3>Your Rewards: {rewards}</h3>
          <div className="quests">
            <h4>Available Quests:</h4>
            <ul>
              {quests.map(quest => (
                <li key={quest.id}>
                  {quest.name}
                  <button onClick={() => handleQuestSubmission(quest.id)}>Participate</button>
                </li>
              ))}
            </ul>
          </div>
        </div>
      ) : (
        <button onClick={connect}>Connect Wallet</button>
      )}
    </div>
  );
};

export default App;

// Note: To make this code runnable, ensure you have the required dependencies
// and the appropriate API functions in api.js for fetching quests and submitting them.
```
