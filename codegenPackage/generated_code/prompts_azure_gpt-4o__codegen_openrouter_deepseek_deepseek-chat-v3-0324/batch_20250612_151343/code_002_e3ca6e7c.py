"""
Generated Code Metadata:
========================
Original URL: https://gravity-cq3.pages.dev
Prompt: Generate a smart contract example that utilizes Gravity's omnichain intent protocol to manage yield-enabled unified balances across multiple chains.
Generated: DETERMINISTIC_e3ca6e7c2ee298dd
Batch ID: 20250612_151343
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
 * @title CrossChainYieldManager
 * @dev A smart contract that manages yield-enabled unified balances across multiple chains
 * using Gravity's omnichain intent protocol.
 */
contract CrossChainYieldManager is Ownable, ReentrancyGuard {
    // Struct to represent a user's balance across chains
    struct UnifiedBalance {
        uint256 totalBalance; // Sum of balances across all chains
        uint256 lastUpdate;   // Timestamp of last balance update
        uint256 yieldRate;    // Current yield rate (APY basis points)
    }

    // Mapping from user address to their unified balance
    mapping(address => UnifiedBalance) public unifiedBalances;

    // Supported chains and their corresponding bridge addresses
    mapping(uint256 => address) public chainBridges;

    // Supported yield tokens
    mapping(address => bool) public supportedTokens;

    // Events
    event Deposit(address indexed user, uint256 chainId, uint256 amount);
    event Withdraw(address indexed user, uint256 chainId, uint256 amount);
    event CrossChainTransfer(
        address indexed user,
        uint256 fromChainId,
        uint256 toChainId,
        uint256 amount
    );
    event YieldUpdated(address indexed user, uint256 newYieldRate);
    event ChainBridgeUpdated(uint256 chainId, address newBridge);

    /**
     * @dev Modifier to check if token is supported
     */
    modifier onlySupportedToken(address token) {
        require(supportedTokens[token], "Token not supported");
        _;
    }

    /**
     * @dev Constructor to initialize the contract
     * @param initialOwner The initial owner of the contract
     */
    constructor(address initialOwner) Ownable(initialOwner) {}

    /**
     * @dev Add a supported token
     * @param token The token address to support
     */
    function addSupportedToken(address token) external onlyOwner {
        supportedTokens[token] = true;
    }

    /**
     * @dev Remove a supported token
     * @param token The token address to remove support for
     */
    function removeSupportedToken(address token) external onlyOwner {
        supportedTokens[token] = false;
    }

    /**
     * @dev Set or update a chain bridge address
     * @param chainId The chain ID
     * @param bridgeAddress The bridge contract address for that chain
     */
    function setChainBridge(uint256 chainId, address bridgeAddress) external onlyOwner {
        chainBridges[chainId] = bridgeAddress;
        emit ChainBridgeUpdated(chainId, bridgeAddress);
    }

    /**
     * @dev Deposit tokens from a specific chain
     * @param token The token address
     * @param chainId The source chain ID
     * @param amount The amount to deposit
     */
    function deposit(
        address token,
        uint256 chainId,
        uint256 amount
    ) external nonReentrant onlySupportedToken(token) {
        require(chainBridges[chainId] != address(0), "Chain not supported");
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from user to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Update unified balance
        _updateYield(msg.sender);
        unifiedBalances[msg.sender].totalBalance += amount;

        emit Deposit(msg.sender, chainId, amount);
    }

    /**
     * @dev Withdraw tokens to a specific chain
     * @param token The token address
     * @param chainId The target chain ID
     * @param amount The amount to withdraw
     */
    function withdraw(
        address token,
        uint256 chainId,
        uint256 amount
    ) external nonReentrant onlySupportedToken(token) {
        require(chainBridges[chainId] != address(0), "Chain not supported");
        require(amount > 0, "Amount must be greater than 0");

        // Update unified balance and check sufficient funds
        _updateYield(msg.sender);
        require(
            unifiedBalances[msg.sender].totalBalance >= amount,
            "Insufficient balance"
        );

        unifiedBalances[msg.sender].totalBalance -= amount;

        // Transfer tokens to user
        IERC20(token).transfer(msg.sender, amount);

        emit Withdraw(msg.sender, chainId, amount);
    }

    /**
     * @dev Transfer balance between chains
     * @param fromChainId The source chain ID
     * @param toChainId The target chain ID
     * @param amount The amount to transfer
     */
    function crossChainTransfer(
        uint256 fromChainId,
        uint256 toChainId,
        uint256 amount
    ) external nonReentrant {
        require(chainBridges[fromChainId] != address(0), "Source chain not supported");
        require(chainBridges[toChainId] != address(0), "Target chain not supported");
        require(amount > 0, "Amount must be greater than 0");

        // In a real implementation, this would interact with Gravity's bridge
        // For this example, we just update the unified balance
        _updateYield(msg.sender);
        require(
            unifiedBalances[msg.sender].totalBalance >= amount,
            "Insufficient balance"
        );

        emit CrossChainTransfer(msg.sender, fromChainId, toChainId, amount);
    }

    /**
     * @dev Update a user's yield rate
     * @param user The user address
     * @param newYieldRate The new yield rate (APY basis points)
     */
    function updateYieldRate(address user, uint256 newYieldRate) external onlyOwner {
        _updateYield(user);
        unifiedBalances[user].yieldRate = newYieldRate;
        emit YieldUpdated(user, newYieldRate);
    }

    /**
     * @dev Internal function to update accrued yield
     * @param user The user address
     */
    function _updateYield(address user) internal {
        UnifiedBalance storage balance = unifiedBalances[user];
        if (balance.lastUpdate == 0) {
            balance.lastUpdate = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - balance.lastUpdate;
        if (timeElapsed > 0 && balance.yieldRate > 0) {
            uint256 yield = (balance.totalBalance * balance.yieldRate * timeElapsed) /
                (365 days * 10000);
            balance.totalBalance += yield;
        }
        balance.lastUpdate = block.timestamp;
    }

    /**
     * @dev Get a user's current unified balance with accrued yield
     * @param user The user address
     * @return The current unified balance
     */
    function getUnifiedBalance(address user) external view returns (uint256) {
        UnifiedBalance memory balance = unifiedBalances[user];
        if (balance.lastUpdate == 0 || balance.yieldRate == 0) {
            return balance.totalBalance;
        }

        uint256 timeElapsed = block.timestamp - balance.lastUpdate;
        uint256 yield = (balance.totalBalance * balance.yieldRate * timeElapsed) /
            (365 days * 10000);
        return balance.totalBalance + yield;
    }
}
```
