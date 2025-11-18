"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichainclaimairdrop.pages.dev
Prompt: Write a smart contract that integrates Chainlink's Compute Functions to perform off-chain computation and return results on-chain.
Generated: DETERMINISTIC_e405488a9b25fa4d
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

// Import the necessary interfaces from Chainlink
import "@chainlink/contracts/src/v0.8/interfaces/ChainlinkRequestInterface.sol";
import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";

// The OffChainComputation contract uses Chainlink to perform off-chain computation
contract OffChainComputation is ChainlinkClient {
    using Chainlink for Chainlink.Request;

    // Define state variables
    address private oracle; // The address of the Chainlink oracle
    bytes32 private jobId; // The job ID for the off-chain computation
    uint256 private fee; // The fee required to pay for the Chainlink request
    uint256 public result; // The result of the off-chain computation

    // Event emitted when the computation result is received
    event ComputationResult(uint256 indexed result);

    // Constructor to initialize the contract with Oracle details
    constructor(address _oracle, bytes32 _jobId, uint256 _fee) {
        setChainlinkOracle(_oracle);
        jobId = _jobId;
        fee = _fee;
    }

    // Request off-chain computation
    function requestComputation(uint256 input) public {
        // Create a Chainlink request for the specific job ID
        Chainlink.Request memory req = buildChainlinkRequest(jobId, address(this), this.fulfill.selector);
        
        // Add input data to the request
        req.addUint("input", input);
        
        // Send the request to the Chainlink oracle
        sendChainlinkRequest(req, fee);
    }

    // Callback function to receive the result from the off-chain computation
    function fulfill(bytes32 _requestId, uint256 _result) public recordChainlinkFulfillment(_requestId) {
        result = _result; // Store the result on-chain
        emit ComputationResult(result); // Emit an event with the result
    }

    // Withdraw LINK tokens from the contract (for administrative purposes)
    function withdrawLINK() public {
        require(LINK.balanceOf(address(this)) >= 0, "No LINK tokens to withdraw");
        require(msg.sender == oracle, "Only oracle can withdraw LINK");
        LINK.transfer(msg.sender, LINK.balanceOf(address(this))); // Transfer LINK to the oracle
    }
}
```
