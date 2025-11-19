"""
Generated Code Metadata:
========================
Original URL: https://multismartsolvehub.pages.dev
Prompt: Develop a token bridge solution for seamless transfers between different blockchain networks using Solidity.
Generated: DETERMINISTIC_fbf94f99085ee947
Batch ID: 20250622_211646
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// TokenBridge contract for transferring tokens between different blockchain networks
contract TokenBridge is Ownable {
    // Event emitted when tokens are locked
    event TokensLocked(address indexed token, address indexed sender, uint256 amount, string destinationChain, address destinationAddress);
    
    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed token, address indexed receiver, uint256 amount);

    // Mapping to track locked tokens
    mapping(bytes32 => bool) public lockedTokens;

    // Function to lock tokens for transfer to another blockchain
    function lockTokens(address token, uint256 amount, string memory destinationChain, address destinationAddress) external {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(IERC20(token).allowance(msg.sender, address(this)) >= amount, "Token allowance not sufficient");
        
        // Create a unique identifier for the lock operation
        bytes32 lockId = keccak256(abi.encodePacked(token, msg.sender, amount, destinationChain, destinationAddress));
        require(!lockedTokens[lockId], "Tokens already locked for this operation");

        // Lock the tokens by transferring them to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        
        // Mark the tokens as locked
        lockedTokens[lockId] = true;

        // Emit the TokensLocked event
        emit TokensLocked(token, msg.sender, amount, destinationChain, destinationAddress);
    }

    // Function to unlock tokens on the destination blockchain
    function unlockTokens(address token, address receiver, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Unlock the tokens by transferring them to the receiver
        IERC20(token).transfer(receiver, amount);
        
        // Emit the TokensUnlocked event
        emit TokensUnlocked(token, receiver, amount);
    }

    // Function to withdraw tokens from the contract (for emergency purposes)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient contract balance");
        
        // Transfer the tokens to the owner
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
