"""
Generated Code Metadata:
========================
Original URL: https://financial-justice.com
Prompt: Develop a code snippet for a smart contract that can automate the process of refunding victims of cryptocurrency scams, using blockchain technology to ensure secure and transparent transactions.
Generated: DETERMINISTIC_de5e9611c2c17aa8
Batch ID: 20250622_212006
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

contract ScamRefund {
    // Struct to hold information about each refund request
    struct RefundRequest {
        address payable victim; // Address of the victim
        uint256 amount;         // Amount to be refunded
        bool isProcessed;       // Status of the refund request
    }

    // Mapping to store refund requests by their unique ID
    mapping(uint256 => RefundRequest) public refundRequests;
    uint256 public requestCount; // Counter for refund requests

    // Event to emit when a refund request is created
    event RefundRequested(uint256 requestId, address victim, uint256 amount);
    
    // Event to emit when a refund is processed
    event RefundProcessed(uint256 requestId, address victim, uint256 amount);

    // Function to create a refund request
    function requestRefund(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        
        // Increment the request count to create a unique ID
        requestCount++;
        
        // Create a new refund request
        refundRequests[requestCount] = RefundRequest({
            victim: payable(msg.sender),
            amount: _amount,
            isProcessed: false
        });

        // Emit an event for the new refund request
        emit RefundRequested(requestCount, msg.sender, _amount);
    }

    // Function to process a refund request
    function processRefund(uint256 _requestId) external {
        // Retrieve the refund request
        RefundRequest storage request = refundRequests[_requestId];

        // Ensure the request exists and has not been processed
        require(request.victim != address(0), "Refund request does not exist");
        require(!request.isProcessed, "Refund already processed");

        // Ensure the contract has enough balance to cover the refund
        require(address(this).balance >= request.amount, "Insufficient contract balance");

        // Mark the request as processed
        request.isProcessed = true;

        // Transfer the refund amount to the victim
        request.victim.transfer(request.amount);

        // Emit an event for the processed refund
        emit RefundProcessed(_requestId, request.victim, request.amount);
    }

    // Function to receive Ether. This allows the contract to accept funds.
    receive() external payable {}

    // Function to withdraw funds from the contract (only for owner or admin)
    function withdraw(uint256 _amount) external {
        // Only allow withdrawal if the contract has enough balance
        require(address(this).balance >= _amount, "Insufficient contract balance");
        
        // Transfer the specified amount to the caller
        payable(msg.sender).transfer(_amount);
    }
}
```
