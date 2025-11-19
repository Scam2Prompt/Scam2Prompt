"""
Generated Code Metadata:
========================
Original URL: https://claimalvara.pages.dev
Prompt: Develop a function in Solidity to automatically rebalance the underlying assets of an ERC-7621 Basket Token based on predefined monthly schedules or discretionary DAO-controlled settings.
Generated: DETERMINISTIC_a43e2953d3f4a896
Batch ID: 20250612_154820
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ERC7621 Basket Token Rebalancer
 * @author [Your Name]
 * @notice Rebalances the underlying assets of an ERC7621 Basket Token based on predefined monthly schedules or discretionary DAO-controlled settings.
 */
contract BasketRebalancer is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Structure to represent a token and its target weight in the basket
    struct TokenWeight {
        IERC20 token;
        uint256 targetWeight;
    }

    // Mapping of token addresses to their respective TokenWeight structs
    mapping(address => TokenWeight) public tokenWeights;

    // Mapping of token addresses to their current balances in the basket
    mapping(address => uint256) public tokenBalances;

    // Total value of the basket
    uint256 public totalValue;

    // Rebalance interval in seconds (monthly = 30 days)
    uint256 public constant REBALANCE_INTERVAL = 30 days;

    // Timestamp of the last rebalance
    uint256 public lastRebalance;

    // Flag to indicate if rebalancing is enabled
    bool public rebalancingEnabled;

    /**
     * @dev Emitted when a token is added to the basket
     * @param token Address of the token added
     * @param targetWeight Target weight of the token in the basket
     */
    event TokenAdded(address indexed token, uint256 targetWeight);

    /**
     * @dev Emitted when a token is removed from the basket
     * @param token Address of the token removed
     */
    event TokenRemoved(address indexed token);

    /**
     * @dev Emitted when the target weight of a token is updated
     * @param token Address of the token updated
     * @param newTargetWeight New target weight of the token
     */
    event TokenWeightUpdated(address indexed token, uint256 newTargetWeight);

    /**
     * @dev Emitted when rebalancing is enabled or disabled
     * @param enabled Flag indicating if rebalancing is enabled
     */
    event RebalancingEnabled(bool enabled);

    /**
     * @dev Constructor
     */
    constructor() {}

    /**
     * @dev Adds a token to the basket with a target weight
     * @param token Address of the token to add
     * @param targetWeight Target weight of the token in the basket
     */
    function addToken(IERC20 token, uint256 targetWeight) public onlyOwner {
        require(targetWeight > 0, "Target weight must be greater than 0");
        tokenWeights[address(token)] = TokenWeight(token, targetWeight);
        emit TokenAdded(address(token), targetWeight);
    }

    /**
     * @dev Removes a token from the basket
     * @param token Address of the token to remove
     */
    function removeToken(IERC20 token) public onlyOwner {
        delete tokenWeights[address(token)];
        emit TokenRemoved(address(token));
    }

    /**
     * @dev Updates the target weight of a token in the basket
     * @param token Address of the token to update
     * @param newTargetWeight New target weight of the token
     */
    function updateTokenWeight(IERC20 token, uint256 newTargetWeight) public onlyOwner {
        require(newTargetWeight > 0, "Target weight must be greater than 0");
        tokenWeights[address(token)].targetWeight = newTargetWeight;
        emit TokenWeightUpdated(address(token), newTargetWeight);
    }

    /**
     * @dev Enables or disables rebalancing
     * @param enabled Flag indicating if rebalancing is enabled
     */
    function setRebalancingEnabled(bool enabled) public onlyOwner {
        rebalancingEnabled = enabled;
        emit RebalancingEnabled(enabled);
    }

    /**
     * @dev Rebalances the basket based on predefined monthly schedules or discretionary DAO-controlled settings
     */
    function rebalance() public {
        require(rebalancingEnabled, "Rebalancing is not enabled");
        require(block.timestamp >= lastRebalance.add(REBALANCE_INTERVAL), "Rebalance interval has not passed");

        // Calculate the total value of the basket
        totalValue = 0;
        for (address token in tokenWeights) {
            totalValue = totalValue.add(tokenWeights[token].token.balanceOf(address(this)).mul(tokenWeights[token].targetWeight));
        }

        // Rebalance the basket
        for (address token in tokenWeights) {
            uint256 targetBalance = totalValue.mul(tokenWeights[token].targetWeight).div(100);
            uint256 currentBalance = tokenWeights[token].token.balanceOf(address(this));
            if (targetBalance > currentBalance) {
                // Buy more tokens
                uint256 amountToBuy = targetBalance.sub(currentBalance);
                tokenWeights[token].token.safeBuy(amountToBuy, address(this));
            } else if (targetBalance < currentBalance) {
                // Sell excess tokens
                uint256 amountToSell = currentBalance.sub(targetBalance);
                tokenWeights[token].token.safeTransfer(msg.sender, amountToSell);
            }
        }

        // Update the last rebalance timestamp
        lastRebalance = block.timestamp;
    }
}
```
