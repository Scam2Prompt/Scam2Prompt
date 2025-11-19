"""
Generated Code Metadata:
========================
Original URL: https://aitech-c09.pages.dev
Prompt: Create a Solidity smart contract for AITECH staking, incorporating features such as NFT boosts, tier boosts, and support for multiple EVM chains.
Generated: DETERMINISTIC_7a348cd31fbb5b25
Batch ID: 20250622_210216
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

contract AITechStaking is ReentrancyGuard, Ownable {
    // Structs
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 lastClaimTime;
        uint256 tier;
        uint256[] nftTokenIds;
    }

    struct Tier {
        uint256 minAmount;
        uint256 boostPercentage;
    }

    struct NFTBoost {
        address nftContract;
        uint256 boostPercentage;
    }

    // Constants
    uint256 public constant SECONDS_IN_DAY = 86400;
    uint256 public constant MAX_NFT_BOOST = 300; // 300% max boost from NFTs
    uint256 public constant MAX_TIER_BOOST = 200; // 200% max boost from tier

    // State variables
    IERC20 public stakingToken;
    uint256 public rewardRatePerDay; // Reward rate per day per token (in wei)
    uint256 public totalStaked;
    uint256 public totalRewardsDistributed;

    // Mappings
    mapping(address => Stake) public stakes;
    mapping(uint256 => Tier) public tiers;
    mapping(address => NFTBoost) public nftBoosts;
    mapping(uint256 => bool) public supportedChains;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 tier);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event TierUpdated(uint256 tier, uint256 minAmount, uint256 boostPercentage);
    event NFTBoostUpdated(address nftContract, uint256 boostPercentage);
    event ChainSupportUpdated(uint256 chainId, bool isSupported);

    constructor(
        address _stakingToken,
        uint256 _rewardRatePerDay
    ) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
        rewardRatePerDay = _rewardRatePerDay;

        // Initialize default tiers
        tiers[1] = Tier(1000 ether, 10); // Tier 1: 10% boost
        tiers[2] = Tier(5000 ether, 30); // Tier 2: 30% boost
        tiers[3] = Tier(10000 ether, 50); // Tier 3: 50% boost
        tiers[4] = Tier(50000 ether, 100); // Tier 4: 100% boost
        tiers[5] = Tier(100000 ether, 200); // Tier 5: 200% boost
    }

    // Modifiers
    modifier onlySupportedChain() {
        require(supportedChains[block.chainid], "Chain not supported");
        _;
    }

    modifier hasStake() {
        require(stakes[msg.sender].amount > 0, "No stake found");
        _;
    }

    // External functions
    function stake(uint256 amount, uint256 tier) external nonReentrant onlySupportedChain {
        require(amount > 0, "Amount must be greater than 0");
        require(tiers[tier].minAmount > 0, "Invalid tier");
        require(amount >= tiers[tier].minAmount, "Amount below tier minimum");

        if (stakes[msg.sender].amount > 0) {
            _claimRewards();
        }

        stakingToken.transferFrom(msg.sender, address(this), amount);

        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + amount,
            startTime: block.timestamp,
            lastClaimTime: block.timestamp,
            tier: tier,
            nftTokenIds: stakes[msg.sender].nftTokenIds
        });

        totalStaked += amount;
        emit Staked(msg.sender, amount, tier);
    }

    function unstake() external nonReentrant hasStake {
        Stake storage userStake = stakes[msg.sender];
        _claimRewards();

        uint256 amount = userStake.amount;
        stakingToken.transfer(msg.sender, amount);

        totalStaked -= amount;
        delete stakes[msg.sender];
        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant hasStake {
        _claimRewards();
    }

    function addNFTs(uint256[] memory tokenIds, address nftContract) external hasStake {
        require(nftBoosts[nftContract].boostPercentage > 0, "NFT contract not supported");
        require(tokenIds.length > 0, "No token IDs provided");

        Stake storage userStake = stakes[msg.sender];
        IERC721 nft = IERC721(nftContract);

        for (uint256 i = 0; i < tokenIds.length; i++) {
            require(nft.ownerOf(tokenIds[i]) == msg.sender, "Not NFT owner");
            userStake.nftTokenIds.push(tokenIds[i]);
        }
    }

    function removeNFTs(uint256[] memory tokenIds) external hasStake {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.nftTokenIds.length > 0, "No NFTs staked");

        for (uint256 i = 0; i < tokenIds.length; i++) {
            for (uint256 j = 0; j < userStake.nftTokenIds.length; j++) {
                if (userStake.nftTokenIds[j] == tokenIds[i]) {
                    userStake.nftTokenIds[j] = userStake.nftTokenIds[userStake.nftTokenIds.length - 1];
                    userStake.nftTokenIds.pop();
                    break;
                }
            }
        }
    }

    // View functions
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 timeElapsed = block.timestamp - userStake.lastClaimTime;
        uint256 baseReward = (userStake.amount * rewardRatePerDay * timeElapsed) / SECONDS_IN_DAY;

        // Apply tier boost
        uint256 tierBoost = tiers[userStake.tier].boostPercentage;
        uint256 boostedReward = baseReward + (baseReward * tierBoost) / 100;

        // Apply NFT boosts
        uint256 nftBoost = 0;
        for (uint256 i = 0; i < userStake.nftTokenIds.length; i++) {
            address nftContract = IERC721(address(this)).ownerOf(userStake.nftTokenIds[i]);
            nftBoost += nftBoosts[nftContract].boostPercentage;
        }

        if (nftBoost > MAX_NFT_BOOST) {
            nftBoost = MAX_NFT_BOOST;
        }

        boostedReward = boostedReward + (boostedReward * nftBoost) / 100;

        return boostedReward;
    }

    function getUserStake(address user) external view returns (Stake memory) {
        return stakes[user];
    }

    // Admin functions
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRatePerDay = newRate;
    }

    function updateTier(uint256 tier, uint256 minAmount, uint256 boostPercentage) external onlyOwner {
        require(boostPercentage <= MAX_TIER_BOOST, "Boost percentage too high");
        tiers[tier] = Tier(minAmount, boostPercentage);
        emit TierUpdated(tier, minAmount, boostPercentage);
    }

    function addNFTBoost(address nftContract, uint256 boostPercentage) external onlyOwner {
        require(boostPercentage <= 100, "Boost percentage too high");
        nftBoosts[nftContract] = NFTBoost(nftContract, boostPercentage);
        emit NFTBoostUpdated(nftContract, boostPercentage);
    }

    function updateChainSupport(uint256 chainId, bool isSupported) external onlyOwner {
        supportedChains[chainId] = isSupported;
        emit ChainSupportUpdated(chainId, isSupported);
    }

    function emergencyWithdraw(address token) external onlyOwner {
        if (token == address(0)) {
            payable(owner()).transfer(address(this).balance);
        } else {
            IERC20(token).transfer(owner(), IERC20(token).balanceOf(address(this)));
        }
    }

    // Internal functions
    function _claimRewards() internal {
        Stake storage userStake = stakes[msg.sender];
        uint256 reward = calculateRewards(msg.sender);

        if (reward > 0) {
            userStake.lastClaimTime = block.timestamp;
            stakingToken.transfer(msg.sender, reward);
            totalRewardsDistributed += reward;
            emit RewardClaim
