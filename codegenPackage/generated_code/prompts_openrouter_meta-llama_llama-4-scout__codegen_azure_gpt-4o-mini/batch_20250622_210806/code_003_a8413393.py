"""
Generated Code Metadata:
========================
Original URL: https://vlaunch-bridge.pages.dev
Prompt: "Design a basic smart contract in Solidity for bridging tokens like VPAD between Ethereum and Binance Smart Chain."
Generated: DETERMINISTIC_a8413393c7a77e5b
Batch ID: 20250622_210806
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Bridge contract for token transfer between Ethereum and Binance Smart Chain
contract TokenBridge is Ownable {
    // Event emitted when tokens are locked
    event TokensLocked(address indexed user, uint256 amount, string destinationChain);
    
    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed user, uint256 amount, string sourceChain);

    // Mapping to track locked tokens
    mapping(address => uint256) public lockedTokens;

    // The token being bridged
    IERC20 public token;

    // Constructor to initialize the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    // Function to lock tokens for bridging
    function lockTokens(uint256 amount, string calldata destinationChain) external {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to the bridge contract
        token.transferFrom(msg.sender, address(this), amount);
        
        // Update the locked tokens mapping
        lockedTokens[msg.sender] += amount;

        // Emit the TokensLocked event
        emit TokensLocked(msg.sender, amount, destinationChain);
    }

    // Function to unlock tokens on the source chain
    function unlockTokens(address user, uint256 amount, string calldata sourceChain) external onlyOwner {
        require(lockedTokens[user] >= amount, "Insufficient locked tokens");

        // Update the locked tokens mapping
        lockedTokens[user] -= amount;

        // Transfer tokens back to the user
        token.transfer(user, amount);

        // Emit the TokensUnlocked event
        emit TokensUnlocked(user, amount, sourceChain);
    }

    // Function to check the locked token balance of a user
    function getLockedTokens(address user) external view returns (uint256) {
        return lockedTokens[user];
    }

    // Function to withdraw tokens in case of emergency
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        token.transfer(owner(), amount);
    }
}
```
