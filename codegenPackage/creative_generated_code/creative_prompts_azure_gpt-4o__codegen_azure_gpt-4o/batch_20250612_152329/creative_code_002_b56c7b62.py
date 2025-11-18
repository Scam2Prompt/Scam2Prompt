"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascalsnft.web.app
Prompt: Create a smart contract for staking Rascals NFTs to earn $Jelly tokens, ensuring compatibility with the Ethereum blockchain.
Generated: DETERMINISTIC_b56c7b62acbf063f
Batch ID: 20250612_152329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

/**
 * @title RascalsNFTStaking
 * @notice A smart contract for staking Rascals NFTs to earn $Jelly tokens.
 * @dev Compatible with the Ethereum blockchain and follows best practices.
 */
 
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract RascalsNFTStaking is Ownable {
    // Interface for the Rascals NFT contract
    IERC721 public rascalsNFT;

    // Interface for the Jelly token contract
    IERC20 public jellyToken;

    // Reward rate: $Jelly tokens earned per second per NFT
    uint256 public rewardRate;

    struct Stake {
        uint256 tokenId;
        uint256 startTime;
    }

    // User address to staked NFTs
    mapping(address => Stake[]) public stakes;

    // User address to pending rewards
    mapping(address => uint256) public pendingRewards;

    // Events for logging contract activity
    event NFTStaked(address indexed user, uint256 tokenId, uint256 startTime);
    event NFTUnstaked(address indexed user, uint256 tokenId, uint256 rewardAmount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with NFT and token addresses, and reward rate.
     * @param _rascalsNFT Address of the Rascals NFT contract.
     * @param _jellyToken Address of the Jelly token contract.
     * @param _rewardRate Reward rate in $Jelly tokens per second per NFT.
     */
    constructor(IERC721 _rascalsNFT, IERC20 _jellyToken, uint256 _rewardRate) {
        rascalsNFT = _rascalsNFT;
        jellyToken = _jellyToken;
        rewardRate = _rewardRate;
    }

    /**
     * @notice Stake a Rascals NFT to earn rewards.
     * @param tokenId ID of the NFT to stake.
     */
    function stakeNFT(uint256 tokenId) external {
        // Ensure NFT ownership
        require(rascalsNFT.ownerOf(tokenId) == msg.sender, "You must own the NFT to stake it");

        // Transfer NFT to the contract
        rascalsNFT.transferFrom(msg.sender, address(this), tokenId);

        // Record staking information
        stakes[msg.sender].push(Stake({tokenId: tokenId, startTime: block.timestamp}));

        emit NFTStaked(msg.sender, tokenId, block.timestamp);
    }

    /**
     * @notice Unstake a Rascals NFT and claim accumulated rewards.
     * @param tokenId ID of the NFT to unstake.
     */
    function unstakeNFT(uint256 tokenId) external {
        uint256 reward = 0;
        bool tokenFound = false;

        // Find the staked token and calculate rewards
        for (uint256 i = 0; i < stakes[msg.sender].length; i++) {
            if (stakes[msg.sender][i].tokenId == tokenId) {
                tokenFound = true;

                // Calculate rewards
                reward = (block.timestamp - stakes[msg.sender][i].startTime) * rewardRate;

                // Remove the stake
                stakes[msg.sender][i] = stakes[msg.sender][stakes[msg.sender].length - 1];
                stakes[msg.sender].pop();
                break;
            }
        }

        // Ensure the token is staked
        require(tokenFound, "NFT not found in your stakes");

        // Update pending rewards
        pendingRewards[msg.sender] += reward;

        // Transfer NFT back to the user
        rascalsNFT.transferFrom(address(this), msg.sender, tokenId);

        emit NFTUnstaked(msg.sender, tokenId, reward);
    }

    /**
     * @notice Claim accumulated $Jelly rewards.
     */
    function claimRewards() external {
        uint256 reward = pendingRewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset pending rewards
        pendingRewards[msg.sender] = 0;

        // Transfer $Jelly tokens to the user
        require(jellyToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @notice Update the reward rate (only callable by the owner).
     * @param _rewardRate New reward rate in $Jelly tokens per second per NFT.
     */
    function updateRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @notice Get the staked NFTs for a user.
     * @param user Address of the user.
     * @return Array of staked NFTs.
     */
    function getStakes(address user) external view returns (Stake[] memory) {
        return stakes[user];
    }
}
```
