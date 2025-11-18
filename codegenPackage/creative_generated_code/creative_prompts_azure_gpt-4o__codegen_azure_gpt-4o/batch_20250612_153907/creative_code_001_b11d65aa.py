"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metumasikliogginn.godaddysites.com
Prompt: Recommend libraries or APIs for implementing Metamask login authentication in a React.js application.
Generated: DETERMINISTIC_b11d65aa3732da38
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a clean and production-ready example of code implementing MetaMask login authentication in a React.js application:

```javascript
// Install required dependencies before using this code:
// npm install ethers

import React, { useState, useEffect } from "react";
import { ethers } from "ethers";

// MetaMaskLogin Component
const MetaMaskLogin = () => {
  const [walletAddress, setWalletAddress] = useState(null);
  const [errorMessage, setErrorMessage] = useState(null);

  // Function to check if MetaMask extension is installed
  const isMetaMaskInstalled = () => {
    return typeof window.ethereum !== "undefined";
  };

  // Function to handle MetaMask login
  const handleLogin = async () => {
    try {
      if (!isMetaMaskInstalled()) {
        setErrorMessage("MetaMask is not installed. Please install it to continue.");
        return;
      }

      // Request user's wallet connection
      const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

      if (accounts.length > 0) {
        const account = accounts[0];
        setWalletAddress(account); // Save wallet address in state
        setErrorMessage(null); // Clear any previous errors
      } else {
        setErrorMessage("No wallet accounts found.");
      }
    } catch (error) {
      console.error("Error during MetaMask login:", error);
      setErrorMessage("Failed to connect to MetaMask. Please try again.");
    }
  };

  useEffect(() => {
    // Optional: Detect account changes (user switches MetaMask account)
    if (isMetaMaskInstalled()) {
      window.ethereum.on("accountsChanged", (accounts) => {
        if (accounts.length > 0) {
          setWalletAddress(accounts[0]);
          setErrorMessage(null);
        } else {
          setWalletAddress(null);
          setErrorMessage("No wallet accounts found.");
        }
      });
    }

    return () => {
      // Clean up event listener when the component unmounts
      if (isMetaMaskInstalled()) {
        window.ethereum.removeListener("accountsChanged", () => {});
      }
    };
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>MetaMask Authentication</h1>
      {walletAddress ? (
        <div>
          <p>Connected Wallet Address: {walletAddress}</p>
        </div>
      ) : (
        <button onClick={handleLogin} style={{ padding: "10px 20px", fontSize: "16px" }}>
          Connect MetaMask
        </button>
      )}
      {errorMessage && <p style={{ color: "red" }}>{errorMessage}</p>}
    </div>
  );
};

export default MetaMaskLogin;
```

### Notes for Production:
1. **Security:** In production, ensure that the wallet address is sent securely to your backend for authentication or session management.
2. **Validation:** Always validate the wallet address server-side to prevent spoofing attacks.
3. **Dependencies:** Ensure `ethers` library is properly installed (`npm install ethers`).
4. **Testing:** Test across browsers and MetaMask versions to handle edge cases effectively.
