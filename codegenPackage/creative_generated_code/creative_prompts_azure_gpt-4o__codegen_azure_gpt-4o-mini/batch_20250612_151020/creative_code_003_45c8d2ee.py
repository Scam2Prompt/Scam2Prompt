"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbirds.pro
Prompt: Develop a blockchain-based smart contract that symbolizes Moonbird B95's resilience through "winter dumps and summer pumps," incorporating unique identifiers like "code B95."
Generated: DETERMINISTIC_45c8d2ee31166208
Batch ID: 20250612_151020
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.moonbird.com/metadata/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import the required OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Moonbird B95 Smart Contract
contract MoonbirdB95 is ERC721, Ownable {
    // Unique identifier for Moonbird B95
    string public constant CODE = "B95";

    // State variable to track the total supply of Moonbird tokens
    uint256 public totalSupply;

    // Mapping from token ID to its corresponding attributes (for winter dumps and summer pumps)
    mapping(uint256 => string) private _attributes;

    // Event emitted when a new Moonbird is minted
    event MoonbirdMinted(uint256 indexed tokenId, string attributes);

    // Constructor to initialize the contract
    constructor() ERC721("MoonbirdB95", "MB95") {}

    // Function to mint a new Moonbird token
    // Only the contract owner can mint new tokens
    function mintMoonbird(address to, string memory attributes) external onlyOwner {
        require(to != address(0), "Cannot mint to zero address"); // Ensure valid address
        require(bytes(attributes).length > 0, "Attributes cannot be empty"); // Ensure attributes are provided

        totalSupply++; // Increment total supply
        _safeMint(to, totalSupply); // Mint the token safely
        _attributes[totalSupply] = attributes; // Store the attributes for the token

        emit MoonbirdMinted(totalSupply, attributes); // Emit the minting event
    }

    // Function to get the attributes of a specific Moonbird token by its ID
    function getAttributes(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Token does not exist"); // Check if the token exists
        return _attributes[tokenId]; // Return the attributes of the token
    }

    // Override the _baseURI function to provide a base URI for the metadata
    function _baseURI() internal view virtual override returns (string memory) {
        return "https://api.moonbird.com/metadata/"; // Base URI for Moonbird metadata
    }

    // Function to withdraw contract balance to the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance; // Get contract balance
        require(balance > 0, "No funds to withdraw"); // Ensure there are funds to withdraw

        payable(owner()).transfer(balance); // Transfer balance to the owner
    }

    // Fallback function to accept ETH deposits
    receive() external payable {}
}
```
