"""
Generated Code Metadata:
========================
Original URL: https://mong-life-mong.pages.dev
Prompt: Provide code to mint and manage $MONG-related NFTs, considering the 6.9% allocation for MONGS NFTs in its tokenomics.
Generated: DETERMINISTIC_9fb0e8450efb43c2
Batch ID: 20250612_153517
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract MONGNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    using SafeMath for uint256;
    
    Counters.Counter private _tokenIdCounter;
    
    // Constants
    uint256 public constant MAX_SUPPLY = 6900; // 6.9% of 100,000
    uint256 public constant MINT_PRICE = 0.069 ether;
    string public constant BASE_URI = "ipfs://Qm.../"; // Replace with actual IPFS URI
    
    // Events
    event Minted(address indexed to, uint256 tokenId);
    event Withdrawn(address indexed owner, uint256 amount);
    
    constructor() ERC721("MONGS NFT", "MONG") {}
    
    // Mint function with payment check
    function mint(address to) external payable {
        require(totalSupply() < MAX_SUPPLY, "All MONGS NFTs have been minted");
        require(msg.value >= MINT_PRICE, "Insufficient payment");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
        
        emit Minted(to, tokenId);
    }
    
    // Total supply helper
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }
    
    // Withdraw funds to owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
        
        emit Withdrawn(owner(), balance);
    }
    
    // Override base URI
    function _baseURI() internal pure override returns (string memory) {
        return BASE_URI;
    }
    
    // Batch mint for owner (for giveaways/airdrops)
    function batchMint(address[] calldata recipients) external onlyOwner {
        require(totalSupply() + recipients.length <= MAX_SUPPLY, "Exceeds max supply");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            uint256 tokenId = _tokenIdCounter.current();
            _tokenIdCounter.increment();
            _safeMint(recipients[i], tokenId);
            emit Minted(recipients[i], tokenId);
        }
    }
    
    // Prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
