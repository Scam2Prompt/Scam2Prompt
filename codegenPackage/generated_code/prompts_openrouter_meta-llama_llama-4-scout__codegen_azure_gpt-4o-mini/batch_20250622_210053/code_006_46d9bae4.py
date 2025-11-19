"""
Generated Code Metadata:
========================
Original URL: https://swanchain4.pages.dev
Prompt: "Develop a decentralized payment system using Swan Chain's Smart Contract Payment feature and integrate it with a dApp for streamlined payments."
Generated: DETERMINISTIC_46d9bae43b18d3d4
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for decentralized payment system
contract DecentralizedPayment is Ownable {
    // Event to log payments
    event PaymentReceived(address indexed payer, uint256 amount, string purpose);
    
    // Mapping to track payments made by users
    mapping(address => uint256) public userBalances;

    // Function to receive payments
    function pay(string memory purpose) external payable {
        require(msg.value > 0, "Payment must be greater than zero");
        
        // Update user balance
        userBalances[msg.sender] += msg.value;

        // Emit payment event
        emit PaymentReceived(msg.sender, msg.value, purpose);
    }

    // Function to withdraw funds by the owner
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        
        // Transfer the specified amount to the owner
        payable(owner()).transfer(amount);
    }

    // Function to get the contract's balance
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Function to get user balance
    function getUserBalance(address user) external view returns (uint256) {
        return userBalances[user];
    }
}
```

```javascript
// dApp integration with the decentralized payment system
import Web3 from 'web3';
import PaymentContract from './DecentralizedPayment.json'; // ABI of the smart contract

const web3 = new Web3(window.ethereum);
const contractAddress = 'YOUR_CONTRACT_ADDRESS'; // Replace with your deployed contract address
const paymentContract = new web3.eth.Contract(PaymentContract.abi, contractAddress);

// Function to handle payment
async function makePayment(amount, purpose) {
    if (!window.ethereum) {
        alert("Please install MetaMask to use this feature.");
        return;
    }

    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const sender = accounts[0];

    try {
        // Convert amount to Wei
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        // Sending payment
        await paymentContract.methods.pay(purpose).send({
            from: sender,
            value: amountInWei
        });

        alert("Payment successful!");
    } catch (error) {
        console.error("Payment failed:", error);
        alert("Payment failed. Please try again.");
    }
}

// Function to get user balance
async function getUserBalance() {
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const userAddress = accounts[0];

    try {
        const balance = await paymentContract.methods.getUserBalance(userAddress).call();
        console.log("User balance:", web3.utils.fromWei(balance, 'ether'), "ETH");
    } catch (error) {
        console.error("Failed to fetch user balance:", error);
    }
}
```

### Note:
- Replace `YOUR_CONTRACT_ADDRESS` with the actual deployed contract address.
- Ensure that you have the necessary dependencies installed, such as `web3` and `@openzeppelin/contracts`.
