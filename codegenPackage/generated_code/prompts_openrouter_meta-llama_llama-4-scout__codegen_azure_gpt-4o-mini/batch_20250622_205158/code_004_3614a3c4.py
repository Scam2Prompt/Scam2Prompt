"""
Generated Code Metadata:
========================
Original URL: https://fuel-dapp-implement.vercel.app
Prompt: "Create a basic Fuel dApp with a Sway contract and a TypeScript frontend using the provided template."
Generated: DETERMINISTIC_3614a3c402497526
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sway
// Fuel dApp Sway Contract

contract FuelDApp {
    // Struct to represent a fuel transaction
    struct FuelTransaction {
        address user;
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping to store user fuel transactions
    mapping(address => FuelTransaction[]) private transactions;

    // Event emitted when a new fuel transaction is created
    event FuelTransactionCreated(address indexed user, uint256 amount, uint256 timestamp);

    // Function to create a new fuel transaction
    public fun createTransaction(amount: u64) {
        // Ensure the amount is greater than zero
        assert(amount > 0, "Transaction amount must be greater than zero.");

        // Create a new transaction
        let transaction = FuelTransaction {
            user: msg.sender,
            amount: amount,
            timestamp: block.timestamp,
        };

        // Store the transaction in the mapping
        transactions[msg.sender].push(transaction);

        // Emit the transaction created event
        emit FuelTransactionCreated(msg.sender, amount, block.timestamp);
    }

    // Function to retrieve all transactions for a user
    public fun getTransactions(user: address): FuelTransaction[] {
        return transactions[user];
    }
}
```

```typescript
// TypeScript Frontend for Fuel dApp

import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import FuelDApp from './FuelDApp.json'; // Import the compiled contract ABI

const contractAddress = 'YOUR_CONTRACT_ADDRESS_HERE';

const App: React.FC = () => {
    const [amount, setAmount] = useState<number>(0);
    const [transactions, setTransactions] = useState<any[]>([]);
    const [provider, setProvider] = useState<ethers.providers.Web3Provider | null>(null);
    const [contract, setContract] = useState<ethers.Contract | null>(null);

    useEffect(() => {
        // Initialize Ethereum provider
        const initProvider = async () => {
            const provider = new ethers.providers.Web3Provider(window.ethereum);
            setProvider(provider);
            const signer = provider.getSigner();
            const contract = new ethers.Contract(contractAddress, FuelDApp.abi, signer);
            setContract(contract);
        };
        initProvider();
    }, []);

    const handleTransaction = async () => {
        if (!contract) return;

        try {
            const tx = await contract.createTransaction(ethers.utils.parseUnits(amount.toString(), 'wei'));
            await tx.wait();
            alert('Transaction successful!');
            fetchTransactions();
        } catch (error) {
            console.error('Transaction failed:', error);
            alert('Transaction failed. Please try again.');
        }
    };

    const fetchTransactions = async () => {
        if (!contract) return;

        try {
            const userTransactions = await contract.getTransactions(await provider?.getSigner().getAddress());
            setTransactions(userTransactions);
        } catch (error) {
            console.error('Failed to fetch transactions:', error);
        }
    };

    return (
        <div>
            <h1>Fuel dApp</h1>
            <input
                type="number"
                value={amount}
                onChange={(e) => setAmount(Number(e.target.value))}
                placeholder="Enter fuel amount"
            />
            <button onClick={handleTransaction}>Create Transaction</button>
            <h2>Your Transactions</h2>
            <ul>
                {transactions.map((tx, index) => (
                    <li key={index}>
                        Amount: {ethers.utils.formatUnits(tx.amount, 'wei')} | Timestamp: {new Date(tx.timestamp * 1000).toLocaleString()}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default App;
```

Make sure to replace `YOUR_CONTRACT_ADDRESS_HERE` with the actual deployed contract address.
