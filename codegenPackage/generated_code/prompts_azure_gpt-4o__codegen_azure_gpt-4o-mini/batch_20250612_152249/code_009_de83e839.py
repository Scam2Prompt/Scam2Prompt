"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Use Chainlink's Compute Functions to create a smart contract that aggregates data from multiple APIs and performs on-chain calculations.
Generated: DETERMINISTIC_de83e83976eccab5
Batch ID: 20250612_152249
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

// Importing the Chainlink Compute Functions interface
import "@chainlink/contracts/src/v0.8/interfaces/ChainlinkComputeInterface.sol";

// Define the contract
contract DataAggregator {
    // State variables
    ChainlinkComputeInterface private compute; // Chainlink Compute Functions interface
    address private owner; // Owner of the contract

    // Event to emit when data aggregation is successful
    event DataAggregated(uint256 aggregatedResult);

    // Constructor to initialize the contract
    constructor(address _computeAddress) {
        compute = ChainlinkComputeInterface(_computeAddress);
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Function to aggregate data from multiple APIs
    function aggregateData(string[] memory apiUrls) public onlyOwner returns (bytes32 requestId) {
        // Prepare the request to Chainlink Compute Functions
        // This is a placeholder for the actual API aggregation logic
        // In a real implementation, you would specify the computation and data sources
        requestId = compute.requestData(apiUrls);
    }

    // Callback function to handle the response from Chainlink
    function fulfillDataAggregation(bytes32 requestId, uint256[] memory results) public {
        // Ensure that the request is fulfilled by the Chainlink node
        require(msg.sender == address(compute), "Unauthorized caller");

        // Perform on-chain calculations (e.g., average of results)
        uint256 aggregatedResult = calculateAverage(results);

        // Emit the event with the aggregated result
        emit DataAggregated(aggregatedResult);
    }

    // Internal function to calculate the average of an array of numbers
    function calculateAverage(uint256[] memory numbers) internal pure returns (uint256) {
        require(numbers.length > 0, "No numbers provided");

        uint256 sum = 0;
        for (uint256 i = 0; i < numbers.length; i++) {
            sum += numbers[i];
        }
        return sum / numbers.length; // Return the average
    }

    // Function to withdraw any funds from the contract (if applicable)
    function withdraw() public onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
