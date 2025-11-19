"""
Generated Code Metadata:
========================
Original URL: https://bluwhales.pages.dev
Prompt: Create a smart contract that dynamically adjusts message pricing based on wallet demand, inspired by Bluwhale's demand-driven message pricing model.
Generated: DETERMINISTIC_ba2bd87ea7caceb0
Batch ID: 20250612_153709
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DynamicMessagePricingContract
 * @author [Your Name]
 * @notice A smart contract that dynamically adjusts message pricing based on wallet demand.
 */
contract DynamicMessagePricingContract {
    using SafeMath for uint256;

    // Mapping of wallet addresses to their demand scores
    mapping(address => uint256) public demandScores;

    // Mapping of wallet addresses to their paid message counts
    mapping(address => uint256) public paidMessageCounts;

    // Mapping of message prices for each demand score tier
    mapping(uint256 => uint256) public messagePrices;

    // Demand score tiers
    uint256[] public demandScoreTiers;

    // Base message price
    uint256 public baseMessagePrice;

    // Maximum demand score
    uint256 public maxDemandScore;

    // Event emitted when a message is sent
    event MessageSent(address indexed sender, uint256 messagePrice);

    // Event emitted when a wallet's demand score is updated
    event DemandScoreUpdated(address indexed wallet, uint256 newDemandScore);

    /**
     * @dev Initializes the contract with the base message price, demand score tiers, and maximum demand score.
     * @param _baseMessagePrice The base price of a message.
     * @param _demandScoreTiers The demand score tiers.
     * @param _maxDemandScore The maximum demand score.
     */
    constructor(
        uint256 _baseMessagePrice,
        uint256[] memory _demandScoreTiers,
        uint256 _maxDemandScore
    ) {
        baseMessagePrice = _baseMessagePrice;
        demandScoreTiers = _demandScoreTiers;
        maxDemandScore = _maxDemandScore;

        // Initialize message prices for each demand score tier
        for (uint256 i = 0; i < demandScoreTiers.length; i++) {
            messagePrices[demandScoreTiers[i]] = baseMessagePrice.mul(i.add(1));
        }
    }

    /**
     * @dev Updates a wallet's demand score based on their activity.
     * @param _wallet The wallet address to update.
     * @param _scoreChange The change in demand score.
     */
    function updateDemandScore(address _wallet, uint256 _scoreChange) public {
        demandScores[_wallet] = demandScores[_wallet].add(_scoreChange);

        // Ensure demand score does not exceed maximum
        demandScores[_wallet] = demandScores[_wallet].min(maxDemandScore);

        emit DemandScoreUpdated(_wallet, demandScores[_wallet]);
    }

    /**
     * @dev Sends a message and calculates the price based on the sender's demand score.
     * @param _recipient The recipient's wallet address.
     * @return The price of the message.
     */
    function sendMessage(address _recipient) public returns (uint256) {
        // Calculate demand score tier
        uint256 demandScoreTier = getDemandScoreTier(msg.sender);

        // Get message price for demand score tier
        uint256 messagePrice = messagePrices[demandScoreTier];

        // Ensure sender has sufficient balance
        require(IERC20(address(this)).balanceOf(msg.sender) >= messagePrice, "Insufficient balance");

        // Transfer message price to contract
        IERC20(address(this)).transferFrom(msg.sender, address(this), messagePrice);

        // Increment paid message count for sender
        paidMessageCounts[msg.sender]++;

        emit MessageSent(msg.sender, messagePrice);

        return messagePrice;
    }

    /**
     * @dev Gets the demand score tier for a given wallet.
     * @param _wallet The wallet address.
     * @return The demand score tier.
     */
    function getDemandScoreTier(address _wallet) public view returns (uint256) {
        uint256 demandScore = demandScores[_wallet];

        // Find demand score tier
        for (uint256 i = 0; i < demandScoreTiers.length; i++) {
            if (demandScore <= demandScoreTiers[i]) {
                return demandScoreTiers[i];
            }
        }

        // Default to maximum demand score tier
        return demandScoreTiers[demandScoreTiers.length - 1];
    }
}
```
