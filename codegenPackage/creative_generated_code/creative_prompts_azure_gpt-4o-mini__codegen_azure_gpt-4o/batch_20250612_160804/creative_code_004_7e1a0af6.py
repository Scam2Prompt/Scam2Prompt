"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitech-pad.pages.dev
Prompt: How can I set up a smart contract for staking AITECH tokens that includes features like NFT boosts and tier boosts?
Generated: DETERMINISTIC_7e1a0af6e2c66315
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title AITECH Staking Contract
 * @author Professional Developer
 * @notice This contract allows staking of AITECH tokens with features like NFT boosts and tier boosts.
 */
contract AITECHStaking {
    // --- State Variables ---
    IERC20 public immutable AITECHToken; // ERC20 AITECH token
    IERC721 public immutable BoostNFT; // ERC721 NFT for staking boosts

    uint256 public constant DECIMALS = 10**18; // Token decimal precision
    uint256 public constant BASE_REWARD_RATE = 100; // Base reward rate per second (in token units)

    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Last timestamp of stake/reward claim
        uint256 tierBoost; // Tier boost percentage (additional rewards)
    }

    mapping(address => StakeInfo) public stakes; // Tracks staking details per user
    mapping(uint256 => uint256) public nftBoosts; // Tracks NFT ID to boost percentage

    // --- Events ---
    event Staked(address indexed user, uint256 amount);
    event ClaimedRewards(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // --- Constructor ---
    constructor(address _AITECHToken, address _BoostNFT) {
        require(_AITECHToken != address(0), "Invalid AITECH token address");
        require(_BoostNFT != address(0), "Invalid NFT contract address");

        AITECHToken = IERC20(_AITECHToken);
        BoostNFT = IERC721(_BoostNFT);
    }

    // --- Modifiers ---
    modifier updateRewards(address _user) {
        StakeInfo storage stake = stakes[_user];
        if (stake.amount > 0) {
            uint256 rewards = calculateRewards(_user);
            stake.timestamp = block.timestamp; // Update timestamp after rewards calculation
            AITECHToken.transfer(_user, rewards); // Automatically transfer rewards
            emit ClaimedRewards(_user, rewards);
        }
        _;
    }

    // --- Public Functions ---
    /**
     * @notice Stake AITECH tokens
     * @param amount Amount of tokens to stake
     * @param tierBoost Tier boost percentage (0-100)
     */
    function stake(uint256 amount, uint256 tierBoost) external updateRewards(msg.sender) {
        require(amount > 0, "Stake amount must be greater than zero");
        require(tierBoost <= 100, "Tier boost percentage cannot exceed 100");

        StakeInfo storage stake = stakes[msg.sender];
        stake.amount += amount;
        stake.tierBoost = tierBoost;
        stake.timestamp = block.timestamp;

        AITECHToken.transferFrom(msg.sender, address(this), amount); // Transfer tokens to contract
        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake AITECH tokens
     */
    function unstake() external updateRewards(msg.sender) {
        StakeInfo storage stake = stakes[msg.sender];
        uint256 amount = stake.amount;
        require(amount > 0, "No tokens to unstake");

        stake.amount = 0; // Reset stake amount
        stake.timestamp = 0; // Reset timestamp

        AITECHToken.transfer(msg.sender, amount); // Return staked tokens to user
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Calculate rewards for a staker
     * @param _user Address of the staker
     * @return rewards Total rewards calculated
     */
    function calculateRewards(address _user) public view returns (uint256 rewards) {
        StakeInfo memory stake = stakes[_user];
        if (stake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - stake.timestamp;
        uint256 baseRewards = (stake.amount * BASE_REWARD_RATE * stakingDuration) / DECIMALS;

        // Calculate NFT boost if applicable
        uint256 nftBoost = getNFTBoost(_user);
        uint256 totalBoost = stake.tierBoost + nftBoost;

        // Apply boost percentages to base rewards
        rewards = baseRewards + ((baseRewards * totalBoost) / 100);
    }

    // --- Internal Functions ---
    /**
     * @notice Get NFT boost percentage for a user
     * @param _user Address of the user
     * @return boost NFT boost percentage
     */
    function getNFTBoost(address _user) internal view returns (uint256 boost) {
        uint256 nftCount = BoostNFT.balanceOf(_user); // Check user's NFT holdings
        if (nftCount > 0) {
            uint256 nftId = BoostNFT.tokenOfOwnerByIndex(_user, 0); // Get first NFT ID owned
            boost = nftBoosts[nftId]; // Fetch boost percentage
        } else {
            boost = 0; // No NFTs owned, zero boost
        }
    }

    // --- Owner Functions ---
    /**
     * @notice Set NFT boost percentage for a specific NFT ID
     * @param nftId ID of the NFT
     * @param boost Boost percentage (0-100)
     */
    function setNFTBoost(uint256 nftId, uint256 boost) external onlyOwner {
        require(boost <= 100, "Boost percentage cannot exceed 100");
        nftBoosts[nftId] = boost; // Assign boost percentage
    }
}

// --- Interfaces ---
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}

interface IERC721 {
    function balanceOf(address owner) external view returns (uint256);

    function tokenOfOwnerByIndex(address owner, uint256 index) external view returns (uint256);
}
```
