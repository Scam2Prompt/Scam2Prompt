"""
Generated Code Metadata:
========================
Original URL: https://usdcoinmixer.com
Prompt: Implement a basic example of a USDC mixer service using a smart contract on a blockchain platform like Ethereum.
Generated: DETERMINISTIC_91b7013a938f6f7f
Batch ID: 20250622_211918
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract USDCMixer is Ownable {
    // Event emitted when funds are mixed
    event Mixed(address indexed user, uint256 amount, uint256 timestamp);

    // Mapping to track user deposits
    mapping(address => uint256) private userBalances;

    // The USDC token contract address
    IERC20 public usdcToken;

    // Constructor to set the USDC token address
    constructor(address _usdcTokenAddress) {
        require(_usdcTokenAddress != address(0), "Invalid USDC token address");
        usdcToken = IERC20(_usdcTokenAddress);
    }

    // Function to deposit USDC into the mixer
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer USDC from the user to this contract
        bool success = usdcToken.transferFrom(msg.sender, address(this), amount);
        require(success, "USDC transfer failed");

        // Update user balance
        userBalances[msg.sender] += amount;

        // Emit event for the deposit
        emit Mixed(msg.sender, amount, block.timestamp);
    }

    // Function to withdraw mixed USDC (for demonstration purposes, this just returns the user's balance)
    function withdraw() external {
        uint256 amount = userBalances[msg.sender];
        require(amount > 0, "No funds to withdraw");

        // Reset user balance before transfer to prevent re-entrancy attacks
        userBalances[msg.sender] = 0;

        // Transfer USDC back to the user
        bool success = usdcToken.transfer(msg.sender, amount);
        require(success, "USDC transfer failed");
    }

    // Function to check user balance
    function getUserBalance() external view returns (uint256) {
        return userBalances[msg.sender];
    }

    // Function to withdraw contract's USDC balance (only owner)
    function withdrawContractBalance() external onlyOwner {
        uint256 contractBalance = usdcToken.balanceOf(address(this));
        require(contractBalance > 0, "No USDC balance in contract");

        // Transfer USDC to the owner
        bool success = usdcToken.transfer(owner(), contractBalance);
        require(success, "USDC transfer failed");
    }
}
```
