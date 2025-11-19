"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://floki-reward.com
Prompt: Create a smart contract for staking FLOKI tokens that rewards users with the TOKEN sister token.
Generated: DETERMINISTIC_1b06a0a5f206f41f
Batch ID: 20250612_135654
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

/**
 * @title FLOKI Token Staking Contract
 * @dev Allows users to stake FLOKI tokens and earn rewards in TOKEN tokens.
 */
contract FlokiStaking {
    // State variables
    IERC20 public flokiToken; // FLOKI token contract
    IERC20 public rewardToken; // Reward TOKEN contract
    address public owner; // Contract owner
    uint256 public rewardRate; // Reward rate per second (TOKEN tokens)

    struct Stake {
        uint256 amount; // Amount of FLOKI tokens staked
        uint256 timestamp; // Timestamp when the staking started
        uint256 rewardsClaimed; // Accumulated rewards claimed
    }

    mapping(address => Stake) public stakes; // Tracks staking information for each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    modifier updateRewards(address user) {
        if (stakes[user].amount > 0) {
            uint256 pendingRewards = calculateRewards(user);
            stakes[user].rewardsClaimed += pendingRewards;
        }
        stakes[user].timestamp = block.timestamp;
        _;
    }

    /**
     * @dev Constructor initializes the contract with tokens and reward rate.
     * @param _flokiToken Address of the FLOKI token contract
     * @param _rewardToken Address of the reward TOKEN contract
     * @param _rewardRate Reward rate in TOKEN tokens per second
     */
    constructor(IERC20 _flokiToken, IERC20 _rewardToken, uint256 _rewardRate) {
        flokiToken = _flokiToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Allows a user to stake a specific amount of FLOKI tokens.
     * @param amount The amount of FLOKI tokens to be staked
     */
    function stake(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Cannot stake 0 tokens");
        flokiToken.transferFrom(msg.sender, address(this), amount);
        stakes[msg.sender].amount += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake their FLOKI tokens and claim rewards.
     */
    function unstake() external updateRewards(msg.sender) {
        uint256 stakedAmount = stakes[msg.sender].amount;
        require(stakedAmount > 0, "No tokens staked");
        stakes[msg.sender].amount = 0;

        // Transfer staked FLOKI tokens back to the user
        flokiToken.transfer(msg.sender, stakedAmount);

        // Claim accumulated rewards
        uint256 reward = stakes[msg.sender].rewardsClaimed;
        stakes[msg.sender].rewardsClaimed = 0;
        rewardToken.transfer(msg.sender, reward);

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Allows a user to claim their accumulated rewards in TOKEN tokens.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 reward = stakes[msg.sender].rewardsClaimed;
        require(reward > 0, "No rewards available");

        stakes[msg.sender].rewardsClaimed = 0;
        rewardToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculates the pending rewards for the given user.
     * @param user The address of the user
     * @return The amount of pending rewards in TOKEN tokens
     */
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory stakeInfo = stakes[user];
        return
            (block.timestamp - stakeInfo.timestamp) *
            stakeInfo.amount *
            rewardRate /
            1e18; // Assuming TOKEN has 18 decimals
    }

    /**
     * @dev Updates the reward rate for the staking program.
     * @param _rewardRate New reward rate in TOKEN tokens per second
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Emergency function to recover tokens sent to the contract by mistake.
     * @param token Address of the token to recover
     * @param amount Amount of tokens to recover
     */
    function recoverTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner, amount);
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
