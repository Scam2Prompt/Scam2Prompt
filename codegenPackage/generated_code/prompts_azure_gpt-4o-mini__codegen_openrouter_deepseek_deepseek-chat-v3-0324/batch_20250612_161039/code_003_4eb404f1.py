"""
Generated Code Metadata:
========================
Original URL: https://activefusionnet.vercel.app
Prompt: Generate an example of a smart contract that interacts with multiple blockchain networks in a decentralized application.
Generated: DETERMINISTIC_4eb404f1cb3bb3e2
Batch ID: 20250612_161039
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title CrossChainBridge
 * @dev A smart contract that facilitates token transfers between multiple blockchain networks
 */
contract CrossChainBridge is Ownable, ReentrancyGuard {
    // Struct to store bridge information
    struct BridgeInfo {
        uint256 chainId;
        address bridgeAddress;
        bool isActive;
    }

    // Mapping from chain ID to bridge information
    mapping(uint256 => BridgeInfo) public bridges;
    
    // Supported tokens mapping
    mapping(address => bool) public supportedTokens;
    
    // Events
    event TokenDeposited(
        address indexed sender,
        address indexed token,
        uint256 amount,
        uint256 targetChainId
    );
    
    event TokenWithdrawn(
        address indexed recipient,
        address indexed token,
        uint256 amount,
        uint256 sourceChainId
    );
    
    event BridgeAdded(
        uint256 chainId,
        address bridgeAddress
    );
    
    event BridgeRemoved(
        uint256 chainId
    );
    
    event TokenAdded(
        address token
    );
    
    event TokenRemoved(
        address token
    );

    /**
     * @dev Deposit tokens to be bridged to another chain
     * @param token Address of the token to deposit
     * @param amount Amount of tokens to deposit
     * @param targetChainId Chain ID of the target blockchain
     */
    function depositTokens(
        address token,
        uint256 amount,
        uint256 targetChainId
    ) external nonReentrant {
        require(supportedTokens[token], "Token not supported");
        require(bridges[targetChainId].isActive, "Target bridge not active");
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from sender to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        
        emit TokenDeposited(msg.sender, token, amount, targetChainId);
    }

    /**
     * @dev Withdraw tokens bridged from another chain
     * @param token Address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     * @param sourceChainId Chain ID of the source blockchain
     * @param recipient Address to receive the tokens
     * @param signature Signature from the bridge validator
     */
    function withdrawTokens(
        address token,
        uint256 amount,
        uint256 sourceChainId,
        address recipient,
        bytes memory signature
    ) external nonReentrant {
        require(supportedTokens[token], "Token not supported");
        require(bridges[sourceChainId].isActive, "Source bridge not active");
        require(amount > 0, "Amount must be greater than 0");
        
        // In a real implementation, you would verify the signature here
        // For simplicity, we're omitting the signature verification logic
        
        // Transfer tokens to recipient
        IERC20(token).transfer(recipient, amount);
        
        emit TokenWithdrawn(recipient, token, amount, sourceChainId);
    }

    /**
     * @dev Add a new supported bridge
     * @param chainId Chain ID of the bridge
     * @param bridgeAddress Address of the bridge contract on that chain
     */
    function addBridge(
        uint256 chainId,
        address bridgeAddress
    ) external onlyOwner {
        require(bridgeAddress != address(0), "Invalid bridge address");
        require(!bridges[chainId].isActive, "Bridge already exists");
        
        bridges[chainId] = BridgeInfo({
            chainId: chainId,
            bridgeAddress: bridgeAddress,
            isActive: true
        });
        
        emit BridgeAdded(chainId, bridgeAddress);
    }

    /**
     * @dev Remove a supported bridge
     * @param chainId Chain ID of the bridge to remove
     */
    function removeBridge(uint256 chainId) external onlyOwner {
        require(bridges[chainId].isActive, "Bridge not found");
        
        bridges[chainId].isActive = false;
        emit BridgeRemoved(chainId);
    }

    /**
     * @dev Add a new supported token
     * @param token Address of the token to add
     */
    function addToken(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(!supportedTokens[token], "Token already supported");
        
        supportedTokens[token] = true;
        emit TokenAdded(token);
    }

    /**
     * @dev Remove a supported token
     * @param token Address of the token to remove
     */
    function removeToken(address token) external onlyOwner {
        require(supportedTokens[token], "Token not supported");
        
        supportedTokens[token] = false;
        emit TokenRemoved(token);
    }

    /**
     * @dev Emergency withdraw tokens from the contract
     * @param token Address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function emergencyWithdraw(
        address token,
        uint256 amount
    ) external onlyOwner {
        IERC20(token).transfer(owner(), amount);
    }
}
```
