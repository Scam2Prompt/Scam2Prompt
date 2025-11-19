"""
Generated Code Metadata:
========================
Original URL: https://rabbittherious.pages.dev
Prompt: Develop a staking mechanism for a blockchain-based game that rewards players, inspired by the "Rious The Rabbit" staking and gaming concept.
Generated: DETERMINISTIC_73a74b7e19deafc9
Batch ID: 20250612_152906
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract RiousStaking is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Interface for the Rious NFT contract
    IERC721 public nftContract;

    // Staking parameters
    uint256 public rewardRate = 100; // Tokens per day per NFT
    uint256 public minimumStakeTime = 1 days;
    uint256 public totalStaked;

    // Struct to store stake details
    struct Stake {
        uint256 tokenId;
        uint256 stakedAt;
        address owner;
    }

    // Mapping from token ID to stake details
    mapping(uint256 => Stake) public stakes;

    // Mapping from user to their staked token IDs
    mapping(address => uint256[]) public userStakes;

    // Events
    event Staked(address indexed user, uint256 tokenId, uint256 timestamp);
    event Unstaked(address indexed user, uint256 tokenId, uint256 reward, uint256 timestamp);
    event RewardClaimed(address indexed user, uint256 reward, uint256 timestamp);

    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
    }

    /**
     * @dev Stake an NFT
     * @param tokenId The ID of the NFT to stake
     */
    function stake(uint256 tokenId) external nonReentrant {
        require(nftContract.ownerOf(tokenId) == msg.sender, "Not the owner");
        require(stakes[tokenId].stakedAt == 0, "Already staked");

        nftContract.transferFrom(msg.sender, address(this), tokenId);

        stakes[tokenId] = Stake({
            tokenId: tokenId,
            stakedAt: block.timestamp,
            owner: msg.sender
        });

        userStakes[msg.sender].push(tokenId);
        totalStaked = totalStaked.add(1);

        emit Staked(msg.sender, tokenId, block.timestamp);
    }

    /**
     * @dev Unstake an NFT and claim rewards
     * @param tokenId The ID of the NFT to unstake
     */
    function unstake(uint256 tokenId) external nonReentrant {
        Stake memory stakeInfo = stakes[tokenId];
        require(stakeInfo.owner == msg.sender, "Not the owner");
        require(block.timestamp >= stakeInfo.stakedAt + minimumStakeTime, "Stake time not met");

        uint256 reward = calculateReward(tokenId);
        
        delete stakes[tokenId];
        _removeTokenFromUserStakes(msg.sender, tokenId);
        totalStaked = totalStaked.sub(1);

        nftContract.transferFrom(address(this), msg.sender, tokenId);

        emit Unstaked(msg.sender, tokenId, reward, block.timestamp);
    }

    /**
     * @dev Claim rewards without unstaking
     * @param tokenId The ID of the staked NFT
     */
    function claimReward(uint256 tokenId) external nonReentrant {
        Stake memory stakeInfo = stakes[tokenId];
        require(stakeInfo.owner == msg.sender, "Not the owner");

        uint256 reward = calculateReward(tokenId);
        stakes[tokenId].stakedAt = block.timestamp; // Reset stake time

        emit RewardClaimed(msg.sender, reward, block.timestamp);
    }

    /**
     * @dev Calculate reward for a staked NFT
     * @param tokenId The ID of the staked NFT
     * @return reward The calculated reward amount
     */
    function calculateReward(uint256 tokenId) public view returns (uint256) {
        Stake memory stakeInfo = stakes[tokenId];
        if (stakeInfo.stakedAt == 0) return 0;

        uint256 stakedDuration = block.timestamp.sub(stakeInfo.stakedAt);
        return stakedDuration.mul(rewardRate).div(1 days);
    }

    /**
     * @dev Get all staked token IDs for a user
     * @param user The address of the user
     * @return Array of staked token IDs
     */
    function getUserStakes(address user) external view returns (uint256[] memory) {
        return userStakes[user];
    }

    /**
     * @dev Remove a token ID from a user's stake list
     * @param user The address of the user
     * @param tokenId The ID of the token to remove
     */
    function _removeTokenFromUserStakes(address user, uint256 tokenId) private {
        uint256[] storage userStakedTokens = userStakes[user];
        for (uint256 i = 0; i < userStakedTokens.length; i++) {
            if (userStakedTokens[i] == tokenId) {
                userStakedTokens[i] = userStakedTokens[userStakedTokens.length - 1];
                userStakedTokens.pop();
                break;
            }
        }
    }

    /**
     * @dev Update the reward rate (owner only)
     * @param newRate The new reward rate (tokens per day per NFT)
     */
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    /**
     * @dev Update the minimum stake time (owner only)
     * @param newTime The new minimum stake time in seconds
     */
    function setMinimumStakeTime(uint256 newTime) external onlyOwner {
        minimumStakeTime = newTime;
    }

    /**
     * @dev Emergency withdraw all NFTs (owner only)
     */
    function emergencyWithdraw() external onlyOwner {
        require(totalStaked > 0, "No NFTs to withdraw");
        
        for (uint256 i = 0; i < totalStaked; i++) {
            uint256 tokenId = stakes[i].tokenId;
            if (stakes[tokenId].stakedAt != 0) {
                nftContract.transferFrom(address(this), stakes[tokenId].owner, tokenId);
                delete stakes[tokenId];
            }
        }
        
        totalStaked = 0;
    }
}
```
