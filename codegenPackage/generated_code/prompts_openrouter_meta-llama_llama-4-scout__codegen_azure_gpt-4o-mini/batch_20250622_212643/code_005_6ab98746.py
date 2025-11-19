"""
Generated Code Metadata:
========================
Original URL: https://spark.fiddler-pkg.com
Prompt: "Design a simple decentralized application (dApp) that utilizes Spark's lending and borrowing features, with a focus on user interface and user experience."
Generated: DETERMINISTIC_6ab987461fb6a8d3
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { Contract } from 'ethers';
import LendingContract from './LendingContract.json'; // ABI for the lending contract

// Define constants
const CONTRACT_ADDRESS = '0xYourContractAddress'; // Replace with your contract address

// Main App component
const App = () => {
    const [account, setAccount] = useState('');
    const [web3, setWeb3] = useState(null);
    const [contract, setContract] = useState(null);
    const [amount, setAmount] = useState('');
    const [action, setAction] = useState('lend'); // 'lend' or 'borrow'
    const [message, setMessage] = useState('');

    // Initialize Web3 and contract
    useEffect(() => {
        const initWeb3 = async () => {
            try {
                // Check if MetaMask is installed
                if (window.ethereum) {
                    const web3Instance = new Web3(window.ethereum);
                    await window.ethereum.request({ method: 'eth_requestAccounts' });
                    const accounts = await web3Instance.eth.getAccounts();
                    setAccount(accounts[0]);
                    setWeb3(web3Instance);
                    const lendingContract = new Contract(CONTRACT_ADDRESS, LendingContract.abi, web3Instance);
                    setContract(lendingContract);
                } else {
                    setMessage('Please install MetaMask to use this dApp.');
                }
            } catch (error) {
                console.error('Error initializing Web3:', error);
                setMessage('Failed to connect to Web3. Please try again.');
            }
        };
        initWeb3();
    }, []);

    // Handle lending and borrowing actions
    const handleAction = async () => {
        if (!amount || isNaN(amount) || amount <= 0) {
            setMessage('Please enter a valid amount.');
            return;
        }

        try {
            setMessage('Processing...');

            if (action === 'lend') {
                // Call lend function from the contract
                const tx = await contract.lend(web3.utils.toWei(amount, 'ether'), { from: account });
                await tx.wait();
                setMessage('Lending successful!');
            } else if (action === 'borrow') {
                // Call borrow function from the contract
                const tx = await contract.borrow(web3.utils.toWei(amount, 'ether'), { from: account });
                await tx.wait();
                setMessage('Borrowing successful!');
            }
        } catch (error) {
            console.error('Error during transaction:', error);
            setMessage('Transaction failed. Please try again.');
        }
    };

    return (
        <div style={{ padding: '20px' }}>
            <h1>Decentralized Lending and Borrowing dApp</h1>
            <p>Connected Account: {account}</p>
            <input
                type="number"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                placeholder="Enter amount in ETH"
                style={{ marginRight: '10px' }}
            />
            <select value={action} onChange={(e) => setAction(e.target.value)} style={{ marginRight: '10px' }}>
                <option value="lend">Lend</option>
                <option value="borrow">Borrow</option>
            </select>
            <button onClick={handleAction}>Submit</button>
            {message && <p>{message}</p>}
        </div>
    );
};

export default App;
```

### Notes:
- Ensure you have the necessary dependencies installed, such as `react`, `web3`, and `ethers`.
- Replace `0xYourContractAddress` with the actual deployed contract address.
- The `LendingContract.json` should contain the ABI of your smart contract.
- This code assumes that the lending and borrowing functions are implemented in the smart contract.
