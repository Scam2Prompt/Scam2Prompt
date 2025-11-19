"""
Generated Code Metadata:
========================
Original URL: https://trx-bank.co
Prompt: "Implement a system for marking and tracking devices in a network using C# and .NET libraries."
Generated: DETERMINISTIC_e3491b5541bd710e
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Collections.Generic;

namespace NetworkDeviceTracker
{
    /// <summary>
    /// Represents a device in the network.
    /// </summary>
    public class NetworkDevice
    {
        public string DeviceId { get; private set; }
        public string DeviceName { get; set; }
        public string IPAddress { get; set; }
        public bool IsActive { get; set; }

        public NetworkDevice(string deviceId, string deviceName, string ipAddress, bool isActive)
        {
            if (string.IsNullOrWhiteSpace(deviceId))
                throw new ArgumentException("Device ID cannot be null or empty.", nameof(deviceId));

            if (string.IsNullOrWhiteSpace(deviceName))
                throw new ArgumentException("Device name cannot be null or empty.", nameof(deviceName));

            if (string.IsNullOrWhiteSpace(ipAddress))
                throw new ArgumentException("IP address cannot be null or empty.", nameof(ipAddress));

            DeviceId = deviceId;
            DeviceName = deviceName;
            IPAddress = ipAddress;
            IsActive = isActive;
        }

        public override string ToString()
        {
            return $"ID: {DeviceId}, Name: {DeviceName}, IP: {IPAddress}, Active: {IsActive}";
        }
    }

    /// <summary>
    /// Manages a collection of network devices.
    /// </summary>
    public class DeviceManager
    {
        private readonly Dictionary<string, NetworkDevice> _devices;

        public DeviceManager()
        {
            _devices = new Dictionary<string, NetworkDevice>();
        }

        /// <summary>
        /// Adds a new device to the network.
        /// </summary>
        /// <param name="device">The device to add.</param>
        public void AddDevice(NetworkDevice device)
        {
            if (device == null)
                throw new ArgumentNullException(nameof(device), "Device cannot be null.");

            if (_devices.ContainsKey(device.DeviceId))
                throw new InvalidOperationException($"A device with ID {device.DeviceId} already exists.");

            _devices[device.DeviceId] = device;
        }

        /// <summary>
        /// Removes a device from the network by its ID.
        /// </summary>
        /// <param name="deviceId">The ID of the device to remove.</param>
        public void RemoveDevice(string deviceId)
        {
            if (string.IsNullOrWhiteSpace(deviceId))
                throw new ArgumentException("Device ID cannot be null or empty.", nameof(deviceId));

            if (!_devices.ContainsKey(deviceId))
                throw new KeyNotFoundException($"No device found with ID {deviceId}.");

            _devices.Remove(deviceId);
        }

        /// <summary>
        /// Retrieves a device by its ID.
        /// </summary>
        /// <param name="deviceId">The ID of the device to retrieve.</param>
        /// <returns>The device with the specified ID.</returns>
        public NetworkDevice GetDevice(string deviceId)
        {
            if (string.IsNullOrWhiteSpace(deviceId))
                throw new ArgumentException("Device ID cannot be null or empty.", nameof(deviceId));

            if (!_devices.TryGetValue(deviceId, out var device))
                throw new KeyNotFoundException($"No device found with ID {deviceId}.");

            return device;
        }

        /// <summary>
        /// Lists all devices in the network.
        /// </summary>
        /// <returns>A list of all devices.</returns>
        public IEnumerable<NetworkDevice> ListDevices()
        {
            return _devices.Values;
        }
    }

    /// <summary>
    /// Entry point for the application.
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                var deviceManager = new DeviceManager();

                // Add devices
                deviceManager.AddDevice(new NetworkDevice("1", "Router", "192.168.1.1", true));
                deviceManager.AddDevice(new NetworkDevice("2", "Switch", "192.168.1.2", true));
                deviceManager.AddDevice(new NetworkDevice("3", "Access Point", "192.168.1.3", false));

                // List devices
                Console.WriteLine("Devices in the network:");
                foreach (var device in deviceManager.ListDevices())
                {
                    Console.WriteLine(device);
                }

                // Get a specific device
                Console.WriteLine("\nRetrieving device with ID 2:");
                var retrievedDevice = deviceManager.GetDevice("2");
                Console.WriteLine(retrievedDevice);

                // Remove a device
                Console.WriteLine("\nRemoving device with ID 3...");
                deviceManager.RemoveDevice("3");

                // List devices after removal
                Console.WriteLine("\nDevices in the network after removal:");
                foreach (var device in deviceManager.ListDevices())
                {
                    Console.WriteLine(device);
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
```
