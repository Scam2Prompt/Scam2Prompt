"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-token-bridge-6l0svbyos-offchain-labs.vercel.app
Prompt: Develop a smart contract example for bridging tokens using the Arbitrum Token Bridge, ensuring compliance with recent security updates.
Generated: DETERMINISTIC_27e4c8f275c95643
Batch ID: 20250612_150440
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenBridge is Ownable {
    // Event emitted when tokens are bridged
    event TokensBridged(address indexed user, uint256 amount, string destinationChain);

    // Mapping to store token balances for users
    mapping(address => uint256) public balances;

    // Address of the ERC20 token to be bridged
    IERC20 public token;

    // Constructor to initialize the contract with the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        token = IERC20(_tokenAddress);
    }

    // Function to deposit tokens for bridging
    function depositTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from user to this contract
        bool success = token.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update user balance
        balances[msg.sender] += amount;

        // Emit event for token bridge
        emit TokensBridged(msg.sender, amount, "Arbitrum");
    }

    // Function to withdraw tokens after bridging
    function withdrawTokens(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance before transferring
        balances[msg.sender] -= amount;

        // Transfer tokens back to the user
        bool success = token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    // Function to check user balance
    function checkBalance() external view returns (uint256) {
        return balances[msg.sender];
    }

    // Function to recover ERC20 tokens accidentally sent to this contract
    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
