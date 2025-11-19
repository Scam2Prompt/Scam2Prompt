"""
Generated Code Metadata:
========================
Original URL: https://genesisgamersguild.pages.dev
Prompt: Develop a cross-chain solution for a Web3 game using Genesis Gamers Guild's Player Network, ensuring compatibility across multiple chains and games.
Generated: DETERMINISTIC_a231c10c0ed3e6fb
Batch ID: 20250612_152109
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

/**
 * @title CrossChainPlayerNetwork
 * @dev A cross-chain compatible player identity and asset management system
 * for Genesis Gamers Guild's Player Network
 */
contract CrossChainPlayerNetwork is ERC721, Ownable {
    using Counters for Counters.Counter;
    using ECDSA for bytes32;

    Counters.Counter private _tokenIdCounter;

    // Chain ID to contract address mapping for cross-chain verification
    mapping(uint256 => address) public trustedRemoteContracts;

    // Player data structure
    struct PlayerData {
        string gamerTag;
        uint256 reputationScore;
        mapping(uint256 => bool) linkedGames; // chainId => isLinked
        mapping(uint256 => mapping(uint256 => uint256)) gameAssets; // chainId => gameId => assetCount
    }

    // Token ID to PlayerData mapping
    mapping(uint256 => PlayerData) private _playerData;

    // Events
    event PlayerRegistered(uint256 indexed tokenId, string gamerTag);
    event CrossChainLinkEstablished(uint256 indexed tokenId, uint256 chainId);
    event AssetTransferred(
        uint256 indexed fromTokenId,
        uint256 indexed toTokenId,
        uint256 chainId,
        uint256 gameId,
        uint256 amount
    );

    constructor() ERC721("GenesisGamersGuildPlayer", "GGGP") {}

    /**
     * @dev Registers a new player with a gamer tag
     * @param gamerTag The player's chosen gamer tag
     */
    function registerPlayer(string memory gamerTag) external {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(msg.sender, tokenId);
        _playerData[tokenId].gamerTag = gamerTag;
        _playerData[tokenId].reputationScore = 100; // Initial reputation
        
        emit PlayerRegistered(tokenId, gamerTag);
    }

    /**
     * @dev Links a player to another chain
     * @param tokenId The player's token ID
     * @param chainId The target chain ID
     * @param signature Signature from the trusted remote contract
     */
    function linkToChain(
        uint256 tokenId,
        uint256 chainId,
        bytes memory signature
    ) external {
        require(ownerOf(tokenId) == msg.sender, "Not token owner");
        require(trustedRemoteContracts[chainId] != address(0), "Chain not trusted");
        
        bytes32 messageHash = keccak256(abi.encodePacked(tokenId, chainId, address(this)));
        address signer = messageHash.toEthSignedMessageHash().recover(signature);
        
        require(signer == trustedRemoteContracts[chainId], "Invalid signature");
        _playerData[tokenId].linkedGames[chainId] = true;
        
        emit CrossChainLinkEstablished(tokenId, chainId);
    }

    /**
     * @dev Transfers assets between chains
     * @param fromTokenId Source player token ID
     * @param toTokenId Destination player token ID
     * @param chainId Target chain ID
     * @param gameId Game identifier
     * @param amount Asset amount to transfer
     * @param signature Verification signature from remote chain
     */
    function transferCrossChainAsset(
        uint256 fromTokenId,
        uint256 toTokenId,
        uint256 chainId,
        uint256 gameId,
        uint256 amount,
        bytes memory signature
    ) external {
        require(ownerOf(fromTokenId) == msg.sender, "Not token owner");
        require(_playerData[fromTokenId].linkedGames[chainId], "Chain not linked");
        require(trustedRemoteContracts[chainId] != address(0), "Chain not trusted");
        
        // Verify the remote chain has approved this transfer
        bytes32 messageHash = keccak256(
            abi.encodePacked(fromTokenId, toTokenId, chainId, gameId, amount, address(this))
        );
        address signer = messageHash.toEthSignedMessageHash().recover(signature);
        require(signer == trustedRemoteContracts[chainId], "Invalid signature");
        
        // Update local state
        _playerData[fromTokenId].gameAssets[chainId][gameId] -= amount;
        
        emit AssetTransferred(fromTokenId, toTokenId, chainId, gameId, amount);
    }

    /**
     * @dev Adds a trusted remote contract for a chain
     * @param chainId The chain ID
     * @param contractAddress The address of the remote contract
     */
    function addTrustedRemote(uint256 chainId, address contractAddress) external onlyOwner {
        trustedRemoteContracts[chainId] = contractAddress;
    }

    /**
     * @dev Removes a trusted remote contract
     * @param chainId The chain ID to remove
     */
    function removeTrustedRemote(uint256 chainId) external onlyOwner {
        delete trustedRemoteContracts[chainId];
    }

    /**
     * @dev Gets player data
     * @param tokenId The player's token ID
     * @return gamerTag The player's gamer tag
     * @return reputationScore The player's reputation score
     */
    function getPlayerData(uint256 tokenId) external view returns (string memory gamerTag, uint256 reputationScore) {
        require(_exists(tokenId), "Token does not exist");
        PlayerData storage data = _playerData[tokenId];
        return (data.gamerTag, data.reputationScore);
    }

    /**
     * @dev Checks if a player is linked to a specific chain
     * @param tokenId The player's token ID
     * @param chainId The chain ID to check
     * @return True if linked, false otherwise
     */
    function isChainLinked(uint256 tokenId, uint256 chainId) external view returns (bool) {
        require(_exists(tokenId), "Token does not exist");
        return _playerData[tokenId].linkedGames[chainId];
    }

    /**
     * @dev Gets a player's asset count for a specific game on a chain
     * @param tokenId The player's token ID
     * @param chainId The chain ID
     * @param gameId The game ID
     * @return The asset count
     */
    function getGameAssets(
        uint256 tokenId,
        uint256 chainId,
        uint256 gameId
    ) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return _playerData[tokenId].gameAssets[chainId][gameId];
    }
}
```
