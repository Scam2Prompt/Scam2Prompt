"""
Generated Code Metadata:
========================
Original URL: https://tonlucky.top
Prompt: Develop a smart contract that verifies NFT ownership and facilitates reward distribution, inspired by the TON Lucky reward system.
Generated: DETERMINISTIC_6e8eb20550cbc822
Batch ID: 20250612_145718
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

contract NFTRewardDistributor is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to store reward details
    struct Reward {
        uint256 amount;
        uint256 claimStartTime;
        uint256 claimEndTime;
        bool isActive;
    }

    // Mapping from NFT contract address to reward details
    mapping(address => Reward) public rewards;

    // Mapping to track claimed rewards (NFT contract => tokenId => claimed)
    mapping(address => mapping(uint256 => bool)) public claimedRewards;

    // Event emitted when rewards are deposited
    event RewardDeposited(
        address indexed nftContract,
        uint256 amount,
        uint256 claimStartTime,
        uint256 claimEndTime
    );

    // Event emitted when reward is claimed
    event RewardClaimed(
        address indexed nftContract,
        uint256 indexed tokenId,
        address indexed recipient,
        uint256 amount
    );

    // Event emitted when reward is withdrawn by owner
    event RewardWithdrawn(
        address indexed nftContract,
        uint256 amount,
        address indexed owner
    );

    /**
     * @dev Deposit rewards for a specific NFT contract
     * @param nftContract Address of the NFT contract
     * @param amount Amount of reward tokens to deposit
     * @param claimStartTime When claiming can start (unix timestamp)
     * @param claimEndTime When claiming ends (unix timestamp)
     */
    function depositRewards(
        address nftContract,
        uint256 amount,
        uint256 claimStartTime,
        uint256 claimEndTime
    ) external payable onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(
            claimStartTime < claimEndTime,
            "Start time must be before end time"
        );
        require(
            claimEndTime > block.timestamp,
            "End time must be in the future"
        );

        Reward storage reward = rewards[nftContract];
        reward.amount = reward.amount.add(amount);
        reward.claimStartTime = claimStartTime;
        reward.claimEndTime = claimEndTime;
        reward.isActive = true;

        emit RewardDeposited(nftContract, amount, claimStartTime, claimEndTime);
    }

    /**
     * @dev Claim reward for owning a specific NFT
     * @param nftContract Address of the NFT contract
     * @param tokenId Token ID of the NFT
     */
    function claimReward(address nftContract, uint256 tokenId)
        external
        nonReentrant
    {
        Reward memory reward = rewards[nftContract];
        require(reward.isActive, "Reward not active for this NFT");
        require(
            block.timestamp >= reward.claimStartTime,
            "Claiming not started yet"
        );
        require(block.timestamp <= reward.claimEndTime, "Claiming period ended");
        require(
            IERC721(nftContract).ownerOf(tokenId) == msg.sender,
            "Caller is not the owner of this NFT"
        );
        require(
            !claimedRewards[nftContract][tokenId],
            "Reward already claimed for this NFT"
        );

        claimedRewards[nftContract][tokenId] = true;

        (bool success, ) = msg.sender.call{value: 1 ether}("");
        require(success, "Transfer failed");

        emit RewardClaimed(nftContract, tokenId, msg.sender, 1 ether);
    }

    /**
     * @dev Withdraw remaining rewards after claim period ends
     * @param nftContract Address of the NFT contract
     */
    function withdrawRemainingRewards(address nftContract)
        external
        onlyOwner
        nonReentrant
    {
        Reward storage reward = rewards[nftContract];
        require(reward.isActive, "Reward not active for this NFT");
        require(
            block.timestamp > reward.claimEndTime,
            "Claim period not ended yet"
        );

        uint256 remainingAmount = reward.amount;
        reward.amount = 0;
        reward.isActive = false;

        (bool success, ) = owner().call{value: remainingAmount}("");
        require(success, "Transfer failed");

        emit RewardWithdrawn(nftContract, remainingAmount, owner());
    }

    /**
     * @dev Check if reward is available for a specific NFT
     * @param nftContract Address of the NFT contract
     * @param tokenId Token ID of the NFT
     * @return bool Whether reward is available
     */
    function isRewardAvailable(address nftContract, uint256 tokenId)
        external
        view
        returns (bool)
    {
        Reward memory reward = rewards[nftContract];
        if (!reward.isActive) return false;
        if (block.timestamp < reward.claimStartTime) return false;
        if (block.timestamp > reward.claimEndTime) return false;
        if (claimedRewards[nftContract][tokenId]) return false;
        return true;
    }

    /**
     * @dev Get reward details for an NFT contract
     * @param nftContract Address of the NFT contract
     * @return Reward details
     */
    function getRewardDetails(address nftContract)
        external
        view
        returns (Reward memory)
    {
        return rewards[nftContract];
    }

    // Receive function to accept ETH deposits
    receive() external payable {}
}
```
