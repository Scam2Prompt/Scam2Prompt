"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim.kippro.world
Prompt: Write code in Solidity to implement a reward distribution mechanism using the $KIP token for AI app owners who contribute to the protocol.
Generated: DETERMINISTIC_900ef0944150b6c9
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title RewardDistribution
 * @dev A contract to distribute $KIP tokens as rewards to AI app owners who contribute to the protocol.
 */
contract RewardDistribution {
    // Address of the $KIP token contract
    IERC20 public kipToken;

    // Owner of the contract
    address public owner;

    // Total contributions mapping (AI App Owner => Contributions)
    mapping(address => uint256) public contributions;

    // Reward percentage (e.g., 5 means 5% of total contributions)
    uint256 public rewardPercentage;

    // Events
    event ContributionAdded(address indexed contributor, uint256 amount);
    event RewardDistributed(address indexed recipient, uint256 rewardAmount);

    /**
     * @dev Modifier to restrict access to contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _kipToken Address of the $KIP token contract.
     * @param _rewardPercentage Reward percentage to distribute (e.g., 5 for 5%).
     */
    constructor(address _kipToken, uint256 _rewardPercentage) {
        require(_kipToken != address(0), "Invalid token address");
        require(_rewardPercentage > 0 && _rewardPercentage <= 100, "Reward percentage must be between 1 and 100");

        kipToken = IERC20(_kipToken);
        rewardPercentage = _rewardPercentage;
        owner = msg.sender;
    }

    /**
     * @dev Function for AI app owners to add their contributions.
     * @param _amount Amount of contribution (in terms of $KIP tokens).
     */
    function addContribution(uint256 _amount) external {
        require(_amount > 0, "Contribution amount must be greater than zero");

        // Transfer $KIP tokens from the contributor to the contract
        bool success = kipToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update contributions mapping
        contributions[msg.sender] += _amount;

        emit ContributionAdded(msg.sender, _amount);
    }

    /**
     * @dev Function to distribute rewards to contributors based on their contributions.
     * Can only be called by the owner.
     */
    function distributeRewards() external onlyOwner {
        // Iterate through all contributors and distribute rewards
        for (address contributor = address(0); contributor != address(0); contributor++) {
            uint256 contributorContribution = contributions[contributor];

            // Skip if no contributions
            if (contributorContribution == 0) {
                continue;
            }

            // Calculate reward amount
            uint256 rewardAmount = (contributorContribution * rewardPercentage) / 100;

            // Transfer reward tokens to the contributor
            bool success = kipToken.transfer(contributor, rewardAmount);
            require(success, "Reward transfer failed");

            emit RewardDistributed(contributor, rewardAmount);
        }
    }

    /**
     * @dev Function to update the reward percentage.
     * Can only be called by the owner.
     * @param _newRewardPercentage New reward percentage to set.
     */
    function updateRewardPercentage(uint256 _newRewardPercentage) external onlyOwner {
        require(_newRewardPercentage > 0 && _newRewardPercentage <= 100, "Reward percentage must be between 1 and 100");
        rewardPercentage = _newRewardPercentage;
    }

    /**
     * @dev Function to withdraw tokens in case of emergency.
     * Can only be called by the owner.
     * @param _amount Amount to withdraw.
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");

        bool success = kipToken.transfer(owner, _amount);
        require(success, "Emergency withdrawal failed");
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
