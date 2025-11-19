"""
Generated Code Metadata:
========================
Original URL: https://decubate-platform.pages.dev
Prompt: Write a smart contract in Solidity to implement a staking mechanism similar to Decubate, allowing users to stake DCB tokens and earn rewards based on fixed and compounding APY rates, with options for NFT and tier boosts.
Generated: DETERMINISTIC_f6fd2f9464aed6e8
Batch ID: 20250612_153517
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DecubateStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Staking token
    IERC20 public stakingToken;

    // Struct to represent a staking plan
    struct Plan {
        uint256 duration; // in seconds
        uint256 apy; // in basis points (10000 = 100%)
        uint256 minStakeAmount;
        uint256 maxStakeAmount;
        bool isCompounding;
        bool isActive;
    }

    // Struct to represent a user's stake
    struct Stake {
        uint256 planId;
        uint256 amount;
        uint256 startTime;
        uint256 endTime;
        uint256 claimedRewards;
        uint256 lastClaimTime;
        bool isActive;
    }

    // Struct for tier boosts
    struct Tier {
        uint256 boostPercentage; // in basis points (10000 = 100%)
        uint256 minStakeAmount;
    }

    // NFT boost configuration
    struct NFTBoost {
        address nftContract;
        uint256 tokenId;
        uint256 boostPercentage; // in basis points (10000 = 100%)
    }

    // State variables
    Plan[] public plans;
    Tier[] public tiers;
    NFTBoost[] public nftBoosts;

    mapping(address => Stake[]) public userStakes;
    mapping(address => uint256) public userTier;

    // Events
    event Staked(address indexed user, uint256 planId, uint256 amount, uint256 stakeId);
    event Unstaked(address indexed user, uint256 stakeId, uint256 amount);
    event RewardClaimed(address indexed user, uint256 stakeId, uint256 amount);
    event PlanAdded(uint256 planId);
    event PlanUpdated(uint256 planId);
    event PlanDeactivated(uint256 planId);
    event TierAdded(uint256 tierId);
    event NFTBoostAdded(uint256 boostId);

    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
    }

    // Add a new staking plan
    function addPlan(
        uint256 _duration,
        uint256 _apy,
        uint256 _minStakeAmount,
        uint256 _maxStakeAmount,
        bool _isCompounding
    ) external onlyOwner {
        plans.push(
            Plan({
                duration: _duration,
                apy: _apy,
                minStakeAmount: _minStakeAmount,
                maxStakeAmount: _maxStakeAmount,
                isCompounding: _isCompounding,
                isActive: true
            })
        );
        emit PlanAdded(plans.length - 1);
    }

    // Update an existing staking plan
    function updatePlan(
        uint256 _planId,
        uint256 _duration,
        uint256 _apy,
        uint256 _minStakeAmount,
        uint256 _maxStakeAmount,
        bool _isCompounding
    ) external onlyOwner {
        require(_planId < plans.length, "Invalid plan ID");
        plans[_planId].duration = _duration;
        plans[_planId].apy = _apy;
        plans[_planId].minStakeAmount = _minStakeAmount;
        plans[_planId].maxStakeAmount = _maxStakeAmount;
        plans[_planId].isCompounding = _isCompounding;
        emit PlanUpdated(_planId);
    }

    // Deactivate a staking plan
    function deactivatePlan(uint256 _planId) external onlyOwner {
        require(_planId < plans.length, "Invalid plan ID");
        plans[_planId].isActive = false;
        emit PlanDeactivated(_planId);
    }

    // Add a new tier
    function addTier(uint256 _boostPercentage, uint256 _minStakeAmount) external onlyOwner {
        tiers.push(Tier({
            boostPercentage: _boostPercentage,
            minStakeAmount: _minStakeAmount
        }));
        emit TierAdded(tiers.length - 1);
    }

    // Add an NFT boost
    function addNFTBoost(address _nftContract, uint256 _tokenId, uint256 _boostPercentage) external onlyOwner {
        nftBoosts.push(NFTBoost({
            nftContract: _nftContract,
            tokenId: _tokenId,
            boostPercentage: _boostPercentage
        }));
        emit NFTBoostAdded(nftBoosts.length - 1);
    }

    // Set user tier
    function setUserTier(address _user, uint256 _tierId) external onlyOwner {
        require(_tierId < tiers.length, "Invalid tier ID");
        userTier[_user] = _tierId;
    }

    // Stake tokens
    function stake(uint256 _planId, uint256 _amount) external nonReentrant {
        require(_planId < plans.length, "Invalid plan ID");
        Plan memory plan = plans[_planId];
        require(plan.isActive, "Plan is not active");
        require(_amount >= plan.minStakeAmount, "Amount below minimum");
        require(_amount <= plan.maxStakeAmount, "Amount exceeds maximum");

        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Create new stake
        uint256 startTime = block.timestamp;
        uint256 endTime = startTime.add(plan.duration);
        
        userStakes[msg.sender].push(Stake({
            planId: _planId,
            amount: _amount,
            startTime: startTime,
            endTime: endTime,
            claimedRewards: 0,
            lastClaimTime: startTime,
            isActive: true
        }));

        emit Staked(msg.sender, _planId, _amount, userStakes[msg.sender].length - 1);
    }

    // Calculate rewards for a stake
    function calculateRewards(address _user, uint256 _stakeId) public view returns (uint256) {
        Stake memory stakeInfo = userStakes[_user][_stakeId];
        require(stakeInfo.isActive, "Stake is not active");

        Plan memory plan = plans[stakeInfo.planId];
        uint256 currentTime = block.timestamp > stakeInfo.endTime ? stakeInfo.endTime : block.timestamp;
        uint256 timeElapsed = currentTime.sub(stakeInfo.lastClaimTime);
        
        if (timeElapsed == 0) {
            return 0;
        }

        uint256 baseReward;
        if (plan.isCompounding) {
            // Compounding interest calculation
            uint256 periods = timeElapsed.div(1 days); // Daily compounding
            uint256 ratePerPeriod = plan.apy.div(365 * 100); // Daily rate in basis points
            
            uint256 principal = stakeInfo.amount;
            for (uint256 i = 0; i < periods; i++) {
                principal = principal.add(principal.mul(ratePerPeriod).div(10000));
            }
            baseReward = principal.sub(stakeInfo.amount);
        } else {
            // Simple interest calculation
            baseReward = stakeInfo.amount.mul(plan.apy).mul(timeElapsed).div(365 days).div(10000);
        }

        // Apply tier boost if applicable
        uint256 tierBoost = 0;
        if (userTier[_user] < tiers.length) {
            Tier memory tier = tiers[userTier[_user]];
            if (stakeInfo.amount >= tier.minStakeAmount) {
                tierBoost = baseReward.mul(tier.boostPercentage).div(10000);
            }
        }

        // Apply NFT boost if applicable
        uint256 nftBoost = 0;
        for (uint256 i = 0; i < nftBoosts.length; i++) {
            // In a real implementation, you would check NFT ownership here
            // This is simplified for demonstration
            nftBoost = nftBoost.add(baseReward.mul(nftBoosts[i].boostPercentage).div(10000));
        }

        return baseReward.add(tierBoost).add(nftBoost);
    }

    // Claim rewards for a stake
    function claimRewards(uint256 _stakeId) external nonReentrant {
        require(_stakeId < userStakes[msg.sender].length, "Invalid stake ID");
        Stake storage stakeInfo = userStakes[msg.sender][_stakeId];
        require(stakeInfo.isActive, "Stake is not active");

        uint256 rewards = calculateRewards(msg.sender, _stakeId);
        require(rewards >
