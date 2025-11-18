"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-eng.pages.dev
Prompt: Create a script in Solidity to calculate double staking rewards for $PEPU tokens on Pepe Unchained's Layer 2 blockchain.
Generated: DETERMINISTIC_aab1a46a8db27bea
Batch ID: 20250612_151141
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
 * @title Double Staking Rewards for $PEPU Tokens
 * @dev This contract calculates and distributes double staking rewards for $PEPU tokens 
 * on Pepe Unchained's Layer 2 blockchain.
 */
contract DoubleStakingRewards {
    // Mapping to store the staked balances of each user
    mapping(address => uint256) public stakedBalances;

    // Mapping to store the rewards of each user
    mapping(address => uint256) public rewards;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate for staking (e.g., annual percentage rate divided by time period)
    uint256 public rewardRate;

    // $PEPU token contract address
    address public pepuToken;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor sets the $PEPU token contract address and reward rate.
     * @param _pepuToken Address of the $PEPU token contract
     * @param _rewardRate Reward rate for staking calculations
     */
    constructor(address _pepuToken, uint256 _rewardRate) {
        require(_pepuToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        pepuToken = _pepuToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake $PEPU tokens into the contract to earn rewards.
     * @param amount Number of $PEPU tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer $PEPU tokens from the caller to the contract
        IERC20(pepuToken).transferFrom(msg.sender, address(this), amount);

        // Update staked balance and total staked
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake $PEPU tokens and withdraw them to the sender's address.
     * @param amount Number of $PEPU tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance and total staked
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer $PEPU tokens back to the caller
        IERC20(pepuToken).transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Calculate and distribute double staking rewards for the caller.
     */
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        // Update rewards balance
        rewards[msg.sender] = 0;

        // Double the reward
        uint256 doubleReward = reward * 2;

        // Transfer the double reward to the caller
        IERC20(pepuToken).transfer(msg.sender, doubleReward);

        emit RewardsClaimed(msg.sender, doubleReward);
    }

    /**
     * @dev Internal function to calculate staking rewards for a user.
     * @param user Address of the user
     * @return Rewards amount calculated
     */
    function calculateRewards(address user) internal view returns (uint256) {
        uint256 stakedAmount = stakedBalances[user];
        return stakedAmount * rewardRate / 100; // Example reward calculation
    }

    /**
     * @dev View function to get the current rewards for a user.
     * @param user Address of the user
     * @return Current rewards for the user
     */
    function viewRewards(address user) external view returns (uint256) {
        return calculateRewards(user);
    }
}

/**
 * @dev Minimal IERC20 interface for $PEPU token operations.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
