"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koi-finance.pages.dev
Prompt: How do I create a vote-escrow NFT for participating in Koi Finance's DAO governance?
Generated: DETERMINISTIC_75c4952a6244329b
Batch ID: 20250612_163732
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
 * @title VoteEscrowNFT
 * @dev An ERC721-based contract to create vote-escrow NFTs for DAO governance participation.
 *      Users can lock their voting power in the form of NFTs for Koi Finance's DAO governance.
 */

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract VoteEscrowNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter to generate unique token IDs
    Counters.Counter private _tokenIdCounter;

    struct EscrowDetails {
        uint256 amountLocked; // Amount of tokens locked for governance
        uint256 lockDuration; // How long the tokens are locked (in seconds)
        uint256 unlockTimestamp; // When the tokens can be unlocked
    }

    // Mapping of token ID to escrow details
    mapping(uint256 => EscrowDetails) public escrowDetails;

    // Event emitted when a new NFT is minted
    event NFTMinted(
        address indexed owner,
        uint256 indexed tokenId,
        uint256 amountLocked,
        uint256 lockDuration
    );

    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed owner, uint256 indexed tokenId);

    /**
     * @dev Constructor to set the name and symbol of the NFT collection.
     */
    constructor() ERC721("VoteEscrowNFT", "VE-NFT") {}

    /**
     * @dev Function to mint a new vote-escrow NFT. Tokens are locked for governance participation.
     * @param amountLocked The amount of tokens being locked.
     * @param lockDuration The duration for which the tokens are locked (in seconds).
     */
    function mintEscrowNFT(uint256 amountLocked, uint256 lockDuration) external {
        require(amountLocked > 0, "Amount locked must be greater than zero");
        require(lockDuration > 0, "Lock duration must be greater than zero");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Record the escrow details in the mapping
        escrowDetails[tokenId] = EscrowDetails({
            amountLocked: amountLocked,
            lockDuration: lockDuration,
            unlockTimestamp: block.timestamp + lockDuration
        });

        // Mint the NFT to the sender
        _safeMint(msg.sender, tokenId);

        emit NFTMinted(msg.sender, tokenId, amountLocked, lockDuration);
    }

    /**
     * @dev Function to unlock tokens associated with a given NFT once the lock duration has passed.
     * @param tokenId The ID of the NFT whose tokens are being unlocked.
     */
    function unlockTokens(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "Caller is not the owner of the NFT");
        require(block.timestamp >= escrowDetails[tokenId].unlockTimestamp, "Tokens are still locked");

        // Clear escrow data
        delete escrowDetails[tokenId];

        emit TokensUnlocked(msg.sender, tokenId);
    }

    /**
     * @dev Function to view the details of an escrowed NFT.
     * @param tokenId The ID of the NFT.
     * @return amountLocked The amount of tokens locked.
     * @return lockDuration The duration for which tokens are locked.
     * @return unlockTimestamp The timestamp when tokens can be unlocked.
     */
    function getEscrowDetails(uint256 tokenId)
        external
        view
        returns (
            uint256 amountLocked,
            uint256 lockDuration,
            uint256 unlockTimestamp
        )
    {
        require(_exists(tokenId), "Token does not exist");
        EscrowDetails memory details = escrowDetails[tokenId];
        return (details.amountLocked, details.lockDuration, details.unlockTimestamp);
    }

    /**
     * @dev Override function to ensure token transfers are disabled.
     * @notice Vote-escrow NFTs are non-transferable.
     */
    function _transfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        require(false, "Vote-escrow NFTs are non-transferable");
    }
}
```
