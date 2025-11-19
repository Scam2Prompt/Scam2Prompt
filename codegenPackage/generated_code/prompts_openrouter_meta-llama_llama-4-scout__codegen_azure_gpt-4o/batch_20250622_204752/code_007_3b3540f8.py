"""
Generated Code Metadata:
========================
Original URL: https://fffrfh.pages.dev
Prompt: Develop a smart contract in Solidity to automate the distribution of MOR token rewards to Capital Providers and Compute contributors.
Generated: DETERMINISTIC_3b3540f8979189ad
Batch ID: 20250622_204752
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

/**
 * @title MOR Token Reward Distribution Contract
 * @dev This contract automates the distribution of MOR token rewards to Capital Providers and Compute Contributors.
 */
contract MORRewardDistributor {
    // Address of the MOR token contract
    IERC20 public morToken;

    // Struct to store reward details
    struct Reward {
        uint256 capitalProviderReward;
        uint256 computeContributorReward;
    }

    // Mapping to store rewards for each address
    mapping(address => Reward) public rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed recipient, uint256 capitalReward, uint256 computeReward);

    // Event emitted when rewards are updated
    event RewardsUpdated(address indexed recipient, uint256 capitalReward, uint256 computeReward);

    /**
     * @dev Constructor to initialize the MOR token contract address.
     * @param _morToken Address of the MOR token contract.
     */
    constructor(address _morToken) {
        require(_morToken != address(0), "Invalid MOR token address");
        morToken = IERC20(_morToken);
    }

    /**
     * @dev Function to update rewards for a specific address.
     * @param recipient Address of the recipient.
     * @param capitalReward Amount of MOR tokens for capital providers.
     * @param computeReward Amount of MOR tokens for compute contributors.
     */
    function updateRewards(
        address recipient,
        uint256 capitalReward,
        uint256 computeReward
    ) external {
        require(recipient != address(0), "Invalid recipient address");
        require(capitalReward > 0 || computeReward > 0, "Rewards must be greater than zero");

        rewards[recipient] = Reward(capitalReward, computeReward);

        emit RewardsUpdated(recipient, capitalReward, computeReward);
    }

    /**
     * @dev Function to distribute rewards to a specific address.
     * @param recipient Address of the recipient.
     */
    function distributeRewards(address recipient) external {
        require(recipient != address(0), "Invalid recipient address");

        Reward memory reward = rewards[recipient];
        require(reward.capitalProviderReward > 0 || reward.computeContributorReward > 0, "No rewards available");

        // Transfer MOR tokens for capital providers
        if (reward.capitalProviderReward > 0) {
            require(
                morToken.transfer(recipient, reward.capitalProviderReward),
                "Capital provider reward transfer failed"
            );
        }

        // Transfer MOR tokens for compute contributors
        if (reward.computeContributorReward > 0) {
            require(
                morToken.transfer(recipient, reward.computeContributorReward),
                "Compute contributor reward transfer failed"
            );
        }

        // Clear rewards after distribution
        delete rewards[recipient];

        emit RewardsDistributed(recipient, reward.capitalProviderReward, reward.computeContributorReward);
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
