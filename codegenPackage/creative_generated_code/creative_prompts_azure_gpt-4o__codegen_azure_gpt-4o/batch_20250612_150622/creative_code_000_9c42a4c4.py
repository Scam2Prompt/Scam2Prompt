"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://to-ousd.pages.dev
Prompt: Write a Solidity function that enables a smart contract to opt-in for receiving yield from OUSD, as described in the Origin Dollar documentation.
Generated: DETERMINISTIC_9c42a4c42cd3be40
Batch ID: 20250612_150622
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

// Interface for OUSD contract with opt-in function
interface IOUSD {
    function rebaseOptIn() external;
}

contract OUSDOptIn {
    // Address of the OUSD contract
    address public ousdContract;

    // Event emitted when the contract opts-in for yield
    event YieldOptIn(address indexed contractAddress);

    // Modifier to ensure OUSD contract address is set
    modifier ousdAddressSet() {
        require(ousdContract != address(0), "OUSD contract address not set");
        _;
    }

    // Constructor to initialize the OUSD contract address
    constructor(address _ousdContract) {
        require(_ousdContract != address(0), "Invalid OUSD contract address");
        ousdContract = _ousdContract;
    }

    // Function to opt-in for receiving yield from OUSD
    function optInForYield() external ousdAddressSet {
        // Interface call to the OUSD contract's opt-in function
        IOUSD(ousdContract).rebaseOptIn();

        // Emit an event to indicate successful opt-in
        emit YieldOptIn(address(this));
    }

    // Function to update the OUSD contract address (if needed)
    function setOUSDContract(address _ousdContract) external {
        require(_ousdContract != address(0), "Invalid OUSD contract address");
        ousdContract = _ousdContract;
    }
}
```
