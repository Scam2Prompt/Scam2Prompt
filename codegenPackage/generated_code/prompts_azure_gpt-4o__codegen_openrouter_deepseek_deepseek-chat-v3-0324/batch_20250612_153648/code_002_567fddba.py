"""
Generated Code Metadata:
========================
Original URL: https://pingu-buy.pages.dev
Prompt: Generate code for a reward mechanism like Pingu's "Ice Chest Airdrops," where token holders receive mystery boxes containing tokens, NFTs, or exclusive rewards based on their holdings.
Generated: DETERMINISTIC_567fddba07f02f23
Batch ID: 20250612_153648
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract IceChestAirdrop is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Reward token contract
    IERC20 public rewardToken;
    
    // NFT contract for exclusive rewards
    IERC721 public nftContract;

    // Mapping to track claimed airdrops
    mapping(address => bool) public hasClaimed;

    // Airdrop details
    uint256 public airdropStartTime;
    uint256 public airdropEndTime;
    uint256 public totalRewardPool;
    uint256 public nftRewardCount;
    uint256 public minHoldAmount;

    // Events
    event AirdropClaimed(address indexed user, uint256 tokenAmount, bool receivedNFT);
    event AirdropConfigured(uint256 startTime, uint256 endTime, uint256 rewardPool, uint256 nftCount, uint256 minHold);
    event EmergencyWithdraw(address indexed owner, uint256 amount);

    constructor(
        address _rewardToken,
        address _nftContract,
        uint256 _minHoldAmount
    ) {
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_nftContract != address(0), "Invalid NFT contract address");
        
        rewardToken = IERC20(_rewardToken);
        nftContract = IERC721(_nftContract);
        minHoldAmount = _minHoldAmount;
    }

    /**
     * @dev Configure airdrop parameters
     * @param _startTime Airdrop start timestamp
     * @param _endTime Airdrop end timestamp
     * @param _rewardPool Total reward pool in tokens
     * @param _nftCount Number of NFTs to distribute
     */
    function configureAirdrop(
        uint256 _startTime,
        uint256 _endTime,
        uint256 _rewardPool,
        uint256 _nftCount
    ) external onlyOwner {
        require(_startTime < _endTime, "Invalid time range");
        require(_rewardPool > 0, "Reward pool must be positive");
        require(rewardToken.balanceOf(address(this)) >= _rewardPool, "Insufficient reward tokens");
        require(nftContract.balanceOf(address(this)) >= _nftCount, "Insufficient NFTs");

        airdropStartTime = _startTime;
        airdropEndTime = _endTime;
        totalRewardPool = _rewardPool;
        nftRewardCount = _nftCount;

        emit AirdropConfigured(_startTime, _endTime, _rewardPool, _nftCount, minHoldAmount);
    }

    /**
     * @dev Claim airdrop reward
     */
    function claimAirdrop() external nonReentrant {
        require(block.timestamp >= airdropStartTime, "Airdrop not started");
        require(block.timestamp <= airdropEndTime, "Airdrop ended");
        require(!hasClaimed[msg.sender], "Already claimed");
        require(rewardToken.balanceOf(msg.sender) >= minHoldAmount, "Insufficient token holdings");

        hasClaimed[msg.sender] = true;

        // Calculate token reward (1-5% of minHoldAmount)
        uint256 tokenReward = _calculateTokenReward();
        bool receivedNFT = _tryGiveNFT();

        // Transfer tokens
        require(rewardToken.transfer(msg.sender, tokenReward), "Token transfer failed");

        emit AirdropClaimed(msg.sender, tokenReward, receivedNFT);
    }

    /**
     * @dev Calculate random token reward (1-5% of minHoldAmount)
     */
    function _calculateTokenReward() private view returns (uint256) {
        uint256 random = uint256(keccak256(abi.encodePacked(block.timestamp, msg.sender))) % 5 + 1;
        return minHoldAmount.mul(random).div(100);
    }

    /**
     * @dev Try to give NFT reward (10% chance)
     */
    function _tryGiveNFT() private returns (bool) {
        if (nftRewardCount == 0) return false;
        
        uint256 random = uint256(keccak256(abi.encodePacked(block.timestamp, msg.sender))) % 10;
        if (random == 0) { // 10% chance
            nftRewardCount = nftRewardCount.sub(1);
            nftContract.safeTransferFrom(address(this), msg.sender, nftRewardCount);
            return true;
        }
        return false;
    }

    /**
     * @dev Emergency withdraw remaining tokens
     */
    function emergencyWithdraw() external onlyOwner {
        require(block.timestamp > airdropEndTime, "Airdrop not ended");
        
        uint256 balance = rewardToken.balanceOf(address(this));
        require(rewardToken.transfer(owner(), balance), "Withdraw failed");
        
        emit EmergencyWithdraw(owner(), balance);
    }

    /**
     * @dev Withdraw remaining NFTs
     */
    function withdrawNFTs() external onlyOwner {
        require(block.timestamp > airdropEndTime, "Airdrop not ended");
        
        uint256 balance = nftContract.balanceOf(address(this));
        for (uint256 i = 0; i < balance; i++) {
            uint256 tokenId = nftContract.tokenOfOwnerByIndex(address(this), 0);
            nftContract.safeTransferFrom(address(this), owner(), tokenId);
        }
    }
}
```
