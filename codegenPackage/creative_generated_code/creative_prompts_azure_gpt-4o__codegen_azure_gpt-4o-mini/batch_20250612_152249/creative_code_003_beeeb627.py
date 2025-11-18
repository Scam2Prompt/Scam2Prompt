"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spores-buv.pages.dev
Prompt: Create a function in Solidity to verify if a wallet address is eligible to participate in an IDO on Spores Network.
Generated: DETERMINISTIC_beeeb627b41243fd
Batch ID: 20250612_152249
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

contract SporesNetworkIDO {
    // State variable to store the list of eligible addresses
    mapping(address => bool) private eligibleAddresses;
    
    // Event to log eligibility status changes
    event EligibilityUpdated(address indexed wallet, bool isEligible);

    // Modifier to check if the caller is the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Owner of the contract
    address public owner;

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    // Function to add an address to the eligibility list
    function addEligibleAddress(address wallet) external onlyOwner {
        require(wallet != address(0), "Invalid address");
        eligibleAddresses[wallet] = true;
        emit EligibilityUpdated(wallet, true);
    }

    // Function to remove an address from the eligibility list
    function removeEligibleAddress(address wallet) external onlyOwner {
        require(wallet != address(0), "Invalid address");
        eligibleAddresses[wallet] = false;
        emit EligibilityUpdated(wallet, false);
    }

    // Function to check if an address is eligible for IDO
    function isEligible(address wallet) external view returns (bool) {
        require(wallet != address(0), "Invalid address");
        return eligibleAddresses[wallet];
    }
}
```
