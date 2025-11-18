"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clashofdragonz-mint.com
Prompt: Develop a smart contract that assigns unique powers and advantages to NFTs based on their family (e.g., Fire, Ice, Earth) for use in a Play-to-Earn game.
Generated: DETERMINISTIC_fbac68cc42f97a01
Batch ID: 20250612_151659
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/nft/": {
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

// Importing OpenZeppelin libraries for ERC721 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the NFT Family
interface INFTFamily {
    enum Family { Fire, Ice, Earth }
}

// Main contract definition
contract ElementalNFT is ERC721Enumerable, Ownable, INFTFamily {
    // Struct to define properties of each NFT
    struct NFTAttributes {
        Family family;
        uint256 powerLevel;
        string uniqueAbility;
    }

    // Mapping from token ID to its attributes
    mapping(uint256 => NFTAttributes) private _nftAttributes;

    // Event emitted when new NFT is created
    event NFTCreated(uint256 indexed tokenId, Family family, uint256 powerLevel, string uniqueAbility);

    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("ElementalNFT", "ENFT") {}

    // Function to mint a new NFT with specific attributes
    function mintNFT(Family family, uint256 powerLevel, string memory uniqueAbility) external onlyOwner {
        require(powerLevel > 0, "Power level must be greater than zero");
        require(bytes(uniqueAbility).length > 0, "Unique ability cannot be empty");

        _tokenIdCounter++;
        uint256 newTokenId = _tokenIdCounter;

        _mint(msg.sender, newTokenId);

        _nftAttributes[newTokenId] = NFTAttributes({
            family: family,
            powerLevel: powerLevel,
            uniqueAbility: uniqueAbility
        });

        emit NFTCreated(newTokenId, family, powerLevel, uniqueAbility);
    }

    // Function to get the attributes of a specific NFT
    function getNFTAttributes(uint256 tokenId) external view returns (NFTAttributes memory) {
        require(_exists(tokenId), "NFT does not exist");
        return _nftAttributes[tokenId];
    }

    // Function to get the total supply of minted NFTs
    function totalSupply() public view override returns (uint256) {
        return _tokenIdCounter;
    }

    // Override required by Solidity, to ensure correct token URI handling (if needed)
    function _baseURI() internal view virtual override returns (string memory) {
        return "https://api.example.com/nft/";
    }

    // Function to withdraw contract balance in case of emergency
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
