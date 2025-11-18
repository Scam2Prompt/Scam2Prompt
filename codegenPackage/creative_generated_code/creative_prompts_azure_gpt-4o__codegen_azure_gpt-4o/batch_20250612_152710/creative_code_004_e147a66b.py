"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qhozali.pages.dev
Prompt: Create a smart contract for minting NFTs that align with the Ghozali 404 hybrid concept on the Base blockchain.
Generated: DETERMINISTIC_e147a66bad056681
Batch ID: 20250612_152710
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
 * @title Ghozali404NFT
 * @dev A smart contract for minting NFTs inspired by the Ghozali 404 hybrid concept on the Base blockchain.
 */
contract Ghozali404NFT {
    // Importing OpenZeppelin's ERC721 implementation
    import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
    import "@openzeppelin/contracts/access/Ownable.sol";
    import "@openzeppelin/contracts/utils/Counters.sol";

    /**
     * @dev Extends OpenZeppelin's ERC721 implementation with Ownable and Counters.
     */
    contract Ghozali404NFT is ERC721, Ownable {
        using Counters for Counters.Counter;

        // Counter to keep track of token IDs
        Counters.Counter private _tokenIds;

        // Base URI for metadata
        string private _baseTokenURI;

        // Maximum supply of NFTs
        uint256 public constant MAX_SUPPLY = 404;

        // Event emitted when a new NFT is minted
        event NFTMinted(address indexed recipient, uint256 tokenId);

        /**
         * @dev Constructor to initialize the contract with a name and symbol for the NFT collection.
         */
        constructor(string memory baseURI) ERC721("Ghozali404NFT", "GHZ404") {
            _baseTokenURI = baseURI;
        }

        /**
         * @dev Internal function to set the base URI for the NFT metadata.
         */
        function _baseURI() internal view virtual override returns (string memory) {
            return _baseTokenURI;
        }

        /**
         * @dev Mint a new NFT. Only the owner can mint NFTs. Ensures the maximum supply is not exceeded.
         * @param recipient The address to receive the minted NFT.
         */
        function mintNFT(address recipient) public onlyOwner {
            // Ensure that the maximum supply is not exceeded
            require(_tokenIds.current() < MAX_SUPPLY, "Maximum supply reached");

            // Increment the token ID counter
            _tokenIds.increment();

            // Get the new token ID
            uint256 newTokenId = _tokenIds.current();

            // Mint the NFT to the recipient
            _safeMint(recipient, newTokenId);

            // Emit the minting event
            emit NFTMinted(recipient, newTokenId);
        }

        /**
         * @dev Set the base URI for metadata. Only the owner can set this value.
         * @param baseURI The new base URI for NFT metadata.
         */
        function setBaseURI(string memory baseURI) public onlyOwner {
            _baseTokenURI = baseURI;
        }

        /**
         * @dev Get the current number of minted NFTs.
         * @return The number of NFTs minted so far.
         */
        function totalMinted() public view returns (uint256) {
            return _tokenIds.current();
        }
    }
}
```
