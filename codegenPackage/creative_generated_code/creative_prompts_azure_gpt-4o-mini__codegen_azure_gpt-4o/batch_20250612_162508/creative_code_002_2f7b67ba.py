"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immortals-nft.web.app
Prompt: What are the steps to mint NFTs for a project with a limited supply, such as the 3333 pixel nightmares in the Immortals collection?
Generated: DETERMINISTIC_2f7b67ba8b074c9b
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a well-documented production-ready implementation in Solidity (a smart contract language for Ethereum) for minting NFTs with a limited supply:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title ImmortalsCollection
 * @dev A contract for minting NFTs with a limited supply.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ImmortalsCollection is ERC721Enumerable, Ownable {
    // Maximum supply of the NFTs
    uint256 public constant MAX_SUPPLY = 3333;

    // Price per NFT
    uint256 public constant MINT_PRICE = 0.05 ether;

    // Base URI for metadata
    string private baseURI;

    // Events
    event NFTMinted(address indexed minter, uint256 indexed tokenId);

    /**
     * @dev Contract constructor, sets the name and symbol of the collection.
     * @param _baseURI Initial base URI for metadata.
     */
    constructor(string memory _baseURI) ERC721("ImmortalsCollection", "IMC") {
        baseURI = _baseURI;
    }

    /**
     * @dev Public mint function for users to mint NFTs.
     * Requires payment of `MINT_PRICE` and checks if supply limit is reached.
     */
    function mint(uint256 _amount) external payable {
        require(_amount > 0, "Must mint at least one NFT.");
        require(totalSupply() + _amount <= MAX_SUPPLY, "Minting would exceed max supply.");
        require(msg.value >= MINT_PRICE * _amount, "Insufficient ETH sent.");

        for (uint256 i = 0; i < _amount; i++) {
            uint256 tokenId = totalSupply() + 1;
            _safeMint(msg.sender, tokenId);
            emit NFTMinted(msg.sender, tokenId);
        }
    }

    /**
     * @dev Function for the owner to set the base URI for metadata.
     * @param _newBaseURI New base URI to be set.
     */
    function setBaseURI(string memory _newBaseURI) external onlyOwner {
        baseURI = _newBaseURI;
    }

    /**
     * @dev Override to return the base URI for metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }

    /**
     * @dev Withdraw function for the owner to withdraw collected ETH.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw.");
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Failed to withdraw funds.");
    }

    /**
     * @dev Fallback function to prevent accidental sending of ETH.
     */
    receive() external payable {
        revert("Use mint function to purchase NFTs.");
    }
}
```

**Dependencies**:
- This contract depends on OpenZeppelin libraries for `ERC721Enumerable` and `Ownable`. You need to install the OpenZeppelin contracts by running:
  ```bash
  npm install @openzeppelin/contracts
  ```
