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

/**
 * @title IoTDataExchange
 * @dev A secure contract for exchanging IoT data on the Mazze blockchain.
 * @dev Utilizes Mazze's high throughput and low latency for real-time device communication.
 */
contract IoTDataExchange {

    // Structure to define an IoT device
    struct Device {
        string deviceId;       // Unique ID for the device
        address owner;         // Address of the device owner
        bool registered;       // Registration status
    }

    // Mapping to store registered IoT devices
    mapping(string => Device) private devices;

    // Event emitted when a device is registered
    event DeviceRegistered(string deviceId, address owner);

    // Event emitted when data is exchanged
    event DataExchanged(string deviceId, address receiver, string data);

    // Modifier to ensure only the owner of a device can perform certain actions
    modifier onlyDeviceOwner(string memory deviceId) {
        require(
            devices[deviceId].owner == msg.sender,
            "Caller is not the owner of the device"
        );
        _;
    }

    /**
     * @dev Registers an IoT device in the system.
     * @param deviceId The unique ID of the IoT device.
     */
    function registerDevice(string memory deviceId) external {
        require(bytes(deviceId).length > 0, "Device ID cannot be empty");
        require(!devices[deviceId].registered, "Device already registered");

        devices[deviceId] = Device({
            deviceId: deviceId,
            owner: msg.sender,
            registered: true
        });

        emit DeviceRegistered(deviceId, msg.sender);
    }

    /**
     * @dev Allows the registered IoT device to exchange data with a receiver.
     * @param deviceId The unique ID of the IoT device.
     * @param receiver The address of the recipient.
     * @param data The data to be exchanged.
     */
    function exchangeData(
        string memory deviceId,
        address receiver,
        string memory data
    ) external onlyDeviceOwner(deviceId) {
        require(receiver != address(0), "Receiver address cannot be zero");
        require(bytes(data).length > 0, "Data cannot be empty");

        // Emit an event to log the data exchange
        emit DataExchanged(deviceId, receiver, data);
    }

    /**
     * @dev Retrieves details of a registered device.
     * @param deviceId The unique ID of the IoT device.
     * @return The owner and registration status of the device.
     */
    function getDeviceDetails(string memory deviceId)
        external
        view
        returns (address owner, bool registered)
    {
        require(devices[deviceId].registered, "Device not registered");

        Device memory device = devices[deviceId];
        return (device.owner, device.registered);
    }
}
```
