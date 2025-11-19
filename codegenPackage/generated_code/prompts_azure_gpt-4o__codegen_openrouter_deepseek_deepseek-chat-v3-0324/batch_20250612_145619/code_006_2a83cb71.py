"""
Generated Code Metadata:
========================
Original URL: https://ethphbi.com
Prompt: Create a frontend JavaScript application that interacts with an Ethereum smart contract to display pledge details and allow users to make new pledges.
Generated: DETERMINISTIC_2a83cb71d0ab6d1a
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import Web3 from 'web3';
import { useState, useEffect } from 'react';

// Smart Contract ABI (replace with your actual contract ABI)
const contractABI = [
  {
    "inputs": [],
    "name": "getPledges",
    "outputs": [
      {
        "internalType": "uint256[]",
        "name": "",
        "type": "uint256[]"
      },
      {
        "internalType": "address[]",
        "name": "",
        "type": "address[]"
      },
      {
        "internalType": "string[]",
        "name": "",
        "type": "string[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "string",
        "name": "_description",
        "type": "string"
      },
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "makePledge",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  }
];

// Contract address (replace with your actual contract address)
const contractAddress = '0x1234567890123456789012345678901234567890';

const App = () => {
  const [web3, setWeb3] = useState(null);
  const [contract, setContract] = useState(null);
  const [account, setAccount] = useState('');
  const [pledges, setPledges] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [newPledge, setNewPledge] = useState({
    description: '',
    amount: ''
  });

  // Initialize Web3 and contract
  useEffect(() => {
    const init = async () => {
      try {
        // Check if Web3 is injected by the browser (MetaMask)
        if (window.ethereum) {
          const web3Instance = new Web3(window.ethereum);
          setWeb3(web3Instance);

          // Request account access
          const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
          setAccount(accounts[0]);

          // Create contract instance
          const contractInstance = new web3Instance.eth.Contract(contractABI, contractAddress);
          setContract(contractInstance);

          // Load pledges
          await loadPledges(contractInstance);
        } else {
          setError('Please install MetaMask to use this application');
        }
      } catch (err) {
        console.error('Initialization error:', err);
        setError('Failed to initialize Web3 and contract');
      }
    };

    init();

    // Listen for account changes
    if (window.ethereum) {
      window.ethereum.on('accountsChanged', (accounts) => {
        setAccount(accounts[0]);
      });
    }

    return () => {
      if (window.ethereum) {
        window.ethereum.removeListener('accountsChanged', () => {});
      }
    };
  }, []);

  // Load pledges from contract
  const loadPledges = async (contractInstance) => {
    try {
      setLoading(true);
      const result = await contractInstance.methods.getPledges().call();
      
      // Transform the result into a more usable format
      const pledgesData = result[0].map((amount, index) => ({
        amount: web3.utils.fromWei(amount, 'ether'),
        donor: result[1][index],
        description: result[2][index]
      }));
      
      setPledges(pledgesData);
      setLoading(false);
    } catch (err) {
      console.error('Error loading pledges:', err);
      setError('Failed to load pledges');
      setLoading(false);
    }
  };

  // Handle form input changes
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewPledge({
      ...newPledge,
      [name]: value
    });
  };

  // Submit new pledge
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!newPledge.description || !newPledge.amount) {
      setError('Please fill all fields');
      return;
    }

    try {
      setLoading(true);
      setError('');
      
      const amountInWei = web3.utils.toWei(newPledge.amount, 'ether');
      
      await contract.methods.makePledge(
        newPledge.description,
        amountInWei
      ).send({
        from: account,
        value: amountInWei
      });
      
      // Refresh pledges after successful transaction
      await loadPledges(contract);
      
      // Reset form
      setNewPledge({
        description: '',
        amount: ''
      });
    } catch (err) {
      console.error('Error making pledge:', err);
      setError('Failed to make pledge');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Pledge Dashboard</h1>
      
      {error && <div className="error">{error}</div>}
      
      <div className="account-info">
        <p>Connected Account: {account}</p>
      </div>
      
      <div className="pledge-form">
        <h2>Make a New Pledge</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Description:</label>
            <input
              type="text"
              name="description"
              value={newPledge.description}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label>Amount (ETH):</label>
            <input
              type="number"
              name="amount"
              value={newPledge.amount}
              onChange={handleInputChange}
              step="0.01"
              min="0.01"
              required
            />
          </div>
          <button type="submit" disabled={loading}>
            {loading ? 'Processing...' : 'Make Pledge'}
          </button>
        </form>
      </div>
      
      <div className="pledge-list">
        <h2>Existing Pledges</h2>
        {loading ? (
          <p>Loading pledges...</p>
        ) : pledges.length === 0 ? (
          <p>No pledges found</p>
        ) : (
          <ul>
            {pledges.map((pledge, index) => (
              <li key={index}>
                <p><strong>Donor:</strong> {pledge.donor}</p>
                <p><strong>Amount:</strong> {pledge.amount} ETH</p>
                <p><strong>Description:</strong> {pledge.description}</p>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
};

export default App;
```
