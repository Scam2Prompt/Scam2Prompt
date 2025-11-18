"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobothebear.pages.dev
Prompt: Create a smart contract in Solidity for minting NFTs in the style of the Bobo Council NFT collection, ensuring the total supply is capped at 2,222 as specified on the website.
Generated: DETERMINISTIC_58fe05e6236b842a
Batch ID: 20250612_151158
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
 * @title BoboCouncilNFT
 * @dev A smart contract for minting NFTs in the style of the Bobo Council collection.
 *      Total supply is capped at 2,222 NFTs.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BoboCouncilNFT is ERC721Enumerable, Ownable {
    // Maximum number of NFTs that can be minted
    uint256 public constant MAX_SUPPLY = 2222;

    // Token ID tracker
    uint256 private _currentTokenId;

    // Base URI for metadata
    string private _baseTokenURI;

    // Events
    event Minted(address indexed recipient, uint256 indexed tokenId);

    /**
     * @dev Initializes the contract with the name and symbol of the collection.
     * @param baseURI The base URI for the metadata.
     */
    constructor(string memory baseURI) ERC721("Bobo Council NFT", "BOBO") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Updates the base URI for metadata.
     *      Callable only by the owner of the contract.
     * @param baseURI The new base URI.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Returns the base URI for the metadata.
     * @return The base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Mints a new NFT to a recipient.
     *      Cannot exceed the total supply cap of 2,222.
     * @param recipient The address to receive the minted NFT.
     */
    function mint(address recipient) external onlyOwner {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        require(recipient != address(0), "Invalid recipient address");

        // Increment token ID
        _currentTokenId++;

        // Mint the NFT
        _safeMint(recipient, _currentTokenId);

        // Emit the minting event
        emit Minted(recipient, _currentTokenId);
    }

    /**
     * @dev Withdraw all funds from the contract.
     *      Callable only by the owner of the contract.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer funds to the owner's address
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdraw failed");
    }

    /**
     * @dev Fallback function to accept ETH.
     */
    receive() external payable {}

    // Prevent accidental ETH transfers to the contract with no data
    fallback() external payable {}
}
```
