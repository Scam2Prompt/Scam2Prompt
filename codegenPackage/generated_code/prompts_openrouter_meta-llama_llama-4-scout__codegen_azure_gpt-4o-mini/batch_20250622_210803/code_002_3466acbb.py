"""
Generated Code Metadata:
========================
Original URL: https://portal-bridge.pages.dev
Prompt: Generate a smart contract code for a token bridge that supports advanced tools for transaction management, similar to Portal Bridge.
Generated: DETERMINISTIC_3466acbbbaf036e3
Batch ID: 20250622_210803
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract TokenBridge is Ownable {
    using SafeMath for uint256;

    // Event emitted when tokens are bridged
    event TokensBridged(address indexed sender, address indexed token, uint256 amount, string destinationChain);
    
    // Event emitted when tokens are released on the destination chain
    event TokensReleased(address indexed recipient, address indexed token, uint256 amount);

    // Mapping to track bridged tokens
    mapping(address => bool) public supportedTokens;

    // Modifier to check if the token is supported
    modifier onlySupportedToken(address token) {
        require(supportedTokens[token], "TokenBridge: Token not supported");
        _;
    }

    // Function to add a supported token
    function addSupportedToken(address token) external onlyOwner {
        require(token != address(0), "TokenBridge: Invalid token address");
        supportedTokens[token] = true;
    }

    // Function to remove a supported token
    function removeSupportedToken(address token) external onlyOwner {
        require(supportedTokens[token], "TokenBridge: Token not supported");
        supportedTokens[token] = false;
    }

    // Function to bridge tokens to another chain
    function bridgeTokens(address token, uint256 amount, string calldata destinationChain) external onlySupportedToken(token) {
        require(amount > 0, "TokenBridge: Amount must be greater than zero");
        
        // Transfer tokens from the sender to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        
        // Emit event for bridging tokens
        emit TokensBridged(msg.sender, token, amount, destinationChain);
    }

    // Function to release tokens on the destination chain
    function releaseTokens(address recipient, address token, uint256 amount) external onlyOwner onlySupportedToken(token) {
        require(amount > 0, "TokenBridge: Amount must be greater than zero");
        
        // Transfer tokens from the contract to the recipient
        IERC20(token).transfer(recipient, amount);
        
        // Emit event for releasing tokens
        emit TokensReleased(recipient, token, amount);
    }

    // Function to withdraw tokens from the contract (for emergency purposes)
    function withdrawTokens(address token, uint256 amount) external onlyOwner onlySupportedToken(token) {
        require(amount > 0, "TokenBridge: Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "TokenBridge: Insufficient balance");

        // Transfer tokens to the owner
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to check the balance of a specific token in the contract
    function getTokenBalance(address token) external view onlySupportedToken(token) returns (uint256) {
        return IERC20(token).balanceOf(address(this));
    }
}
```
