"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://muzikoin.pages.dev
Prompt: Create a decentralized application (dApp) that allows users to buy MuziKoin tokens and supports KYC verification as described on the MuziKoin platform.
Generated: DETERMINISTIC_3edab0e7512bc9ab
Batch ID: 20250612_163948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin contracts for ERC20 token and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MuziKoin is ERC20, Ownable {
    // KYC storage for users
    mapping(address => bool) public kycVerified;

    // Event to log KYC verification
    event KYCVerified(address indexed user);

    // Constructor to mint initial supply of MuziKoin tokens
    constructor(uint256 initialSupply) ERC20("MuziKoin", "MZK") {
        _mint(msg.sender, initialSupply);
    }

    // Function to verify KYC for a user
    function verifyKYC(address user) external onlyOwner {
        require(!kycVerified[user], "User already verified");
        kycVerified[user] = true;
        emit KYCVerified(user);
    }

    // Function to buy MuziKoin tokens
    function buyTokens() external payable {
        // Ensure KYC is verified
        require(kycVerified[msg.sender], "KYC verification required");

        // Require non-zero Ether value
        require(msg.value > 0, "Ether value must be greater than zero");

        // Set token price (e.g., 1 MZK = 0.001 ETH)
        uint256 tokenPrice = 0.001 ether;

        // Calculate the number of tokens to purchase
        uint256 tokensToBuy = msg.value / tokenPrice;

        // Ensure the contract has enough tokens
        require(balanceOf(owner()) >= tokensToBuy, "Not enough tokens available");

        // Transfer tokens to the buyer
        _transfer(owner(), msg.sender, tokensToBuy);
    }

    // Function to withdraw Ether from the contract
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {
        // This function allows the contract to receive Ether directly
    }
}
```

```javascript
// Frontend code (e.g., using React.js)

import React, { useState } from 'react';
import Web3 from 'web3';
import MuziKoinContract from './MuziKoin.json'; // ABI and contract address

const App = () => {
    const [account, setAccount] = useState('');
    const [web3, setWeb3] = useState(null);
    const [contract, setContract] = useState(null);
    const [isKYCVerified, setIsKYCVerified] = useState(false);

    // Initialize Web3 and contract instance
    const initWeb3 = async () => {
        if (window.ethereum) {
            const web3Instance = new Web3(window.ethereum);
            const accounts = await web3Instance.eth.requestAccounts();
            const contractInstance = new web3Instance.eth.Contract(
                MuziKoinContract.abi,
                MuziKoinContract.networks[5777].address // Replace with your network ID
            );

            setWeb3(web3Instance);
            setAccount(accounts[0]);
            setContract(contractInstance);
        } else {
            alert('Please install MetaMask!');
        }
    };

    // Function to verify KYC
    const verifyKYC = async () => {
        try {
            await contract.methods.verifyKYC(account).send({ from: account });
            setIsKYCVerified(true);
            alert('KYC verified successfully!');
        } catch (error) {
            console.error("Error verifying KYC:", error);
            alert('KYC verification failed. Please try again.');
        }
    };

    // Function to buy tokens
    const buyTokens = async (amount) => {
        try {
            const tokenPrice = Web3.utils.toWei('0.001', 'ether');
            const totalCost = tokenPrice * amount;

            await contract.methods.buyTokens().send({
                from: account,
                value: totalCost
            });
            alert(`${amount} MuziKoin purchased successfully!`);
        } catch (error) {
            console.error("Error buying tokens:", error);
            alert('Token purchase failed. Please ensure KYC is verified and try again.');
        }
    };

    // Call initWeb3 on component mount
    React.useEffect(() => {
        initWeb3();
    }, []);

    return (
        <div>
            <h1>Welcome to MuziKoin dApp</h1>
            <p>Your account: {account}</p>
            <button onClick={verifyKYC}>Verify KYC</button>
            {isKYCVerified && (
                <div>
                    <button onClick={() => buyTokens(1)}>Buy 1 MuziKoin</button>
                </div>
            )}
        </div>
    );
};

export default App;
```

This code represents a simple decentralized application (dApp) for buying MuziKoin tokens while supporting KYC verification. The smart contract is written in Solidity and the frontend in React.js. Make sure to adapt the contract address and network ID in the frontend code based on your specific deployment.
