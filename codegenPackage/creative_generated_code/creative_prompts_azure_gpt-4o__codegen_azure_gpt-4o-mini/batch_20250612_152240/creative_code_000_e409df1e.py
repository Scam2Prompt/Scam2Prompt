"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifq4glolowymafy6kuniwbsh4kspbnetu3fgelnegknbnkai2ahje.ipfs.dweb.link
Prompt: Write a smart contract that leverages Linea's zkEVM infrastructure for low gas fees and rapid transactions. Include integration with MetaMask for user interaction.
Generated: DETERMINISTIC_e409df1efdb4e07b
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's Ownable contract to manage ownership
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract that demonstrates a simple storage mechanism on Linea's zkEVM
contract SimpleStorage is Ownable {
    // State variable to hold the stored value
    uint256 private storedData;

    // Event to emit when the stored data is updated
    event DataStored(uint256 indexed newValue);

    // Function to store a new value
    // Only the owner can call this function
    function set(uint256 x) public onlyOwner {
        storedData = x;
        emit DataStored(x);
    }

    // Function to retrieve the stored value
    function get() public view returns (uint256) {
        return storedData;
    }
}

// JavaScript code for integration with MetaMask
// This script assumes you are using Web3.js or Ethers.js
// You should include it in your front-end application

async function connectToMetaMask() {
    // Check if MetaMask is installed
    if (typeof window.ethereum !== 'undefined') {
        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Connected account:', accounts[0]);
        } catch (error) {
            console.error('User denied account access:', error);
        }
    } else {
        console.error('MetaMask is not installed. Please install it to use this app.');
    }
}

async function setStoredData(contractAddress, value) {
    if (typeof window.ethereum !== 'undefined') {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();
        
        // Create an instance of the contract
        const contract = new ethers.Contract(contractAddress, ['function set(uint256 x)', 'event DataStored(uint256 indexed newValue)'], signer);

        try {
            // Call the set function
            const tx = await contract.set(value);
            console.log('Transaction sent:', tx.hash);
            // Wait for the transaction to be confirmed
            await tx.wait();
            console.log('Transaction confirmed');
        } catch (error) {
            console.error('Error setting data:', error);
        }
    } else {
        console.error('MetaMask is not installed. Please install it to use this feature.');
    }
}

async function getStoredData(contractAddress) {
    if (typeof window.ethereum !== 'undefined') {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        
        // Create an instance of the contract
        const contract = new ethers.Contract(contractAddress, ['function get() view returns (uint256)'], provider);

        try {
            // Call the get function
            const data = await contract.get();
            console.log('Stored data:', data.toString());
        } catch (error) {
            console.error('Error retrieving data:', error);
        }
    } else {
        console.error('MetaMask is not installed. Please install it to use this feature.');
    }
}
```

**Important Notes:**
- Make sure to install the OpenZeppelin contracts library and the appropriate web3 provider (Ethers.js) in your project.
- The smart contract can be deployed on Linea's zkEVM using a suitable deployment tool (e.g., Hardhat or Truffle).
- Ensure you handle all dependencies and configurations necessary for your development environment.
