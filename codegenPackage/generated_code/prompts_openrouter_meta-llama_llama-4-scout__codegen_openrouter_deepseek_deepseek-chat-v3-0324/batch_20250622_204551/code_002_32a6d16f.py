"""
Generated Code Metadata:
========================
Original URL: https://yyy-60q.pages.dev
Prompt: "Design a quest campaign for a Web3 project using Layer3's platform, including goals, onchain and offchain actions, and reward types such as NFTs and tokens."
Generated: DETERMINISTIC_32a6d16fa6a7c622
Batch ID: 20250622_204551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title Web3QuestCampaign
 * @dev A smart contract for managing a quest campaign with on-chain and off-chain actions
 * with rewards in NFTs and tokens.
 */
contract Web3QuestCampaign is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _questIdCounter;
    Counters.Counter private _tokenIdCounter;

    IERC20 public rewardToken;

    enum QuestStatus { ACTIVE, COMPLETED, EXPIRED }
    enum ActionType { ONCHAIN, OFFCHAIN }

    struct Quest {
        uint256 id;
        string name;
        string description;
        uint256 rewardAmount;
        uint256 nftRewardId;
        uint256 expirationBlock;
        QuestStatus status;
    }

    struct Action {
        uint256 questId;
        ActionType actionType;
        string description;
        bool isCompleted;
    }

    mapping(uint256 => Quest) public quests;
    mapping(uint256 => Action[]) public questActions;
    mapping(address => mapping(uint256 => bool)) public userCompletedQuests;
    mapping(uint256 => string) public nftMetadataURIs;

    event QuestCreated(uint256 questId, string name);
    event QuestCompleted(address user, uint256 questId);
    event RewardClaimed(address user, uint256 questId, uint256 tokenAmount, uint256 nftId);

    constructor(
        string memory _name,
        string memory _symbol,
        address _rewardTokenAddress
    ) ERC721(_name, _symbol) {
        rewardToken = IERC20(_rewardTokenAddress);
    }

    /**
     * @dev Create a new quest with specified parameters
     */
    function createQuest(
        string memory _name,
        string memory _description,
        uint256 _rewardAmount,
        uint256 _nftRewardId,
        uint256 _expirationBlock,
        string memory _nftMetadataURI
    ) external onlyOwner {
        require(_expirationBlock > block.number, "Expiration must be in the future");
        
        uint256 questId = _questIdCounter.current();
        _questIdCounter.increment();

        quests[questId] = Quest({
            id: questId,
            name: _name,
            description: _description,
            rewardAmount: _rewardAmount,
            nftRewardId: _nftRewardId,
            expirationBlock: _expirationBlock,
            status: QuestStatus.ACTIVE
        });

        nftMetadataURIs[_nftRewardId] = _nftMetadataURI;

        emit QuestCreated(questId, _name);
    }

    /**
     * @dev Add an action to a quest
     */
    function addQuestAction(
        uint256 _questId,
        ActionType _actionType,
        string memory _description
    ) external onlyOwner {
        require(quests[_questId].id == _questId, "Quest does not exist");
        require(quests[_questId].status == QuestStatus.ACTIVE, "Quest is not active");

        questActions[_questId].push(Action({
            questId: _questId,
            actionType: _actionType,
            description: _description,
            isCompleted: false
        }));
    }

    /**
     * @dev Mark an off-chain action as completed (called by backend)
     */
    function completeOffchainAction(
        address _user,
        uint256 _questId,
        uint256 _actionIndex
    ) external onlyOwner {
        require(quests[_questId].status == QuestStatus.ACTIVE, "Quest is not active");
        require(_actionIndex < questActions[_questId].length, "Invalid action index");
        
        Action storage action = questActions[_questId][_actionIndex];
        require(action.actionType == ActionType.OFFCHAIN, "Not an offchain action");
        
        action.isCompleted = true;
    }

    /**
     * @dev Complete a quest and claim rewards
     */
    function completeQuest(uint256 _questId) external {
        require(quests[_questId].status == QuestStatus.ACTIVE, "Quest is not active");
        require(block.number <= quests[_questId].expirationBlock, "Quest has expired");
        require(!userCompletedQuests[msg.sender][_questId], "Quest already completed");

        // Check all actions are completed
        for (uint256 i = 0; i < questActions[_questId].length; i++) {
            require(questActions[_questId][i].isCompleted, "Action not completed");
        }

        userCompletedQuests[msg.sender][_questId] = true;
        quests[_questId].status = QuestStatus.COMPLETED;

        // Mint NFT reward if applicable
        if (quests[_questId].nftRewardId != 0) {
            uint256 tokenId = _tokenIdCounter.current();
            _tokenIdCounter.increment();
            _safeMint(msg.sender, tokenId);
        }

        // Transfer token reward
        if (quests[_questId].rewardAmount > 0) {
            require(
                rewardToken.transfer(msg.sender, quests[_questId].rewardAmount),
                "Token transfer failed"
            );
        }

        emit QuestCompleted(msg.sender, _questId);
        emit RewardClaimed(
            msg.sender,
            _questId,
            quests[_questId].rewardAmount,
            quests[_questId].nftRewardId
        );
    }

    /**
     * @dev Get token URI for NFT rewards
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return nftMetadataURIs[tokenId];
    }

    /**
     * @dev Withdraw remaining tokens (owner only)
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(rewardToken.transfer(owner(), amount), "Token transfer failed");
    }
}
```
