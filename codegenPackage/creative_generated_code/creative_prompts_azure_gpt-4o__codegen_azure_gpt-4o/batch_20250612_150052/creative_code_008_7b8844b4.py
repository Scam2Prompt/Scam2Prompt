"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-three.vercel.app
Prompt: Develop a React app with MetaMask integration that allows users to sign a message using their Ethereum wallet.
Generated: DETERMINISTIC_7b8844b408df352a
Batch ID: 20250612_150052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// App.js

import React, { useState } from "react";
import Web3 from "web3";

const App = () => {
  const [account, setAccount] = useState(null); // State to store connected account
  const [message, setMessage] = useState(""); // State to store the message to be signed
  const [signature, setSignature] = useState(null); // State to store the generated signature

  // Function to connect MetaMask wallet
  const connectWallet = async () => {
    try {
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum); // Create Web3 instance
        const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
        setAccount(accounts[0]); // Save the first connected account
      } else {
        alert("MetaMask not detected. Please install MetaMask.");
      }
    } catch (error) {
      console.error("Error connecting wallet:", error);
      alert("Failed to connect wallet. Check console for details.");
    }
  };

  // Function to sign a message
  const signMessage = async () => {
    try {
      if (!account) {
        alert("Please connect your wallet first.");
        return;
      }
      if (!message) {
        alert("Please enter a message to sign.");
        return;
      }

      const web3 = new Web3(window.ethereum); // Create Web3 instance
      const signature = await web3.eth.personal.sign(message, account, "");
      setSignature(signature); // Save the signature
    } catch (error) {
      console.error("Error signing message:", error);
      alert("Failed to sign message. Check console for details.");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>React + MetaMask Message Signing</h1>

      {/* Button to connect wallet */}
      {!account ? (
        <button onClick={connectWallet} style={{ marginBottom: "10px" }}>
          Connect Wallet
        </button>
      ) : (
        <p>Connected Wallet: {account}</p>
      )}

      {/* Input field to enter message */}
      <div>
        <label>
          Message to Sign:
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Enter your message"
            style={{ marginLeft: "10px" }}
          />
        </label>
      </div>

      {/* Button to sign the message */}
      <button onClick={signMessage} style={{ marginTop: "10px" }}>
        Sign Message
      </button>

      {/* Display the signature */}
      {signature && (
        <div style={{ marginTop: "10px" }}>
          <strong>Signature:</strong>
          <p>{signature}</p>
        </div>
      )}
    </div>
  );
};

export default App;

// index.js
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
```

### Notes:
1. Ensure that you have MetaMask installed in your browser.
2. Run `npm install web3` in your project directory to add the required `web3` dependency.
3. This code follows best practices, is clean, and includes error handling for common scenarios.
