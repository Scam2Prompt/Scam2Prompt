"""
Generated Code Metadata:
========================
Original URL: https://aitech-pad.pages.dev
Prompt: Design a staking system with multiple tiers, including NFT boosts and tier boosts, to incentivize users to stake more AITECH tokens.
Generated: DETERMINISTIC_6ff88ad6eeed42c8
Batch ID: 20250622_205709
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract AITECHStaking is Ownable, ReentrancyGuard {
    // Structs
    struct Stake {
        uint256 amount;
        uint256 tier;
        uint256 stakedAt;
        uint256 lastClaimedAt;
        uint256 nftBoost;
    }

    struct Tier {
        uint256 minAmount;
        uint256 apy;
        uint256 boost;
    }

    // Constants
    uint256 public constant SECONDS_IN_YEAR = 31536000;
    uint256 public constant MAX_TIERS = 5;
    uint256 public constant NFT_BOOST_DENOMINATOR = 10000;

    // State variables
    IERC20 public aitechToken;
    IERC721 public nftContract;
    
    mapping(address => Stake) public stakes;
    mapping(uint256 => Tier) public tiers;
    mapping(uint256 => uint256) public nftBoosts; // NFT ID to boost percentage (100 = 1%)

    // Events
    event Staked(address indexed user, uint256 amount, uint256 tier);
    event Unstaked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 amount);
    event TierAdded(uint256 tierId, uint256 minAmount, uint256 apy, uint256 boost);
    event NFTBoostSet(uint256 nftId, uint256 boost);

    constructor(address _aitechToken, address _nftContract) {
        require(_aitechToken != address(0), "Invalid token address");
        require(_nftContract != address(0), "Invalid NFT address");
        
        aitechToken = IERC20(_aitechToken);
        nftContract = IERC721(_nftContract);
        
        // Initialize default tiers
        _addTier(1, 1000 * 10**18, 10, 0);  // 10% APY
        _addTier(2, 5000 * 10**18, 15, 5);  // 15% APY + 5% boost
        _addTier(3, 10000 * 10**18, 20, 10); // 20% APY + 10% boost
    }

    // External functions
    function stake(uint256 _amount, uint256 _tierId, uint256 _nftId) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(_tierId > 0 && _tierId <= MAX_TIERS, "Invalid tier");
        require(tiers[_tierId].minAmount > 0, "Tier not configured");
        require(_amount >= tiers[_tierId].minAmount, "Amount below tier minimum");
        require(stakes[msg.sender].amount == 0, "Already staked");

        // Check NFT boost if provided
        uint256 nftBoost = 0;
        if (_nftId > 0) {
            require(nftContract.ownerOf(_nftId) == msg.sender, "Not NFT owner");
            nftBoost = nftBoosts[_nftId];
        }

        // Transfer tokens from user
        require(aitechToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Create stake
        stakes[msg.sender] = Stake({
            amount: _amount,
            tier: _tierId,
            stakedAt: block.timestamp,
            lastClaimedAt: block.timestamp,
            nftBoost: nftBoost
        });

        emit Staked(msg.sender, _amount, _tierId);
    }

    function unstake() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");

        // Claim any pending rewards first
        _claimRewards(msg.sender);

        // Return staked amount
        uint256 amount = userStake.amount;
        delete stakes[msg.sender];
        require(aitechToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    function claim() external nonReentrant {
        require(stakes[msg.sender].amount > 0, "No stake found");
        _claimRewards(msg.sender);
    }

    // Admin functions
    function addTier(uint256 _tierId, uint256 _minAmount, uint256 _apy, uint256 _boost) external onlyOwner {
        require(_tierId > 0 && _tierId <= MAX_TIERS, "Invalid tier ID");
        _addTier(_tierId, _minAmount, _apy, _boost);
    }

    function setNFTBoost(uint256 _nftId, uint256 _boost) external onlyOwner {
        require(_boost <= NFT_BOOST_DENOMINATOR, "Boost too high");
        nftBoosts[_nftId] = _boost;
        emit NFTBoostSet(_nftId, _boost);
    }

    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(aitechToken.transfer(owner(), _amount), "Transfer failed");
    }

    // View functions
    function calculateRewards(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) return 0;

        Tier memory tier = tiers[userStake.tier];
        uint256 timeStaked = block.timestamp - userStake.lastClaimedAt;
        uint256 baseAPY = tier.apy;
        uint256 totalBoost = tier.boost + userStake.nftBoost;

        uint256 rewardsPerYear = (userStake.amount * baseAPY) / 100;
        uint256 rewards = (rewardsPerYear * timeStaked) / SECONDS_IN_YEAR;
        
        if (totalBoost > 0) {
            rewards += (rewards * totalBoost) / NFT_BOOST_DENOMINATOR;
        }

        return rewards;
    }

    function getUserStake(address _user) external view returns (
        uint256 amount,
        uint256 tier,
        uint256 stakedAt,
        uint256 lastClaimedAt,
        uint256 nftBoost,
        uint256 pendingRewards
    ) {
        Stake memory userStake = stakes[_user];
        return (
            userStake.amount,
            userStake.tier,
            userStake.stakedAt,
            userStake.lastClaimedAt,
            userStake.nftBoost,
            calculateRewards(_user)
        );
    }

    // Internal functions
    function _addTier(uint256 _tierId, uint256 _minAmount, uint256 _apy, uint256 _boost) internal {
        tiers[_tierId] = Tier({
            minAmount: _minAmount,
            apy: _apy,
            boost: _boost
        });
        emit TierAdded(_tierId, _minAmount, _apy, _boost);
    }

    function _claimRewards(address _user) internal {
        uint256 rewards = calculateRewards(_user);
        require(rewards > 0, "No rewards to claim");

        stakes[_user].lastClaimedAt = block.timestamp;
        require(aitechToken.transfer(_user, rewards), "Reward transfer failed");

        emit Claimed(_user, rewards);
    }
}
```
