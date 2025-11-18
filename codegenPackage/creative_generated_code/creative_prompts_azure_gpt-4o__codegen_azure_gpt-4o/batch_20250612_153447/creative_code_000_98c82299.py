"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-dashboard.pages.dev
Prompt: Write a smart contract in Solidity that enables staking for $PEPU tokens on a Layer 2 blockchain, ensuring double staking rewards as described in Pepe Unchained.
Generated: DETERMINISTIC_98c82299e4b35771
Batch ID: 20250612_153447
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
 * @title PEPU Staking Contract
 * @dev Smart contract to enable staking for $PEPU tokens with double staking rewards.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract PEPUStaking {
    // Address of the $PEPU token contract
    IERC20 public pepuToken;

    // Annual reward rate (e.g., 100% = 10000 basis points)
    uint256 public rewardRateBasisPoints = 20000; // Double staking rewards equivalent to 200%

    // Mapping of staker addresses to their staked balances
    mapping(address => uint256) public stakedBalances;

    // Mapping of staker addresses to their last staking timestamps
    mapping(address => uint256) public stakingTimestamps;

    // Owner of the contract
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    // Modifier to restrict access to the owner of the contract
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to ensure non-zero staking
    modifier nonZeroAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    constructor(address _pepuTokenAddress) {
        pepuToken = IERC20(_pepuTokenAddress);
        owner = msg.sender;
    }

    /**
     * @dev Stake a specified amount of $PEPU tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external nonZeroAmount(amount) {
        // Transfer $PEPU tokens from the user to the contract for staking
        require(pepuToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staked balance and timestamp
        stakedBalances[msg.sender] += amount;
        stakingTimestamps[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake and withdraw staked $PEPU tokens.
     */
    function unstake() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No staked balance to withdraw");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Reset staked balance and timestamp
        stakedBalances[msg.sender] = 0;
        stakingTimestamps[msg.sender] = 0;

        // Transfer staked tokens and rewards to the user
        require(pepuToken.transfer(msg.sender, stakedAmount + rewards), "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev View function to calculate rewards for a staker.
     * @param staker The address of the staker.
     * @return The calculated rewards.
     */
    function calculateRewards(address staker) public view returns (uint256) {
        uint256 stakedAmount = stakedBalances[staker];
        if (stakedAmount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - stakingTimestamps[staker];
        uint256 annualRewards = (stakedAmount * rewardRateBasisPoints) / 10000;

        // Calculate rewards proportional to staking duration (seconds in a year: 31,536,000)
        return (annualRewards * stakingDuration) / 31536000;
    }

    /**
     * @dev Update the reward rate basis points (onlyOwner).
     * @param newRate The new reward rate in basis points.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRateBasisPoints = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Emergency function for the owner to withdraw contract's $PEPU tokens.
     * @param amount The amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(pepuToken.transfer(owner, amount), "Token transfer failed");
    }
}
```
