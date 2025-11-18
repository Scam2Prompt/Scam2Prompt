"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellybabiesnft.web.app
Prompt: Write a smart contract in Solidity that enables an NFT staking mechanism similar to the "Jelly Staking" feature described on the Jelly Babies NFT website, allowing users to earn $Jelly tokens as rewards.
Generated: DETERMINISTIC_9f3757e49928e344
Batch ID: 20250612_142645
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
 * @title NFT Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake NFTs to earn $Jelly token rewards.
 */
interface INFTCollection {
    function ownerOf(uint256 tokenId) external view returns (address);
    function transferFrom(address from, address to, uint256 tokenId) external;
}

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract NFTStaking {
    // NFT Collection contract
    INFTCollection public nftCollection;

    // $Jelly token contract
    IERC20 public jellyToken;

    // Reward rate (tokens per second)
    uint256 public rewardRate;

    // Mapping of tokenId to the staker's address
    mapping(uint256 => address) public stakedNFTs;

    // Mapping of staker's address to staking information
    mapping(address => uint256) public stakingStartTime;

    // Mapping of staker's address to accumulated rewards
    mapping(address => uint256) public accumulatedRewards;

    // Contract owner
    address public owner;

    // Events for logging
    event NFTStaked(address indexed staker, uint256 tokenId);
    event NFTUnstaked(address indexed staker, uint256 tokenId);
    event RewardsClaimed(address indexed staker, uint256 rewardAmount);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Modifier to ensure the caller is the staker of the NFT.
     */
    modifier onlyStaker(uint256 tokenId) {
        require(stakedNFTs[tokenId] == msg.sender, "Caller is not the staker of this NFT");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _nftCollection Address of the NFT collection contract.
     * @param _jellyToken Address of the $Jelly token contract.
     * @param _rewardRate Reward rate in tokens per second.
     */
    constructor(INFTCollection _nftCollection, IERC20 _jellyToken, uint256 _rewardRate) {
        nftCollection = _nftCollection;
        jellyToken = _jellyToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Stake an NFT to start earning rewards.
     * @param tokenId ID of the NFT to stake.
     */
    function stakeNFT(uint256 tokenId) external {
        // Ensure the caller owns the NFT
        require(nftCollection.ownerOf(tokenId) == msg.sender, "Caller does not own the NFT");

        // Transfer NFT to the contract
        nftCollection.transferFrom(msg.sender, address(this), tokenId);

        // Record staking start time
        stakingStartTime[msg.sender] = block.timestamp;

        // Record the staker for the NFT
        stakedNFTs[tokenId] = msg.sender;

        emit NFTStaked(msg.sender, tokenId);
    }

    /**
     * @dev Unstake an NFT and stop earning rewards.
     * @param tokenId ID of the NFT to unstake.
     */
    function unstakeNFT(uint256 tokenId) external onlyStaker(tokenId) {
        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Transfer NFT back to the staker
        nftCollection.transferFrom(address(this), msg.sender, tokenId);

        // Clear staking data
        stakedNFTs[tokenId] = address(0);
        stakingStartTime[msg.sender] = 0;

        emit NFTUnstaked(msg.sender, tokenId);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external {
        // Update rewards before claiming
        _updateRewards(msg.sender);

        // Get the reward amount
        uint256 rewardAmount = accumulatedRewards[msg.sender];

        // Ensure there are rewards to claim
        require(rewardAmount > 0, "No rewards available to claim");

        // Reset accumulated rewards
        accumulatedRewards[msg.sender] = 0;

        // Transfer $Jelly tokens to the caller
        require(jellyToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Internal function to update rewards for a staker.
     * @param staker Address of the staker.
     */
    function _updateRewards(address staker) internal {
        uint256 startTime = stakingStartTime[staker];

        // If staking has started, calculate rewards
        if (startTime > 0) {
            uint256 stakingDuration = block.timestamp - startTime;
            uint256 earnedRewards = stakingDuration * rewardRate;

            // Update accumulated rewards
            accumulatedRewards[staker] += earnedRewards;

            // Reset staking start time to current time
            stakingStartTime[staker] = block.timestamp;
        }
    }

    /**
     * @dev Update the reward rate (owner-only function).
     * @param _rewardRate New reward rate in tokens per second.
     */
    function updateRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Withdraw $Jelly tokens from the contract (owner-only function).
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(jellyToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        require(jellyToken.transfer(owner, amount), "Token transfer failed");
    }
}
```
