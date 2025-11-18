"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hummingbirdonbnb.pages.dev
Prompt: Create a smart contract in Solidity for an NFT launchpad similar to Mint Magic, allowing users to mint NFTs and integrate utilities for businesses and celebrities.
Generated: DETERMINISTIC_b3b87eda26e50de2
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title NFTLaunchpad
 * @dev A smart contract for minting NFTs and integrating utilities for businesses and celebrities.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTLaunchpad is ERC721URIStorage, Ownable {
    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed minter, uint256 indexed tokenId, string tokenURI);

    // Event emitted when utilities are updated for an NFT
    event UtilitiesUpdated(uint256 indexed tokenId, string utilities);

    // Counter to track token IDs
    uint256 private _tokenIdCounter;

    // Mapping to store utilities for each NFT
    mapping(uint256 => string) public nftUtilities;

    // Minting fee (in wei)
    uint256 public mintingFee;

    /**
     * @dev Constructor initializes the contract with a name and symbol for the NFT collection.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol, uint256 _mintingFee) ERC721(name, symbol) {
        mintingFee = _mintingFee;
    }

    /**
     * @dev Allows users to mint a new NFT with a specific token URI.
     *      Requires the payment of a minting fee.
     * @param tokenURI The metadata URI of the NFT.
     */
    function mintNFT(string memory tokenURI) external payable {
        require(msg.value == mintingFee, "Incorrect minting fee.");

        // Increment token counter
        _tokenIdCounter++;
        uint256 tokenId = _tokenIdCounter;

        // Mint the NFT to the caller
        _safeMint(msg.sender, tokenId);

        // Set the token URI for the minted NFT
        _setTokenURI(tokenId, tokenURI);

        // Emit event for minting
        emit NFTMinted(msg.sender, tokenId, tokenURI);
    }

    /**
     * @dev Updates utilities for a specific NFT.
     *      Only the owner of the NFT can update its utilities.
     * @param tokenId The ID of the NFT.
     * @param utilities The utility data (e.g., special access, privileges, etc.).
     */
    function updateUtilities(uint256 tokenId, string memory utilities) external {
        require(ownerOf(tokenId) == msg.sender, "Caller is not the owner of the NFT.");

        // Update utilities in the mapping
        nftUtilities[tokenId] = utilities;

        // Emit event for utilities update
        emit UtilitiesUpdated(tokenId, utilities);
    }

    /**
     * @dev Allows the owner to update the minting fee.
     * @param newFee The new minting fee (in wei).
     */
    function setMintingFee(uint256 newFee) external onlyOwner {
        mintingFee = newFee;
    }

    /**
     * @dev Allows the owner of the contract to withdraw collected fees.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal.");

        // Transfer the balance to the owner
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed.");
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers to the contract.
     */
    receive() external payable {
        revert("Direct deposits not allowed.");
    }

    fallback() external payable {
        revert("Invalid call.");
    }
}
```
