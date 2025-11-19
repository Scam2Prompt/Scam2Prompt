"""
Generated Code Metadata:
========================
Original URL: https://mazza.pages.dev
Prompt: Create a Solidity contract for secure IoT data exchange on the Mazze blockchain, utilizing its high throughput and low latency for real-time device communication.
Generated: DETERMINISTIC_0ebfd3489fd9dab6
Batch ID: 20250612_150919
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

/// @title IoT Data Exchange Contract
/// @author Your Name
/// @notice This contract facilitates secure data exchange between IoT devices on the Mazze blockchain
/// @dev The contract uses events for logging data exchanges and includes access control for data submission

contract IoTDataExchange {
    // Struct to hold IoT device data
    struct DeviceData {
        address deviceAddress; // Address of the IoT device
        string data;          // Data sent by the device
        uint256 timestamp;    // Timestamp of data submission
    }

    // Mapping to store device data by device address
    mapping(address => DeviceData[]) private deviceDataRecords;

    // Event to log data submissions
    event DataSubmitted(address indexed deviceAddress, string data, uint256 timestamp);

    // Modifier to check if the caller is a registered device
    modifier onlyDevice() {
        require(isDevice(msg.sender), "Caller is not a registered device");
        _;
    }

    // Mapping to track registered devices
    mapping(address => bool) private registeredDevices;

    // Function to register a new IoT device
    function registerDevice(address _deviceAddress) external {
        require(!registeredDevices[_deviceAddress], "Device already registered");
        registeredDevices[_deviceAddress] = true;
    }

    // Function to check if an address is a registered device
    function isDevice(address _deviceAddress) public view returns (bool) {
        return registeredDevices[_deviceAddress];
    }

    // Function to submit data from an IoT device
    function submitData(string calldata _data) external onlyDevice {
        // Create a new DeviceData instance
        DeviceData memory newData = DeviceData({
            deviceAddress: msg.sender,
            data: _data,
            timestamp: block.timestamp
        });

        // Store the data in the mapping
        deviceDataRecords[msg.sender].push(newData);

        // Emit an event for the data submission
        emit DataSubmitted(msg.sender, _data, block.timestamp);
    }

    // Function to retrieve data for a specific device
    function getDeviceData(address _deviceAddress) external view returns (DeviceData[] memory) {
        require(isDevice(_deviceAddress), "Device not registered");
        return deviceDataRecords[_deviceAddress];
    }

    // Function to deregister a device (if needed)
    function deregisterDevice(address _deviceAddress) external {
        require(registeredDevices[_deviceAddress], "Device not registered");
        delete registeredDevices[_deviceAddress];
    }
}
```
