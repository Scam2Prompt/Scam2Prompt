"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ututu.pages.dev
Prompt: Write a Solidity function that prevents purchases exceeding the presale cap of 1000 ETH and ensures accurate token allocation based on the specified exchange rate.
Generated: DETERMINISTIC_1ea1034207bca137
Batch ID: 20250612_152924
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

contract Presale {
    // State variables
    uint256 public constant PRESALE_CAP = 1000 ether; // Maximum amount of ETH accepted in presale
    uint256 public totalETHContributed; // Tracks total ETH contributed so far
    uint256 public tokenExchangeRate; // Number of tokens allocated per 1 ETH
    address public owner;

    mapping(address => uint256) public contributions; // Tracks individual contributions
    mapping(address => uint256) public tokenAllocations; // Tracks allocated tokens per contributor

    // Events
    event Purchase(address indexed purchaser, uint256 ethAmount, uint256 tokenAmount);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize the token exchange rate and set the contract owner
    constructor(uint256 _tokenExchangeRate) {
        require(_tokenExchangeRate > 0, "Exchange rate must be greater than zero");
        tokenExchangeRate = _tokenExchangeRate;
        owner = msg.sender;
    }

    // Function to purchase tokens during the presale
    function purchaseTokens() external payable {
        require(msg.value > 0, "ETH amount must be greater than zero");
        require(totalETHContributed + msg.value <= PRESALE_CAP, "Presale cap exceeded");

        // Calculate the number of tokens to allocate
        uint256 tokensToAllocate = msg.value * tokenExchangeRate;

        // Update state variables
        totalETHContributed += msg.value;
        contributions[msg.sender] += msg.value;
        tokenAllocations[msg.sender] += tokensToAllocate;

        // Emit purchase event
        emit Purchase(msg.sender, msg.value, tokensToAllocate);
    }

    // Function to withdraw ETH balance (only accessible by the owner)
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH balance to withdraw");
        payable(owner).transfer(balance);
    }

    // Function to update the token exchange rate (only accessible by the owner)
    function updateExchangeRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Exchange rate must be greater than zero");
        tokenExchangeRate = _newRate;
    }

    // Function to check presale status
    function isPresaleActive() external view returns (bool) {
        return totalETHContributed < PRESALE_CAP;
    }

    // Fallback function to prevent accidental ETH transfers
    fallback() external payable {
        revert("Direct ETH transfers are not allowed");
    }

    // Receive function to handle ETH transfers explicitly (e.g., via .transfer())
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```
