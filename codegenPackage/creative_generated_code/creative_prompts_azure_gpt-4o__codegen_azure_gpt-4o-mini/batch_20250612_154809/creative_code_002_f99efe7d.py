"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-slippagebot.pages.dev
Prompt: Create a Solidity function for detecting and interacting with newly deployed contracts on the Ethereum mainnet, using the `findContracts` logic described in the Uniswap Slippage Bot.
Generated: DETERMINISTIC_f99efe7db43ce40e
Batch ID: 20250612_154809
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

contract ContractTracker {
    // Event to log new contract addresses
    event NewContractDetected(address indexed contractAddress);

    // A list to hold detected contract addresses
    address[] public detectedContracts;

    // Function to detect if an address is a contract
    function isContract(address _addr) internal view returns (bool) {
        uint256 size;
        assembly {
            size := extcodesize(_addr)
        }
        return size > 0;
    }

    // Function to find newly deployed contracts
    function findContracts(address[] memory _addresses) external {
        // Validate input
        require(_addresses.length > 0, "The address array cannot be empty");

        for (uint256 i = 0; i < _addresses.length; i++) {
            address addr = _addresses[i];
            // Check if the address is a contract
            if (isContract(addr)) {
                // Check if the contract has already been detected
                bool alreadyDetected = false;
                for (uint256 j = 0; j < detectedContracts.length; j++) {
                    if (detectedContracts[j] == addr) {
                        alreadyDetected = true;
                        break;
                    }
                }
                // If it's a new contract, add it to the list and emit an event
                if (!alreadyDetected) {
                    detectedContracts.push(addr);
                    emit NewContractDetected(addr);
                }
            }
        }
    }

    // Function to get the detected contracts
    function getDetectedContracts() external view returns (address[] memory) {
        return detectedContracts;
    }
}
```
