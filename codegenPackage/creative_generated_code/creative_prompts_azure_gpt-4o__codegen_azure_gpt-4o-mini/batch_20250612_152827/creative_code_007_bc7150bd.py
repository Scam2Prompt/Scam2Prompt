"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ktest-296.pages.dev
Prompt: Suggest a method to audit a smart contract for a token presale to ensure compliance with the 5,000 ETH cap and the total supply limit of 100,000,000 KSI.
Generated: DETERMINISTIC_bc7150bda140c4ba
Batch ID: 20250612_152827
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

contract TokenPresale {
    // Variable to store the total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 100_000_000 * 10**18; // 100 million tokens with 18 decimals
    // Variable to track the cap for presale in ETH
    uint256 public constant ETH_CAP = 5_000 ether; // 5,000 ETH cap
    // Variable to track the total amount of ETH raised in the presale
    uint256 public totalRaised;
    
    // Event to log presale purchases
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 weiAmount);

    // Mapping to track purchased tokens by users
    mapping(address => uint256) public balances;

    // Function to purchase tokens during the presale
    function buyTokens() external payable {
        require(msg.value > 0, "Must send ETH to purchase tokens");
        require(totalRaised + msg.value <= ETH_CAP, "ETH cap exceeded");

        // Calculate the number of tokens to be allocated (assuming a 1:1 ratio for simplicity)
        uint256 tokensToAllocate = msg.value * TOKEN_PRICE; // Assume TOKEN_PRICE is defined

        // Check if the requested tokens exceed the total supply
        require(totalSupply() + tokensToAllocate <= TOTAL_SUPPLY, "Total supply limit exceeded");

        // Update state variables
        totalRaised += msg.value;
        balances[msg.sender] += tokensToAllocate;

        // Emit an event for the purchase
        emit TokensPurchased(msg.sender, tokensToAllocate, msg.value);
    }

    // Function to check the total supply of tokens issued
    function totalSupply() public view returns (uint256) {
        uint256 totalIssued = 0;
        // Iterate through all buyers to calculate total issued tokens
        for (uint256 i = 0; i < buyerAddresses.length; i++) {
            totalIssued += balances[buyerAddresses[i]];
        }
        return totalIssued;
    }

    // Function to withdraw raised ETH to a designated address
    function withdrawFunds(address payable beneficiary) external onlyOwner {
        require(beneficiary != address(0), "Invalid beneficiary address");
        require(address(this).balance > 0, "No funds to withdraw");

        // Transfer the balance to the beneficiary
        beneficiary.transfer(address(this).balance);
    }

    // Modifier to restrict access to certain functions
    modifier onlyOwner() {
        // Implement owner check logic
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }
    
    // Store the owner's address
    address private owner;

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }
}
```
