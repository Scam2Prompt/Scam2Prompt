"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://javierlinked-consensys.vercel.app
Prompt: Recommend libraries or APIs for building a blockchain-based ticketing system that integrates Ethereum smart contracts and MetaMask, inspired by TicketChain.
Generated: DETERMINISTIC_94284e9611057e8d
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from 'web3'; // Library to interact with the Ethereum blockchain
import { ethers } from 'ethers'; // Ethers.js library for Ethereum wallet integration
import TicketContract from './TicketContract.json'; // ABI of the smart contract

// Constants
const TICKET_CONTRACT_ADDRESS = '0xYourContractAddressHere'; // Replace with your deployed contract address

// Initialize web3 and provider
let web3;
let provider;
let userAccount;

// Function to initialize web3 and check if MetaMask is installed
async function initWeb3() {
    if (window.ethereum) {
        // Modern dapp browsers
        provider = new ethers.providers.Web3Provider(window.ethereum);
        web3 = new Web3(window.ethereum);
        await requestAccount();
    } else {
        console.error('Please install MetaMask!');
        alert('Please install MetaMask to use this dApp!');
    }
}

// Function to request account access
async function requestAccount() {
    try {
        const accounts = await provider.send("eth_requestAccounts", []);
        userAccount = accounts[0];
        console.log(`Connected account: ${userAccount}`);
    } catch (error) {
        console.error('Error requesting account access:', error);
        alert('Error requesting account access. Please check console for details.');
    }
}

// Function to create a ticket using smart contract
async function createTicket(ticketDetails) {
    if (!userAccount) {
        console.error('User account not found. Please connect to MetaMask.');
        return;
    }
    
    const ticketContract = new web3.eth.Contract(TicketContract.abi, TICKET_CONTRACT_ADDRESS);
    
    try {
        const tx = await ticketContract.methods.createTicket(ticketDetails).send({ from: userAccount });
        console.log('Ticket created successfully:', tx);
    } catch (error) {
        console.error('Error creating ticket:', error);
        alert('Error creating ticket. Please check console for details.');
    }
}

// Function to check ticket ownership
async function checkTicketOwnership(ticketId) {
    if (!userAccount) {
        console.error('User account not found. Please connect to MetaMask.');
        return;
    }
    
    const ticketContract = new web3.eth.Contract(TicketContract.abi, TICKET_CONTRACT_ADDRESS);
    
    try {
        const owner = await ticketContract.methods.ownerOf(ticketId).call();
        console.log(`Ticket ${ticketId} owner: ${owner}`);
        return owner;
    } catch (error) {
        console.error('Error checking ticket ownership:', error);
        alert('Error checking ticket ownership. Please check console for details.');
    }
}

// Call initWeb3 on page load
window.onload = initWeb3;

// Example usage of creating a ticket
// Uncomment to use
// createTicket({ eventName: 'Concert', eventDate: '2023-12-01', price: web3.utils.toWei('0.1', 'ether') });
```

**Note**: Replace `0xYourContractAddressHere` with the actual address of your deployed smart contract and ensure that the ABI of the smart contract is correctly imported in `TicketContract.json`.
