"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soiletdemo.pages.dev
Prompt: Write a smart contract in Solidity that supports staking $MGMES tokens and distributes rewards based on blockchain-verified event results, as described in The Meme Games Token documentation.
Generated: DETERMINISTIC_5045e215459a9d5f
Batch ID: 20250612_145715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin contracts for security and commonly used functionality.
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MemeGamesStaking is Ownable, ReentrancyGuard {
    // $MGMES token interface
    IERC20 public mgmesToken;

    // Struct to hold staking details
    struct Stake {
        uint256 amount;  // Amount of $MGMES tokens staked
        uint256 reward;  // Reward accumulated for the stake
        uint256 lastUpdated;  // Timestamp of the last reward update
    }

    // Mapping to manage staker details
    mapping(address => Stake) public stakes;

    // Total tokens staked
    uint256 public totalStaked;

    // Reward rate per second (to be set by the contract owner)
    uint256 public rewardRate;

    // Event to notify when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event to notify when rewards are distributed
    event RewardDistributed(address indexed user, uint256 reward);

    // Event to notify when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event to notify when the reward rate is updated
    event RewardRateUpdated(uint256 newRate);

    // Constructor to initialize the contract with $MGMES token address
    constructor(address _mgmesToken) {
        require(_mgmesToken != address(0), "Token address cannot be zero");
        mgmesToken = IERC20(_mgmesToken);
    }

    // Function to set the reward rate (onlyOwner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    // Modifier to update rewards for a user before any state change
    modifier updateReward(address _user) {
        if (stakes[_user].amount > 0) {
            stakes[_user].reward += _calculateReward(_user);
        }
        stakes[_user].lastUpdated = block.timestamp;
        _;
    }

    // Function to allow users to stake $MGMES tokens
    function stake(uint256 _amount) external nonReentrant updateReward(msg.sender) {
        require(_amount > 0, "Cannot stake zero tokens");
        require(mgmesToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        stakes[msg.sender].amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked tokens along with rewards
    function withdraw() external nonReentrant updateReward(msg.sender) {
        uint256 stakedAmount = stakes[msg.sender].amount;
        uint256 rewardAmount = stakes[msg.sender].reward;

        require(stakedAmount > 0, "No tokens to withdraw");

        // Reset user's stake details
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].reward = 0;
        totalStaked -= stakedAmount;

        // Transfer the staked amount and rewards back to the user
        require(mgmesToken.transfer(msg.sender, stakedAmount), "Token transfer failed");
        if (rewardAmount > 0) {
            require(mgmesToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");
            emit RewardDistributed(msg.sender, rewardAmount);
        }

        emit Withdrawn(msg.sender, stakedAmount);
    }

    // Function to calculate the reward for a user
    function _calculateReward(address _user) internal view returns (uint256) {
        Stake memory userStake = stakes[_user];
        uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
        return (userStake.amount * rewardRate * timeElapsed) / 1e18;
    }

    // Function to get the total reward for a user (including pending rewards)
    function rewardOf(address _user) external view returns (uint256) {
        return stakes[_user].reward + _calculateReward(_user);
    }

    // Function to resolve blockchain-verified event results and distribute rewards
    // Only callable by the owner
    function distributeEventRewards(address _winner, uint256 _rewardAmount) external onlyOwner {
        require(_winner != address(0), "Winner address cannot be zero");
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        require(mgmesToken.balanceOf(address(this)) >= _rewardAmount, "Not enough tokens in contract");

        stakes[_winner].reward += _rewardAmount;

        emit RewardDistributed(_winner, _rewardAmount);
    }

    // Emergency function for the owner to withdraw all tokens
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = mgmesToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        require(mgmesToken.transfer(msg.sender, balance), "Token transfer failed");
    }

    // Fallback function to prevent ETH deposits
    receive() external payable {
        revert("This contract does not accept ETH");
    }
}
```
