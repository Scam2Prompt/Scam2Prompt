"""
Generated Code Metadata:
========================
Original URL: https://tokencatgirl.pages.dev
Prompt: Write a smart contract in Solidity for staking CATGIRL¢ tokens, incorporating features mentioned in the Catgirl ecosystem, such as rewards tied to NFT collectibles.
Generated: DETERMINISTIC_9339f630d91b8268
Batch ID: 20250612_153606
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Catgirl Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake CATGIRL tokens and earn rewards based on NFT collectibles.
 */
contract CatgirlStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfos;

    // Mapping of NFT rewards
    mapping (uint256 => NFTReward) public nftRewards;

    // CATGIRL token contract
    ERC20 public catgirlToken;

    // NFT contract
    IERC721 public nftContract;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward token contract (if different from CATGIRL)
    ERC20 public rewardToken;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    // Event emitted when NFT reward is added
    event NFTRewardAdded(uint256 nftId, uint256 rewardAmount);

    // Event emitted when NFT reward is removed
    event NFTRewardRemoved(uint256 nftId);

    /**
     * @param _catgirlToken CATGIRL token contract address
     * @param _nftContract NFT contract address
     * @param _rewardToken Reward token contract address (optional)
     */
    constructor(
        address _catgirlToken,
        address _nftContract,
        address _rewardToken
    ) public {
        require(_catgirlToken != address(0), "Invalid CATGIRL token address");
        require(_nftContract != address(0), "Invalid NFT contract address");

        catgirlToken = ERC20(_catgirlToken);
        nftContract = IERC721(_nftContract);

        if (_rewardToken != address(0)) {
            rewardToken = ERC20(_rewardToken);
        } else {
            rewardToken = catgirlToken;
        }
    }

    /**
     * @dev Stake CATGIRL tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid stake amount");
        require(catgirlToken.balanceOf(msg.sender) >= _amount, "Insufficient CATGIRL tokens");

        // Update user's staking information
        userStakingInfos[msg.sender].stakedAmount = userStakingInfos[msg.sender].stakedAmount.add(_amount);
        userStakingInfos[msg.sender].lastUpdateTime = block.timestamp;

        // Transfer tokens to contract
        catgirlToken.transferFrom(msg.sender, address(this), _amount);

        // Update total staked tokens
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake CATGIRL tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid unstake amount");
        require(userStakingInfos[msg.sender].stakedAmount >= _amount, "Insufficient staked tokens");

        // Update user's staking information
        userStakingInfos[msg.sender].stakedAmount = userStakingInfos[msg.sender].stakedAmount.sub(_amount);
        userStakingInfos[msg.sender].lastUpdateTime = block.timestamp;

        // Transfer tokens to user
        catgirlToken.transfer(msg.sender, _amount);

        // Update total staked tokens
        totalStaked = totalStaked.sub(_amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);

        // Update user's staking information
        userStakingInfos[msg.sender].lastUpdateTime = block.timestamp;

        // Transfer rewards to user
        rewardToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate rewards for user
     * @param _user User address
     * @return Rewards amount
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        uint256 stakedAmount = userStakingInfos[_user].stakedAmount;
        uint256 lastUpdateTime = userStakingInfos[_user].lastUpdateTime;

        // Calculate base rewards
        uint256 baseRewards = stakedAmount.mul(block.timestamp.sub(lastUpdateTime)).mul(1e18);

        // Calculate NFT rewards
        uint256 nftRewardsAmount = 0;
        for (uint256 i = 0; i < nftContract.balanceOf(_user); i++) {
            uint256 nftId = nftContract.tokenOfOwnerByIndex(_user, i);
            nftRewardsAmount = nftRewardsAmount.add(nftRewards[nftId].rewardAmount);
        }

        return baseRewards.add(nftRewardsAmount);
    }

    /**
     * @dev Add NFT reward
     * @param _nftId NFT ID
     * @param _rewardAmount Reward amount
     */
    function addNFTReward(uint256 _nftId, uint256 _rewardAmount) external {
        require(nftContract.ownerOf(_nftId) != address(0), "Invalid NFT owner");

        nftRewards[_nftId] = NFTReward(_rewardAmount);

        emit NFTRewardAdded(_nftId, _rewardAmount);
    }

    /**
     * @dev Remove NFT reward
     * @param _nftId NFT ID
     */
    function removeNFTReward(uint256 _nftId) external {
        delete nftRewards[_nftId];

        emit NFTRewardRemoved(_nftId);
    }

    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 lastUpdateTime;
    }

    struct NFTReward {
        uint256 rewardAmount;
    }
}
```
