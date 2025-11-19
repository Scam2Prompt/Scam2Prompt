"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurnft-blur.github.io
Prompt: Generate a smart contract for a Blur NFT that includes automatic royalty payments to the original artist upon resale.
Generated: DETERMINISTIC_1f16e48a953d894e
Batch ID: 20250612_161317
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

// Importing OpenZeppelin's ERC721 and Ownable contracts
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// The NFT contract for Blur
contract BlurNFT is ERC721Enumerable, Ownable {
    using SafeMath for uint256;

    // Mapping from token ID to the original artist's address
    mapping(uint256 => address) private _originalArtists;

    // Royalty percentage (in basis points, where 10000 basis points = 100%)
    uint256 public royaltyPercentage;

    // Event to log the royalty payment
    event RoyaltyPaid(address indexed artist, uint256 amount);

    // Constructor to initialize the contract with a name and symbol, and royalty percentage
    constructor(string memory name, string memory symbol, uint256 _royaltyPercentage) 
        ERC721(name, symbol) 
    {
        require(_royaltyPercentage <= 10000, "Royalty percentage must be <= 100%");
        royaltyPercentage = _royaltyPercentage;
    }

    // Function to mint new NFT
    function mintNFT(address to, string memory tokenURI) external onlyOwner {
        uint256 tokenId = totalSupply().add(1);
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
        _originalArtists[tokenId] = to; // Set the original artist
    }

    // Function to handle royalty payments on resale
    function _transfer(address from, address to, uint256 tokenId) internal override {
        super._transfer(from, to, tokenId);
        
        // Calculate royalty amount
        uint256 salePrice = msg.value; // Assuming msg.value represents the sale price in this context
        uint256 royaltyAmount = salePrice.mul(royaltyPercentage).div(10000);

        // Pay the original artist
        address originalArtist = _originalArtists[tokenId];
        if (originalArtist != address(0) && royaltyAmount > 0) {
            (bool success, ) = originalArtist.call{value: royaltyAmount}("");
            require(success, "Royalty payment failed"); // Ensure payment was successful
            emit RoyaltyPaid(originalArtist, royaltyAmount); // Emit event
        }
    }

    // Function to receive Ether. Required for royalty payments
    receive() external payable {}

    // Function to withdraw contract balance to owner's address
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdraw failed"); // Ensure withdrawal was successful
    }
}
```
