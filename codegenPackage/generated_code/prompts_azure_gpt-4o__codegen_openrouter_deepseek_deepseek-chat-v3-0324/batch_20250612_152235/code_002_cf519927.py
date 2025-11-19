"""
Generated Code Metadata:
========================
Original URL: https://puffmypanda.pages.dev
Prompt: Create a staking protocol in Solidity for Puff Puff Pandas NFTs that allows holders to lock their NFTs and earn yield in $PUFFS tokens, as outlined in the Puff Like A Panda ecosystem.
Generated: DETERMINISTIC_cf5199279853e068
Batch ID: 20250612_152235
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PuffPuffPandasStaking is ReentrancyGuard, Ownable {
    // Interfaces for ERC721 and ERC20
    IERC721 public nftCollection;
    IERC20 public puffToken;

    // Struct to store stake information
    struct Stake {
        address owner;
        uint256 tokenId;
        uint256 stakedAt;
    }

    // Reward rate per NFT per second
    uint256 public rewardRatePerToken;

    // Mapping from tokenId to Stake
    mapping(uint256 => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 indexed tokenId, uint256 timestamp);
    event Unstaked(address indexed user, uint256 indexed tokenId, uint256 timestamp, uint256 reward);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    constructor(
        address _nftCollection,
        address _puffToken,
        uint256 _rewardRatePerToken
    ) {
        require(_nftCollection != address(0), "NFT collection address cannot be zero");
        require(_puffToken != address(0), "PUFF token address cannot be zero");
        
        nftCollection = IERC721(_nftCollection);
        puffToken = IERC20(_puffToken);
        rewardRatePerToken = _rewardRatePerToken;
    }

    /**
     * @dev Stake an NFT to earn rewards
     * @param tokenId The ID of the NFT to stake
     */
    function stake(uint256 tokenId) external nonReentrant {
        require(nftCollection.ownerOf(tokenId) == msg.sender, "You don't own this NFT");
        require(stakes[tokenId].owner == address(0), "NFT is already staked");

        stakes[tokenId] = Stake({
            owner: msg.sender,
            tokenId: tokenId,
            stakedAt: block.timestamp
        });

        nftCollection.transferFrom(msg.sender, address(this), tokenId);

        emit Staked(msg.sender, tokenId, block.timestamp);
    }

    /**
     * @dev Unstake an NFT and claim rewards
     * @param tokenId The ID of the NFT to unstake
     */
    function unstake(uint256 tokenId) external nonReentrant {
        Stake memory stakeInfo = stakes[tokenId];
        require(stakeInfo.owner == msg.sender, "You don't own this stake");

        uint256 reward = calculateReward(tokenId);
        delete stakes[tokenId];

        nftCollection.transferFrom(address(this), msg.sender, tokenId);

        if (reward > 0) {
            require(puffToken.transfer(msg.sender, reward), "Reward transfer failed");
        }

        emit Unstaked(msg.sender, tokenId, block.timestamp, reward);
    }

    /**
     * @dev Claim rewards without unstaking
     * @param tokenId The ID of the staked NFT
     */
    function claimReward(uint256 tokenId) external nonReentrant {
        Stake memory stakeInfo = stakes[tokenId];
        require(stakeInfo.owner == msg.sender, "You don't own this stake");

        uint256 reward = calculateReward(tokenId);
        require(reward > 0, "No rewards to claim");

        stakes[tokenId].stakedAt = block.timestamp;

        require(puffToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate reward for a staked NFT
     * @param tokenId The ID of the staked NFT
     * @return reward The calculated reward amount
     */
    function calculateReward(uint256 tokenId) public view returns (uint256) {
        Stake memory stakeInfo = stakes[tokenId];
        if (stakeInfo.owner == address(0)) return 0;

        uint256 stakedDuration = block.timestamp - stakeInfo.stakedAt;
        return stakedDuration * rewardRatePerToken;
    }

    /**
     * @dev Update the reward rate (only owner)
     * @param newRate The new reward rate per token per second
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRatePerToken = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Withdraw any accidentally sent ERC20 tokens (only owner)
     * @param token The token contract address
     * @param amount The amount to withdraw
     */
    function withdrawERC20(address token, uint256 amount) external onlyOwner {
        require(token != address(puffToken), "Cannot withdraw reward token");
        IERC20(token).transfer(owner(), amount);
    }

    /**
     * @dev Withdraw any accidentally sent ERC721 tokens (only owner)
     * @param token The token contract address
     * @param tokenId The ID of the NFT to withdraw
     */
    function withdrawERC721(address token, uint256 tokenId) external onlyOwner {
        require(token != address(nftCollection), "Cannot withdraw staked NFTs");
        IERC721(token).transferFrom(address(this), owner(), tokenId);
    }
}
```
