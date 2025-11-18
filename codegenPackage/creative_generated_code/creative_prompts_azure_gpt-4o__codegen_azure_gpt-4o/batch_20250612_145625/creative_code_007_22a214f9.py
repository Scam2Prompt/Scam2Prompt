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

/**
 * @title KaratonSurakartaCommemorativeNFT
 * @dev Contract to mint commemorative NFTs for the 280th anniversary of Karaton Surakarta
 * tied to $MASA token transactions.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract KaratonSurakartaCommemorativeNFT is ERC721, Ownable {
    IERC20 public masaToken; // Reference to the $MASA token contract
    uint256 public nextTokenId = 1; // Counter for the next NFT token ID
    uint256 public masaTransactionThreshold = 100 * 10**18; // Threshold amount of $MASA tokens (100 tokens here)
    mapping(address => bool) public hasMinted; // Tracks addresses that have already minted an NFT

    // Event to log the minting of a commemorative NFT
    event CommemorativeNFTMinted(address indexed recipient, uint256 tokenId);

    /**
     * @param _masaToken Address of the $MASA token contract
     */
    constructor(address _masaToken) ERC721("KaratonSurakartaNFT", "KSNFT") {
        require(_masaToken != address(0), "Invalid $MASA token address");
        masaToken = IERC20(_masaToken);
    }

    /**
     * @notice Mint a commemorative NFT for users based on $MASA token transactions
     */
    function mintCommemorativeNFT() external {
        // Ensure the caller has not minted an NFT before
        require(!hasMinted[msg.sender], "You have already minted a commemorative NFT!");

        // Ensure the caller has transferred a sufficient amount of $MASA tokens
        uint256 masaBalance = masaToken.balanceOf(msg.sender);
        require(masaBalance >= masaTransactionThreshold, "Insufficient $MASA token transactions to qualify!");

        // Mark the caller as having minted an NFT
        hasMinted[msg.sender] = true;

        // Mint the NFT
        uint256 tokenId = nextTokenId;
        nextTokenId++;
        _safeMint(msg.sender, tokenId);

        // Emit event to log the minting
        emit CommemorativeNFTMinted(msg.sender, tokenId);
    }

    /**
     * @notice Update the $MASA token transaction threshold (only owner can call this).
     * @param _newThreshold The new $MASA token transaction threshold (in wei).
     */
    function updateTransactionThreshold(uint256 _newThreshold) external onlyOwner {
        require(_newThreshold > 0, "Threshold must be greater than zero");
        masaTransactionThreshold = _newThreshold;
    }
}
```
