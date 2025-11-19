"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theoldcastle.pages.dev
Prompt: How can I implement a smart contract to stake $FOMO tokens in The Old Castle Defense ecosystem?
Generated: DETERMINISTIC_959f88756106e0a5
Batch ID: 20250612_163502
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
 * @title FOMO Token Staking Contract
 * @dev A smart contract for staking FOMO tokens in The Old Castle Defense ecosystem.
 */
contract FOMOStaking {
    // Address of the FOMO token contract
    IERC20 public immutable fomoToken;

    // Struct to store staker details
    struct Staker {
        uint256 stakedAmount; // Amount of tokens staked
        uint256 rewardDebt;   // Rewards already accounted for
        uint256 lastUpdated;  // Timestamp of last update
    }

    // Mapping to track information for each staker
    mapping(address => Staker) public stakers;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate in tokens per second (e.g., 1 FOMO per second)
    uint256 public rewardRate;

    // Admin address
    address public admin;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRewardRate);

    /**
     * @dev Modifier to restrict access to admin-only functions.
     */
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    /**
     * @dev Constructor to set the token address and reward rate.
     * @param _fomoToken Address of the FOMO token contract.
     * @param _rewardRate Initial reward rate.
     */
    constructor(IERC20 _fomoToken, uint256 _rewardRate) {
        require(address(_fomoToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        fomoToken = _fomoToken;
        rewardRate = _rewardRate;
        admin = msg.sender;
    }

    /**
     * @dev Function to stake FOMO tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Update rewards before changing staked amount
        updateRewards(msg.sender);

        // Transfer tokens from the staker to the contract
        require(fomoToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staker data
        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount += amount;
        staker.lastUpdated = block.timestamp;

        // Update total staked
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake FOMO tokens and claim rewards.
     */
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "No tokens staked");

        // Update rewards before unstaking
        updateRewards(msg.sender);

        uint256 amountToUnstake = staker.stakedAmount;

        // Reset staker data
        staker.stakedAmount = 0;
        staker.rewardDebt = 0;

        // Update total staked
        totalStaked -= amountToUnstake;

        // Transfer staked tokens back to the user
        require(fomoToken.transfer(msg.sender, amountToUnstake), "Token transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Function to claim accumulated rewards.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];

        // Update rewards before claiming
        updateRewards(msg.sender);

        uint256 claimableRewards = staker.rewardDebt;
        require(claimableRewards > 0, "No rewards to claim");

        // Reset reward debt after claiming
        staker.rewardDebt = 0;

        // Transfer rewards to the user
        require(fomoToken.transfer(msg.sender, claimableRewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, claimableRewards);
    }

    /**
     * @dev Internal function to calculate and update rewards for a staker.
     * @param user Address of the staker.
     */
    function updateRewards(address user) internal {
        Staker storage staker = stakers[user];
        
        if (staker.stakedAmount > 0) {
            uint256 timeElapsed = block.timestamp - staker.lastUpdated;
            uint256 newRewards = timeElapsed * staker.stakedAmount * rewardRate / 1e18;
            staker.rewardDebt += newRewards;
        }

        staker.lastUpdated = block.timestamp;
    }

    /**
     * @dev Function to update the reward rate. Admin-only.
     * @param newRewardRate New reward rate in tokens per second.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyAdmin {
        require(newRewardRate > 0, "Reward rate must be greater than 0");
        rewardRate = newRewardRate;

        emit RewardRateUpdated(newRewardRate);
    }

    /**
     * @dev Function to get the claimable rewards for a user.
     * @param user Address of the user.
     * @return Claimable rewards.
     */
    function getClaimableRewards(address user) external view returns (uint256) {
        Staker storage staker = stakers[user];
        if (staker.stakedAmount == 0) return staker.rewardDebt;

        uint256 timeElapsed = block.timestamp - staker.lastUpdated;
        uint256 newRewards = timeElapsed * staker.stakedAmount * rewardRate / 1e18;

        return staker.rewardDebt + newRewards;
    }
}

/**
 * @dev Interface for ERC-20 tokens.
 */
interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
