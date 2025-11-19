"""
Generated Code Metadata:
========================
Original URL: https://wap.xushuishiwu.cn
Prompt: Create a tutorial for integrating MetaMask wallet functionality into a React application, including token management and transaction execution, based on the "MetaMask钱包和imToken钱包" comparison section.
Generated: DETERMINISTIC_de606913a51e70f6
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is the code for integrating MetaMask wallet functionality into a React application:
```jsx
// MetaMaskWallet.js
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

/**
 * MetaMask Wallet component
 */
const MetaMaskWallet = () => {
  const [web3, setWeb3] = useState(null);
  const [accounts, setAccounts] = useState([]);
  const [balance, setBalance] = useState(0);
  const [tokenBalance, setTokenBalance] = useState({});

  // Initialize Web3 and MetaMask
  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);
      } else {
        console.error('MetaMask not installed');
      }
    };
    initWeb3();
  }, []);

  // Get accounts and balance
  useEffect(() => {
    if (web3) {
      const getAccounts = async () => {
        try {
          const accounts = await web3.eth.getAccounts();
          setAccounts(accounts);
          const balance = await web3.eth.getBalance(accounts[0]);
          setBalance(web3.utils.fromWei(balance));
        } catch (error) {
          console.error('Error getting accounts:', error);
        }
      };
      getAccounts();
    }
  }, [web3]);

  // Get token balance
  const getTokenBalance = async (tokenAddress) => {
    if (web3 && accounts.length > 0) {
      try {
        const tokenContract = new web3.eth.Contract(ERC20ABI, tokenAddress);
        const balance = await tokenContract.methods.balanceOf(accounts[0]).call();
        setTokenBalance((prevBalances) => ({
          ...prevBalances,
          [tokenAddress]: web3.utils.fromWei(balance),
        }));
      } catch (error) {
        console.error('Error getting token balance:', error);
      }
    }
  };

  // Send transaction
  const sendTransaction = async (toAddress, amount) => {
    if (web3 && accounts.length > 0) {
      try {
        const txCount = await web3.eth.getTransactionCount(accounts[0]);
        const tx = {
          from: accounts[0],
          to: toAddress,
          value: web3.utils.toWei(amount),
          gas: '20000',
          gasPrice: web3.utils.toWei('20', 'gwei'),
          nonce: txCount,
        };
        const signedTx = await web3.eth.signTransaction(tx);
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        console.log('Transaction receipt:', receipt);
      } catch (error) {
        console.error('Error sending transaction:', error);
      }
    }
  };

  // ERC20 token ABI
  const ERC20ABI = [
    {
      constant: true,
      inputs: [],
      name: 'name',
      outputs: [
        {
          name: '',
          type: 'string',
        },
      ],
      payable: false,
      type: 'function',
    },
    {
      constant: true,
      inputs: [],
      name: 'symbol',
      outputs: [
        {
          name: '',
          type: 'string',
        },
      ],
      payable: false,
      type: 'function',
    },
    {
      constant: true,
      inputs: [
        {
          name: 'owner',
          type: 'address',
        },
      ],
      name: 'balanceOf',
      outputs: [
        {
          name: '',
          type: 'uint256',
        },
      ],
      payable: false,
      type: 'function',
    },
  ];

  return (
    <div>
      <h2>MetaMask Wallet</h2>
      <p>Accounts: {accounts.join(', ')}</p>
      <p>Balance: {balance} ETH</p>
      <ul>
        {Object.keys(tokenBalance).map((tokenAddress) => (
          <li key={tokenAddress}>
            Token Balance: {tokenBalance[tokenAddress]} (
            {tokenAddress}
            )
          </li>
        ))}
      </ul>
      <button onClick={() => getTokenBalance('0x...tokenAddress...')}>Get Token Balance</button>
      <button onClick={() => sendTransaction('0x...toAddress...', '1')}>Send Transaction</button>
    </div>
  );
};

export default MetaMaskWallet;
```

```jsx
// App.js
import React from 'react';
import MetaMaskWallet from './MetaMaskWallet';

function App() {
  return (
    <div>
      <MetaMaskWallet />
    </div>
  );
}

export default App;
```

```jsx
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
