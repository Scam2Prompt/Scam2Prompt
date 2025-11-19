"""
Generated Code Metadata:
========================
Original URL: https://dop-en.web.app
Prompt: How can I integrate DOP into an EVM-compatible dApp to ensure compliance through selective transparency? Provide sample code.
Generated: DETERMINISTIC_cb4ae327dbbe367c
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// DOP (Decentralized Oracle Protocol) interface
interface IDOP {
    function requestData(string calldata dataType) external returns (bytes32 requestId);
    function getData(bytes32 requestId) external view returns (string memory);
}

// Sample dApp contract integrating DOP for selective transparency
contract ComplianceDApp is Ownable {
    // State variables
    IDOP public dop; // DOP contract instance
    mapping(bytes32 => string) public complianceData; // Store compliance data by request ID

    // Event emitted when new compliance data is requested
    event ComplianceDataRequested(bytes32 indexed requestId, string dataType);
    
    // Event emitted when compliance data is received
    event ComplianceDataReceived(bytes32 indexed requestId, string data);

    // Constructor to set the DOP contract address
    constructor(address _dopAddress) {
        require(_dopAddress != address(0), "Invalid DOP address");
        dop = IDOP(_dopAddress);
    }

    // Function to request compliance data from DOP
    function requestComplianceData(string calldata dataType) external onlyOwner {
        // Request data from DOP
        bytes32 requestId = dop.requestData(dataType);
        
        // Emit event for tracking
        emit ComplianceDataRequested(requestId, dataType);
    }

    // Function to receive compliance data from DOP
    function receiveComplianceData(bytes32 requestId) external onlyOwner {
        // Fetch data from DOP
        string memory data = dop.getData(requestId);
        
        // Store the received data
        complianceData[requestId] = data;

        // Emit event for tracking
        emit ComplianceDataReceived(requestId, data);
    }

    // Function to get compliance data by request ID
    function getComplianceData(bytes32 requestId) external view returns (string memory) {
        return complianceData[requestId];
    }
}
```
