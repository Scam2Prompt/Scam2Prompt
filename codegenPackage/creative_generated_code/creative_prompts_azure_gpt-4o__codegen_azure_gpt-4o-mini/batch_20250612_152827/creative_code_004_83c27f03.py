"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ktest-296.pages.dev
Prompt: Provide an example of a Solidity contract that enforces a presale cap of 5,000 ETH and calculates token distribution based on the rate of 1 ETH = 99,500 KSI.
Generated: DETERMINISTIC_83c27f03c2b9d685
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

contract Presale {
    // State variables
    uint256 public constant PRESALE_CAP = 5000 ether; // Cap for the presale in ETH
    uint256 public constant TOKEN_RATE = 99500; // Rate of token distribution (1 ETH = 99,500 KSI)
    
    uint256 public totalRaised; // Total amount of ETH raised
    mapping(address => uint256) public contributions; // Mapping to track individual contributions
    
    // Event to log successful contributions
    event ContributionReceived(address indexed contributor, uint256 amount, uint256 tokensIssued);
    
    // Modifier to check if presale cap is not exceeded
    modifier notExceedingCap(uint256 _amount) {
        require(totalRaised + _amount <= PRESALE_CAP, "Presale cap exceeded");
        _;
    }
    
    // Function to contribute ETH to the presale
    function contribute() external payable notExceedingCap(msg.value) {
        require(msg.value > 0, "Contribution must be greater than 0");
        
        // Calculate the number of tokens to be issued
        uint256 tokensToIssue = msg.value * TOKEN_RATE;
        
        // Update the total raised amount and individual contribution
        totalRaised += msg.value;
        contributions[msg.sender] += msg.value;
        
        // Emit the contribution event
        emit ContributionReceived(msg.sender, msg.value, tokensToIssue);
        
        // Logic to handle token issuance can be added here
        // For example, minting tokens to the contributor's address
    }
    
    // Function to withdraw collected ETH (only owner can call)
    function withdraw() external onlyOwner {
        // Logic to withdraw the funds
        payable(owner()).transfer(address(this).balance);
    }
    
    // Function to get the current balance of the contract
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Owner of the contract
    address private owner;

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Fallback function to receive ETH
    receive() external payable {
        contribute(); // Automatically call contribute if ETH is sent directly
    }
}
```
