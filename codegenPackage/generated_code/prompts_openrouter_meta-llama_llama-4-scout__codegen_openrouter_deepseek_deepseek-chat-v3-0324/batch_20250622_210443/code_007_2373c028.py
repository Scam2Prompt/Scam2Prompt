"""
Generated Code Metadata:
========================
Original URL: https://tradecurvemarket-en.pages.dev
Prompt: "Generate a smart contract in Solidity for the Tradecurve ecosystem that handles TCRV token utilities, including rewards, staking, and discounts on trading transactions, deployable on the Ethereum network."
Generated: DETERMINISTIC_2373c0286f1f9314
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract TCRVUtilities is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Token contract
    IERC20 public tcrvToken;

    // Staking variables
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
    }

    mapping(address => Stake) public stakes;
    uint256 public totalStaked;
    uint256 public stakingRewardRate = 10; // 10% annual reward
    uint256 public constant SECONDS_IN_YEAR = 31536000;

    // Trading discount variables
    uint256 public discountTier1 = 1000 * 10**18; // 1,000 TCRV
    uint256 public discountTier2 = 5000 * 10**18; // 5,000 TCRV
    uint256 public discountTier3 = 10000 * 10**18; // 10,000 TCRV
    uint256 public discountRateTier1 = 5; // 5%
    uint256 public discountRateTier2 = 10; // 10%
    uint256 public discountRateTier3 = 15; // 15%

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event DiscountApplied(address indexed user, uint256 discountRate);

    constructor(address _tcrvToken) {
        require(_tcrvToken != address(0), "Invalid token address");
        tcrvToken = IERC20(_tcrvToken);
    }

    // Staking functions
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(tcrvToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Claim any existing rewards before staking
        if (stakes[msg.sender].amount > 0) {
            _claimReward();
        }

        tcrvToken.safeTransferFrom(msg.sender, address(this), amount);
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].stakedAt = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Claim rewards before unstaking
        _claimReward();

        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;
        tcrvToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    function claimReward() external nonReentrant {
        require(stakes[msg.sender].amount > 0, "No staked amount");
        _claimReward();
    }

    function _claimReward() private {
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            stakes[msg.sender].stakedAt = block.timestamp;
            tcrvToken.safeTransfer(msg.sender, reward);
            emit RewardClaimed(msg.sender, reward);
        }
    }

    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.stakedAt;
        uint256 reward = (userStake.amount * stakingRewardRate * stakingDuration) / 
                        (SECONDS_IN_YEAR * 100);
        return reward;
    }

    // Trading discount functions
    function getTradingDiscount(address user) external returns (uint256) {
        uint256 balance = tcrvToken.balanceOf(user);
        uint256 discountRate = 0;

        if (balance >= discountTier3) {
            discountRate = discountRateTier3;
        } else if (balance >= discountTier2) {
            discountRate = discountRateTier2;
        } else if (balance >= discountTier1) {
            discountRate = discountRateTier1;
        }

        emit DiscountApplied(user, discountRate);
        return discountRate;
    }

    // Admin functions
    function setStakingRewardRate(uint256 newRate) external onlyOwner {
        require(newRate <= 100, "Rate cannot exceed 100%");
        stakingRewardRate = newRate;
    }

    function setDiscountTiers(
        uint256 tier1,
        uint256 tier2,
        uint256 tier3
    ) external onlyOwner {
        require(tier1 < tier2 && tier2 < tier3, "Invalid tier values");
        discountTier1 = tier1;
        discountTier2 = tier2;
        discountTier3 = tier3;
    }

    function setDiscountRates(
        uint256 rate1,
        uint256 rate2,
        uint256 rate3
    ) external onlyOwner {
        require(rate1 < rate2 && rate2 < rate3, "Invalid rate values");
        require(rate3 <= 50, "Maximum discount rate is 50%");
        discountRateTier1 = rate1;
        discountRateTier2 = rate2;
        discountRateTier3 = rate3;
    }

    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(tcrvToken) || 
                tcrvToken.balanceOf(address(this)) - totalStaked >= amount,
                "Cannot withdraw staked tokens");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
