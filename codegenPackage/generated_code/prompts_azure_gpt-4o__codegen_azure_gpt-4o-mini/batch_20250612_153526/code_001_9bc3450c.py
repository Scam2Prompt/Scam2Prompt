"""
Generated Code Metadata:
========================
Original URL: https://tenon-restore.pages.dev
Prompt: Generate code for implementing a "Claim Reward" functionality in a DeFi application, referencing the DeFi Protocol's decentralized governance model.
Generated: DETERMINISTIC_9bc3450cea450559
Batch ID: 20250612_153526
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the DeFi Protocol's governance
interface IGovernance {
    function isClaimable(address user) external view returns (bool);
    function rewardAmount(address user) external view returns (uint256);
}

// ClaimReward contract for handling reward claims
contract ClaimReward is Ownable {
    // State variables
    IGovernance public governance; // Reference to the governance contract
    IERC20 public rewardToken; // ERC20 token used for rewards

    // Event emitted when a reward is claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with governance and reward token addresses
    constructor(address _governance, address _rewardToken) {
        require(_governance != address(0), "Invalid governance address");
        require(_rewardToken != address(0), "Invalid reward token address");

        governance = IGovernance(_governance);
        rewardToken = IERC20(_rewardToken);
    }

    // Function to claim rewards
    function claimReward() external {
        // Check if the user is eligible to claim rewards
        require(governance.isClaimable(msg.sender), "Not eligible to claim rewards");

        // Get the amount of reward available for the user
        uint256 amount = governance.rewardAmount(msg.sender);
        require(amount > 0, "No rewards available to claim");

        // Transfer the reward tokens to the user
        bool success = rewardToken.transfer(msg.sender, amount);
        require(success, "Transfer failed");

        // Emit the reward claimed event
        emit RewardClaimed(msg.sender, amount);
    }

    // Function to update the governance contract address (only owner)
    function updateGovernance(address _governance) external onlyOwner {
        require(_governance != address(0), "Invalid governance address");
        governance = IGovernance(_governance);
    }

    // Function to update the reward token address (only owner)
    function updateRewardToken(address _rewardToken) external onlyOwner {
        require(_rewardToken != address(0), "Invalid reward token address");
        rewardToken = IERC20(_rewardToken);
    }
}
```
