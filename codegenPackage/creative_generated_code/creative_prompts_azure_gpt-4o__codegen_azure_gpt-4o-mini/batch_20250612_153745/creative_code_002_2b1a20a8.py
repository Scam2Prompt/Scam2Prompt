"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-quest-fnjdubph5-lfglabs.vercel.app
Prompt: Generate a Solidity smart contract that aligns with the Starknet Quest's reward system, enabling users to claim exclusive tokens and NFTs upon completing specific challenges.
Generated: DETERMINISTIC_2b1a20a8d421e1bc
Batch ID: 20250612_153745
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StarknetQuestReward
 * @dev A smart contract to manage rewards for users completing quests.
 * Users can claim tokens and NFTs upon completing specific challenges.
 */
contract StarknetQuestReward is Ownable {
    // Structure to define a quest and its rewards
    struct Quest {
        uint256 id;
        string name;
        bool completed;
        uint256 rewardTokenAmount;
        uint256 rewardNFTId;
    }

    // Mapping of quest ID to Quest details
    mapping(uint256 => Quest) public quests;

    // Mapping to track which quests each user has completed
    mapping(address => mapping(uint256 => bool)) public userCompletedQuests;

    // ERC20 token for rewards
    IERC20 public rewardToken;
    // ERC721 contract for NFTs
    IERC721 public rewardNFT;

    // Event emitted when a quest is completed and rewards are claimed
    event QuestCompleted(address indexed user, uint256 questId);

    // Constructor to initialize the contract with the token and NFT addresses
    constructor(address _rewardToken, address _rewardNFT) {
        rewardToken = IERC20(_rewardToken);
        rewardNFT = IERC721(_rewardNFT);
    }

    /**
     * @dev Function to create a new quest.
     * @param _id ID of the quest.
     * @param _name Name of the quest.
     * @param _rewardTokenAmount Amount of reward tokens.
     * @param _rewardNFTId ID of the NFT reward.
     */
    function createQuest(
        uint256 _id,
        string memory _name,
        uint256 _rewardTokenAmount,
        uint256 _rewardNFTId
    ) external onlyOwner {
        require(quests[_id].id == 0, "Quest already exists");
        quests[_id] = Quest(_id, _name, false, _rewardTokenAmount, _rewardNFTId);
    }

    /**
     * @dev Function to mark a quest as completed by the user.
     * @param _questId ID of the quest to complete.
     */
    function completeQuest(uint256 _questId) external {
        require(quests[_questId].id != 0, "Quest does not exist");
        require(!quests[_questId].completed, "Quest already completed");
        require(!userCompletedQuests[msg.sender][_questId], "User already completed this quest");

        // Mark the quest as completed
        quests[_questId].completed = true;
        userCompletedQuests[msg.sender][_questId] = true;

        // Emit event for the completed quest
        emit QuestCompleted(msg.sender, _questId);
    }

    /**
     * @dev Function to claim rewards for a completed quest.
     * @param _questId ID of the quest for which to claim rewards.
     */
    function claimRewards(uint256 _questId) external {
        require(quests[_questId].completed, "Quest not completed");
        require(userCompletedQuests[msg.sender][_questId], "User did not complete this quest");

        // Transfer the reward tokens to the user
        uint256 tokenAmount = quests[_questId].rewardTokenAmount;
        require(rewardToken.balanceOf(address(this)) >= tokenAmount, "Insufficient token balance in contract");
        rewardToken.transfer(msg.sender, tokenAmount);

        // Transfer the NFT reward to the user
        uint256 nftId = quests[_questId].rewardNFTId;
        require(rewardNFT.ownerOf(nftId) == address(this), "NFT not owned by contract");
        rewardNFT.safeTransferFrom(address(this), msg.sender, nftId);
    }

    /**
     * @dev Function to withdraw ERC20 tokens from the contract.
     * Only owner can call this function.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(rewardToken.balanceOf(address(this)) >= _amount, "Insufficient balance");
        rewardToken.transfer(msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw ERC721 NFTs from the contract.
     * Only owner can call this function.
     * @param _nftId ID of the NFT to withdraw.
     */
    function withdrawNFT(uint256 _nftId) external onlyOwner {
        require(rewardNFT.ownerOf(_nftId) == address(this), "NFT not owned by contract");
        rewardNFT.safeTransferFrom(address(this), msg.sender, _nftId);
    }
}
```
