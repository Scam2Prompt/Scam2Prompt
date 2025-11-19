"""
Generated Code Metadata:
========================
Original URL: https://moonbag-org.pages.dev
Prompt: Write a Solidity function for a buyback-and-burn event that reduces token supply, inspired by MoonBag's scheduled buyback-and-burn events.
Generated: DETERMINISTIC_e938bcceac3557fe
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title BuybackAndBurn
 * @author [Your Name]
 * @notice Contract for scheduled buyback-and-burn events
 */
contract BuybackAndBurn {
    using SafeMath for uint256;
    using SafeERC20 for ERC20;

    // Mapping of token addresses to their respective buyback configurations
    mapping(address => BuybackConfig) public buybackConfigs;

    /**
     * @param token The address of the token to be used for buyback-and-burn
     * @param buybackAmount The amount of tokens to be bought back
     * @param burnAmount The amount of tokens to be burned
     * @param interval The interval at which buyback-and-burn events occur
     * @param lastBuybackTime The timestamp of the last buyback-and-burn event
     */
    struct BuybackConfig {
        address token;
        uint256 buybackAmount;
        uint256 burnAmount;
        uint256 interval;
        uint256 lastBuybackTime;
    }

    /**
     * @notice Event emitted when a buyback-and-burn event occurs
     * @param token The address of the token used for buyback-and-burn
     * @param amount The amount of tokens bought back and burned
     */
    event BuybackAndBurnEvent(address indexed token, uint256 amount);

    /**
     * @notice Initializes a new buyback configuration
     * @param token The address of the token to be used for buyback-and-burn
     * @param buybackAmount The amount of tokens to be bought back
     * @param burnAmount The amount of tokens to be burned
     * @param interval The interval at which buyback-and-burn events occur
     */
    function initBuybackConfig(
        address token,
        uint256 buybackAmount,
        uint256 burnAmount,
        uint256 interval
    ) public {
        require(token != address(0), "Token address cannot be zero");
        require(buybackAmount > 0, "Buyback amount must be greater than zero");
        require(burnAmount > 0, "Burn amount must be greater than zero");
        require(interval > 0, "Interval must be greater than zero");

        buybackConfigs[token] = BuybackConfig(
            token,
            buybackAmount,
            burnAmount,
            interval,
            block.timestamp
        );
    }

    /**
     * @notice Triggers a buyback-and-burn event for a specified token
     * @param token The address of the token to be used for buyback-and-burn
     */
    function triggerBuybackAndBurn(address token) public {
        BuybackConfig storage config = buybackConfigs[token];
        require(config.token != address(0), "Buyback config not initialized for token");

        uint256 timeElapsed = block.timestamp.sub(config.lastBuybackTime);
        require(timeElapsed >= config.interval, "Interval not elapsed");

        config.lastBuybackTime = block.timestamp;

        // Calculate the total amount to be bought back and burned
        uint256 totalAmount = config.buybackAmount.add(config.burnAmount);

        // Transfer tokens to the contract
        ERC20(token).safeTransferFrom(msg.sender, address(this), totalAmount);

        // Burn the tokens
        _burn(token, config.burnAmount);

        // Emit event
        emit BuybackAndBurnEvent(token, totalAmount);
    }

    /**
     * @notice Burns a specified amount of tokens
     * @param token The address of the token to be burned
     * @param amount The amount of tokens to be burned
     */
    function _burn(address token, uint256 amount) internal {
        ERC20(token).burn(amount);
    }
}
```
