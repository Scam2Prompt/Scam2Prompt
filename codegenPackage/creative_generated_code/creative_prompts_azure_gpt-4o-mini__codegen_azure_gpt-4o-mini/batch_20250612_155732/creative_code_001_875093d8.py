"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xai320k.com
Prompt: Provide an example of how to implement a presale smart contract for the xAI320K token using Solidity.
Generated: DETERMINISTIC_875093d8bd032b60
Batch ID: 20250612_155732
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

// Importing the OpenZeppelin ERC20 token contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Presale contract for the xAI320K token
contract Presale is Ownable {
    // The ERC20 token being sold
    ERC20Burnable public token;

    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public tokenPrice; // price in wei
    uint256 public tokensSold;

    // Mapping to track how much each address has contributed
    mapping(address => uint256) public contributions;

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensWithdrawn(address indexed owner, uint256 amount);

    // Constructor to initialize the presale
    constructor(
        address _tokenAddress,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime,
        uint256 _tokenPrice
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_presaleStartTime < _presaleEndTime, "Start time must be before end time");
        require(_tokenPrice > 0, "Token price must be greater than 0");
        
        token = ERC20Burnable(_tokenAddress);
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
        tokenPrice = _tokenPrice;
    }

    // Modifier to check if the presale is active
    modifier duringPresale() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        _;
    }

    // Function to buy tokens during the presale
    function buyTokens(uint256 _amount) external payable duringPresale {
        require(msg.value == _amount * tokenPrice, "Incorrect ETH amount sent");
        require(token.balanceOf(address(this)) >= _amount, "Not enough tokens available");

        contributions[msg.sender] += _amount;
        tokensSold += _amount;

        // Transfer tokens to buyer
        token.transfer(msg.sender, _amount);
        emit TokensPurchased(msg.sender, _amount);
    }

    // Function to withdraw ETH from the presale
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner's address
        payable(owner()).transfer(balance);
    }

    // Function to end the presale early (if needed)
    function endPresale() external onlyOwner {
        presaleEndTime = block.timestamp;
    }

    // Function to check the presale status
    function isPresaleActive() external view returns (bool) {
        return block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime;
    }
}
```
