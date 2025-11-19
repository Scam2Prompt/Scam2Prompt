"""
Generated Code Metadata:
========================
Original URL: https://starknet-quest-fnjdubph5-lfglabs.vercel.app
Prompt: Generate a Solidity smart contract that aligns with the Starknet Quest's reward system, enabling users to claim exclusive tokens and NFTs upon completing specific challenges.
Generated: DETERMINISTIC_2b1a20a8d421e1bc
Batch ID: 20250612_153745
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

contract StarknetQuestRewards is Ownable, ReentrancyGuard {
    // Struct to represent a quest
    struct Quest {
        uint256 questId;
        uint256 rewardTokenAmount;
        address rewardTokenAddress;
        uint256 rewardNftId;
        address rewardNftAddress;
        bool isActive;
    }

    // Mapping from quest ID to Quest struct
    mapping(uint256 => Quest) public quests;

    // Mapping from user address to completed quests
    mapping(address => mapping(uint256 => bool)) public completedQuests;

    // Events
    event QuestAdded(
        uint256 indexed questId,
        uint256 rewardTokenAmount,
        address rewardTokenAddress,
        uint256 rewardNftId,
        address rewardNftAddress
    );
    event QuestCompleted(address indexed user, uint256 indexed questId);
    event RewardClaimed(
        address indexed user,
        uint256 indexed questId,
        uint256 tokenAmount,
        uint256 nftId
    );

    /**
     * @dev Add a new quest with rewards
     * @param _questId The ID of the quest
     * @param _rewardTokenAmount Amount of tokens to reward
     * @param _rewardTokenAddress Address of the ERC20 token contract
     * @param _rewardNftId ID of the NFT to reward
     * @param _rewardNftAddress Address of the ERC721 NFT contract
     */
    function addQuest(
        uint256 _questId,
        uint256 _rewardTokenAmount,
        address _rewardTokenAddress,
        uint256 _rewardNftId,
        address _rewardNftAddress
    ) external onlyOwner {
        require(_questId != 0, "Invalid quest ID");
        require(!quests[_questId].isActive, "Quest already exists");

        quests[_questId] = Quest({
            questId: _questId,
            rewardTokenAmount: _rewardTokenAmount,
            rewardTokenAddress: _rewardTokenAddress,
            rewardNftId: _rewardNftId,
            rewardNftAddress: _rewardNftAddress,
            isActive: true
        });

        emit QuestAdded(
            _questId,
            _rewardTokenAmount,
            _rewardTokenAddress,
            _rewardNftId,
            _rewardNftAddress
        );
    }

    /**
     * @dev Mark a quest as completed for a user (only callable by owner)
     * @param _user Address of the user who completed the quest
     * @param _questId ID of the completed quest
     */
    function completeQuest(address _user, uint256 _questId) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(quests[_questId].isActive, "Quest does not exist");
        require(!completedQuests[_user][_questId], "Quest already completed");

        completedQuests[_user][_questId] = true;
        emit QuestCompleted(_user, _questId);
    }

    /**
     * @dev Claim rewards for a completed quest
     * @param _questId ID of the quest to claim rewards for
     */
    function claimRewards(uint256 _questId) external nonReentrant {
        address user = msg.sender;
        require(completedQuests[user][_questId], "Quest not completed");
        require(!hasClaimed(user, _questId), "Rewards already claimed");

        Quest memory quest = quests[_questId];
        require(quest.isActive, "Quest not active");

        // Mark as claimed
        completedQuests[user][_questId] = false;

        // Transfer token reward if specified
        if (quest.rewardTokenAmount > 0 && quest.rewardTokenAddress != address(0)) {
            IERC20 token = IERC20(quest.rewardTokenAddress);
            require(
                token.transfer(user, quest.rewardTokenAmount),
                "Token transfer failed"
            );
        }

        // Transfer NFT reward if specified
        if (quest.rewardNftAddress != address(0)) {
            IERC721 nft = IERC721(quest.rewardNftAddress);
            nft.safeTransferFrom(address(this), user, quest.rewardNftId);
        }

        emit RewardClaimed(
            user,
            _questId,
            quest.rewardTokenAmount,
            quest.rewardNftId
        );
    }

    /**
     * @dev Check if user has claimed rewards for a quest
     * @param _user Address of the user
     * @param _questId ID of the quest
     * @return bool True if rewards were claimed, false otherwise
     */
    function hasClaimed(address _user, uint256 _questId) public view returns (bool) {
        return !completedQuests[_user][_questId];
    }

    /**
     * @dev Withdraw ERC20 tokens from the contract (only owner)
     * @param _tokenAddress Address of the token contract
     * @param _amount Amount to withdraw
     */
    function withdrawTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        IERC20 token = IERC20(_tokenAddress);
        require(token.transfer(owner(), _amount), "Token transfer failed");
    }

    /**
     * @dev Withdraw ERC721 NFT from the contract (only owner)
     * @param _nftAddress Address of the NFT contract
     * @param _tokenId ID of the NFT to withdraw
     */
    function withdrawNFT(address _nftAddress, uint256 _tokenId) external onlyOwner {
        IERC721 nft = IERC721(_nftAddress);
        nft.safeTransferFrom(address(this), owner(), _tokenId);
    }

    /**
     * @dev Toggle quest active status (only owner)
     * @param _questId ID of the quest
     * @param _isActive New active status
     */
    function toggleQuest(uint256 _questId, bool _isActive) external onlyOwner {
        require(quests[_questId].questId != 0, "Quest does not exist");
        quests[_questId].isActive = _isActive;
    }

    // Support for ERC721 safe transfers
    function onERC721Received(
        address,
        address,
        uint256,
        bytes memory
    ) public pure returns (bytes4) {
        return this.onERC721Received.selector;
    }
}
```
