"""
Generated Code Metadata:
========================
Original URL: https://embersft.costhentic.com
Prompt: Create a smart contract in Solidity that supports staking functionality for Ember NFTs and includes mechanisms for DAO participation and airdrops.
Generated: DETERMINISTIC_d920d89c8a99ff43
Batch ID: 20250612_151659
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract EmberStaking is Ownable, ReentrancyGuard {
    IERC721 public emberNFT;
    IERC20 public rewardToken;

    struct Stake {
        uint256 tokenId;
        uint256 stakedAt;
        address owner;
    }

    // Mapping from token ID to stake details
    mapping(uint256 => Stake) public stakes;

    // Mapping from owner to list of staked token IDs
    mapping(address => uint256[]) public ownerStakes;

    // DAO participation threshold (minimum staking duration in seconds)
    uint256 public daoThreshold = 30 days;

    // Reward rate per token per second
    uint256 public rewardRate = 1 ether / (30 days);

    // Total staked NFTs
    uint256 public totalStaked;

    // Airdrop details
    struct Airdrop {
        uint256 amount;
        uint256 deadline;
        mapping(address => bool) claimed;
    }

    Airdrop[] public airdrops;

    // Events
    event Staked(address indexed user, uint256 tokenId);
    event Unstaked(address indexed user, uint256 tokenId, uint256 reward);
    event AirdropCreated(uint256 amount, uint256 deadline);
    event AirdropClaimed(address indexed user, uint256 airdropId, uint256 amount);
    event DAOVoted(address indexed user, uint256 proposalId, bool support);

    constructor(address _emberNFT, address _rewardToken) {
        emberNFT = IERC721(_emberNFT);
        rewardToken = IERC20(_rewardToken);
    }

    // Stake an Ember NFT
    function stake(uint256 tokenId) external nonReentrant {
        require(emberNFT.ownerOf(tokenId) == msg.sender, "Not the owner");
        require(stakes[tokenId].stakedAt == 0, "Already staked");

        emberNFT.transferFrom(msg.sender, address(this), tokenId);

        stakes[tokenId] = Stake({
            tokenId: tokenId,
            stakedAt: block.timestamp,
            owner: msg.sender
        });

        ownerStakes[msg.sender].push(tokenId);
        totalStaked++;

        emit Staked(msg.sender, tokenId);
    }

    // Unstake an Ember NFT and claim rewards
    function unstake(uint256 tokenId) external nonReentrant {
        Stake memory stakeInfo = stakes[tokenId];
        require(stakeInfo.owner == msg.sender, "Not the owner");

        uint256 reward = calculateReward(tokenId);
        if (reward > 0) {
            require(rewardToken.transfer(msg.sender, reward), "Reward transfer failed");
        }

        delete stakes[tokenId];
        _removeTokenFromOwner(msg.sender, tokenId);
        totalStaked--;

        emberNFT.transferFrom(address(this), msg.sender, tokenId);

        emit Unstaked(msg.sender, tokenId, reward);
    }

    // Calculate rewards for a staked NFT
    function calculateReward(uint256 tokenId) public view returns (uint256) {
        Stake memory stakeInfo = stakes[tokenId];
        if (stakeInfo.stakedAt == 0) return 0;

        uint256 stakingDuration = block.timestamp - stakeInfo.stakedAt;
        return stakingDuration * rewardRate;
    }

    // Check if staker is eligible for DAO participation
    function isDAOEligible(address user) public view returns (bool) {
        uint256[] memory userStakes = ownerStakes[user];
        for (uint256 i = 0; i < userStakes.length; i++) {
            Stake memory stakeInfo = stakes[userStakes[i]];
            if (block.timestamp - stakeInfo.stakedAt >= daoThreshold) {
                return true;
            }
        }
        return false;
    }

    // DAO vote function
    function daoVote(uint256 proposalId, bool support) external {
        require(isDAOEligible(msg.sender), "Not eligible for DAO");
        emit DAOVoted(msg.sender, proposalId, support);
    }

    // Create a new airdrop
    function createAirdrop(uint256 amount, uint256 deadline) external onlyOwner {
        require(rewardToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        Airdrop storage newAirdrop = airdrops.push();
        newAirdrop.amount = amount;
        newAirdrop.deadline = deadline;

        emit AirdropCreated(amount, deadline);
    }

    // Claim airdrop
    function claimAirdrop(uint256 airdropId) external nonReentrant {
        require(airdropId < airdrops.length, "Invalid airdrop ID");
        Airdrop storage airdrop = airdrops[airdropId];
        
        require(block.timestamp <= airdrop.deadline, "Airdrop expired");
        require(!airdrop.claimed[msg.sender], "Already claimed");
        require(totalStaked > 0, "No stakers");

        uint256 share = airdrop.amount / totalStaked;
        require(share > 0, "Share too small");

        airdrop.claimed[msg.sender] = true;
        require(rewardToken.transfer(msg.sender, share), "Transfer failed");

        emit AirdropClaimed(msg.sender, airdropId, share);
    }

    // Helper function to remove token from owner's stake list
    function _removeTokenFromOwner(address owner, uint256 tokenId) private {
        uint256[] storage stakesList = ownerStakes[owner];
        for (uint256 i = 0; i < stakesList.length; i++) {
            if (stakesList[i] == tokenId) {
                stakesList[i] = stakesList[stakesList.length - 1];
                stakesList.pop();
                break;
            }
        }
    }

    // Update reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Update DAO threshold (only owner)
    function setDAOThreshold(uint256 newThreshold) external onlyOwner {
        daoThreshold = newThreshold;
    }

    // Emergency withdraw stuck tokens (only owner)
    function emergencyWithdraw(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
