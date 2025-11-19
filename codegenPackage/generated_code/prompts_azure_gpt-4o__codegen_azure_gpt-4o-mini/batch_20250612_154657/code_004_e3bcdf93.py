"""
Generated Code Metadata:
========================
Original URL: https://on1force.web.app
Prompt: Create a smart contract that enforces the rules for transferring 0N1 FRAMES NFTs, ensuring that ownership of the original 0N1 Force NFT automatically transfers the respective Frame.
Generated: DETERMINISTIC_e3bcdf93bae944d3
Batch ID: 20250612_154657
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

// Importing the ERC721 interface for NFT functionality
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for managing 0N1 FRAMES NFTs
contract ON1Frames is ERC721Enumerable, Ownable {
    // Mapping from original 0N1 Force NFT ID to the corresponding Frame NFT ID
    mapping(uint256 => uint256) private originalToFrame;
    // Mapping to track if a Frame NFT has been minted
    mapping(uint256 => bool) private frameMinted;

    // Event emitted when a Frame NFT is transferred
    event FrameTransferred(address indexed from, address indexed to, uint256 indexed frameId);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("0N1 Frames", "FRAME") {}

    // Function to mint a Frame NFT for the owner of the original 0N1 Force NFT
    function mintFrame(uint256 originalId) external {
        // Ensure the original NFT exists and is owned by the caller
        require(IERC721(originalNFTAddress).ownerOf(originalId) == msg.sender, "You do not own the original NFT");
        require(!frameMinted[originalId], "Frame already minted for this original NFT");

        // Mint the Frame NFT
        uint256 frameId = totalSupply() + 1; // Generate a new Frame ID
        _mint(msg.sender, frameId);
        originalToFrame[originalId] = frameId; // Link original NFT to Frame NFT
        frameMinted[originalId] = true; // Mark Frame as minted

        emit FrameTransferred(address(0), msg.sender, frameId); // Emit transfer event
    }

    // Function to transfer a Frame NFT
    function transferFrame(address to, uint256 frameId) external {
        // Ensure the caller is the owner of the Frame NFT
        require(ownerOf(frameId) == msg.sender, "You do not own this Frame NFT");
        // Transfer the Frame NFT
        _transfer(msg.sender, to, frameId);
        emit FrameTransferred(msg.sender, to, frameId); // Emit transfer event
    }

    // Function to get the Frame NFT ID associated with an original NFT ID
    function getFrameId(uint256 originalId) external view returns (uint256) {
        return originalToFrame[originalId];
    }

    // Function to check if a Frame NFT has been minted for an original NFT
    function isFrameMinted(uint256 originalId) external view returns (bool) {
        return frameMinted[originalId];
    }
}
```
