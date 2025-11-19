"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owy-wtf.web.app
Prompt: How can I implement a presale mechanism for a memecoin on Ethereum, as described on the Owy website?
Generated: DETERMINISTIC_27987bba69c57572
Batch ID: 20250612_155242
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

// Import the OpenZeppelin ERC20 contract and Ownable for ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Presale contract for a memecoin
contract MemecoinPresale is Ownable {
    // ERC20 token contract
    ERC20 public token;
    
    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public tokenPrice; // Price per token in wei
    uint256 public hardCap; // Maximum amount to be raised
    uint256 public totalRaised; // Total amount raised in the presale

    // Mapping to track contributions of each address
    mapping(address => uint256) public contributions;

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleFinalized();

    // Constructor to initialize the presale contract
    constructor(
        ERC20 _token,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime,
        uint256 _tokenPrice,
        uint256 _hardCap
    ) {
        require(_presaleStartTime < _presaleEndTime, "Invalid presale duration");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_hardCap > 0, "Hard cap must be greater than zero");

        token = _token;
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
        tokenPrice = _tokenPrice;
        hardCap = _hardCap;
    }

    // Modifier to check if presale is active
    modifier isPresaleActive() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        _;
    }

    // Function to purchase tokens during presale
    function buyTokens() external payable isPresaleActive {
        require(msg.value > 0, "Must send ether to purchase tokens");
        require(totalRaised + msg.value <= hardCap, "Hard cap exceeded");

        uint256 tokensToPurchase = (msg.value * 1 ether) / tokenPrice;
        contributions[msg.sender] += msg.value;
        totalRaised += msg.value;

        // Transfer tokens to buyer
        require(token.balanceOf(address(this)) >= tokensToPurchase, "Insufficient tokens in contract");
        token.transfer(msg.sender, tokensToPurchase);

        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    // Function to finalize the presale and withdraw raised funds
    function finalizePresale() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale is still ongoing");
        require(totalRaised > 0, "No funds raised");

        // Transfer raised funds to owner
        payable(owner()).transfer(address(this).balance);
        
        emit PresaleFinalized();
    }

    // Function to withdraw unsold tokens
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale is still ongoing");

        uint256 unsoldTokens = token.balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        token.transfer(owner(), unsoldTokens);
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed, use buyTokens function");
    }
}
```
