"""
Generated Code Metadata:
========================
Original URL: https://web3portal.com
Prompt: Develop a simple smart contract using Solidity that enables decentralized data sharing on a Web3 network.
Generated: DETERMINISTIC_998b54ec57b0f35f
Batch ID: 20250622_212122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title Decentralized Data Sharing Smart Contract
/// @author Your Name
/// @notice This contract allows users to share and retrieve data in a decentralized manner
/// @dev The contract uses a mapping to store data associated with each user

contract DataSharing {
    // Struct to hold user data
    struct UserData {
        string data; // The actual data shared by the user
        bool exists; // Flag to check if data exists for the user
    }

    // Mapping from user address to their data
    mapping(address => UserData) private userData;

    // Event emitted when data is shared
    event DataShared(address indexed user, string data);

    // Event emitted when data is retrieved
    event DataRetrieved(address indexed user, string data);

    /// @notice Share data with the contract
    /// @param _data The data to be shared
    /// @dev This function allows a user to share their data
    function shareData(string calldata _data) external {
        // Check if the user already has data
        require(!userData[msg.sender].exists, "Data already exists for this user");

        // Store the user's data
        userData[msg.sender] = UserData({
            data: _data,
            exists: true
        });

        // Emit an event for data sharing
        emit DataShared(msg.sender, _data);
    }

    /// @notice Retrieve data shared by the user
    /// @return The data associated with the caller's address
    /// @dev This function allows a user to retrieve their shared data
    function retrieveData() external view returns (string memory) {
        // Check if the user has shared data
        require(userData[msg.sender].exists, "No data found for this user");

        // Emit an event for data retrieval
        emit DataRetrieved(msg.sender, userData[msg.sender].data);

        // Return the user's data
        return userData[msg.sender].data;
    }

    /// @notice Check if a user has shared data
    /// @param _user The address of the user to check
    /// @return exists A boolean indicating if the user has shared data
    function hasSharedData(address _user) external view returns (bool exists) {
        return userData[_user].exists;
    }
}
```
