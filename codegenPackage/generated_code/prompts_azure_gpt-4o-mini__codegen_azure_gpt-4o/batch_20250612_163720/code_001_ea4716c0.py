"""
Generated Code Metadata:
========================
Original URL: https://ondofinance-claim.pages.dev
Prompt: Generate a smart contract in Solidity that allows users to stake ONDO tokens and earn rewards based on their participation in the Ondo ecosystem.
Generated: DETERMINISTIC_ea4716c0f4ce9d0f
Batch ID: 20250612_163720
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
 * @title OndoStakingContract
 * @dev A smart contract that allows users to stake ONDO tokens and earn rewards based on their participation.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract OndoStakingContract is Ownable {
    // Address of the ONDO token contract
    IERC20 public ondoToken;

    // Reward rate per second (e.g., 1e18 = 1 ONDO token per second)
    uint256 public rewardRate;

    // Total staked tokens
    uint256 public totalStaked;

    // Struct to store staking information for each user
    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already paid out
        uint256 lastUpdated; // Last time the stake was updated
    }

    // Mapping of user address to their staking information
    mapping(address => StakeInfo) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract with the ONDO token address and reward rate.
     * @param _ondoToken Address of the ONDO token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _ondoToken, uint256 _rewardRate) {
        ondoToken = _ondoToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to update rewards for the user before executing the function.
     * @param _user Address of the user.
     */
    modifier updateReward(address _user) {
        if (stakes[_user].amount > 0) {
            uint256 pendingReward = calculateReward(_user);
            stakes[_user].rewardDebt += pendingReward;
        }
        stakes[_user].lastUpdated = block.timestamp;
        _;
    }

    /**
     * @dev Function to stake ONDO tokens.
     * @param _amount Amount of ONDO tokens to stake.
     */
    function stake(uint256 _amount) external updateReward(msg.sender) {
        require(_amount > 0, "Cannot stake zero tokens");

        // Transfer ONDO tokens from the user to the contract
        require(
            ondoToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staking information
        stakes[msg.sender].amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw staked ONDO tokens.
     * @param _amount Amount of ONDO tokens to withdraw.
     */
    function withdraw(uint256 _amount) external updateReward(msg.sender) {
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(
            stakes[msg.sender].amount >= _amount,
            "Insufficient staked balance"
        );

        // Update staking information
        stakes[msg.sender].amount -= _amount;
        totalStaked -= _amount;

        // Transfer ONDO tokens back to the user
        require(
            ondoToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Function to claim earned rewards.
     */
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards to claim");

        // Reset reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        require(
            ondoToken.transfer(msg.sender, reward),
            "Reward transfer failed"
        );

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function calculateReward(address _user) public view returns (uint256) {
        StakeInfo memory stake = stakes[_user];
        if (stake.amount == 0) {
            return 0;
        }
        uint256 timeElapsed = block.timestamp - stake.lastUpdated;
        return (stake.amount * rewardRate * timeElapsed) / 1e18;
    }

    /**
     * @dev Function to update the reward rate. Only callable by the owner.
     * @param _newRewardRate New reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }
}
```
