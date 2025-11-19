"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbag-org.pages.dev
Prompt: Generate a smart contract for the MoonBag ($MBAG) token that includes features for staking and referral incentives as described on the MoonBag website.
Generated: DETERMINISTIC_e6aa00fda58a7d49
Batch ID: 20250612_163156
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

// Import the necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// The MoonBag token contract
contract MoonBag is ERC20, Ownable, ReentrancyGuard {
    // Staking structure
    struct Staker {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Pending rewards
        uint256 lastStakedTime; // Time of last stake
    }

    // Mapping of stakers
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward variables
    uint256 public rewardRate = 100; // Reward rate per second
    uint256 public totalRewardsDistributed;

    // Referral system
    mapping(address => address) public referrals; // Referral mapping
    mapping(address => uint256) public referralRewards; // Referral rewards
    uint256 public referralBonus = 10; // Bonus for referrers

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event ReferralPaid(address indexed referrer, uint256 reward);

    // Constructor to set the token name and symbol
    constructor() ERC20("MoonBag", "$MBAG") {
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint initial supply
    }

    // Function to stake tokens
    function stake(uint256 amount, address referrer) external nonReentrant {
        require(amount > 0, "Cannot stake 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update referral information
        if (referrals[msg.sender] == address(0) && referrer != msg.sender) {
            referrals[msg.sender] = referrer;
        }

        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        payRewards(msg.sender); // Pay any pending rewards before staking

        staker.amount += amount;
        totalStaked += amount;
        staker.lastStakedTime = block.timestamp;

        // Transfer tokens to the contract
        transfer(address(this), amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked balance");

        payRewards(msg.sender); // Pay any pending rewards before unstaking

        staker.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to pay rewards to user
    function payRewards(address user) internal {
        Staker storage staker = stakers[user];
        uint256 owed = calculateReward(user);
        if (owed > 0) {
            staker.rewardDebt += owed; // Track rewards owed
            totalRewardsDistributed += owed; // Update total rewards distributed
            
            // Transfer rewards to the user
            _mint(user, owed);
            emit RewardPaid(user, owed);

            // Handle referral rewards
            if (referrals[user] != address(0)) {
                uint256 referrerReward = (owed * referralBonus) / 100;
                referralRewards[referrals[user]] += referrerReward; // Increment referrer rewards
                emit ReferralPaid(referrals[user], referrerReward);
            }
        }
        staker.lastStakedTime = block.timestamp;
    }

    // Function to calculate rewards based on staked time
    function calculateReward(address user) public view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 stakingDuration = block.timestamp - staker.lastStakedTime;
        return (stakingDuration * rewardRate * staker.amount) / 1e18; // Calculate rewards
    }

    // Function for the owner to withdraw accumulated referral rewards
    function withdrawReferralRewards() external onlyOwner {
        uint256 amount = referralRewards[msg.sender];
        require(amount > 0, "No rewards to withdraw");
        referralRewards[msg.sender] = 0;
        _mint(msg.sender, amount); // Mint tokens for the owner
    }

    // Function to set reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to set referral bonus (only owner)
    function setReferralBonus(uint256 newBonus) external onlyOwner {
        referralBonus = newBonus;
    }

    // Function to view total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    // Function to view staker's details
    function getStakerDetails(address user) external view returns (uint256 amount, uint256 rewardDebt) {
        Staker storage staker = stakers[user];
        return (staker.amount, staker.rewardDebt);
    }
}
```
