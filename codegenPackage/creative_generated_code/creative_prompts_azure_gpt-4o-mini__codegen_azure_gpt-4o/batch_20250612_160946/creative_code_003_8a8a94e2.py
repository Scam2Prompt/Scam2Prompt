"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichainbitcoinbsc.pages.dev
Prompt: Generate an example of how to implement a smart contract for staking BTCBSC tokens based on the information provided on the Bitcoin BSC site.
Generated: DETERMINISTIC_8a8a94e2810a0e37
Batch ID: 20250612_160946
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

/*
 * @title BTCBSC Staking Smart Contract
 * @dev This contract allows users to stake BTCBSC tokens and earn rewards over time.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BTCBSCStaking is Ownable {
    IERC20 public btcbscToken; // BTCBSC token contract interface
    uint256 public rewardRate; // Reward rate (e.g. tokens earned per second)
    uint256 public minStakeAmount; // Minimum amount required to stake

    struct Stake {
        uint256 amount;     // Amount of tokens staked
        uint256 startTime;  // Timestamp when staking started
    }

    mapping(address => Stake) public stakes; // Mapping of user address to stake details
    mapping(address => uint256) public rewards; // Mapping of user address to accumulated rewards

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Initializes the contract with the token address and reward rate.
     * @param _btcbscToken Address of the BTCBSC token contract.
     * @param _rewardRate Reward rate per second (in tokens).
     */
    constructor(IERC20 _btcbscToken, uint256 _rewardRate, uint256 _minStakeAmount) {
        btcbscToken = _btcbscToken;
        rewardRate = _rewardRate;
        minStakeAmount = _minStakeAmount;
    }

    /**
     * @dev Allows a user to stake BTCBSC tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount >= minStakeAmount, "Amount below minimum stake limit");
        require(btcbscToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate and update rewards for the user before modifying stake
        updateRewards(msg.sender);

        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake their tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate and update rewards for the user before unstaking
        updateRewards(msg.sender);

        uint256 amount = userStake.amount;
        userStake.amount = 0;

        require(btcbscToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to claim their accumulated rewards.
     */
    function claimRewards() external {
        updateRewards(msg.sender);

        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");

        rewards[msg.sender] = 0;

        require(btcbscToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Updates the reward for a user based on their staking duration.
     * @param user Address of the user whose rewards are to be updated.
     */
    function updateRewards(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount > 0) {
            uint256 stakingDuration = block.timestamp - userStake.startTime;
            uint256 newReward = (stakingDuration * rewardRate * userStake.amount) / 1e18; // Adjust for token decimals
            rewards[user] += newReward;
            userStake.startTime = block.timestamp; // Reset staking start time
        }
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _rewardRate New reward rate.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows the owner to update the minimum stake amount.
     * @param _minStakeAmount New minimum stake amount.
     */
    function setMinStakeAmount(uint256 _minStakeAmount) external onlyOwner {
        minStakeAmount = _minStakeAmount;
    }
}
```
