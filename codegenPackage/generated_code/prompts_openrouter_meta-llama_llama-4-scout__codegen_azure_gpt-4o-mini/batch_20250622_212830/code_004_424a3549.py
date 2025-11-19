"""
Generated Code Metadata:
========================
Original URL: https://apps-odos.fi
Prompt: Write a code snippet in Solidity to create a smart contract that interacts with the Odos API to fetch the estimated gas cost for a trade.
Generated: DETERMINISTIC_424a3549b465639e
Batch ID: 20250622_212830
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

// Importing necessary interfaces for interacting with external contracts
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

// Interface for the Odos API (mocked for demonstration purposes)
interface IOdosAPI {
    function getEstimatedGasCost(address fromToken, address toToken, uint256 amount) external view returns (uint256);
}

// Smart contract to interact with the Odos API for gas cost estimation
contract GasCostEstimator is Ownable {
    using Address for address;

    // Address of the Odos API contract
    IOdosAPI public odosAPI;

    // Event to emit when gas cost is estimated
    event GasCostEstimated(uint256 estimatedGasCost);

    // Constructor to set the Odos API contract address
    constructor(address _odosAPI) {
        require(_odosAPI.isContract(), "Invalid Odos API address");
        odosAPI = IOdosAPI(_odosAPI);
    }

    // Function to estimate gas cost for a trade
    function estimateGasCost(address fromToken, address toToken, uint256 amount) external onlyOwner returns (uint256) {
        require(fromToken != address(0), "Invalid fromToken address");
        require(toToken != address(0), "Invalid toToken address");
        require(amount > 0, "Amount must be greater than zero");

        // Fetching the estimated gas cost from the Odos API
        uint256 estimatedGasCost;
        try odosAPI.getEstimatedGasCost(fromToken, toToken, amount) returns (uint256 gasCost) {
            estimatedGasCost = gasCost;
        } catch {
            revert("Failed to fetch estimated gas cost from Odos API");
        }

        // Emitting the estimated gas cost
        emit GasCostEstimated(estimatedGasCost);
        return estimatedGasCost;
    }

    // Function to update the Odos API contract address (only callable by the owner)
    function updateOdosAPI(address newOdosAPI) external onlyOwner {
        require(newOdosAPI.isContract(), "Invalid Odos API address");
        odosAPI = IOdosAPI(newOdosAPI);
    }
}
```
