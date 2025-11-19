"""
Generated Code Metadata:
========================
Original URL: https://yooshi-io.pages.dev
Prompt: Develop a smart contract in Solidity to create a custom NFT farming pool on the YooShi platform, allowing users to stake their NFTs and earn YooShi tokens as rewards.
Generated: DETERMINISTIC_56d461be8c769480
Batch ID: 20250622_210122
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

/**
 * @title NFT Farming Pool for YooShi Rewards
 * @dev This contract allows users to stake their NFTs and earn YooShi tokens as rewards.
 */
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTFarmingPool is Ownable {
    // Address of the NFT contract
    IERC721 public nftContract;

    // Address of the YooShi token contract
    IERC20 public yooShiToken;

    // Reward rate in YooShi tokens per NFT per second
    uint256 public rewardRate;

    // Mapping to track staked NFTs and their staking timestamps
    mapping(uint256 => address) public stakedNFTs;
    mapping(uint256 => uint256) public stakingTimestamps;

    // Mapping to track user rewards
    mapping(address => uint256) public pendingRewards;

    // Event declarations
    event NFTStaked(address indexed user, uint256 indexed tokenId);
    event NFTUnstaked(address indexed user, uint256 indexed tokenId);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _nftContract Address of the NFT contract.
     * @param _yooShiToken Address of the YooShi token contract.
     * @param _rewardRate Reward rate in YooShi tokens per NFT per second.
     */
    constructor(
        address _nftContract,
        address _yooShiToken,
        uint256 _rewardRate
    ) {
        nftContract = IERC721(_nftContract);
        yooShiToken = IERC20(_yooShiToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake an NFT to start earning rewards.
     * @param tokenId ID of the NFT to stake.
     */
    function stakeNFT(uint256 tokenId) external {
        // Ensure the NFT is not already staked
        require(stakedNFTs[tokenId] == address(0), "NFT already staked");

        // Transfer the NFT to the contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);

        // Record staking details
        stakedNFTs[tokenId] = msg.sender;
        stakingTimestamps[tokenId] = block.timestamp;

        emit NFTStaked(msg.sender, tokenId);
    }

    /**
     * @dev Unstake an NFT and claim pending rewards.
     * @param tokenId ID of the NFT to unstake.
     */
    function unstakeNFT(uint256 tokenId) external {
        // Ensure the caller is the staker
        require(stakedNFTs[tokenId] == msg.sender, "Not the staker");

        // Calculate and update pending rewards
        _updateRewards(msg.sender, tokenId);

        // Transfer the NFT back to the user
        nftContract.transferFrom(address(this), msg.sender, tokenId);

        // Clear staking details
        stakedNFTs[tokenId] = address(0);
        stakingTimestamps[tokenId] = 0;

        emit NFTUnstaked(msg.sender, tokenId);
    }

    /**
     * @dev Claim all pending rewards.
     */
    function claimRewards() external {
        uint256 rewards = pendingRewards[msg.sender];
        require(rewards > 0, "No rewards to claim");

        // Reset pending rewards
        pendingRewards[msg.sender] = 0;

        // Transfer YooShi tokens to the user
        require(
            yooShiToken.transfer(msg.sender, rewards),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user Address of the user.
     * @param tokenId ID of the staked NFT.
     */
    function _updateRewards(address user, uint256 tokenId) internal {
        uint256 stakingDuration = block.timestamp - stakingTimestamps[tokenId];
        uint256 rewards = stakingDuration * rewardRate;

        // Accumulate rewards for the user
        pendingRewards[user] += rewards;

        // Reset staking timestamp
        stakingTimestamps[tokenId] = block.timestamp;
    }

    /**
     * @dev Update the reward rate. Only callable by the owner.
     * @param _rewardRate New reward rate in YooShi tokens per NFT per second.
     */
    function updateRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }
}
```
