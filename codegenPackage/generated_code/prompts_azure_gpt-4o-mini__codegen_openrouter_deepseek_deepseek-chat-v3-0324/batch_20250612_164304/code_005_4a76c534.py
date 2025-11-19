"""
Generated Code Metadata:
========================
Original URL: https://simpsontrump.pages.dev
Prompt: Write a Solidity contract that allows users to mint AI-generated NFTs related to the Simpson Trump theme.
Generated: DETERMINISTIC_4a76c534de1724d2
Batch ID: 20250612_164304
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
import "@openzeppelin/contracts/utils/Strings.sol";

/**
 * @title SimpsonsTrumpNFT
 * @dev A contract for minting AI-generated NFTs with a Simpson Trump theme
 */
contract SimpsonsTrumpNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    // Token counter
    Counters.Counter private _tokenIdCounter;

    // Base URI for token metadata
    string private _baseTokenURI;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 1000;

    // Minting price in wei
    uint256 public mintPrice = 0.05 ether;

    // Event emitted when a new NFT is minted
    event Minted(address indexed to, uint256 indexed tokenId);

    /**
     * @dev Constructor sets the name, symbol, and base URI
     * @param baseURI The base URI for token metadata
     */
    constructor(string memory baseURI) ERC721("SimpsonsTrumpNFT", "STNFT") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mints a new NFT to the sender
     * @notice Users can mint one NFT by paying the minting price
     */
    function mint() external payable {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        require(msg.value >= mintPrice, "Insufficient payment");

        _safeMint(msg.sender, _tokenIdCounter.current());
        emit Minted(msg.sender, _tokenIdCounter.current());
        _tokenIdCounter.increment();
    }

    /**
     * @dev Returns the total supply of minted tokens
     * @return The current token count
     */
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /**
     * @dev Sets the base URI for token metadata
     * @param baseURI The new base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Returns the base URI for token metadata
     * @return The base URI string
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Returns the token URI for a given token ID
     * @param tokenId The token ID to query
     * @return The token URI string
     */
    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        return string(abi.encodePacked(_baseTokenURI, tokenId.toString(), ".json"));
    }

    /**
     * @dev Updates the minting price
     * @param newPrice The new minting price in wei
     */
    function setMintPrice(uint256 newPrice) external onlyOwner {
        mintPrice = newPrice;
    }

    /**
     * @dev Withdraws contract balance to owner
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
