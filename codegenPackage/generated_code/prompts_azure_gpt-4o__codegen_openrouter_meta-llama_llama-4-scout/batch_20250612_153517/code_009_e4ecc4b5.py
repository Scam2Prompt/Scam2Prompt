"""
Generated Code Metadata:
========================
Original URL: https://monarch-game.pages.dev
Prompt: Write a Solidity contract to implement staking functionality for dragon holders, allowing them to earn `$LEGACY` tokens and claim add-ons.
Generated: DETERMINISTIC_e4ecc4b5b66a8db2
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Dragon Staking Contract
 * @author [Your Name]
 * @notice This contract allows dragon holders to stake their dragons and earn $LEGACY tokens.
 */
contract DragonStaking is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of dragon owners to their staking information
    mapping(address => Staker) public stakers;

    // Mapping of dragon IDs to their staking status
    mapping(uint256 => bool) public stakedDragons;

    // $LEGACY token contract
    IERC20 public legacyToken;

    // Dragon NFT contract
    IERC721 public dragonNFT;

    // Staking duration in seconds
    uint256 public stakingDuration;

    // $LEGACY token reward per second
    uint256 public rewardPerSecond;

    // Add-on rewards
    mapping(uint256 => AddonReward) public addonRewards;

    // Event emitted when a dragon is staked
    event DragonStaked(address indexed owner, uint256 indexed dragonId);

    // Event emitted when a dragon is unstaked
    event DragonUnstaked(address indexed owner, uint256 indexed dragonId);

    // Event emitted when a staker claims $LEGACY tokens
    event LegacyTokensClaimed(address indexed owner, uint256 amount);

    // Event emitted when a staker claims an add-on reward
    event AddonRewardClaimed(address indexed owner, uint256 indexed dragonId, uint256 rewardId);

    /**
     * @param _legacyToken $LEGACY token contract
     * @param _dragonNFT Dragon NFT contract
     * @param _stakingDuration Staking duration in seconds
     * @param _rewardPerSecond $LEGACY token reward per second
     */
    constructor(
        IERC20 _legacyToken,
        IERC721 _dragonNFT,
        uint256 _stakingDuration,
        uint256 _rewardPerSecond
    ) {
        legacyToken = _legacyToken;
        dragonNFT = _dragonNFT;
        stakingDuration = _stakingDuration;
        rewardPerSecond = _rewardPerSecond;
    }

    /**
     * @dev Stake a dragon
     * @param _dragonId Dragon ID
     */
    function stakeDragon(uint256 _dragonId) public {
        require(dragonNFT.ownerOf(_dragonId) == msg.sender, "Only the dragon owner can stake");
        require(!stakedDragons[_dragonId], "Dragon is already staked");

        stakedDragons[_dragonId] = true;
        stakers[msg.sender].stakedDragons.push(_dragonId);
        stakers[msg.sender].stakingStartTime = block.timestamp;

        emit DragonStaked(msg.sender, _dragonId);
    }

    /**
     * @dev Unstake a dragon
     * @param _dragonId Dragon ID
     */
    function unstakeDragon(uint256 _dragonId) public {
        require(stakedDragons[_dragonId], "Dragon is not staked");
        require(dragonNFT.ownerOf(_dragonId) == msg.sender, "Only the dragon owner can unstake");

        stakedDragons[_dragonId] = false;
        stakers[msg.sender].earnedLegacy = stakers[msg.sender].earnedLegacy.add(
            rewardPerSecond.mul(block.timestamp.sub(stakers[msg.sender].stakingStartTime))
        );
        stakers[msg.sender].stakingStartTime = 0;

        emit DragonUnstaked(msg.sender, _dragonId);
    }

    /**
     * @dev Claim $LEGACY tokens
     */
    function claimLegacyTokens() public {
        uint256 legacyTokens = stakers[msg.sender].earnedLegacy;
        require(legacyTokens > 0, "No $LEGACY tokens to claim");

        stakers[msg.sender].earnedLegacy = 0;
        legacyToken.safeTransfer(msg.sender, legacyTokens);

        emit LegacyTokensClaimed(msg.sender, legacyTokens);
    }

    /**
     * @dev Claim an add-on reward for a staked dragon
     * @param _dragonId Dragon ID
     * @param _rewardId Add-on reward ID
     */
    function claimAddonReward(uint256 _dragonId, uint256 _rewardId) public {
        require(stakedDragons[_dragonId], "Dragon is not staked");
        require(addonRewards[_rewardId].reward > 0, "Invalid add-on reward");

        AddonReward memory reward = addonRewards[_rewardId];
        stakers[msg.sender].claimedAddons.push(_rewardId);
        legacyToken.safeTransfer(msg.sender, reward.reward);

        emit AddonRewardClaimed(msg.sender, _dragonId, _rewardId);
    }

    // Struct to represent a staker
    struct Staker {
        uint256[] stakedDragons;
        uint256 stakingStartTime;
        uint256 earnedLegacy;
        uint256[] claimedAddons;
    }

    // Struct to represent an add-on reward
    struct AddonReward {
        uint256 reward;
        uint256[] eligibleDragons;
    }

    // Update the $LEGACY token reward per second
    function updateRewardPerSecond(uint256 _newRewardPerSecond) public onlyOwner {
        rewardPerSecond = _newRewardPerSecond;
    }

    // Update the staking duration
    function updateStakingDuration(uint256 _newStakingDuration) public onlyOwner {
        stakingDuration = _newStakingDuration;
    }

    // Add an add-on reward
    function addAddonReward(uint256 _rewardId, uint256 _reward, uint256[] memory _eligibleDragons) public onlyOwner {
        addonRewards[_rewardId] = AddonReward(_reward, _eligibleDragons);
    }
}
```
