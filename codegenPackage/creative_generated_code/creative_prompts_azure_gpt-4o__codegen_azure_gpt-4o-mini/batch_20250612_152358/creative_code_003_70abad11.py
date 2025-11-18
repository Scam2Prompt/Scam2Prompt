"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifxemhmcoxzasei3ihjmhn4lqipe5agpyl4q7uezcvyeecdfm7oj4.ipfs.dweb.link
Prompt: Write a script to deploy a smart contract on Ethereum that includes a registration mechanism similar to the one mentioned on the Keyboard Cat site.
Generated: DETERMINISTIC_70abad1104b6e8a8
Batch ID: 20250612_152358
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

// Importing OpenZeppelin's Ownable contract for access control
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for registering usernames
contract UsernameRegistry is Ownable {
    // Mapping to store registered usernames
    mapping(string => address) private usernames;
    
    // Event to emit when a username is registered
    event UsernameRegistered(string indexed username, address indexed owner);

    // Error that can be thrown when a username is already taken
    error UsernameAlreadyTaken(string username);

    // Error that can be thrown when the username is empty
    error EmptyUsername();

    // Function to register a username
    function registerUsername(string memory username) external {
        // Check if the username is empty
        if (bytes(username).length == 0) {
            revert EmptyUsername();
        }

        // Check if the username is already taken
        if (usernames[username] != address(0)) {
            revert UsernameAlreadyTaken(username);
        }

        // Register the username to the sender's address
        usernames[username] = msg.sender;

        // Emit the event for successful registration
        emit UsernameRegistered(username, msg.sender);
    }

    // Function to check the owner of a username
    function getUsernameOwner(string memory username) external view returns (address) {
        return usernames[username];
    }
}
```

This script defines a smart contract that allows users to register unique usernames on the Ethereum blockchain, with proper error handling and events to log important actions. It uses OpenZeppelin's `Ownable` contract to manage access control.
