"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://projectdeksa.pages.dev
Prompt: Write a Solidity function to celebrate the 280th anniversary of Karaton Surakarta by minting commemorative NFTs tied to $MASA token transactions.
Generated: DETERMINISTIC_22a214f9450208a2
Batch ID: 20250612_145625
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

// Import the OpenZeppelin ERC721 contract for NFT implementation
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the $MASA token
interface IMasaToken {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
}

contract KaratonSurakartaNFT is ERC721, Ownable {
    // Counter for the total number of NFTs minted
    uint256 private _tokenIdCounter;

    // Address of the $MASA token contract
    IMasaToken public masaToken;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed recipient, uint256 tokenId);

    // Constructor to initialize the NFT contract and $MASA token address
    constructor(address _masaTokenAddress) ERC721("Karaton Surakarta Commemorative NFT", "KSCNFT") {
        masaToken = IMasaToken(_masaTokenAddress);
    }

    /**
     * @dev Function to mint a NFT for a user who interacts with the $MASA token.
     * @param recipient The address that will receive the minted NFT.
     * @param amount The amount of $MASA tokens to be transferred for minting.
     */
    function mintNFT(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero.");
        require(amount > 0, "Amount must be greater than zero.");

        // Transfer the specified amount of $MASA tokens from the caller to the contract
        // Note: Assume the caller has previously approved the transfer of $MASA tokens
        bool success = masaToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed.");

        // Minting the NFT
        uint256 tokenId = _tokenIdCounter++;
        _mint(recipient, tokenId);

        // Emit NFT minted event
        emit NFTMinted(recipient, tokenId);
    }

    /**
     * @dev Function to withdraw $MASA tokens from the contract.
     * Only the contract owner can call this function.
     * @param amount The amount of $MASA tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero.");
        // Here you would implement withdrawal logic depending on the $MASA token contract
        // For the sake of this example, we are assuming the $MASA token follows ERC20 standards
        // Transfer the specified amount of $MASA tokens to the owner's address
        // (Assume an external withdraw function exists in the $MASA token)
    }
}
```
