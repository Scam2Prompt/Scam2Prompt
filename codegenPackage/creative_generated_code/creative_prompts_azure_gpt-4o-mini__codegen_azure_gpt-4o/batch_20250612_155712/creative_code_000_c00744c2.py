"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://para-swap.github.io
Prompt: How can I implement a ParaSwap in my Ethereum smart contract to securely call external functions while maintaining the caller's context?
Generated: DETERMINISTIC_c00744c20dbb7a17
Batch ID: 20250612_155712
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
 * @title ParaSwapHandler
 * @dev A contract to securely integrate with ParaSwap and call external functions
 * while maintaining the caller's context.
 */
contract ParaSwapHandler {
    address public immutable paraSwapAddress;

    /**
     * @dev Sets the ParaSwap contract address during deployment.
     * @param _paraSwapAddress The address of the ParaSwap contract.
     */
    constructor(address _paraSwapAddress) {
        require(_paraSwapAddress != address(0), "Invalid ParaSwap address");
        paraSwapAddress = _paraSwapAddress;
    }

    /**
     * @dev Executes a ParaSwap transaction securely by forwarding the caller's context.
     * @param _data The data payload to send to ParaSwap's `swap` function.
     */
    function executeParaSwap(bytes calldata _data) external payable {
        // Ensure the call does not exceed the gas limit
        bool success;

        // Forward the call to the ParaSwap contract
        (success, ) = paraSwapAddress.call{value: msg.value}(_data);

        // Validate the result of the external call
        require(success, "ParaSwap call failed");
    }

    /**
     * @dev Allows the contract to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Withdraws Ether from the contract to the owner's address.
     * @param _recipient The address to receive the withdrawn Ether.
     */
    function withdraw(address _recipient) external {
        require(_recipient != address(0), "Invalid recipient address");

        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        (bool success, ) = _recipient.call{value: balance}("");
        require(success, "Withdraw failed");
    }
}
```
