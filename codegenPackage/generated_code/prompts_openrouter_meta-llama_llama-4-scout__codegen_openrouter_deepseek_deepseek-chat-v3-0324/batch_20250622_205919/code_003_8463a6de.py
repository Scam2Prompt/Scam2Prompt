"""
Generated Code Metadata:
========================
Original URL: https://superverse-io.pages.dev
Prompt: Design a staking interface for SuperVerse DAO that allows users to stake SUPER tokens and NFTs, estimate rewards, and review blockchain transactions before execution.
Generated: DETERMINISTIC_8463a6de9c67e9bf
Batch ID: 20250622_205919
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
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface ISuperToken {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function allowance(address owner, address spender) external view returns (uint256);
}

interface ISuperNFT {
    function safeTransferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
    function getApproved(uint256 tokenId) external view returns (address);
    function isApprovedForAll(address owner, address operator) external view returns (bool);
}

contract SuperVerseStaking is ReentrancyGuard, Ownable {
    using SafeMath for uint256;

    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastClaimed;
        bool isActive;
    }

    struct NFTStake {
        uint256 tokenId;
        uint256 stakedAt;
        uint256 lastClaimed;
        bool isActive;
    }

    // Token and NFT contract addresses
    ISuperToken public superToken;
    ISuperNFT public superNFT;

    // Staking parameters
    uint256 public rewardRate = 100; // 100 tokens per token per year
    uint256 public nftRewardRate = 500; // 500 tokens per NFT per year
    uint256 public minStakeDuration = 7 days;
    uint256 public totalStaked;

    // Mappings for staking data
    mapping(address => Stake) public tokenStakes;
    mapping(address => mapping(uint256 => NFTStake)) public nftStakes;
    mapping(address => uint256[]) public userStakedNFTs;

    // Events
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event NFTStaked(address indexed user, uint256 tokenId);
    event NFTUnstaked(address indexed user, uint256 tokenId);
    event NFTRewardsClaimed(address indexed user, uint256 amount);

    constructor(address _superToken, address _superNFT) {
        require(_superToken != address(0), "Invalid token address");
        require(_superNFT != address(0), "Invalid NFT address");
        superToken = ISuperToken(_superToken);
        superNFT = ISuperNFT(_superNFT);
    }

    /**
     * @dev Stake SUPER tokens
     * @param amount Amount of tokens to stake
     */
    function stakeTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(superToken.balanceOf(msg.sender) >= amount, "Insufficient balance");
        require(superToken.allowance(msg.sender, address(this)) >= amount, "Not approved");

        Stake storage userStake = tokenStakes[msg.sender];
        require(!userStake.isActive, "Already staking");

        // Transfer tokens from user to contract
        bool success = superToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update staking data
        userStake.amount = amount;
        userStake.stakedAt = block.timestamp;
        userStake.lastClaimed = block.timestamp;
        userStake.isActive = true;
        totalStaked = totalStaked.add(amount);

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Unstake SUPER tokens and claim rewards
     */
    function unstakeTokens() external nonReentrant {
        Stake storage userStake = tokenStakes[msg.sender];
        require(userStake.isActive, "No active stake");
        require(block.timestamp >= userStake.stakedAt.add(minStakeDuration), "Minimum stake duration not met");

        uint256 stakedAmount = userStake.amount;
        uint256 reward = calculateTokenReward(msg.sender);

        // Transfer staked tokens and rewards back to user
        if (reward > 0) {
            require(superToken.transfer(msg.sender, reward), "Reward transfer failed");
            emit RewardsClaimed(msg.sender, reward);
        }

        require(superToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        // Update staking data
        totalStaked = totalStaked.sub(stakedAmount);
        userStake.amount = 0;
        userStake.isActive = false;

        emit TokensUnstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Stake NFT
     * @param tokenId ID of the NFT to stake
     */
    function stakeNFT(uint256 tokenId) external nonReentrant {
        require(superNFT.ownerOf(tokenId) == msg.sender, "Not NFT owner");
        require(
            superNFT.getApproved(tokenId) == address(this) || 
            superNFT.isApprovedForAll(msg.sender, address(this)),
            "Not approved"
        );

        NFTStake storage nftStake = nftStakes[msg.sender][tokenId];
        require(!nftStake.isActive, "NFT already staked");

        // Transfer NFT from user to contract
        superNFT.safeTransferFrom(msg.sender, address(this), tokenId);

        // Update staking data
        nftStake.tokenId = tokenId;
        nftStake.stakedAt = block.timestamp;
        nftStake.lastClaimed = block.timestamp;
        nftStake.isActive = true;
        userStakedNFTs[msg.sender].push(tokenId);

        emit NFTStaked(msg.sender, tokenId);
    }

    /**
     * @dev Unstake NFT and claim rewards
     * @param tokenId ID of the NFT to unstake
     */
    function unstakeNFT(uint256 tokenId) external nonReentrant {
        NFTStake storage nftStake = nftStakes[msg.sender][tokenId];
        require(nftStake.isActive, "NFT not staked");
        require(block.timestamp >= nftStake.stakedAt.add(minStakeDuration), "Minimum stake duration not met");

        uint256 reward = calculateNFTReward(msg.sender, tokenId);

        // Transfer NFT back to user
        superNFT.safeTransferFrom(address(this), msg.sender, tokenId);

        // Transfer rewards if any
        if (reward > 0) {
            require(superToken.transfer(msg.sender, reward), "Reward transfer failed");
            emit NFTRewardsClaimed(msg.sender, reward);
        }

        // Update staking data
        nftStake.isActive = false;
        removeStakedNFT(msg.sender, tokenId);

        emit NFTUnstaked(msg.sender, tokenId);
    }

    /**
     * @dev Claim token staking rewards without unstaking
     */
    function claimTokenRewards() external nonReentrant {
        Stake storage userStake = tokenStakes[msg.sender];
        require(userStake.isActive, "No active stake");

        uint256 reward = calculateTokenReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        userStake.lastClaimed = block.timestamp;
        require(superToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Claim NFT staking rewards without unstaking
     * @param tokenId ID of the staked NFT
     */
    function claimNFTRewards(uint256 tokenId) external nonReentrant {
        NFTStake storage nftStake = nftStakes[msg.sender][tokenId];
        require(nftStake.isActive, "NFT not staked");

        uint256 reward = calculateNFTReward(msg.sender, tokenId);
        require(reward > 0, "No rewards to claim");

        nftStake.lastClaimed = block.timestamp;
        require(superToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit NFTRewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate estimated token rewards for a user
     * @param user Address of the user
     * @return Estimated reward amount
     */
    function calculateTokenReward(address user) public view returns (uint256) {
        Stake memory userStake = tokenStakes[user];
        if (!userStake.isActive) return 0;

        uint256 timeStaked = block.timestamp.sub(userStake.lastClaimed);
        return userSt
