"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mazza.pages.dev
Prompt: Create a Solidity contract for secure IoT data exchange on the Mazze blockchain, utilizing its high throughput and low latency for real-time device communication.
Generated: DETERMINISTIC_0ebfd3489fd9dab6
Batch ID: 20250612_150919
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

// Importing required libraries for security and utility
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

// Interface for external devices to interact with the contract
interface IDevice {
    function sendData(string calldata data) external returns (bool);
    function retrieveData() external view returns (string memory);
}

// Main contract for secure IoT data exchange
contract IoTDataExchange is Ownable {
    // Event emitted whenever new data is received
    event DataReceived(address indexed device, string data);

    // Mapping to store data associated with devices
    mapping(address => string) private deviceData;

    // Modifier to check if the caller is a registered device
    modifier onlyDevice() {
        require(deviceData[msg.sender].length > 0, "Caller is not a registered device");
        _;
    }

    // Function to register a new device
    function registerDevice(address device) external onlyOwner {
        require(device != address(0), "Invalid device address");
        require(bytes(deviceData[device]).length == 0, "Device already registered");

        deviceData[device] = ""; // Initialize device data
    }

    // Function for devices to send data
    function sendData(string calldata data) external onlyDevice returns (bool) {
        require(bytes(data).length > 0, "Data cannot be empty");

        deviceData[msg.sender] = data; // Store data for the device
        emit DataReceived(msg.sender, data); // Emit event

        return true; // Indicate success
    }

    // Function for devices to retrieve their data
    function retrieveData() external view onlyDevice returns (string memory) {
        return deviceData[msg.sender]; // Return stored data
    }

    // Function to remove a device's registration
    function removeDevice(address device) external onlyOwner {
        require(device != address(0), "Invalid device address");
        require(bytes(deviceData[device]).length > 0, "Device not registered");

        delete deviceData[device]; // Remove device data
    }

    // Function to get a device's stored data (for owner only)
    function getDeviceData(address device) external view onlyOwner returns (string memory) {
        require(device != address(0), "Invalid device address");
        return deviceData[device]; // Return data for the specified device
    }
}
```
