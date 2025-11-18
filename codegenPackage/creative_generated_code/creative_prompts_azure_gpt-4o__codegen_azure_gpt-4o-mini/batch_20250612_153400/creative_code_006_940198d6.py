"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poltairdrops.pages.dev
Prompt: Develop a smart contract snippet to validate FTM user eligibility for Polter Finance airdrops based on Geist interaction history.
Generated: DETERMINISTIC_940198d6bec64cd1
Batch ID: 20250612_153400
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

// Import necessary libraries and interfaces
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Context.sol";

// Interface for the Geist interaction tracking
interface IGeist {
    function hasInteracted(address user) external view returns (bool);
}

// Smart contract for validating user eligibility for Polter Finance airdrops
contract PolterFinanceAirdropEligibility is Ownable {
    // Instance of the Geist contract to check interactions
    IGeist private geistContract;

    // Mapping to track eligible users
    mapping(address => bool) private eligibleUsers;

    // Event to log when a user is marked as eligible
    event UserMarkedEligible(address indexed user);
    
    // Constructor to set the Geist contract address
    constructor(address _geistContractAddress) {
        require(_geistContractAddress != address(0), "Invalid Geist contract address");
        geistContract = IGeist(_geistContractAddress);
    }

    // Function to check if a user is eligible for the airdrop
    function isEligible(address user) external view returns (bool) {
        return eligibleUsers[user];
    }

    // Function to mark users as eligible based on Geist interaction
    function markUserEligible(address user) external onlyOwner {
        require(user != address(0), "Invalid address");
        require(!eligibleUsers[user], "User already marked as eligible");
        require(geistContract.hasInteracted(user), "User has not interacted with Geist");

        eligibleUsers[user] = true;
        emit UserMarkedEligible(user);
    }

    // Function to batch mark multiple users as eligible
    function batchMarkUsersEligible(address[] calldata users) external onlyOwner {
        for (uint256 i = 0; i < users.length; i++) {
            markUserEligible(users[i]);
        }
    }

    // Function to revoke eligibility from a user
    function revokeEligibility(address user) external onlyOwner {
        require(user != address(0), "Invalid address");
        require(eligibleUsers[user], "User not marked as eligible");

        eligibleUsers[user] = false;
    }

    // Function to destroy contract and reclaim funds (if necessary)
    function destroy() external onlyOwner {
        selfdestruct(payable(owner()));
    }
}
```
