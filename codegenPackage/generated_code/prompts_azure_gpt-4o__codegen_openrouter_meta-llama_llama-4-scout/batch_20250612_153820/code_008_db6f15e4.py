"""
Generated Code Metadata:
========================
Original URL: https://whale.market
Prompt: Write a smart contract to facilitate token buyback and burn mechanisms, following Whales Market's emission strategy.
Generated: DETERMINISTIC_db6f15e4d8ad747c
Batch ID: 20250612_153820
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TokenBuybackAndBurn
 * @author [Your Name]
 * @notice A smart contract to facilitate token buyback and burn mechanisms.
 */
contract TokenBuybackAndBurn is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of token addresses to their respective buyback and burn configurations
    mapping(address => BuybackConfig) public buybackConfigs;

    // Event emitted when a token is bought back and burned
    event TokenBoughtBackAndBurned(address indexed token, uint256 amount);

    // Event emitted when a new buyback configuration is added
    event BuybackConfigAdded(address indexed token, uint256 buybackFee, uint256 burnAmount);

    // Event emitted when a buyback configuration is updated
    event BuybackConfigUpdated(address indexed token, uint256 buybackFee, uint256 burnAmount);

    /**
     * @dev Struct representing a buyback configuration
     */
    struct BuybackConfig {
        uint256 buybackFee; // Fee for buying back tokens (in bps)
        uint256 burnAmount; // Amount of tokens to burn
    }

    /**
     * @dev Adds a new buyback configuration for a token
     * @param token Address of the token
     * @param buybackFee Fee for buying back tokens (in bps)
     * @param burnAmount Amount of tokens to burn
     */
    function addBuybackConfig(address token, uint256 buybackFee, uint256 burnAmount) public {
        require(token != address(0), "Invalid token address");
        require(buybackFee > 0, "Buyback fee must be greater than 0");
        require(burnAmount > 0, "Burn amount must be greater than 0");

        buybackConfigs[token] = BuybackConfig(buybackFee, burnAmount);
        emit BuybackConfigAdded(token, buybackFee, burnAmount);
    }

    /**
     * @dev Updates an existing buyback configuration for a token
     * @param token Address of the token
     * @param buybackFee Fee for buying back tokens (in bps)
     * @param burnAmount Amount of tokens to burn
     */
    function updateBuybackConfig(address token, uint256 buybackFee, uint256 burnAmount) public {
        require(token != address(0), "Invalid token address");
        require(buybackConfigs[token].buybackFee > 0, "Buyback config not found");

        buybackConfigs[token] = BuybackConfig(buybackFee, burnAmount);
        emit BuybackConfigUpdated(token, buybackFee, burnAmount);
    }

    /**
     * @dev Buys back and burns tokens using the configured buyback strategy
     * @param token Address of the token to buy back and burn
     * @param amount Amount of tokens to buy back
     */
    function buyBackAndBurn(address token, uint256 amount) public nonReentrant {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than 0");

        BuybackConfig memory config = buybackConfigs[token];
        require(config.buybackFee > 0, "Buyback config not found");

        // Calculate the buyback fee
        uint256 buybackFee = amount.mul(config.buybackFee).div(10000);

        // Transfer tokens to the contract
        ERC20(token).transferFrom(msg.sender, address(this), amount);

        // Burn tokens
        ERC20Burnable(token).burn(amount);

        // Emit event
        emit TokenBoughtBackAndBurned(token, amount);
    }
}
```
