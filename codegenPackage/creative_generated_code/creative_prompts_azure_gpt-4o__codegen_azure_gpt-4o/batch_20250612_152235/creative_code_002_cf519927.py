"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puffmypanda.pages.dev
Prompt: Create a staking protocol in Solidity for Puff Puff Pandas NFTs that allows holders to lock their NFTs and earn yield in $PUFFS tokens, as outlined in the Puff Like A Panda ecosystem.
Generated: DETERMINISTIC_cf5199279853e068
Batch ID: 20250612_152235
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
 * @title PuffPuffPandasNFTStaking
 * @notice A staking protocol for Puff Puff Pandas NFT holders to earn $PUFFS tokens.
 * @dev This contract allows users to stake their NFTs and earn rewards in $PUFFS tokens.
 */
contract PuffPuffPandasNFTStaking {
    // Interface for the NFT contract
    IERC721 public nftContract;

    // ERC20 token contract for $PUFFS rewards
    IERC20 public rewardsToken;

    // Reward rate per second (in $PUFFS tokens)
    uint256 public rewardRate;

    // Struct to store staking information for a specific NFT
    struct Stake {
        address owner;
        uint256 stakedAt;
    }

    // Mapping of token ID to staking information
    mapping(uint256 => Stake) public stakes;

    // Mapping of address to total rewards earned
    mapping(address => uint256) public rewards;

    // Events
    event Staked(address indexed user, uint256 tokenId, uint256 timestamp);
    event Unstaked(address indexed user, uint256 tokenId, uint256 timestamp);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(address _nftContract, address _rewardsToken, uint256 _rewardRate) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        require(_rewardsToken != address(0), "Invalid rewards token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        nftContract = IERC721(_nftContract);
        rewardsToken = IERC20(_rewardsToken);
        rewardRate = _rewardRate;
    }

    /**
     * @notice Stake a Puff Puff Panda NFT.
     * @dev Transfers the NFT from the user to the contract and starts the staking timer.
     * @param tokenId The ID of the NFT to stake.
     */
    function stake(uint256 tokenId) external {
        require(nftContract.ownerOf(tokenId) == msg.sender, "Caller is not the owner of the NFT");
        require(stakes[tokenId].owner == address(0), "NFT is already staked");

        // Transfer the NFT to the contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);

        // Record staking info
        stakes[tokenId] = Stake({
            owner: msg.sender,
            stakedAt: block.timestamp
        });

        emit Staked(msg.sender, tokenId, block.timestamp);
    }

    /**
     * @notice Unstake a Puff Puff Panda NFT.
     * @dev Transfers the NFT back to the user and calculates rewards earned.
     * @param tokenId The ID of the NFT to unstake.
     */
    function unstake(uint256 tokenId) external {
        Stake memory stakeData = stakes[tokenId];
        require(stakeData.owner == msg.sender, "Caller is not the owner of the staked NFT");

        // Calculate rewards
        uint256 stakingDuration = block.timestamp - stakeData.stakedAt;
        uint256 rewardAmount = stakingDuration * rewardRate;

        // Update rewards mapping
        rewards[msg.sender] += rewardAmount;

        // Remove staking data
        delete stakes[tokenId];

        // Transfer the NFT back to the user
        nftContract.transferFrom(address(this), msg.sender, tokenId);

        emit Unstaked(msg.sender, tokenId, block.timestamp);
    }

    /**
     * @notice Claim accumulated $PUFFS rewards.
     * @dev Transfers the rewards tokens to the user.
     */
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset rewards for the user
        rewards[msg.sender] = 0;

        // Transfer the rewards tokens
        require(rewardsToken.transfer(msg.sender, rewardAmount), "Rewards transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @notice Get the staking details for a specific NFT.
     * @param tokenId The ID of the NFT.
     * @return The staking details (owner and staking timestamp).
     */
    function getStakeDetails(uint256 tokenId) external view returns (address, uint256) {
        Stake memory stakeData = stakes[tokenId];
        return (stakeData.owner, stakeData.stakedAt);
    }
}

// Minimal interfaces for interacting with ERC721 and ERC20 tokens
interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
}

interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
}
```
