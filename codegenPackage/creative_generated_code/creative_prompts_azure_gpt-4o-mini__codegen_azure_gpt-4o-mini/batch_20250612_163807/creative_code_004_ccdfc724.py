"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://botcodesrc.pages.dev
Prompt: Create a Solidity function that orders contracts by their available liquidity, based on the logic outlined in the OneinchSlippageBot example.
Generated: DETERMINISTIC_ccdfc7243da6a9d5
Batch ID: 20250612_163807
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

interface IToken {
    function balanceOf(address account) external view returns (uint256);
}

interface IExchange {
    function getLiquidity() external view returns (uint256);
}

contract LiquidityManager {
    // Structure to hold contract information
    struct ContractInfo {
        address contractAddress;
        uint256 liquidity;
    }

    // Array to store the ordered contracts
    ContractInfo[] public orderedContracts;

    // Event emitted when contracts are ordered
    event ContractsOrdered(ContractInfo[] orderedContracts);

    // Function to order contracts by their available liquidity
    function orderContractsByLiquidity(address[] calldata contracts) external {
        require(contracts.length > 0, "No contracts provided");

        // Clear previous ordering
        delete orderedContracts;

        // Retrieve liquidity for each contract
        for (uint256 i = 0; i < contracts.length; i++) {
            try IExchange(contracts[i]).getLiquidity() returns (uint256 liquidity) {
                orderedContracts.push(ContractInfo({
                    contractAddress: contracts[i],
                    liquidity: liquidity
                }));
            } catch {
                // If fetching liquidity fails, log a warning and skip the contract
                continue;
            }
        }

        // Sort contracts by liquidity using Bubble Sort for simplicity
        // Note: In production, consider using a more efficient sorting algorithm
        for (uint256 i = 0; i < orderedContracts.length; i++) {
            for (uint256 j = 0; j < orderedContracts.length - 1; j++) {
                if (orderedContracts[j].liquidity < orderedContracts[j + 1].liquidity) {
                    // Swap if the current liquidity is less than the next
                    (orderedContracts[j], orderedContracts[j + 1]) = (orderedContracts[j + 1], orderedContracts[j]);
                }
            }
        }

        // Emit the ordered contracts
        emit ContractsOrdered(orderedContracts);
    }

    // Function to get the ordered contracts
    function getOrderedContracts() external view returns (ContractInfo[] memory) {
        return orderedContracts;
    }
}
```
