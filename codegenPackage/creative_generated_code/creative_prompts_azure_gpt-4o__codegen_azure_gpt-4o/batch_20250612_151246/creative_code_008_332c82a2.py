"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neiroethereum.pages.dev
Prompt: Develop a React application that integrates MetaMask and allows users to claim $NEIRO tokens via a referral link, including transaction confirmation and token balance display.
Generated: DETERMINISTIC_332c82a21736a0b0
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// App.js
import React, { useState, useEffect } from "react";
import Web3 from "web3";
import detectEthereumProvider from "@metamask/detect-provider";
import "./App.css";

// Constants
const TOKEN_CONTRACT_ADDRESS = "<TOKEN_CONTRACT_ADDRESS>";
const TOKEN_ABI = [
  // Add the ABI of the ERC20 Token Contract here (shortened for brevity)
];

function App() {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState(null);
  const [tokenBalance, setTokenBalance] = useState("0");
  const [isTransactionPending, setIsTransactionPending] = useState(false);
  const [referralLink, setReferralLink] = useState("");

  useEffect(() => {
    // Check if MetaMask is installed and connect to the provider
    const initWeb3 = async () => {
      const provider = await detectEthereumProvider();
      if (provider) {
        const web3Instance = new Web3(provider);
        setWeb3(web3Instance);
      } else {
        alert("Please install MetaMask to use this application!");
      }
    };

    initWeb3();
  }, []);

  useEffect(() => {
    // Fetch token balance if account changes
    const fetchBalance = async () => {
      if (web3 && account) {
        const tokenContract = new web3.eth.Contract(TOKEN_ABI, TOKEN_CONTRACT_ADDRESS);
        const balance = await tokenContract.methods.balanceOf(account).call();
        setTokenBalance(web3.utils.fromWei(balance, "ether"));
      }
    };

    fetchBalance();
  }, [web3, account]);

  const connectWallet = async () => {
    try {
      const accounts = await web3.eth.requestAccounts();
      setAccount(accounts[0]);
    } catch (error) {
      console.error("Error connecting to wallet:", error);
      alert("Failed to connect to MetaMask. Please try again.");
    }
  };

  const claimTokens = async () => {
    if (!referralLink) {
      alert("Referral link is required to claim tokens.");
      return;
    }

    if (web3 && account) {
      try {
        setIsTransactionPending(true);
        const tokenContract = new web3.eth.Contract(TOKEN_ABI, TOKEN_CONTRACT_ADDRESS);
        const referralAddress = referralLink.trim(); // Referral address provided via link

        // Call the claim function (replace 'claimTokens' with relevant contract method)
        const tx = await tokenContract.methods.claimTokens(referralAddress).send({ from: account });
        console.log("Transaction successful:", tx);

        // Update balance after claiming tokens
        const balance = await tokenContract.methods.balanceOf(account).call();
        setTokenBalance(web3.utils.fromWei(balance, "ether"));
      } catch (error) {
        console.error("Error claiming tokens:", error);
        alert("Failed to claim tokens. Please try again later.");
      } finally {
        setIsTransactionPending(false);
      }
    } else {
      alert("Please connect your wallet first.");
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Claim $NEIRO Tokens</h1>
        {!account ? (
          <button onClick={connectWallet}>Connect Wallet</button>
        ) : (
          <div>
            <p>Connected Account: {account}</p>
            <p>Token Balance: {tokenBalance} $NEIRO</p>
            <input
              type="text"
              placeholder="Enter referral link"
              value={referralLink}
              onChange={(e) => setReferralLink(e.target.value)}
            />
            <button onClick={claimTokens} disabled={isTransactionPending}>
              {isTransactionPending ? "Processing..." : "Claim Tokens"}
            </button>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;

// App.css
.App {
  text-align: center;
  font-family: Arial, sans-serif;
}

.App-header {
  margin: 20px;
}

button {
  margin: 10px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

input {
  padding: 10px;
  margin: 10px;
  font-size: 16px;
}

p {
  font-size: 18px;
}
```
