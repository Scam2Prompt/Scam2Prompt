"""
Generated Code Metadata:
========================
Original URL: https://tgdrop.cc
Prompt: Create a smart contract in Solidity for a TON-based reward system that distributes rewards based on NFT or USDT qualifications.
Generated: DETERMINISTIC_573797429fbaa59a
Batch ID: 20250612_153915
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

contract TONRewardSystem is Ownable, ReentrancyGuard {
    IERC20 public usdtToken;
    IERC721 public nftToken;

    struct Reward {
        uint256 amount;
        uint256 claimableAfter;
        bool claimed;
    }

    mapping(address => Reward) public rewards;
    mapping(uint256 => bool) public qualifiedNFTs;
    mapping(address => bool) public qualifiedUSDTHolders;

    uint256 public rewardAmount;
    uint256 public lockPeriod;

    event RewardSet(address indexed user, uint256 amount, uint256 claimableAfter);
    event RewardClaimed(address indexed user, uint256 amount);
    event NFTQualified(uint256 indexed tokenId);
    event USDTQualified(address indexed holder);
    event RewardParametersUpdated(uint256 newRewardAmount, uint256 newLockPeriod);

    constructor(
        address _usdtTokenAddress,
        address _nftTokenAddress,
        uint256 _rewardAmount,
        uint256 _lockPeriod
    ) {
        require(_usdtTokenAddress != address(0), "USDT token address cannot be zero");
        require(_nftTokenAddress != address(0), "NFT token address cannot be zero");
        require(_rewardAmount > 0, "Reward amount must be greater than zero");

        usdtToken = IERC20(_usdtTokenAddress);
        nftToken = IERC721(_nftTokenAddress);
        rewardAmount = _rewardAmount;
        lockPeriod = _lockPeriod;
    }

    function setRewardParameters(uint256 _rewardAmount, uint256 _lockPeriod) external onlyOwner {
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        rewardAmount = _rewardAmount;
        lockPeriod = _lockPeriod;
        emit RewardParametersUpdated(_rewardAmount, _lockPeriod);
    }

    function qualifyNFT(uint256 tokenId) external onlyOwner {
        require(nftToken.ownerOf(tokenId) != address(0), "NFT does not exist");
        qualifiedNFTs[tokenId] = true;
        emit NFTQualified(tokenId);
    }

    function qualifyUSDT(address holder) external onlyOwner {
        require(holder != address(0), "Holder address cannot be zero");
        qualifiedUSDTHolders[holder] = true;
        emit USDTQualified(holder);
    }

    function checkEligibility(address user) public view returns (bool) {
        // Check NFT qualification
        uint256 balance = nftToken.balanceOf(user);
        for (uint256 i = 0; i < balance; i++) {
            uint256 tokenId = nftToken.tokenOfOwnerByIndex(user, i);
            if (qualifiedNFTs[tokenId]) {
                return true;
            }
        }

        // Check USDT qualification
        if (qualifiedUSDTHolders[user] && usdtToken.balanceOf(user) > 0) {
            return true;
        }

        return false;
    }

    function distributeReward(address user) external nonReentrant {
        require(checkEligibility(user), "User is not eligible for reward");
        require(rewards[user].amount == 0, "Reward already distributed");

        rewards[user] = Reward({
            amount: rewardAmount,
            claimableAfter: block.timestamp + lockPeriod,
            claimed: false
        });

        emit RewardSet(user, rewardAmount, block.timestamp + lockPeriod);
    }

    function claimReward() external nonReentrant {
        Reward storage reward = rewards[msg.sender];
        require(reward.amount > 0, "No reward to claim");
        require(!reward.claimed, "Reward already claimed");
        require(block.timestamp >= reward.claimableAfter, "Reward not yet claimable");

        reward.claimed = true;
        require(usdtToken.transfer(msg.sender, reward.amount), "USDT transfer failed");

        emit RewardClaimed(msg.sender, reward.amount);
    }

    function withdrawUSDT(uint256 amount) external onlyOwner {
        require(usdtToken.transfer(owner(), amount), "USDT transfer failed");
    }
}
```
