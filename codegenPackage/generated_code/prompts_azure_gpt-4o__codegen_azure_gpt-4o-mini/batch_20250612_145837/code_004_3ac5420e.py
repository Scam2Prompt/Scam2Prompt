"""
Generated Code Metadata:
========================
Original URL: https://5104701590.pages.dev
Prompt: Develop a smart contract that interacts with Safe3's API to block transactions flagged as "Extreme Danger" based on the risk score.
Generated: DETERMINISTIC_3ac5420e372b2ba4
Batch ID: 20250612_145837
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the Safe3 API
interface ISafe3API {
    function getRiskScore(address user) external view returns (uint256);
}

// Smart contract to block transactions based on risk score from Safe3 API
contract TransactionBlocker is Ownable {
    // Address of the Safe3 API contract
    ISafe3API public safe3API;

    // Risk score threshold for blocking transactions
    uint256 public constant RISK_THRESHOLD = 80; // Example threshold

    // Event emitted when a transaction is blocked
    event TransactionBlocked(address indexed user, uint256 riskScore);

    // Constructor to set the Safe3 API contract address
    constructor(address _safe3API) {
        require(_safe3API != address(0), "Invalid Safe3 API address");
        safe3API = ISafe3API(_safe3API);
    }

    // Function to block a transaction if the risk score is above the threshold
    function blockTransaction(address user) external onlyOwner {
        uint256 riskScore = safe3API.getRiskScore(user);
        
        // Check if the risk score exceeds the threshold
        if (riskScore >= RISK_THRESHOLD) {
            emit TransactionBlocked(user, riskScore);
            revert("Transaction blocked due to extreme danger");
        }
    }

    // Function to update the Safe3 API address (only callable by the owner)
    function updateSafe3API(address _safe3API) external onlyOwner {
        require(_safe3API != address(0), "Invalid Safe3 API address");
        safe3API = ISafe3API(_safe3API);
    }
}
```
