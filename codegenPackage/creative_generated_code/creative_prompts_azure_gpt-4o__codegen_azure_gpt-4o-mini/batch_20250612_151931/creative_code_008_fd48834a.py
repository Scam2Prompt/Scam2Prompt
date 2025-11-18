"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wenwen.pages.dev
Prompt: Write a Solidity contract to enable staking of WEN tokens with rewards distributed based on tokenomics principles.
Generated: DETERMINISTIC_fd48834a196172b4
Batch ID: 20250612_151931
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

// Importing OpenZeppelin ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title WENStaking
 * @dev A staking contract for WEN tokens with reward distribution.
 */
contract WENStaking is ReentrancyGuard, Ownable {
    // Token to be staked
    IERC20 public wenToken;

    // Staker information
    struct Staker {
        uint256 amountStaked;       // Amount of tokens staked
        uint256 lastClaimed;        // Last time rewards were claimed
        uint256 totalRewards;       // Total rewards earned
    }

    // Mapping of staker addresses to their information
    mapping(address => Staker) public stakers;

    // Reward rate (tokens per second) for staking
    uint256 public rewardRate;

    // Event to emit when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event to emit when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 reward);

    // Event to emit when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the WEN token and reward rate.
     * @param _wenToken Address of the WEN token contract.
     * @param _rewardRate Reward rate for staking.
     */
    constructor(IERC20 _wenToken, uint256 _rewardRate) {
        wenToken = _wenToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake WEN tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(wenToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        Staker storage staker = stakers[msg.sender];

        // Update staker information
        staker.amountStaked += _amount;
        staker.lastClaimed = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);

        require(rewards > 0, "No rewards available");

        // Update last claimed time
        staker.lastClaimed = block.timestamp;
        staker.totalRewards += rewards;

        // Transfer rewards to the staker
        require(wenToken.transfer(msg.sender, rewards), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Unstake WEN tokens and claim any outstanding rewards.
     */
    function unstake() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No tokens staked");

        // Calculate and claim rewards
        claimRewards();

        uint256 amountToUnstake = staker.amountStaked;

        // Reset staker information
        staker.amountStaked = 0;

        // Transfer staked tokens back to the staker
        require(wenToken.transfer(msg.sender, amountToUnstake), "Transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Calculate the staking rewards for a user.
     * @param _user Address of the staker.
     * @return The total rewards earned by the user.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        Staker storage staker = stakers[_user];
        uint256 timeStaked = block.timestamp - staker.lastClaimed;
        return (staker.amountStaked * rewardRate * timeStaked);
    }

    /**
     * @dev Update reward rate for staking.
     * @param _newRate New reward rate to set.
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }
}
```
