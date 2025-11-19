"""
Generated Code Metadata:
========================
Original URL: https://degeneratebugs.firebaseapp.com
Prompt: Create a function in Solidity to handle the reveal of Degen Fat Cats NFTs once a certain condition is met.
Generated: DETERMINISTIC_f2f92e85a71590d6
Batch ID: 20250622_210316
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
import "@openzeppelin/contracts/utils/Strings.sol";

contract DegenFatCats is ERC721, Ownable {
    using Strings for uint256;

    // State variables
    bool public isRevealed = false;
    string public baseURI;
    string public notRevealedURI;
    uint256 public revealThreshold;
    uint256 public totalSupply;

    // Events
    event Revealed(string newBaseURI);
    event MetadataUpdate(uint256 _tokenId);

    // Modifier to check if reveal condition is met
    modifier whenRevealThresholdReached() {
        require(totalSupply >= revealThreshold, "Reveal threshold not reached");
        _;
    }

    /**
     * @dev Constructor
     * @param _name Token name
     * @param _symbol Token symbol
     * @param _notRevealedURI URI for not revealed metadata
     * @param _revealThreshold Number of tokens needed to be minted before reveal
     */
    constructor(
        string memory _name,
        string memory _symbol,
        string memory _notRevealedURI,
        uint256 _revealThreshold
    ) ERC721(_name, _symbol) {
        notRevealedURI = _notRevealedURI;
        revealThreshold = _revealThreshold;
    }

    /**
     * @dev Reveal the NFTs by setting the base URI
     * @param _newBaseURI The new base URI for revealed metadata
     */
    function reveal(string memory _newBaseURI) external onlyOwner whenRevealThresholdReached {
        require(!isRevealed, "Already revealed");
        baseURI = _newBaseURI;
        isRevealed = true;
        emit Revealed(_newBaseURI);
    }

    /**
     * @dev Override tokenURI to return different URI before and after reveal
     * @param tokenId The token ID to query
     */
    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");

        if (!isRevealed) {
            return notRevealedURI;
        }

        return string(abi.encodePacked(baseURI, tokenId.toString(), ".json"));
    }

    /**
     * @dev Mint a new token (only owner for this example)
     * @param to The address to mint to
     */
    function safeMint(address to) external onlyOwner {
        uint256 tokenId = totalSupply + 1;
        _safeMint(to, tokenId);
        totalSupply++;
    }

    /**
     * @dev Update the reveal threshold (only owner)
     * @param _newThreshold The new reveal threshold
     */
    function setRevealThreshold(uint256 _newThreshold) external onlyOwner {
        require(!isRevealed, "Already revealed");
        revealThreshold = _newThreshold;
    }

    /**
     * @dev Update the not revealed URI (only owner)
     * @param _newNotRevealedURI The new not revealed URI
     */
    function setNotRevealedURI(string memory _newNotRevealedURI) external onlyOwner {
        require(!isRevealed, "Already revealed");
        notRevealedURI = _newNotRevealedURI;
    }
}
```
