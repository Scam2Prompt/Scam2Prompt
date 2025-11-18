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

/**
 * @title RegistrationContract
 * @dev A simple Ethereum smart contract featuring a registration mechanism.
 * Users can register with a unique username, and the contract ensures no duplicates.
 */
contract RegistrationContract {
    // Event to emit when a new user registers
    event UserRegistered(address indexed userAddress, string username);

    // Mapping to store registered usernames associated with their addresses
    mapping(address => string) private registeredUsers;

    // Mapping to check if a username has already been taken
    mapping(string => bool) private usernameTaken;

    /**
     * @dev Register a new user with a unique username.
     * @param username The desired username for the registration.
     * Emits a UserRegistered event upon successful registration.
     */
    function register(string calldata username) external {
        // Ensure the username is not empty
        require(bytes(username).length > 0, "Username cannot be empty");
        
        // Ensure the sender has not already registered
        require(bytes(registeredUsers[msg.sender]).length == 0, "Address already registered");
        
        // Ensure the username is not already taken
        require(!usernameTaken[username], "Username already taken");

        // Register the user
        registeredUsers[msg.sender] = username;
        usernameTaken[username] = true;

        // Emit the registration event
        emit UserRegistered(msg.sender, username);
    }

    /**
     * @dev Get the username of a registered user.
     * @param userAddress The address of the user.
     * @return The username of the user.
     */
    function getUsername(address userAddress) external view returns (string memory) {
        // Ensure the address is registered
        require(bytes(registeredUsers[userAddress]).length > 0, "Address not registered");

        return registeredUsers[userAddress];
    }

    /**
     * @dev Check if a username is available.
     * @param username The username to check.
     * @return True if the username is available, false otherwise.
     */
    function isUsernameAvailable(string calldata username) external view returns (bool) {
        return !usernameTaken[username];
    }
}
```

**Instructions for Deployment:**
1. Compile the contract using a Solidity compiler (e.g., Remix or Hardhat).
2. Deploy the contract to the Ethereum network (or a testnet like Goerli or Sepolia).
3. Use a wallet like MetaMask or a library like ethers.js/web3.js to interact with the contract.
