"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonic-labs.vercel.app
Prompt: Write a smart contract that interacts with Sonic's native bridge to securely transfer assets between Ethereum and Sonic. Include security measures and best practices.
Generated: DETERMINISTIC_cbfcab98be7403e8
Batch ID: 20250612_145917
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

// Import necessary interfaces for ERC20 tokens and bridge interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SonicBridge
 * @dev A smart contract for safely transferring assets between Ethereum and Sonic using a bridge.
 */
contract SonicBridge is Ownable {
    // Event emitted when tokens are locked for bridging
    event TokensLocked(address indexed user, address indexed token, uint256 amount, uint256 indexed bridgeId);
    
    // Event emitted when tokens are released after bridging
    event TokensReleased(address indexed user, address indexed token, uint256 amount, uint256 indexed bridgeId);
    
    // Mapping to track which tokens are allowed for bridging
    mapping(address => bool) public allowedTokens;

    // Function to allow specific tokens to be bridged
    function allowToken(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        allowedTokens[token] = true;
    }

    // Function to disallow specific tokens from being bridged
    function disallowToken(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        allowedTokens[token] = false;
    }

    /**
     * @dev Locks tokens in this contract for bridging to Sonic.
     * @param token The address of the token to lock.
     * @param amount The amount of tokens to lock.
     * @param bridgeId The identifier for the bridge operation.
     */
    function lockTokens(address token, uint256 amount, uint256 bridgeId) external {
        require(allowedTokens[token], "Token not allowed for bridging");
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from the user to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        
        // Emit event for locking of tokens
        emit TokensLocked(msg.sender, token, amount, bridgeId);
    }

    /**
     * @dev Releases tokens back to the user after bridging from Sonic.
     * @param token The address of the token to release.
     * @param amount The amount of tokens to release.
     * @param bridgeId The identifier for the bridge operation.
     */
    function releaseTokens(address token, uint256 amount, uint256 bridgeId) external onlyOwner {
        require(allowedTokens[token], "Token not allowed for bridging");
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from this contract to the user
        IERC20(token).transfer(msg.sender, amount);
        
        // Emit event for releasing of tokens
        emit TokensReleased(msg.sender, token, amount, bridgeId);
    }
    
    /**
     * @dev Withdraws tokens from the contract in case of an emergency.
     * @param token The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");
        
        // Transfer tokens back to the owner
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
