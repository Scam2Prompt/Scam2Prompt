"""
Generated Code Metadata:
========================
Original URL: https://singularity-finance.pages.dev
Prompt: Write a smart contract to tokenize curated data contributions into yield-bearing assets for the AI economy, leveraging Singularity Finance's data ownership monetization model.
Generated: DETERMINISTIC_e12069ff1dfc70cf
Batch ID: 20250612_145831
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
 * @title DataContributionToken
 * @author Singularity Finance
 * @notice A tokenized data contribution contract for the AI economy
 */
contract DataContributionToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of data contributors to their contribution amounts
    mapping(address => uint256) public contributions;

    // Mapping of data contributors to their reward amounts
    mapping(address => uint256) public rewards;

    // Total rewards available for distribution
    uint256 public totalRewards;

    // Yield-bearing asset reward rate (in percent)
    uint256 public rewardRate;

    // Data ownership monetization model parameters
    uint256 public dataMonetizationRate;
    uint256 public dataOwnershipThreshold;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param rewardRate Yield-bearing asset reward rate (in percent)
     * @param dataMonetizationRate Data ownership monetization rate
     * @param dataOwnershipThreshold Data ownership threshold
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 rewardRate,
        uint256 dataMonetizationRate,
        uint256 dataOwnershipThreshold
    ) ERC20(name, symbol) {
        require(rewardRate > 0, "Reward rate must be greater than 0");
        require(dataMonetizationRate > 0, "Data monetization rate must be greater than 0");
        require(dataOwnershipThreshold > 0, "Data ownership threshold must be greater than 0");

        this.rewardRate = rewardRate;
        this.dataMonetizationRate = dataMonetizationRate;
        this.dataOwnershipThreshold = dataOwnershipThreshold;
    }

    /**
     * @notice Contribute data and receive token reward
     * @param amount Data contribution amount
     */
    function contributeData(uint256 amount) external nonReentrant {
        require(amount > 0, "Contribution amount must be greater than 0");

        // Update contributor's contribution amount
        contributions[msg.sender] = contributions[msg.sender].add(amount);

        // Mint tokens to contributor
        _mint(msg.sender, amount);

        // Update total rewards available for distribution
        totalRewards = totalRewards.add(amount.mul(rewardRate).div(100));
    }

    /**
     * @notice Claim reward
     */
    function claimReward() external nonReentrant {
        // Calculate reward amount
        uint256 rewardAmount = rewards[msg.sender];

        // Reset reward amount
        rewards[msg.sender] = 0;

        // Transfer reward to contributor
        _transfer(address(this), msg.sender, rewardAmount);
    }

    /**
     * @notice Update reward rate
     * @param newRewardRate New yield-bearing asset reward rate (in percent)
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        require(newRewardRate > 0, "Reward rate must be greater than 0");
        rewardRate = newRewardRate;
    }

    /**
     * @notice Update data ownership monetization model parameters
     * @param newDataMonetizationRate New data ownership monetization rate
     * @param newDataOwnershipThreshold New data ownership threshold
     */
    function updateDataMonetizationParams(
        uint256 newDataMonetizationRate,
        uint256 newDataOwnershipThreshold
    ) external onlyOwner {
        require(newDataMonetizationRate > 0, "Data monetization rate must be greater than 0");
        require(newDataOwnershipThreshold > 0, "Data ownership threshold must be greater than 0");

        dataMonetizationRate = newDataMonetizationRate;
        dataOwnershipThreshold = newDataOwnershipThreshold;
    }

    /**
     * @notice Distribute rewards to contributors
     */
    function distributeRewards() external onlyOwner {
        for (address contributor in contributions) {
            uint256 contributionAmount = contributions[contributor];
            uint256 rewardAmount = contributionAmount.mul(rewardRate).div(100);

            // Update contributor's reward amount
            rewards[contributor] = rewards[contributor].add(rewardAmount);
        }
    }

    /**
     * @notice Burn tokens
     * @param amount Amount to burn
     */
    function burn(uint256 amount) public override {
        // Check if burning would exceed contributor's balance
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Burn tokens
        _burn(msg.sender, amount);
    }
}
```
