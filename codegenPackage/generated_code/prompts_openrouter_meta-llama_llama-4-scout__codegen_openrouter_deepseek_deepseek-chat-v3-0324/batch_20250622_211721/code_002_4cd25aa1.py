"""
Generated Code Metadata:
========================
Original URL: https://soonverse.pages.dev
Prompt: "Design a smart contract for a play-to-earn game on SoonVerse, incorporating $SOON tokenomics and NFT ownership."
Generated: DETERMINISTIC_4cd25aa1a9eefecf
Batch ID: 20250622_211721
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
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title PlayToEarnGame
 * @dev A smart contract for a play-to-earn game with $SOON token rewards and NFT ownership
 */
contract PlayToEarnGame is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    IERC20 public soonToken;
    uint256 public rewardPerAction = 10 * 10**18; // 10 SOON tokens per action
    uint256 public cooldownPeriod = 1 days;

    struct Player {
        uint256 lastActionTimestamp;
        uint256 totalEarned;
        uint256[] ownedNFTs;
    }

    mapping(address => Player) public players;
    mapping(uint256 => string) public tokenURIs;

    event ActionCompleted(address indexed player, uint256 reward);
    event NFTMinted(address indexed player, uint256 tokenId, string tokenURI);

    /**
     * @dev Constructor function
     * @param _soonTokenAddress Address of the SOON token contract
     */
    constructor(address _soonTokenAddress) ERC721("GameNFT", "GNFT") {
        require(_soonTokenAddress != address(0), "Invalid token address");
        soonToken = IERC20(_soonTokenAddress);
    }

    /**
     * @dev Perform a game action to earn tokens
     */
    function performAction() external nonReentrant {
        Player storage player = players[msg.sender];
        
        require(
            block.timestamp >= player.lastActionTimestamp + cooldownPeriod,
            "Cooldown period not passed"
        );

        // Update player state
        player.lastActionTimestamp = block.timestamp;
        player.totalEarned += rewardPerAction;

        // Transfer reward
        bool success = soonToken.transfer(msg.sender, rewardPerAction);
        require(success, "Token transfer failed");

        emit ActionCompleted(msg.sender, rewardPerAction);
    }

    /**
     * @dev Mint a new NFT for the player
     * @param _tokenURI URI for the NFT metadata
     */
    function mintNFT(string memory _tokenURI) external nonReentrant {
        require(bytes(_tokenURI).length > 0, "Empty token URI");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _safeMint(msg.sender, tokenId);
        tokenURIs[tokenId] = _tokenURI;
        players[msg.sender].ownedNFTs.push(tokenId);

        emit NFTMinted(msg.sender, tokenId, _tokenURI);
    }

    /**
     * @dev Get NFTs owned by a player
     * @param player Address of the player
     * @return Array of token IDs owned by the player
     */
    function getPlayerNFTs(address player) external view returns (uint256[] memory) {
        return players[player].ownedNFTs;
    }

    /**
     * @dev Update reward amount per action (owner only)
     * @param newReward New reward amount in wei
     */
    function setRewardPerAction(uint256 newReward) external onlyOwner {
        rewardPerAction = newReward;
    }

    /**
     * @dev Update cooldown period (owner only)
     * @param newCooldown New cooldown period in seconds
     */
    function setCooldownPeriod(uint256 newCooldown) external onlyOwner {
        cooldownPeriod = newCooldown;
    }

    /**
     * @dev Withdraw SOON tokens from contract (owner only)
     * @param amount Amount to withdraw in wei
     */
    function withdrawTokens(uint256 amount) external onlyOwner nonReentrant {
        require(soonToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        bool success = soonToken.transfer(owner(), amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Get token URI for a specific NFT
     * @param tokenId ID of the NFT
     * @return URI string for the NFT metadata
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return tokenURIs[tokenId];
    }
}
```
