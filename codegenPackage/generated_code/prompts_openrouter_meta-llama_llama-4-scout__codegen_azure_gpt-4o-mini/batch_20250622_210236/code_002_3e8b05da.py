"""
Generated Code Metadata:
========================
Original URL: https://node-sophon.com
Prompt: "Generate a simple smart contract using Solidity to interact with Sophon's blockchain, focusing on user-centric entertainment applications."
Generated: DETERMINISTIC_3e8b05dac9efd3a2
Batch ID: 20250622_210236
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

/// @title User-Centric Entertainment Smart Contract
/// @author Your Name
/// @notice This contract allows users to create and manage entertainment applications on the Sophon blockchain
/// @dev This contract is designed to be simple and user-friendly

contract EntertainmentApp {
    // Struct to represent an entertainment application
    struct App {
        uint256 id;
        string name;
        string description;
        address owner;
        bool isActive;
    }

    // Mapping to store applications by their ID
    mapping(uint256 => App) private apps;
    // Counter for app IDs
    uint256 private appIdCounter;

    // Event emitted when a new app is created
    event AppCreated(uint256 indexed appId, string name, address indexed owner);
    // Event emitted when an app is activated or deactivated
    event AppStatusChanged(uint256 indexed appId, bool isActive);

    /// @notice Creates a new entertainment application
    /// @param _name The name of the application
    /// @param _description A brief description of the application
    /// @dev Emits an AppCreated event upon successful creation
    function createApp(string calldata _name, string calldata _description) external {
        require(bytes(_name).length > 0, "App name cannot be empty");
        require(bytes(_description).length > 0, "App description cannot be empty");

        appIdCounter++;
        apps[appIdCounter] = App(appIdCounter, _name, _description, msg.sender, true);

        emit AppCreated(appIdCounter, _name, msg.sender);
    }

    /// @notice Toggles the active status of an application
    /// @param _appId The ID of the application to be toggled
    /// @dev Emits an AppStatusChanged event upon successful status change
    function toggleAppStatus(uint256 _appId) external {
        App storage app = apps[_appId];
        require(app.id != 0, "App does not exist");
        require(app.owner == msg.sender, "Only the owner can change the status");

        app.isActive = !app.isActive;

        emit AppStatusChanged(_appId, app.isActive);
    }

    /// @notice Retrieves the details of an application
    /// @param _appId The ID of the application to retrieve
    /// @return The application details
    /// @dev Reverts if the application does not exist
    function getApp(uint256 _appId) external view returns (App memory) {
        App storage app = apps[_appId];
        require(app.id != 0, "App does not exist");
        return app;
    }

    /// @notice Retrieves the total number of applications created
    /// @return The total number of applications
    function getTotalApps() external view returns (uint256) {
        return appIdCounter;
    }
}
```
