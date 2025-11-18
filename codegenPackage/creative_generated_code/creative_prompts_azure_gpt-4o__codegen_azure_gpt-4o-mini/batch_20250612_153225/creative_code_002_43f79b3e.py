"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-presales1.pages.dev
Prompt: Generate a Solidity smart contract snippet to manage the presale cap of 1000 BASE for the JESSE token, ensuring no purchases exceed the cap.
Generated: DETERMINISTIC_43f79b3e66166ca2
Batch ID: 20250612_153225
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

contract JesseTokenPresale {
    // State variables
    uint256 public constant PRESALE_CAP = 1000 * 10**18; // Presale cap in BASE token (adjust decimals as needed)
    uint256 public totalRaised; // Total amount raised during presale
    mapping(address => uint256) public contributions; // Store contributions per address
    address public owner; // Owner of the contract

    // Events for logging
    event ContributionReceived(address indexed contributor, uint256 amount);
    event PresaleCapReached();

    // Modifier to restrict functions to the owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can execute this");
        _;
    }

    // Constructor to set the owner
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to contribute to the presale
    function contribute() external payable {
        // Check if contribution is valid
        require(msg.value > 0, "Contribution must be greater than zero");
        uint256 newTotalRaised = totalRaised + msg.value; // Calculate new total raised

        // Check if the new total exceeds the presale cap
        require(newTotalRaised <= PRESALE_CAP, "Presale cap exceeded");

        // Update state variables
        totalRaised = newTotalRaised;
        contributions[msg.sender] += msg.value;

        // Emit contribution event
        emit ContributionReceived(msg.sender, msg.value);

        // Check if presale cap reached
        if (totalRaised == PRESALE_CAP) {
            emit PresaleCapReached();
        }
    }

    // Function to withdraw funds from presale (only callable by the owner)
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance; // Get contract balance
        require(balance > 0, "No funds available for withdrawal");
        
        // Transfer the balance to the owner
        payable(owner).transfer(balance);
    }

    // Function to get the current contract balance
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers are not allowed. Use contribute() function.");
    }
}
```
