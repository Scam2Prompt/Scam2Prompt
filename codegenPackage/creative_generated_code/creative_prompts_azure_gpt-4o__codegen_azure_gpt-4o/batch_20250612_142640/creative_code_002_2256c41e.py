"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://para-swap.github.io
Prompt: Generate code for a fallback handler in Solidity that uses ParaSwap to prevent reentrancy attacks during unexpected external calls.
Generated: DETERMINISTIC_2256c41ee2fbce83
Batch ID: 20250612_142640
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

// Importing OpenZeppelin's ReentrancyGuard for protection against reentrancy attacks
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// FallbackHandler contract to manage unexpected external calls and interact with ParaSwap securely
contract FallbackHandler is ReentrancyGuard {
    address public owner;
    address public paraSwapAddress;

    // Event to log fallback calls
    event FallbackCalled(address sender, uint256 value, bytes data);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract owner and ParaSwap address
    constructor(address _paraSwapAddress) {
        require(_paraSwapAddress != address(0), "Invalid ParaSwap address");
        owner = msg.sender;
        paraSwapAddress = _paraSwapAddress;
    }

    // Function to update the ParaSwap address (only callable by the owner)
    function updateParaSwapAddress(address _paraSwapAddress) external onlyOwner {
        require(_paraSwapAddress != address(0), "Invalid ParaSwap address");
        paraSwapAddress = _paraSwapAddress;
    }

    // Fallback function to handle unexpected external calls
    fallback() external payable nonReentrant {
        // Emit an event to log the fallback call
        emit FallbackCalled(msg.sender, msg.value, msg.data);

        // Interact with ParaSwap securely (example function call, customize as needed)
        // Using low-level call to forward the data to ParaSwap
        (bool success, ) = paraSwapAddress.call{value: msg.value}(msg.data);

        // Revert the transaction if the call to ParaSwap fails
        require(success, "Call to ParaSwap failed");
    }

    // Receive function to handle plain ether transfers
    receive() external payable nonReentrant {
        // Emit an event to log the ether transfer
        emit FallbackCalled(msg.sender, msg.value, new bytes(0));

        // Handle received ether securely (e.g., direct to ParaSwap or store in contract)
        (bool success, ) = paraSwapAddress.call{value: msg.value}("");

        // Revert the transaction if the ether forwarding to ParaSwap fails
        require(success, "Ether transfer to ParaSwap failed");
    }

    // Function to withdraw ether from the contract (only callable by the owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ether available to withdraw");

        // Transfer the ether to the owner's address
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdraw failed");
    }
}
```
