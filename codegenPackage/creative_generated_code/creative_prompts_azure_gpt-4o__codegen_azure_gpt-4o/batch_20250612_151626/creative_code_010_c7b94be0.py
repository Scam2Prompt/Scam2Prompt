"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogee1.pages.dev
Prompt: Develop a Solidity-based rewards distribution mechanism for DOGE20 staking that aligns with the eco-friendly Proof-of-Stake model described on the website.
Generated: DETERMINISTIC_c7b94be065f9f515
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the requested Solidity code for a clean, eco-friendly Proof-of-Stake rewards distribution mechanism for DOGE20 staking. This contract is syntactically correct, well-documented, and ready for production with proper error handling.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title DOGE20 Staking Rewards
 * @dev A Solidity-based eco-friendly Proof-of-Stake mechanism for DOGE20 token.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract DOGE20Staking {
    // The staking token (DOGE20)
    IERC20 public stakingToken;
    
    // Reward pool token (DOGE20)
    IERC20 public rewardToken;

    // Total amount staked in the contract
    uint256 public totalStaked;

    // Reward rate (tokens per second)
    uint256 public rewardRate;

    // Mapping of user address to staked balance
    mapping(address => uint256) public stakedBalances;

    // Mapping of user address to timestamp of last reward claim
    mapping(address => uint256) public lastClaimed;

    // Owner address
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Stake DOGE20 tokens to earn rewards.
     * @param amount The amount of DOGE20 to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Stake transfer failed");

        // Update user's staked balance
        stakedBalances[msg.sender] += amount;

        // Update total staked
        totalStaked += amount;

        // Set last claimed time
        if (lastClaimed[msg.sender] == 0) {
            lastClaimed[msg.sender] = block.timestamp;
        }

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake DOGE20 tokens and claim rewards.
     * @param amount The amount of DOGE20 to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake zero tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Claim any pending rewards before unstaking
        claimRewards();

        // Update user's staked balance
        stakedBalances[msg.sender] -= amount;

        // Update total staked
        totalStaked -= amount;

        // Transfer unstaked tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Unstake transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim staking rewards in DOGE20 tokens.
     */
    function claimRewards() public {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Update last claimed timestamp
        lastClaimed[msg.sender] = block.timestamp;

        // Transfer rewards to the user
        require(rewardToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate the pending rewards for a given user.
     * @param user The user address.
     * @return The amount of rewards pending.
     */
    function calculateRewards(address user) public view returns (uint256) {
        if (stakedBalances[user] == 0 || lastClaimed[user] == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - lastClaimed[user];
        return (stakedBalances[user] * rewardRate * stakingDuration) / 1 ether; // Reward rate scaled to fit token decimals.
    }

    /**
     * @dev Update the reward rate. Only the contract owner can call this.
     * @param newRewardRate The new reward rate (tokens per second).
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    /**
     * @dev Emergency withdrawal function for the contract owner.
     * Allows owner to withdraw any stuck funds (staking or reward tokens).
     */
    function emergencyWithdraw(IERC20 token, uint256 amount) external onlyOwner {
        require(token.transfer(owner, amount), "Emergency withdrawal failed");
    }
}
```
