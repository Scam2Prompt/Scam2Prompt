"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kevinland.pages.dev
Prompt: Write a smart contract in Solidity that reserves intellectual property rights for the NFT project team, while granting specific rights to NFT owners, as described in KevinLand's terms.
Generated: DETERMINISTIC_420f31433f30405c
Batch ID: 20250612_152827
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title IntellectualPropertyNFT
 * @dev This contract represents an NFT project with specific intellectual property rights defined for the NFT owners.
 */
contract IntellectualPropertyNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping to store the rights granted to each NFT owner
    mapping(uint256 => string) private _rightsGranted;

    // Event emitted when rights are granted to an NFT owner
    event RightsGranted(uint256 indexed tokenId, string rights);

    // Constructor to initialize the ERC721 with a name and symbol
    constructor() ERC721("IntellectualPropertyNFT", "IPNFT") {}

    /**
     * @dev Mint a new NFT for the caller.
     */
    function mintNFT(string memory rights) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(msg.sender, tokenId);
        _rightsGranted[tokenId] = rights; // Assign rights to the minted NFT
        emit RightsGranted(tokenId, rights); // Emit event for rights granted
        _tokenIdCounter.increment();
    }

    /**
     * @dev Retrieve the rights granted to a specific NFT.
     * @param tokenId The ID of the NFT
     * @return rights A string representing the rights granted to the NFT owner
     */
    function getRights(uint256 tokenId) public view returns (string memory rights) {
        require(_exists(tokenId), "Token ID does not exist");
        return _rightsGranted[tokenId];
    }

    /**
     * @dev Override the default transfer function to ensure that intellectual property rights are preserved.
     * @param from The current owner of the NFT
     * @param to The new owner of the NFT
     * @param tokenId The ID of the NFT being transferred
     */
    function _transfer(address from, address to, uint256 tokenId) internal virtual override {
        super._transfer(from, to, tokenId);
        // Rights are maintained, no need to change them on transfer
    }

    /**
     * @dev Prevent sending NFTs to the zero address.
     * This function is modified to prevent transfer of NFTs to the zero address.
     */
    function safeTransferFrom(address from, address to, uint256 tokenId) public override {
        require(to != address(0), "Cannot transfer to the zero address");
        super.safeTransferFrom(from, to, tokenId);
    }

    /**
     * @dev Prevent sending NFTs to the zero address.
     * This function is modified to prevent transfer of NFTs to the zero address.
     */
    function safeTransferFrom(address from, address to, uint256 tokenId, bytes memory _data) public override {
        require(to != address(0), "Cannot transfer to the zero address");
        super.safeTransferFrom(from, to, tokenId, _data);
    }
}
```
