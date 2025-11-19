"""
Generated Code Metadata:
========================
Original URL: https://automation-feat-front-3795-display-log-tr-chainlinklabs.vercel.app
Prompt: Write a code snippet to retrieve the status and balance of a Chainlink Automation upkeep using the provided registry address.
Generated: DETERMINISTIC_4bc85e3113f0ea87
Batch ID: 20250622_205218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@chainlink/contracts/src/v0.8/interfaces/AutomationRegistryInterface2_0.sol";

contract UpkeepStatusChecker {
    AutomationRegistryInterface2_0 public immutable registry;

    constructor(address _registryAddress) {
        registry = AutomationRegistryInterface2_0(_registryAddress);
    }

    /**
     * @dev Retrieves the status and balance of a Chainlink Automation upkeep
     * @param upkeepId The ID of the upkeep to check
     * @return upkeepNeeded Whether the upkeep is needed
     * @return performData The perform data bytes
     * @return upkeepBalance The current balance of the upkeep
     * @return maxValidBlocknumber The max block number until which the upkeep is valid
     * @return lastPerformBlockNumber The block number when the upkeep was last performed
     */
    function getUpkeepStatus(uint256 upkeepId)
        public
        view
        returns (
            bool upkeepNeeded,
            bytes memory performData,
            uint96 upkeepBalance,
            uint256 maxValidBlocknumber,
            uint256 lastPerformBlockNumber
        )
    {
        (upkeepNeeded, performData) = registry.checkUpkeep(upkeepId);
        
        (
            ,
            upkeepBalance,
            lastPerformBlockNumber,
            maxValidBlocknumber,
            
        ) = registry.getUpkeep(upkeepId);

        return (
            upkeepNeeded,
            performData,
            upkeepBalance,
            maxValidBlocknumber,
            lastPerformBlockNumber
        );
    }

    /**
     * @dev Retrieves only the balance of a Chainlink Automation upkeep
     * @param upkeepId The ID of the upkeep to check
     * @return upkeepBalance The current balance of the upkeep
     */
    function getUpkeepBalance(uint256 upkeepId) public view returns (uint96 upkeepBalance) {
        (, upkeepBalance, , , ) = registry.getUpkeep(upkeepId);
        return upkeepBalance;
    }
}
```
