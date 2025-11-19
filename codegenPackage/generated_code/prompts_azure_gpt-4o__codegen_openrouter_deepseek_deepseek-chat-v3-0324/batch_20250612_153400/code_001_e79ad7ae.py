"""
Generated Code Metadata:
========================
Original URL: https://merlion.pages.dev
Prompt: Generate a Solidity smart contract for staking NFTs in the Merlin ecosystem, incorporating features like reward distribution based on Star Points.
Generated: DETERMINISTIC_e79ad7ae4d019a71
Batch ID: 20250612_153400
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract MerlinStaking is ReentrancyGuard, Ownable {
    using SafeMath for uint256;

    // Interface for the NFT contract
    IERC721 public nftContract;

    // Struct to store staker information
    struct Staker {
        uint256[] tokenIds; // Array of staked token IDs
        uint256 totalStarPoints; // Total Star Points accumulated
        uint256 lastClaimTime; // Last time rewards were claimed
        uint256 unclaimedRewards; // Amount of unclaimed rewards
    }

    // Mapping from staker address to their info
    mapping(address => Staker) public stakers;

    // Mapping from token ID to owner address
    mapping(uint256 => address) public tokenOwner;

    // Reward rate per Star Point per second
    uint256 public rewardRate;

    // Star Points mapping for each token ID
    mapping(uint256 => uint256) public tokenStarPoints;

    // Total Star Points staked in the contract
    uint256 public totalStarPointsStaked;

    // Events
    event Staked(address indexed user, uint256[] tokenIds);
    event Unstaked(address indexed user, uint256[] tokenIds);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event StarPointsUpdated(uint256 tokenId, uint256 starPoints);

    constructor(address _nftContract, uint256 _rewardRate) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake NFTs into the contract
     * @param tokenIds Array of NFT token IDs to stake
     */
    function stake(uint256[] calldata tokenIds) external nonReentrant {
        require(tokenIds.length > 0, "No token IDs provided");

        Staker storage staker = stakers[msg.sender];

        // Calculate rewards before updating the staker's info
        if (staker.totalStarPoints > 0) {
            uint256 rewards = calculateRewards(msg.sender);
            staker.unclaimedRewards = staker.unclaimedRewards.add(rewards);
        }

        // Transfer NFTs and update staker info
        for (uint256 i = 0; i < tokenIds.length; i++) {
            uint256 tokenId = tokenIds[i];
            require(nftContract.ownerOf(tokenId) == msg.sender, "Not the owner");
            require(tokenOwner[tokenId] == address(0), "Token already staked");

            nftContract.transferFrom(msg.sender, address(this), tokenId);
            tokenOwner[tokenId] = msg.sender;
            staker.tokenIds.push(tokenId);
            staker.totalStarPoints = staker.totalStarPoints.add(tokenStarPoints[tokenId]);
            totalStarPointsStaked = totalStarPointsStaked.add(tokenStarPoints[tokenId]);
        }

        staker.lastClaimTime = block.timestamp;
        emit Staked(msg.sender, tokenIds);
    }

    /**
     * @dev Unstake NFTs from the contract
     * @param tokenIds Array of NFT token IDs to unstake
     */
    function unstake(uint256[] calldata tokenIds) external nonReentrant {
        require(tokenIds.length > 0, "No token IDs provided");

        Staker storage staker = stakers[msg.sender];
        require(staker.tokenIds.length >= tokenIds.length, "Not enough tokens staked");

        // Calculate and update rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);
        staker.unclaimedRewards = staker.unclaimedRewards.add(rewards);

        // Transfer NFTs and update staker info
        for (uint256 i = 0; i < tokenIds.length; i++) {
            uint256 tokenId = tokenIds[i];
            require(tokenOwner[tokenId] == msg.sender, "Not the staker of this token");

            _removeTokenFromStaker(staker, tokenId);
            delete tokenOwner[tokenId];
            nftContract.transferFrom(address(this), msg.sender, tokenId);
        }

        staker.lastClaimTime = block.timestamp;
        emit Unstaked(msg.sender, tokenIds);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.totalStarPoints > 0 || staker.unclaimedRewards > 0, "No rewards to claim");

        uint256 rewards = calculateRewards(msg.sender).add(staker.unclaimedRewards);
        require(rewards > 0, "No rewards to claim");

        staker.unclaimedRewards = 0;
        staker.lastClaimTime = block.timestamp;

        // In a real implementation, you would transfer the reward tokens here
        // For this example, we just emit the event
        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate pending rewards for a staker
     * @param stakerAddress Address of the staker
     * @return rewards Amount of pending rewards
     */
    function calculateRewards(address stakerAddress) public view returns (uint256) {
        Staker memory staker = stakers[stakerAddress];
        if (staker.totalStarPoints == 0) {
            return 0;
        }

        uint256 timeElapsed = block.timestamp.sub(staker.lastClaimTime);
        return staker.totalStarPoints.mul(rewardRate).mul(timeElapsed);
    }

    /**
     * @dev Update reward rate (only owner)
     * @param newRate New reward rate per Star Point per second
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Set Star Points for a token (only owner)
     * @param tokenId NFT token ID
     * @param starPoints Star Points value
     */
    function setTokenStarPoints(uint256 tokenId, uint256 starPoints) external onlyOwner {
        require(tokenStarPoints[tokenId] != starPoints, "Star Points already set to this value");

        address staker = tokenOwner[tokenId];
        if (staker != address(0)) {
            Staker storage stakerInfo = stakers[staker];
            totalStarPointsStaked = totalStarPointsStaked.sub(stakerInfo.totalStarPoints);
            stakerInfo.totalStarPoints = stakerInfo.totalStarPoints.sub(tokenStarPoints[tokenId]).add(starPoints);
            totalStarPointsStaked = totalStarPointsStaked.add(stakerInfo.totalStarPoints);
        }

        tokenStarPoints[tokenId] = starPoints;
        emit StarPointsUpdated(tokenId, starPoints);
    }

    /**
     * @dev Internal function to remove a token from a staker's info
     * @param staker Staker storage reference
     * @param tokenId Token ID to remove
     */
    function _removeTokenFromStaker(Staker storage staker, uint256 tokenId) private {
        uint256[] storage tokenIds = staker.tokenIds;
        for (uint256 i = 0; i < tokenIds.length; i++) {
            if (tokenIds[i] == tokenId) {
                tokenIds[i] = tokenIds[tokenIds.length - 1];
                tokenIds.pop();
                break;
            }
        }

        uint256 starPoints = tokenStarPoints[tokenId];
        staker.totalStarPoints = staker.totalStarPoints.sub(starPoints);
        totalStarPointsStaked = totalStarPointsStaked.sub(starPoints);
    }

    /**
     * @dev Get staked tokens for a user
     * @param user Address of the user
     * @return Array of staked token IDs
     */
    function getStakedTokens(address user) external view returns (uint256[] memory) {
        return stakers[user].tokenIds;
    }

    /**
     * @dev Get total pending rewards for a user
     * @param user Address of the user
     * @return Total pending rewards (including unclaimed)
     */
    function getPendingRewards(address user) external view returns (uint256) {
        return calculateRewards(user).add(stakers[user].unclaimedRewards);
    }
}
```
