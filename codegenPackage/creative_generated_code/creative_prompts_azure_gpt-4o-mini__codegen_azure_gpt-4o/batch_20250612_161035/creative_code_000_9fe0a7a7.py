"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://studio-git-scott-dashboard-update-metaplex.vercel.app
Prompt: How can I use Truffle to mint a 10K NFT collection like the "Golden Pig" featured on their dashboard?
Generated: DETERMINISTIC_9fe0a7a71e298436
Batch ID: 20250612_161035
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

// Import ERC721 standard implementation from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GoldenPigNFT is ERC721Enumerable, Ownable {
    // Total supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Base URI for metadata
    string private baseTokenURI;

    // Counter to keep track of minted tokens
    uint256 private currentTokenId;

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory _baseTokenURI) ERC721("Golden Pig Collection", "GPC") {
        setBaseURI(_baseTokenURI);
    }

    /**
     * @dev Function to mint a single NFT to a specific address.
     * @param to Address to receive the minted NFT.
     */
    function mint(address to) external onlyOwner {
        require(currentTokenId < MAX_SUPPLY, "Maximum supply reached");

        // Increment the token counter and mint the NFT
        currentTokenId++;
        _safeMint(to, currentTokenId);
    }

    /**
     * @dev Batch mint NFTs to a specific address.
     * @param to Address to receive the minted NFTs.
     * @param quantity Number of NFTs to mint.
     */
    function mintBatch(address to, uint256 quantity) external onlyOwner {
        require(currentTokenId + quantity <= MAX_SUPPLY, "Exceeds maximum supply");

        // Mint the specified quantity of NFTs
        for (uint256 i = 0; i < quantity; i++) {
            currentTokenId++;
            _safeMint(to, currentTokenId);
        }
    }

    /**
     * @dev Set the base URI for metadata.
     * @param _baseTokenURI The base URI string.
     */
    function setBaseURI(string memory _baseTokenURI) public onlyOwner {
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Override the base URI function to return the base token URI.
     * @return baseTokenURI The base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }

    /**
     * @dev Function to withdraw contract balance (for example, if the NFTs are sold for Ether).
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        // Transfer the contract's balance to the owner
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to receive Ether directly (optional, if applicable).
     */
    receive() external payable {}

    /**
     * @dev Function to get the total number of NFTs minted.
     * @return currentTokenId The current count of minted NFTs.
     */
    function totalMinted() external view returns (uint256) {
        return currentTokenId;
    }
}
```

This is an ERC721 smart contract using OpenZeppelin libraries that supports minting up to 10,000 NFTs with the option to batch mint. It includes proper error handling, metadata configuration, and withdrawal functionality. Ensure to deploy this contract using Truffle or another Ethereum-compatible framework.
