"""
Generated Code Metadata:
========================
Original URL: https://growtoken.xyz
Prompt: Create a smart contract that allows users to stake their assets within the GROW DAO platform, ensuring transparency and community governance.
Generated: DETERMINISTIC_48e4c728fe879e4d
Batch ID: 20250612_162526
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Pausable.sol";

/**
 * @title GROW DAO Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake their assets within the GROW DAO platform.
 */
contract GrowDAOSTaking is Ownable, Pausable {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of asset staking information
    mapping(address => AssetStakingInfo) public assetStakingInfos;

    // Event emitted when a user stakes assets
    event Staked(address indexed user, address indexed asset, uint256 amount);

    // Event emitted when a user unstakes assets
    event Unstaked(address indexed user, address indexed asset, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 rewards);

    // Struct to store user staking information
    struct UserStakingInfo {
        mapping(address => uint256) stakedAssets; // Mapping of staked assets
        uint256 totalStaked; // Total staked amount
    }

    // Struct to store asset staking information
    struct AssetStakingInfo {
        uint256 totalStaked; // Total staked amount
        uint256 rewardsPerShare; // Rewards per share
    }

    // List of supported assets
    address[] public supportedAssets;

    /**
     * @notice Constructor
     * @param _supportedAssets List of supported assets
     */
    constructor(address[] memory _supportedAssets) public {
        require(_supportedAssets.length > 0, "At least one supported asset is required");

        // Initialize supported assets
        for (uint256 i = 0; i < _supportedAssets.length; i++) {
            supportedAssets.push(_supportedAssets[i]);
            assetStakingInfos[_supportedAssets[i]] = AssetStakingInfo(0, 0);
        }
    }

    /**
     * @notice Stake assets
     * @param _asset Asset to stake
     * @param _amount Amount to stake
     */
    function stake(address _asset, uint256 _amount) public whenNotPaused {
        require(supportedAssets.contains(_asset), "Unsupported asset");
        require(_amount > 0, "Stake amount must be greater than zero");

        // Update user staking information
        userStakingInfos[msg.sender].stakedAssets[_asset] = userStakingInfos[msg.sender].stakedAssets[_asset].add(_amount);
        userStakingInfos[msg.sender].totalStaked = userStakingInfos[msg.sender].totalStaked.add(_amount);

        // Update asset staking information
        assetStakingInfos[_asset].totalStaked = assetStakingInfos[_asset].totalStaked.add(_amount);

        // Transfer staked assets to contract
        IERC20(_asset).transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _asset, _amount);
    }

    /**
     * @notice Unstake assets
     * @param _asset Asset to unstake
     * @param _amount Amount to unstake
     */
    function unstake(address _asset, uint256 _amount) public whenNotPaused {
        require(supportedAssets.contains(_asset), "Unsupported asset");
        require(userStakingInfos[msg.sender].stakedAssets[_asset] >= _amount, "Insufficient staked assets");
        require(_amount > 0, "Unstake amount must be greater than zero");

        // Update user staking information
        userStakingInfos[msg.sender].stakedAssets[_asset] = userStakingInfos[msg.sender].stakedAssets[_asset].sub(_amount);
        userStakingInfos[msg.sender].totalStaked = userStakingInfos[msg.sender].totalStaked.sub(_amount);

        // Update asset staking information
        assetStakingInfos[_asset].totalStaked = assetStakingInfos[_asset].totalStaked.sub(_amount);

        // Transfer unstaked assets to user
        IERC20(_asset).transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _asset, _amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() public whenNotPaused {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update user staking information
        userStakingInfos[msg.sender].totalStaked = 0;

        // Transfer rewards to user
        IERC20(supportedAssets[0]).transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Calculate rewards for a user
     * @param _user User to calculate rewards for
     * @return Rewards for the user
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        uint256 rewards = 0;
        for (uint256 i = 0; i < supportedAssets.length; i++) {
            rewards = rewards.add(userStakingInfos[_user].stakedAssets[supportedAssets[i]].mul(assetStakingInfos[supportedAssets[i]].rewardsPerShare));
        }
        return rewards;
    }

    /**
     * @notice Update rewards per share for an asset
     * @param _asset Asset to update rewards per share for
     * @param _rewardsPerShare New rewards per share
     */
    function updateRewardsPerShare(address _asset, uint256 _rewardsPerShare) public onlyOwner {
        require(supportedAssets.contains(_asset), "Unsupported asset");

        assetStakingInfos[_asset].rewardsPerShare = _rewardsPerShare;
    }

    /**
     * @notice Pause the contract
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @notice Unpause the contract
     */
    function unpause() public onlyOwner {
        _unpause();
    }
}

library Address {
    function contains(address[] memory _array, address _value) internal pure returns (bool) {
        for (uint256 i = 0; i < _array.length; i++) {
            if (_array[i] == _value) {
                return true;
            }
        }
        return false;
    }
}
```
