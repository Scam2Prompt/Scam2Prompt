"""
Generated Code Metadata:
========================
Original URL: https://blockdappresolve.firebaseapp.com
Prompt: Design a token bridge solution using Solidity, enabling seamless transfers and interoperability between different blockchain networks.
Generated: DETERMINISTIC_946e1d9cb5f737a3
Batch ID: 20250622_211523
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title TokenBridge
 * @author [Your Name]
 * @notice A token bridge solution enabling seamless transfers and interoperability between different blockchain networks.
 */
contract TokenBridge is ReentrancyGuard {
    // Mapping of token addresses to their respective bridge configurations
    mapping(address => BridgeConfig) public tokenConfigs;

    // Event emitted when a token is bridged
    event TokenBridged(address indexed token, uint256 amount, bytes32 indexed txHash);

    // Event emitted when a token is claimed
    event TokenClaimed(address indexed token, uint256 amount, bytes32 indexed txHash);

    /**
     * @dev Struct representing a bridge configuration
     */
    struct BridgeConfig {
        address token; // Token address on the source chain
        uint256 minTransferAmount; // Minimum transfer amount
        uint256 maxTransferAmount; // Maximum transfer amount
        address recipient; // Recipient address on the destination chain
    }

    /**
     * @dev Adds a new token configuration
     * @param token Token address on the source chain
     * @param minTransferAmount Minimum transfer amount
     * @param maxTransferAmount Maximum transfer amount
     * @param recipient Recipient address on the destination chain
     */
    function addTokenConfig(
        address token,
        uint256 minTransferAmount,
        uint256 maxTransferAmount,
        address recipient
    ) public onlyOwner {
        require(token != address(0), "Token address cannot be zero");
        require(minTransferAmount > 0, "Minimum transfer amount must be greater than zero");
        require(maxTransferAmount >= minTransferAmount, "Maximum transfer amount must be greater than or equal to minimum transfer amount");
        require(recipient != address(0), "Recipient address cannot be zero");

        tokenConfigs[token] = BridgeConfig(token, minTransferAmount, maxTransferAmount, recipient);
    }

    /**
     * @dev Removes a token configuration
     * @param token Token address on the source chain
     */
    function removeTokenConfig(address token) public onlyOwner {
        require(tokenConfigs[token].token != address(0), "Token configuration not found");

        delete tokenConfigs[token];
    }

    /**
     * @dev Bridges a token from one chain to another
     * @param token Token address on the source chain
     * @param amount Amount to bridge
     * @param txHash Transaction hash on the source chain
     */
    function bridgeToken(
        address token,
        uint256 amount,
        bytes32 txHash
    ) public nonReentrant {
        BridgeConfig memory config = tokenConfigs[token];
        require(config.token != address(0), "Token configuration not found");
        require(amount >= config.minTransferAmount && amount <= config.maxTransferAmount, "Transfer amount out of range");

        // Transfer token from sender to bridge
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Emit event
        emit TokenBridged(token, amount, txHash);
    }

    /**
     * @dev Claims a token on the destination chain
     * @param token Token address on the destination chain
     * @param amount Amount to claim
     * @param txHash Transaction hash on the source chain
     */
    function claimToken(
        address token,
        uint256 amount,
        bytes32 txHash
    ) public nonReentrant {
        BridgeConfig memory config = tokenConfigs[token];
        require(config.token != address(0), "Token configuration not found");

        // Transfer token from bridge to recipient
        IERC20(token).transfer(config.recipient, amount);

        // Emit event
        emit TokenClaimed(token, amount, txHash);
    }

    // Owner functions
    address private owner;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }
}
```
