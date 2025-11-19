"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moon-bag-claim.pages.dev
Prompt: Generate a smart contract for the MoonBag ($MBAG) token that includes features for staking and referral incentives as described on the MoonBag website.
Generated: DETERMINISTIC_e6aa00fda58a7d49
Batch ID: 20250612_155229
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean and production-ready Solidity smart contract code implementing a MoonBag ($MBAG) token with staking and referral incentives:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title MoonBag Token (MBAG) with Staking and Referral Incentives
 * @dev ERC20 implementation with staking and referral features.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MoonBagToken is ERC20, Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 amount;      // Amount of tokens staked
        uint256 timestamp;   // Time when the user started staking
    }

    // Mapping to store staking information per user
    mapping(address => Stake) public stakes;

    // Mapping to store referral rewards per user
    mapping(address => uint256) public referralRewards;

    // Staking reward rate (percentage per year, scaled by 1e2, e.g., 500 = 5%)
    uint256 public stakingRewardRate;
    
    // Referral reward rate (percentage, scaled by 1e2, e.g., 100 = 1%)
    uint256 public referralRewardRate;
    
    // Event to log staking activity
    event Staked(address indexed user, uint256 amount);
    
    // Event to log unstaking activity
    event Unstaked(address indexed user, uint256 amount);
    
    // Event to log referral reward distribution
    event ReferralReward(address indexed referrer, uint256 amount);

    /**
     * @dev Constructor for the MoonBagToken contract.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _initialSupply Initial total supply of the token.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _initialSupply,
        uint256 _stakingRewardRate,
        uint256 _referralRewardRate
    ) ERC20(_name, _symbol) {
        _mint(msg.sender, _initialSupply * (10**decimals())); // Mint initial supply to contract owner
        stakingRewardRate = _stakingRewardRate;
        referralRewardRate = _referralRewardRate;
    }

    /**
     * @dev Stake tokens into the contract to earn rewards.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        _transfer(msg.sender, address(this), amount); // Transfer tokens to contract

        // Update staking data
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            // Calculate and update rewards for existing stake
            uint256 pendingReward = calculateStakingReward(msg.sender);
            userStake.amount += pendingReward; // Compound reward
        }
        
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 reward = calculateStakingReward(msg.sender);
        uint256 totalAmount = userStake.amount + reward;

        // Reset staking data
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer tokens back to user
        _transfer(address(this), msg.sender, totalAmount);

        emit Unstaked(msg.sender, totalAmount);
    }

    /**
     * @dev Calculate staking rewards for a user.
     * @param user Address of the staker.
     * @return reward Amount of reward earned.
     */
    function calculateStakingReward(address user) public view returns (uint256 reward) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.timestamp; // Duration in seconds
        reward = (userStake.amount * stakingRewardRate * stakingDuration) / (365 days * 10000); // Annualized reward
    }

    /**
     * @dev Distribute referral rewards to the referrer.
     * @param referrer Address of the referrer.
     * @param amount Amount of tokens involved in the referral.
     */
    function distributeReferralReward(address referrer, uint256 amount) external {
        require(referrer != address(0), "Invalid referrer address");
        require(amount > 0, "Referral amount must be greater than zero");

        uint256 reward = (amount * referralRewardRate) / 10000; // Calculate referral reward
        referralRewards[referrer] += reward;

        _mint(referrer, reward); // Mint tokens as reward for the referrer

        emit ReferralReward(referrer, reward);
    }

    /**
     * @dev Update staking reward rate. Callable only by the contract owner.
     * @param _stakingRewardRate New staking reward rate.
     */
    function setStakingRewardRate(uint256 _stakingRewardRate) external onlyOwner {
        stakingRewardRate = _stakingRewardRate;
    }

    /**
     * @dev Update referral reward rate. Callable only by the contract owner.
     * @param _referralRewardRate New referral reward rate.
     */
    function setReferralRewardRate(uint256 _referralRewardRate) external onlyOwner {
        referralRewardRate = _referralRewardRate;
    }
}
```

### Key Features:
- ERC20-based token with staking and referral incentive mechanisms.
- Staking rewards are calculated based on annual percentage yield (APY).
- Referral incentives are distributed by minting new tokens as rewards.
- Includes owner-only functions for adjusting reward rates.
