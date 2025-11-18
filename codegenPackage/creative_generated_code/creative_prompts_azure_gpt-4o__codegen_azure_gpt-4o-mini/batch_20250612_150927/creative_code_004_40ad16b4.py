"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allocation-hybrid.pages.dev
Prompt: Write a smart contract that interacts with Hybrid's on-chain intelligence layer to fetch AI-driven insights for Web3 applications.
Generated: DETERMINISTIC_40ad16b49ae7e1a0
Batch ID: 20250612_150927
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

// Interface for Hybrid's on-chain intelligence layer
interface IHybridIntelligence {
    function fetchAIInsights(uint256 queryId) external view returns (string memory);
}

contract Web3Insights {
    // Address of the Hybrid's intelligence layer contract
    IHybridIntelligence private hybridIntelligence;

    // Event emitted when insights are fetched
    event InsightsFetched(uint256 indexed queryId, string insights);

    // Constructor to set the address of the Hybrid's intelligence layer
    constructor(address _hybridIntelligenceAddress) {
        require(_hybridIntelligenceAddress != address(0), "Invalid address");
        hybridIntelligence = IHybridIntelligence(_hybridIntelligenceAddress);
    }

    // Function to fetch AI-driven insights based on a queryId
    function getAIInsights(uint256 queryId) external {
        require(queryId > 0, "Invalid queryId");

        string memory insights;
        
        // Attempt to fetch insights from the Hybrid's intelligence layer
        try hybridIntelligence.fetchAIInsights(queryId) returns (string memory result) {
            insights = result;
        } catch {
            revert("Failed to fetch insights from Hybrid intelligence layer");
        }

        // Emit an event with the fetched insights
        emit InsightsFetched(queryId, insights);
    }
}
```
