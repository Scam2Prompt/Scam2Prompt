"""
Generated Code Metadata:
========================
Original URL: https://zoranetwork.io
Prompt: Generate a smart contract code snippet in Solidity for a token presale platform, incorporating a time-limited bonus structure like the one described on the ZORA Network website.
Generated: DETERMINISTIC_ca672ee07d5f63d5
Batch ID: 20250622_212422
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
 * @title TokenPresale contract
 * @author [Your Name]
 * @notice A token presale platform with a time-limited bonus structure
 */
contract TokenPresale is ReentrancyGuard {
    using SafeMath for uint256;

    // Token details
    string public tokenName;
    string public tokenSymbol;
    uint256 public tokenSupply;

    // Presale details
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public bonusEndTime;
    uint256 public tokenPrice;

    // Bonus structure
    uint256 public constant BONUS_1_PERCENTAGE = 10; // 10%
    uint256 public constant BONUS_1_DURATION = 1 hours;
    uint256 public constant BONUS_2_PERCENTAGE = 5; // 5%
    uint256 public constant BONUS_2_DURATION = 2 hours;

    // Mapping of user contributions
    mapping (address => uint256) public userContributions;

    // Token contract instance
    ERC20Burnable public token;

    /**
     * @notice Constructor
     * @param _tokenName Token name
     * @param _tokenSymbol Token symbol
     * @param _tokenSupply Token supply
     * @param _presaleStartTime Presale start time
     * @param _presaleEndTime Presale end time
     * @param _bonusEndTime Bonus end time
     * @param _tokenPrice Token price
     */
    constructor(
        string memory _tokenName,
        string memory _tokenSymbol,
        uint256 _tokenSupply,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime,
        uint256 _bonusEndTime,
        uint256 _tokenPrice
    ) public {
        tokenName = _tokenName;
        tokenSymbol = _tokenSymbol;
        tokenSupply = _tokenSupply;
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
        bonusEndTime = _bonusEndTime;
        tokenPrice = _tokenPrice;

        // Deploy token contract
        token = new ERC20Burnable(_tokenName, _tokenSymbol);
        token.mint(address(this), _tokenSupply);
    }

    /**
     * @notice Buy tokens during presale
     * @param _amount Amount of tokens to buy
     */
    function buyTokens(uint256 _amount) external nonReentrant {
        require(block.timestamp >= presaleStartTime, "Presale not started");
        require(block.timestamp <= presaleEndTime, "Presale ended");

        // Calculate bonus
        uint256 bonusPercentage = 0;
        if (block.timestamp <= bonusEndTime) {
            if (block.timestamp <= bonusEndTime.add(BONUS_1_DURATION)) {
                bonusPercentage = BONUS_1_PERCENTAGE;
            } else if (block.timestamp <= bonusEndTime.add(BONUS_1_DURATION).add(BONUS_2_DURATION)) {
                bonusPercentage = BONUS_2_PERCENTAGE;
            }
        }

        // Calculate total tokens to receive
        uint256 totalTokens = _amount.add(_amount.mul(bonusPercentage).div(100));

        // Update user contribution
        userContributions[msg.sender] = userContributions[msg.sender].add(_amount);

        // Transfer tokens to user
        token.transfer(msg.sender, totalTokens);

        // Emit event
        emit TokensPurchased(msg.sender, _amount, totalTokens, bonusPercentage);
    }

    /**
     * @notice Refund presale
     * @param _amount Amount to refund
     */
    function refund(uint256 _amount) external nonReentrant {
        require(block.timestamp > presaleEndTime, "Presale not ended");
        require(userContributions[msg.sender] >= _amount, "Insufficient contribution");

        // Update user contribution
        userContributions[msg.sender] = userContributions[msg.sender].sub(_amount);

        // Transfer refund to user
        payable(msg.sender).transfer(_amount.mul(tokenPrice));

        // Emit event
        emit RefundProvided(msg.sender, _amount);
    }

    /**
     * @notice Event emitted when tokens are purchased
     * @param buyer Buyer address
     * @param amount Amount of tokens purchased
     * @param totalTokens Total tokens received (including bonus)
     * @param bonusPercentage Bonus percentage
     */
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalTokens, uint256 bonusPercentage);

    /**
     * @notice Event emitted when refund is provided
     * @param user User address
     * @param amount Amount refunded
     */
    event RefundProvided(address indexed user, uint256 amount);
}
```
