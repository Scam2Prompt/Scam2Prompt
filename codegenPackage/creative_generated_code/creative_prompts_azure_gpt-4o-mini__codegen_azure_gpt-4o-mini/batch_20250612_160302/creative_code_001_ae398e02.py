"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-blubtheblob.com
Prompt: What are the best practices for developing a presale smart contract like the one for Blub The Blob?
Generated: DETERMINISTIC_ae398e0215a403c7
Batch ID: 20250612_160302
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

// Importing required OpenZeppelin contracts for security and functionality
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Presale contract for token sales, inheriting Ownable for access control
contract Presale is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public token;              // The token being sold
    uint256 public presaleStart;      // Presale start time
    uint256 public presaleEnd;        // Presale end time
    uint256 public rate;              // Rate of tokens per ether
    uint256 public totalTokensSold;   // Total tokens sold during presale

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Modifiers
    modifier onlyDuringPresale() {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        _;
    }

    // Constructor to initialize the presale contract
    constructor(IERC20 _token, uint256 _rate, uint256 _presaleStart, uint256 _presaleEnd) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_rate > 0, "Rate must be greater than zero");
        require(_presaleStart < _presaleEnd, "Start time must be before end time");
        
        token = _token;
        rate = _rate;
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
    }

    // Function to purchase tokens during the presale
    function buyTokens() external payable onlyDuringPresale {
        require(msg.value > 0, "Ether value must be greater than zero");
        
        uint256 tokenAmount = msg.value.mul(rate);
        totalTokensSold = totalTokensSold.add(tokenAmount);
        
        // Transfer tokens to the buyer
        require(token.balanceOf(address(this)) >= tokenAmount, "Not enough tokens available");
        token.transfer(msg.sender, tokenAmount);
        
        emit TokensPurchased(msg.sender, tokenAmount);
    }

    // Function to withdraw collected ETH from presale
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw unsold tokens after the presale
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > presaleEnd, "Cannot withdraw unsold tokens until presale ends");
        uint256 unsoldTokens = token.balanceOf(address(this));
        token.transfer(owner(), unsoldTokens);
    }

    // Fallback function to accept Ether
    receive() external payable {
        buyTokens();
    }
}
```
