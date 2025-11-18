"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layer-1yd.pages.dev
Prompt: Write a Solidity function to check the version compatibility of OFT contracts using the `oftVersion` method provided by LayerZero.
Generated: DETERMINISTIC_0cf868a9746aafd7
Batch ID: 20250612_150226
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

// Importing LayerZero interface for interacting with OFT contracts
import "@layerzero/contracts/interfaces/ILayerZeroOFT.sol";

contract OFTVersionChecker {
    // State variable to store the LayerZero OFT contract address
    address public oftContractAddress;

    // Event to emit when version compatibility is checked
    event VersionChecked(address indexed contractAddress, uint256 version, bool compatible);

    // Constructor to set the OFT contract address
    constructor(address _oftContractAddress) {
        // Validate that the address is a contract
        require(_oftContractAddress != address(0), "Invalid OFT contract address");
        oftContractAddress = _oftContractAddress;
    }

    /**
     * @dev Checks the version compatibility of the OFT contract.
     * @return compatible True if the version is compatible, false otherwise.
     */
    function checkVersionCompatibility() external returns (bool compatible) {
        try ILayerZeroOFT(oftContractAddress).oftVersion() returns (uint256 version) {
            // Assuming version 1 is the required version for compatibility
            compatible = (version == 1);
            emit VersionChecked(oftContractAddress, version, compatible);
        } catch {
            // Emit a failed check due to an error
            emit VersionChecked(oftContractAddress, 0, false);
            revert("Failed to check version compatibility");
        }
    }
}
```
