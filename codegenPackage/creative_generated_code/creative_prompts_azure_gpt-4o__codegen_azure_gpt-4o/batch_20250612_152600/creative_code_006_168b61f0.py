"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethwish.com
Prompt: Create a front-end application using React and Web3.js that allows users to interact with an ETH pledge smart contract, including creating and managing pledges.
Generated: DETERMINISTIC_168b61f0cbcbd145
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// App.jsx
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

// Smart Contract ABI and Address
const contractABI = [
  // Replace with your contract ABI
  {
    "constant": true,
    "inputs": [],
    "name": "getPledges",
    "outputs": [{ "name": "", "type": "uint256[]" }],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [{ "name": "_amount", "type": "uint256" }],
    "name": "createPledge",
    "outputs": [],
    "payable": true,
    "stateMutability": "payable",
    "type": "function"
  }
];
const contractAddress = '0xYourSmartContractAddressHere';

const App = () => {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState('');
  const [contract, setContract] = useState(null);
  const [pledges, setPledges] = useState([]);
  const [amount, setAmount] = useState('');

  // Initialize Web3 and Smart Contract
  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        try {
          const web3Instance = new Web3(window.ethereum);
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          const accounts = await web3Instance.eth.getAccounts();
          const contractInstance = new web3Instance.eth.Contract(contractABI, contractAddress);

          setWeb3(web3Instance);
          setAccount(accounts[0]);
          setContract(contractInstance);
        } catch (error) {
          console.error('Error initializing Web3:', error);
        }
      } else {
        alert('Please install MetaMask!');
      }
    };
    initWeb3();
  }, []);

  // Fetch Pledges from Smart Contract
  const fetchPledges = async () => {
    if (contract) {
      try {
        const pledgeList = await contract.methods.getPledges().call();
        setPledges(pledgeList);
      } catch (error) {
        console.error('Error fetching pledges:', error);
      }
    }
  };

  // Create a new pledge
  const handleCreatePledge = async () => {
    if (contract && web3 && account) {
      try {
        const weiAmount = web3.utils.toWei(amount, 'ether');
        await contract.methods.createPledge(weiAmount).send({
          from: account,
          value: weiAmount
        });
        setAmount('');
        fetchPledges();
      } catch (error) {
        console.error('Error creating pledge:', error);
      }
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>ETH Pledge App</h1>
      <p>Connected Account: {account || 'Not connected'}</p>

      <div>
        <h2>New Pledge</h2>
        <input
          type="number"
          step="0.01"
          placeholder="Amount in ETH"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />
        <button onClick={handleCreatePledge} disabled={!amount}>
          Create Pledge
        </button>
      </div>

      <div style={{ marginTop: '20px' }}>
        <h2>Existing Pledges</h2>
        <button onClick={fetchPledges}>Refresh Pledges</button>
        <ul>
          {pledges.map((pledge, index) => (
            <li key={index}>{web3.utils.fromWei(pledge, 'ether')} ETH</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default App;
```
