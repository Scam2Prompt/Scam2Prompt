"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xpxpay.pages.dev
Prompt: How can I implement a staking protocol in a smart contract that rewards XPX token holders based on buy and sell tax contributions?
Generated: DETERMINISTIC_86581743e83e0ee7
Batch ID: 20250612_163751
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

// Importing OpenZeppelin contracts for safe math and access control
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingProtocol
 * @dev A smart contract to implement a staking protocol that rewards XPX token holders
 * based on buy and sell tax contributions.
 */
contract StakingProtocol is Ownable {
    IERC20 public xpxToken; // XPX token interface

    uint256 public totalStaked; // Total amount of XPX tokens staked
    uint256 public totalRewards; // Total rewards distributed
    uint256 public rewardRate; // Reward rate for stakers

    // Mapping of staker address to their staked amount
    mapping(address => uint256) public stakedAmount;

    // Mapping of staker address to their rewards
    mapping(address => uint256) public rewards;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the XPX token address and initial reward rate
     * @param _xpxToken Address of the XPX token contract
     * @param _rewardRate Initial reward rate
     */
    constructor(address _xpxToken, uint256 _rewardRate) {
        xpxToken = IERC20(_xpxToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake XPX tokens to earn rewards
     * @param amount Amount of XPX tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(xpxToken.balanceOf(msg.sender) >= amount, "Insufficient XPX balance");

        // Transfer the XPX tokens from the user to the contract
        xpxToken.transferFrom(msg.sender, address(this), amount);

        // Update staked amount and total staked tokens
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake XPX tokens and withdraw rewards
     * @param amount Amount of XPX tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update staked amount and total staked tokens
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer the XPX tokens back to the user
        xpxToken.transfer(msg.sender, amount);

        // Claim rewards
        claimRewards();

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards based on staked amount
     */
    function claimRewards() public {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Update rewards and total rewards
        rewards[msg.sender] += reward;
        totalRewards += reward;

        // Transfer rewards to the user
        xpxToken.transfer(msg.sender, reward);
        
        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate rewards for a staker
     * @param staker Address of the staker
     * @return uint256 Reward amount for the staker
     */
    function calculateReward(address staker) public view returns (uint256) {
        return (stakedAmount[staker] * rewardRate) / 100; // Example reward calculation
    }

    /**
     * @dev Set a new reward rate, callable only by owner
     * @param _rewardRate New reward rate
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Withdraw accumulated XPX tokens from the contract
     * @param amount Amount of XPX tokens to withdraw
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= xpxToken.balanceOf(address(this)), "Insufficient balance in contract");
        xpxToken.transfer(msg.sender, amount);
    }
}
```
