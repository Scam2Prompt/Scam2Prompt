"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://news.trustlootbox.com
Prompt: Develop a smart contract that ensures each wallet can mint only one NFT during the Trust Wallet Mystery Box free-mint event, adhering to the event's rules.
Generated: DETERMINISTIC_25c24a71614bc608
Batch ID: 20250612_145521
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

// Import the ERC721 standard interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TrustWalletMysteryBox is ERC721Enumerable, Ownable {
    // Event to log successful NFT mints
    event MysteryBoxMinted(address indexed minter, uint256 tokenId);

    // Mapping to track if a wallet has already minted an NFT
    mapping(address => bool) private hasMinted;

    // Maximum number of Mystery Boxes
    uint256 public constant MAX_SUPPLY = 10000;

    // Base URI for metadata
    string private baseURI;

    constructor() ERC721("TrustWalletMysteryBox", "TWMB") {}

    /**
     * @notice Allows a wallet to mint a single NFT during the free-mint event.
     * Requirements:
     * - Caller must not have minted before.
     * - Total supply must not exceed MAX_SUPPLY.
     */
    function mintMysteryBox() external {
        require(!hasMinted[msg.sender], "You have already minted your Mystery Box.");
        require(totalSupply() < MAX_SUPPLY, "All Mystery Boxes have been minted.");

        // Mark the wallet as having minted
        hasMinted[msg.sender] = true;

        // Generate a new token ID based on current total supply
        uint256 tokenId = totalSupply() + 1;

        // Mint the NFT to the caller
        _safeMint(msg.sender, tokenId);

        // Emit event for successful mint
        emit MysteryBoxMinted(msg.sender, tokenId);
    }

    /**
     * @notice Sets the base URI for metadata.
     * Can only be called by the contract owner.
     */
    function setBaseURI(string calldata uri) external onlyOwner {
        baseURI = uri;
    }

    /**
     * @notice Overrides the _baseURI function from ERC721.
     * Returns the base URI for token metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }

    /**
     * @notice Withdraws contract balance to the owner's wallet.
     * Can only be called by the contract owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available to withdraw.");
        payable(owner()).transfer(balance);
    }

    // Fallback and receive functions to handle accidental ETH transfers
    fallback() external payable {}
    receive() external payable {}
}
```
