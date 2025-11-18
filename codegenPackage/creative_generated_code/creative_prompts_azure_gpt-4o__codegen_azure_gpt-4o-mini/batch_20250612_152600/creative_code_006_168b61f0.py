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
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import PledgeContractABI from './PledgeContractABI.json'; // Import the ABI of the contract

const PledgeApp = () => {
  const [account, setAccount] = useState('');
  const [pledgeAmount, setPledgeAmount] = useState('');
  const [pledges, setPledges] = useState([]);
  const [contract, setContract] = useState(null);
  
  // Initialize Web3 and contract
  useEffect(() => {
    const initWeb3 = async () => {
      try {
        // Check if the browser has MetaMask installed
        if (window.ethereum) {
          const web3 = new Web3(window.ethereum);
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          const accounts = await web3.eth.getAccounts();
          setAccount(accounts[0]);
          
          // Initialize the pledge contract
          const networkId = await web3.eth.net.getId();
          const deployedNetwork = PledgeContractABI.networks[networkId];
          const instance = new web3.eth.Contract(PledgeContractABI.abi, deployedNetwork && deployedNetwork.address);
          setContract(instance);
        } else {
          alert('Please install MetaMask!');
        }
      } catch (error) {
        console.error("Error initializing Web3: ", error);
      }
    };
    
    initWeb3();
  }, []);

  // Create a pledge
  const createPledge = async () => {
    if (!contract) return;
    try {
      await contract.methods.createPledge().send({
        from: account,
        value: Web3.utils.toWei(pledgeAmount, 'ether')
      });
      alert('Pledge created successfully!');
      fetchPledges(); // Refresh the pledge list
    } catch (error) {
      console.error("Error creating pledge: ", error);
      alert('Error creating pledge. Please try again.');
    }
  };

  // Fetch pledges from the blockchain
  const fetchPledges = async () => {
    if (!contract) return;
    try {
      const pledgeCount = await contract.methods.getPledgeCount().call();
      const fetchedPledges = [];
      for (let i = 0; i < pledgeCount; i++) {
        const pledge = await contract.methods.pledges(i).call();
        fetchedPledges.push(pledge);
      }
      setPledges(fetchedPledges);
    } catch (error) {
      console.error("Error fetching pledges: ", error);
    }
  };

  // Handle pledge input change
  const handleChange = (event) => {
    setPledgeAmount(event.target.value);
  };

  // Use effect to fetch pledges upon account change
  useEffect(() => {
    if (contract) {
      fetchPledges();
    }
  }, [contract]);

  return (
    <div>
      <h1>Pledge DApp</h1>
      <p>Connected Account: {account}</p>
      <input
        type="text"
        placeholder="Pledge Amount (ETH)"
        value={pledgeAmount}
        onChange={handleChange}
      />
      <button onClick={createPledge}>Create Pledge</button>

      <h2>Your Pledges:</h2>
      <ul>
        {pledges.map((pledge, index) => (
          <li key={index}>
            Amount: {Web3.utils.fromWei(pledge.amount, 'ether')} ETH, Status: {pledge.status}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PledgeApp;
```

### PledgeContractABI.json (example ABI structure)
```json
{
  "contracts": {
    "PledgeContract": {
      "abi": [ /* Your ABI goes here */ ],
      "networks": {
        "1": {
          "address": "0xYourContractAddress"
        }
      }
    }
  }
}
```

### Note
1. Ensure to add the actual ABI of your Pledge Contract in the `PledgeContractABI.json`.
2. Handle the promise rejections and error handling as per your application's requirements.
3. Make sure you have setup your project with `create-react-app` for this code to work seamlessly with React.
