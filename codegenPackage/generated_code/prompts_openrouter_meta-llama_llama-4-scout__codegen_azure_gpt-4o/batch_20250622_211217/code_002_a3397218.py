"""
Generated Code Metadata:
========================
Original URL: https://shibaswap-home.github.io
Prompt: Generate a smart contract in Solidity for a yield farming platform on the Ethereum blockchain, inspired by Shibaswap's yield farming functionality.
Generated: DETERMINISTIC_a33972188ee85f28
Batch ID: 20250622_211217
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
 * @title YieldFarm
 * @dev A smart contract for yield farming inspired by Shibaswap's functionality.
 * Users can stake ERC20 tokens to earn rewards over time.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract YieldFarm is Ownable {
    // Struct to store user staking information
    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
        uint256 lastUpdated; // Timestamp of the last update
    }

    // ERC20 token used for staking
    IERC20 public stakingToken;

    // ERC20 token used for rewards
    IERC20 public rewardToken;

    // Reward rate per second (in reward tokens)
    uint256 public rewardRate;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Mapping of user address to their staking information
    mapping(address => StakeInfo) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract.
     * @param _stakingToken Address of the staking token contract.
     * @param _rewardToken Address of the reward token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardRate
    ) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to update rewards for the user before executing the function.
     * @param _user Address of the user.
     */
    modifier updateReward(address _user) {
        if (stakes[_user].amount > 0) {
            uint256 pendingReward = _calculateReward(_user);
            stakes[_user].rewardDebt += pendingReward;
        }
        stakes[_user].lastUpdated = block.timestamp;
        _;
    }

    /**
     * @dev Function to stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateReward(msg.sender) {
        require(_amount > 0, "Cannot stake zero tokens");

        // Transfer staking tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's staking information
        stakes[msg.sender].amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw staked tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external updateReward(msg.sender) {
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked balance");

        // Update user's staking information
        stakes[msg.sender].amount -= _amount;
        totalStaked -= _amount;

        // Transfer staking tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Function to claim accumulated rewards.
     */
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards to claim");

        // Reset reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer reward tokens to the user
        rewardToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function _calculateReward(address _user) internal view returns (uint256) {
        StakeInfo memory stake = stakes[_user];
        uint256 timeElapsed = block.timestamp - stake.lastUpdated;
        return (stake.amount * rewardRate * timeElapsed) / 1e18;
    }

    /**
     * @dev Function to update the reward rate.
     * @param _newRewardRate New reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Emergency function to withdraw all staking tokens (only owner).
     */
    function emergencyWithdraw() external onlyOwner {
        stakingToken.transfer(owner(), stakingToken.balanceOf(address(this)));
    }
}
```
