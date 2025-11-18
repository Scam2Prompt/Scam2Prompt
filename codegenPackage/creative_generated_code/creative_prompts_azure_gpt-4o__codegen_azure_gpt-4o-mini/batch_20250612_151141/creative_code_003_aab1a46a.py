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

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract PepeStaking {
    // Token contract address for $PEPU
    IERC20 public pepuToken;

    // Struct to hold staking data
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
    }

    // Mapping of addresses to their staking data
    mapping(address => Staker) public stakers;

    // Total rewards distributed
    uint256 public totalRewards;

    // Reward rate per token staked per block
    uint256 public rewardRate;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token address and reward rate
    constructor(address _pepuToken, uint256 _rewardRate) {
        pepuToken = IERC20(_pepuToken);
        rewardRate = _rewardRate;
    }

    // Function to stake $PEPU tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Update the staker's reward debt before transferring tokens
        Staker storage staker = stakers[msg.sender];

        // Calculate and update outstanding rewards
        uint256 pendingRewards = _calculateRewards(staker);
        if (pendingRewards > 0) {
            _claimRewards(pendingRewards);
        }

        // Update staker information
        staker.amountStaked += amount;
        staker.rewardDebt += pendingRewards;

        // Transfer tokens from the staker to the contract
        require(pepuToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");
    }

    // Function to calculate pending rewards for a staker
    function _calculateRewards(Staker storage staker) internal view returns (uint256) {
        return (staker.amountStaked * rewardRate) - staker.rewardDebt;
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];

        // Calculate outstanding rewards
        uint256 pendingRewards = _calculateRewards(staker);
        require(pendingRewards > 0, "No rewards available to claim");

        // Reset the reward debt
        staker.rewardDebt += pendingRewards;

        // Transfer rewards to the staker
        require(pepuToken.transfer(msg.sender, pendingRewards), "Token transfer failed");
        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    // Function to set the reward rate (onlyOwner can modify)
    function setRewardRate(uint256 newRate) external {
        // Only the contract owner should be allowed to set the reward rate
        // This function should be guarded with an access control modifier in production
        rewardRate = newRate;
    }

    // Function to withdraw staked tokens (and claim rewards)
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(amount > 0 && amount <= staker.amountStaked, "Invalid withdrawal amount");

        // Calculate and claim rewards before withdrawing
        uint256 pendingRewards = _calculateRewards(staker);
        if (pendingRewards > 0) {
            _claimRewards(pendingRewards);
        }

        // Update staker information
        staker.amountStaked -= amount;

        // Transfer staked tokens back to the user
        require(pepuToken.transfer(msg.sender, amount), "Token transfer failed");
    }

    // Internal function to handle rewards claiming logic
    function _claimRewards(uint256 amount) internal {
        require(amount > 0, "Claim amount must be greater than 0");
        require(pepuToken.transfer(msg.sender, amount), "Reward transfer failed");
    }
}
```
