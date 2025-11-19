"""
Generated Code Metadata:
========================
Original URL: https://quedge.io
Prompt: "Create a JavaScript code snippet to track and display the earnings and performance metrics of an Aethir Edge device."
Generated: DETERMINISTIC_2015b1c25627c337
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Aethir Edge Device Earnings and Performance Tracker
 * This script tracks and displays the earnings and performance metrics of an Aethir Edge device.
 * It includes error handling and follows best practices for clean, maintainable code.
 */

// Mock data for demonstration purposes (replace with actual API or data source)
const edgeDeviceData = {
  id: "device123",
  name: "Aethir Edge Device 1",
  earnings: 0, // Total earnings in USD
  performanceMetrics: {
    cpuUsage: 0, // CPU usage percentage
    memoryUsage: 0, // Memory usage percentage
    uptime: 0, // Uptime in hours
  },
};

// Function to simulate fetching updated data (replace with actual API call)
async function fetchDeviceData(deviceId) {
  try {
    // Simulate an API call with a delay
    await new Promise((resolve) => setTimeout(resolve, 1000));

    // Mock updated data (replace with actual API response)
    return {
      earnings: Math.random() * 1000, // Random earnings for demonstration
      performanceMetrics: {
        cpuUsage: Math.random() * 100, // Random CPU usage percentage
        memoryUsage: Math.random() * 100, // Random memory usage percentage
        uptime: Math.random() * 1000, // Random uptime in hours
      },
    };
  } catch (error) {
    console.error("Error fetching device data:", error);
    throw new Error("Failed to fetch device data.");
  }
}

// Function to update the device data
async function updateDeviceData(device) {
  try {
    const updatedData = await fetchDeviceData(device.id);
    device.earnings = updatedData.earnings;
    device.performanceMetrics = updatedData.performanceMetrics;
    console.log("Device data updated successfully.");
  } catch (error) {
    console.error("Error updating device data:", error);
  }
}

// Function to display the device data
function displayDeviceData(device) {
  console.log("=== Aethir Edge Device Metrics ===");
  console.log(`Device Name: ${device.name}`);
  console.log(`Total Earnings: $${device.earnings.toFixed(2)}`);
  console.log("Performance Metrics:");
  console.log(`  CPU Usage: ${device.performanceMetrics.cpuUsage.toFixed(2)}%`);
  console.log(`  Memory Usage: ${device.performanceMetrics.memoryUsage.toFixed(2)}%`);
  console.log(`  Uptime: ${device.performanceMetrics.uptime.toFixed(2)} hours`);
  console.log("=================================");
}

// Main function to track and display device metrics
async function trackDeviceMetrics(device) {
  try {
    console.log("Fetching and updating device metrics...");
    await updateDeviceData(device);
    displayDeviceData(device);
  } catch (error) {
    console.error("Error tracking device metrics:", error);
  }
}

// Run the tracker for the edge device
trackDeviceMetrics(edgeDeviceData);
```
