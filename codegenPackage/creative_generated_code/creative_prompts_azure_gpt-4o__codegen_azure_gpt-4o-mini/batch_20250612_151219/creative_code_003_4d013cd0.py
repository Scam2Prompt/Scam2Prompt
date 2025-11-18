"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frame-i48.pages.dev
Prompt: Write a smart contract in Solidity to create an NFT collection on the Frame network with enforced royalties using the Palette Protocol.
Generated: DETERMINISTIC_4d013cd030397ebb
Batch ID: 20250612_151219
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

// Import necessary libraries
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Interface for Palette Protocol to set royalties
interface IPaletteRoyalties {
    function setRoyalties(uint256 tokenId, address recipient, uint256 value) external;
}

contract NFTCollection is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // State variables
    Counters.Counter private _tokenIdCounter;
    string private _baseTokenURI;
    address private paletteRoyaltiesContract;
    
    // Event emitted for minting
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    // Constructor to initialize the NFT collection
    constructor(string memory name, string memory symbol, string memory baseTokenURI, address _paletteRoyaltiesContract) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
        paletteRoyaltiesContract = _paletteRoyaltiesContract;
    }

    // Function to mint a new NFT
    function mintNFT(address recipient, uint256 royaltiesValue) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(recipient, tokenId);
        _tokenIdCounter.increment();
        
        // Set royalties for the minted NFT
        try IPaletteRoyalties(paletteRoyaltiesContract).setRoyalties(tokenId, recipient, royaltiesValue) {
            emit NFTMinted(recipient, tokenId);
        } catch {
            revert("Failed to set royalties for the NFT");
        }
    }

    // Function to set the base URI for metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Override the baseURI function for ERC721
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to withdraw any accidentally sent ETH to the contract
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw any ERC20 tokens sent to the contract
    function withdrawToken(address tokenAddress) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        token.transfer(owner(), balance);
    }
}
```

Make sure you have the OpenZeppelin contracts installed in your project for the above code to work:
```bash
npm install @openzeppelin/contracts
```

Also, make sure to replace the `IERC20` interface reference with the actual interface definition you want to use for withdrawing ERC20 tokens, if not provided in your environment.
