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

```javascript
// App.js
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import './App.css';

// Replace with your contract's ABI and address
const contractABI = [/* Your contract ABI here */];
const contractAddress = '0xYourContractAddressHere';

function App() {
  const [account, setAccount] = useState(null);
  const [tokenBalance, setTokenBalance] = useState(0);
  const [loading, setLoading] = useState(false);
  const [web3, setWeb3] = useState(null);
  const [contract, setContract] = useState(null);

  useEffect(() => {
    // Initialize web3 and contract
    const init = async () => {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        const accounts = await web3Instance.eth.requestAccounts();
        const userAccount = accounts[0];
        const tokenContract = new web3Instance.eth.Contract(contractABI, contractAddress);

        setWeb3(web3Instance);
        setContract(tokenContract);
        setAccount(userAccount);
      } else {
        alert('Please install MetaMask!');
      }
    };

    init();
  }, []);

  // Function to claim tokens through a referral link
  const claimTokens = async (referral) => {
    if (!contract) {
      console.error('Contract not initialized');
      return;
    }

    setLoading(true);
    try {
      const response = await contract.methods.claimTokens(referral).send({ from: account });
      console.log('Transaction successful:', response);
      fetchTokenBalance();
    } catch (error) {
      console.error('Transaction failed:', error);
      alert('Transaction failed. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  // Fetch user's token balance
  const fetchTokenBalance = async () => {
    if (!contract || !account) {
      console.error('Contract or account not initialized');
      return;
    }

    try {
      const balance = await contract.methods.balanceOf(account).call();
      setTokenBalance(balance);
    } catch (error) {
      console.error('Error fetching balance:', error);
      alert('Error fetching balance. Please try again later.');
    }
  };

  // Call fetchTokenBalance whenever account changes
  useEffect(() => {
    fetchTokenBalance();
  }, [account]);

  return (
    <div className="App">
      <h1>$NEIRO Token Claim</h1>
      {account ? (
        <>
          <p>Your account: {account}</p>
          <p>Your $NEIRO balance: {web3 ? web3.utils.fromWei(tokenBalance, 'ether') : 0}</p>
          <input type="text" placeholder="Enter referral link" id="referral" />
          <button onClick={() => claimTokens(document.getElementById('referral').value)} disabled={loading}>
            {loading ? 'Claiming...' : 'Claim Tokens'}
          </button>
        </>
      ) : (
        <p>Please connect your MetaMask wallet.</p>
      )}
    </div>
  );
}

export default App;

// App.css
.App {
  text-align: center;
}

button {
  margin-top: 10px;
}

// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

Ensure you replace `/* Your contract ABI here */` and `0xYourContractAddressHere` with your actual contract ABI and address before running this application. Also, make sure to have MetaMask installed and set up for this to work properly.
