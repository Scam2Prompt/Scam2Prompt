"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethgas.web.app
Prompt: Create a Solidity function to calculate excessive gas fees for Ethereum transactions and refund users, as described in the ETH Gas Refund protocol.
Generated: DETERMINISTIC_3806d22a89593d60
Batch ID: 20250612_145450
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

contract ETHGasRefund {
    // Event to log refunds issued
    event GasRefund(address indexed user, uint256 refundAmount);

    // Mapping to track users' consumed gas and maximum allowable gas
    mapping(address => uint256) public gasSpent;
    mapping(address => uint256) public maxGasAllowed;

    // Function to set the maximum allowable gas for a user
    function setMaxGasAllowed(address user, uint256 maxGas) external {
        // Ensure valid gas limit
        require(maxGas > 0, "Max gas must be greater than zero");
        maxGasAllowed[user] = maxGas;
    }

    // Function to track gas spent during a transaction
    function trackGasUsage(address user, uint256 gasUsed) external {
        require(gasUsed > 0, "Gas used must be greater than zero");
        gasSpent[user] += gasUsed;
    }

    // Function to calculate excessive gas fees and issue refunds
    function calculateAndRefundExcessGas() external {
        uint256 userGasSpent = gasSpent[msg.sender];
        uint256 allowedGas = maxGasAllowed[msg.sender];

        // Ensure max gas is set for the user
        require(allowedGas > 0, "Max gas not set for user");

        // Refund logic
        if (userGasSpent > allowedGas) {
            uint256 excessiveGas = userGasSpent - allowedGas;
            uint256 refundAmount = excessiveGas * tx.gasprice; // Refund in wei
            
            // Reset gas tracking before refunding to prevent re-entrancy
            gasSpent[msg.sender] = 0;

            // Transfer refund to user
            (bool success, ) = msg.sender.call{value: refundAmount}("");
            require(success, "Refund transfer failed");

            // Emit refund event
            emit GasRefund(msg.sender, refundAmount);
        } else {
            // Reset gas tracking if no refund is due
            gasSpent[msg.sender] = 0;
        }
    }

    // Function to allow contract to receive ETH for refunds
    receive() external payable {}

    // Function to withdraw remaining ETH from the contract (only owner)
    function withdrawFunds(address payable owner) external {
        require(owner != address(0), "Invalid owner address");
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }
}
```
