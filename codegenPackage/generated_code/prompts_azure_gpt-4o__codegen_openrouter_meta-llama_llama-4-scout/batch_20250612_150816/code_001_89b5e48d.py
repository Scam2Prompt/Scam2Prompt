"""
Generated Code Metadata:
========================
Original URL: https://bonemv.com
Prompt: Generate a smart contract in Solidity that facilitates reward distribution upon wallet connection, inspired by the functionality described in REWARD Portal v2.
Generated: DETERMINISTIC_89b5e48d56dd8ee4
Batch ID: 20250612_150816
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title RewardDistributionContract
 * @author [Your Name]
 * @notice A smart contract for distributing rewards upon wallet connection.
 */
contract RewardDistributionContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of wallet addresses to their respective reward balances
    mapping(address => uint256) public rewardBalances;

    // Mapping of wallet addresses to their respective claim status
    mapping(address => bool) public claimedRewards;

    // Address of the reward token
    address public rewardTokenAddress;

    // Total reward amount available for distribution
    uint256 public totalRewardsAvailable;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed recipient, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor for the RewardDistributionContract.
     * @param _rewardTokenAddress Address of the reward token.
     * @param _totalRewardsAvailable Total reward amount available for distribution.
     */
    constructor(address _rewardTokenAddress, uint256 _totalRewardsAvailable) {
        require(_rewardTokenAddress != address(0), "Reward token address cannot be zero");
        require(_totalRewardsAvailable > 0, "Total rewards available must be greater than zero");

        rewardTokenAddress = _rewardTokenAddress;
        totalRewardsAvailable = _totalRewardsAvailable;
    }

    /**
     * @dev Distributes rewards to a wallet address.
     * @param _recipient Address of the recipient.
     * @param _amount Amount of rewards to distribute.
     */
    function distributeRewards(address _recipient, uint256 _amount) public {
        require(msg.sender == owner(), "Only the owner can distribute rewards");
        require(_recipient != address(0), "Recipient address cannot be zero");
        require(_amount > 0, "Reward amount must be greater than zero");
        require(totalRewardsAvailable >= _amount, "Insufficient rewards available");

        // Update the reward balance for the recipient
        rewardBalances[_recipient] = rewardBalances[_recipient].add(_amount);

        // Update the total rewards available
        totalRewardsAvailable = totalRewardsAvailable.sub(_amount);

        // Emit an event for reward distribution
        emit RewardsDistributed(_recipient, _amount);
    }

    /**
     * @dev Claims rewards for a wallet address.
     */
    function claimRewards() public nonReentrant {
        require(claimedRewards[msg.sender] == false, "Rewards already claimed");
        require(rewardBalances[msg.sender] > 0, "No rewards available");

        // Retrieve the reward balance for the sender
        uint256 rewardBalance = rewardBalances[msg.sender];

        // Reset the reward balance for the sender
        rewardBalances[msg.sender] = 0;

        // Mark rewards as claimed for the sender
        claimedRewards[msg.sender] = true;

        // Transfer the rewards to the sender
        IERC20(rewardTokenAddress).transfer(msg.sender, rewardBalance);

        // Emit an event for reward claim
        emit RewardsClaimed(msg.sender, rewardBalance);
    }

    /**
     * @dev Updates the total rewards available.
     * @param _newTotalRewardsAvailable New total reward amount available for distribution.
     */
    function updateTotalRewardsAvailable(uint256 _newTotalRewardsAvailable) public {
        require(msg.sender == owner(), "Only the owner can update total rewards available");
        require(_newTotalRewardsAvailable >= 0, "New total rewards available must be non-negative");

        totalRewardsAvailable = _newTotalRewardsAvailable;
    }

    /**
     * @dev Returns the reward balance for a wallet address.
     * @param _recipient Address of the recipient.
     * @return Reward balance for the recipient.
     */
    function getRewardBalance(address _recipient) public view returns (uint256) {
        return rewardBalances[_recipient];
    }
}
```
