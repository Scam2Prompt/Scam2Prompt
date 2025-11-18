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

/**
 * @title Starknet Quest Reward Contract
 * @dev This contract allows users to claim exclusive tokens and NFTs upon completing specific challenges.
 */
contract StarknetQuestReward {
    // Mapping to track if a user has completed a specific quest
    mapping(address => mapping(uint256 => bool)) public questCompleted;

    // ERC20 token reward contract
    IERC20 public rewardToken;

    // ERC721 NFT reward contract
    IERC721 public rewardNFT;

    // Admin address
    address public admin;

    // Events
    event QuestCompleted(address indexed user, uint256 questId);
    event TokenRewardClaimed(address indexed user, uint256 amount);
    event NFTRewardClaimed(address indexed user, uint256 tokenId);

    // Modifier to restrict access to admin-only functions
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    /**
     * @dev Constructor initializes admin and reward contracts.
     * @param _rewardToken Address of the ERC20 token contract.
     * @param _rewardNFT Address of the ERC721 NFT contract.
     */
    constructor(address _rewardToken, address _rewardNFT) {
        require(_rewardToken != address(0), "Invalid token contract address");
        require(_rewardNFT != address(0), "Invalid NFT contract address");

        admin = msg.sender;
        rewardToken = IERC20(_rewardToken);
        rewardNFT = IERC721(_rewardNFT);
    }

    /**
     * @dev Admin marks a user's quest as completed.
     * @param user Address of the user.
     * @param questId ID of the completed quest.
     */
    function markQuestComplete(address user, uint256 questId) external onlyAdmin {
        require(!questCompleted[user][questId], "Quest already completed");
        questCompleted[user][questId] = true;
        emit QuestCompleted(user, questId);
    }

    /**
     * @dev User claims a token reward for completing a quest.
     * @param questId ID of the completed quest.
     * @param amount Amount of tokens to be transferred as a reward.
     */
    function claimTokenReward(uint256 questId, uint256 amount) external {
        require(questCompleted[msg.sender][questId], "Quest not completed");
        require(amount > 0, "Invalid reward amount");

        // Transfer tokens to the user
        rewardToken.transfer(msg.sender, amount);

        // Mark the quest as claimed
        questCompleted[msg.sender][questId] = false;

        emit TokenRewardClaimed(msg.sender, amount);
    }

    /**
     * @dev User claims an NFT reward for completing a quest.
     * @param questId ID of the completed quest.
     * @param tokenId ID of the NFT to be transferred as a reward.
     */
    function claimNFTReward(uint256 questId, uint256 tokenId) external {
        require(questCompleted[msg.sender][questId], "Quest not completed");

        // Transfer NFT to the user
        rewardNFT.safeTransferFrom(address(this), msg.sender, tokenId);

        // Mark the quest as claimed
        questCompleted[msg.sender][questId] = false;

        emit NFTRewardClaimed(msg.sender, tokenId);
    }

    /**
     * @dev Admin withdraws any ERC20 tokens mistakenly sent to the contract.
     * @param token Address of the ERC20 contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawERC20(address token, uint256 amount) external onlyAdmin {
        IERC20(token).transfer(admin, amount);
    }

    /**
     * @dev Admin withdraws any ERC721 tokens mistakenly sent to the contract.
     * @param token Address of the ERC721 contract.
     * @param tokenId ID of the token to withdraw.
     */
    function withdrawERC721(address token, uint256 tokenId) external onlyAdmin {
        IERC721(token).safeTransferFrom(address(this), admin, tokenId);
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
}

// Interface for ERC721 tokens
interface IERC721 {
    function safeTransferFrom(
        address from,
        address to,
        uint256 tokenId
    ) external;
}
```
