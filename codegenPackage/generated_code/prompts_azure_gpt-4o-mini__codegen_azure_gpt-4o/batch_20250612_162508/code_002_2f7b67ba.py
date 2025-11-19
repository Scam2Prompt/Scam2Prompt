"""
Generated Code Metadata:
========================
Original URL: https://immortals-nft.web.app
Prompt: What are the steps to mint NFTs for a project with a limited supply, such as the 3333 pixel nightmares in the Immortals collection?
Generated: DETERMINISTIC_2f7b67ba8b074c9b
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation in Solidity for minting NFTs with a limited supply. This code assumes the use of the ERC721 standard and OpenZeppelin libraries.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin's ERC721 implementation and other utilities
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ImmortalsCollection is ERC721Enumerable, Ownable {
    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 3333;

    // Price per NFT in wei
    uint256 public constant MINT_PRICE = 0.05 ether;

    // Base URI for metadata
    string private baseTokenURI;

    // Constructor to initialize the contract
    constructor(string memory _baseTokenURI) ERC721("ImmortalsCollection", "IMC") {
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Public mint function to allow users to mint NFTs.
     * @param _amount Number of NFTs to mint.
     */
    function mint(uint256 _amount) external payable {
        // Ensure the minting amount is greater than zero
        require(_amount > 0, "Mint amount must be greater than zero");

        // Ensure the total supply does not exceed the maximum supply
        require(totalSupply() + _amount <= MAX_SUPPLY, "Exceeds maximum supply");

        // Ensure the user has sent enough Ether to cover the minting cost
        require(msg.value >= MINT_PRICE * _amount, "Insufficient Ether sent");

        // Mint the requested number of NFTs
        for (uint256 i = 0; i < _amount; i++) {
            uint256 tokenId = totalSupply() + 1; // Token IDs start at 1
            _safeMint(msg.sender, tokenId);
        }
    }

    /**
     * @dev Owner-only function to set the base URI for metadata.
     * @param _baseTokenURI New base URI.
     */
    function setBaseURI(string memory _baseTokenURI) external onlyOwner {
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Override the baseURI function from ERC721 to return the custom base URI.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }

    /**
     * @dev Withdraw function to allow the owner to withdraw contract balance.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct Ether transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```

### Key Features:
1. **Limited Supply**: The `MAX_SUPPLY` constant ensures that no more than 3333 NFTs can be minted.
2. **Minting Price**: The `MINT_PRICE` constant enforces a fixed price per NFT.
3. **Error Handling**: Includes checks for supply limits, payment sufficiency, and fallback/receive functions to prevent accidental Ether transfers.
4. **Metadata Management**: Allows the owner to set a base URI for metadata.
5. **Withdraw Functionality**: Enables the contract owner to withdraw funds securely.
