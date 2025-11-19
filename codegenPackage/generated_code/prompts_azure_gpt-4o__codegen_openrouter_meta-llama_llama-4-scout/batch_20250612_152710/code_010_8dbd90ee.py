"""
Generated Code Metadata:
========================
Original URL: https://moonedge-finance-io.web.app
Prompt: Write a Solidity contract for a tier-based staking mechanism that unlocks exclusive VC rounds for top-tier stakers, as described in MoonEdge's Evermoon VC round.
Generated: DETERMINISTIC_8dbd90ee1c488df9
Batch ID: 20250612_152710
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TierBasedStakingContract
 * @author [Your Name]
 * @notice A tier-based staking mechanism that unlocks exclusive VC rounds for top-tier stakers.
 */
contract TierBasedStakingContract is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of tier requirements
    mapping(uint256 => TierRequirement) public tierRequirements;

    // Mapping of VC round information
    mapping(uint256 => VCRound) public vcRounds;

    // IERC20 token used for staking
    IERC20 public stakingToken;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Number of tiers
    uint256 public numTiers;

    // Number of VC rounds
    uint256 public numVCRounds;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when VC round is unlocked
    event VCRoundUnlocked(uint256 tier, uint256 vcRoundId);

    // Struct to store user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 tier;
    }

    // Struct to store tier requirements
    struct TierRequirement {
        uint256 minStakedAmount;
        uint256 vcRoundId;
    }

    // Struct to store VC round information
    struct VCRound {
        uint256 vcRoundId;
        bool isUnlocked;
    }

    /**
     * @notice Constructor
     * @param _stakingToken IERC20 token used for staking
     * @param _numTiers Number of tiers
     * @param _numVCRounds Number of VC rounds
     */
    constructor(IERC20 _stakingToken, uint256 _numTiers, uint256 _numVCRounds) {
        stakingToken = _stakingToken;
        numTiers = _numTiers;
        numVCRounds = _numVCRounds;

        // Initialize tier requirements
        for (uint256 i = 1; i <= numTiers; i++) {
            tierRequirements[i] = TierRequirement(0, 0);
        }

        // Initialize VC rounds
        for (uint256 i = 1; i <= numVCRounds; i++) {
            vcRounds[i] = VCRound(i, false);
        }
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid stake amount");

        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.add(_amount);

        // Update user staking information
        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.add(_amount);

        // Update user's tier
        uint256 newTier = getTier(userStakingInfo.stakedAmount);
        if (newTier > userStakingInfo.tier) {
            userStakingInfo.tier = newTier;

            // Unlock VC round if applicable
            if (tierRequirements[newTier].vcRoundId > 0 && !vcRounds[tierRequirements[newTier].vcRoundId].isUnlocked) {
                vcRounds[tierRequirements[newTier].vcRoundId].isUnlocked = true;
                emit VCRoundUnlocked(newTier, tierRequirements[newTier].vcRoundId);
            }
        }

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid unstake amount");

        // Check if user has sufficient staked amount
        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        require(userStakingInfo.stakedAmount >= _amount, "Insufficient staked amount");

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.sub(_amount);

        // Update user staking information
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.sub(_amount);

        // Transfer tokens from contract to user
        stakingToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Get user's tier based on staked amount
     * @param _stakedAmount Staked amount
     * @return Tier number
     */
    function getTier(uint256 _stakedAmount) public view returns (uint256) {
        for (uint256 i = numTiers; i > 0; i--) {
            if (_stakedAmount >= tierRequirements[i].minStakedAmount) {
                return i;
            }
        }
        return 0;
    }

    /**
     * @notice Update tier requirement
     * @param _tier Tier number
     * @param _minStakedAmount Minimum staked amount required for tier
     * @param _vcRoundId VC round ID
     */
    function updateTierRequirement(uint256 _tier, uint256 _minStakedAmount, uint256 _vcRoundId) external {
        require(_tier > 0 && _tier <= numTiers, "Invalid tier");
        require(_vcRoundId > 0 && _vcRoundId <= numVCRounds, "Invalid VC round ID");

        tierRequirements[_tier].minStakedAmount = _minStakedAmount;
        tierRequirements[_tier].vcRoundId = _vcRoundId;
    }

    /**
     * @notice Get VC round information
     * @param _vcRoundId VC round ID
     * @return VCRound struct
     */
    function getVCRound(uint256 _vcRoundId) external view returns (VCRound memory) {
        return vcRounds[_vcRoundId];
    }
}
```
