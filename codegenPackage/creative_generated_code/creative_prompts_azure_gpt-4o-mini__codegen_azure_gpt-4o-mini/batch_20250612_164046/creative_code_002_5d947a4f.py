"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycoden.pages.dev
Prompt: Create a function in Solidity that orders contracts by their available liquidity, similar to the `orderContractsByLiquidity` function in the OneinchSlippageBot.
Generated: DETERMINISTIC_5d947a4f410938d4
Batch ID: 20250612_164046
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

contract LiquidityManager {
    struct ContractInfo {
        address contractAddress;
        uint256 liquidity;
    }

    // Array to hold all contracts and their liquidity
    ContractInfo[] private contracts;

    // Event to log the ordered contracts
    event ContractsOrdered(ContractInfo[] orderedContracts);

    /**
     * @dev Adds a new contract to the list with the specified liquidity.
     * @param _contractAddress The address of the contract.
     * @param _liquidity The available liquidity of the contract.
     */
    function addContract(address _contractAddress, uint256 _liquidity) external {
        require(_contractAddress != address(0), "Invalid contract address");
        require(_liquidity > 0, "Liquidity must be greater than zero");

        contracts.push(ContractInfo({
            contractAddress: _contractAddress,
            liquidity: _liquidity
        }));
    }

    /**
     * @dev Orders the contracts by their available liquidity in descending order.
     * Emits a ContractsOrdered event with the ordered contracts.
     */
    function orderContractsByLiquidity() external {
        require(contracts.length > 0, "No contracts to order");

        // Using bubble sort for simplicity, though it's not optimal for large arrays
        for (uint256 i = 0; i < contracts.length; i++) {
            for (uint256 j = 0; j < contracts.length - 1 - i; j++) {
                if (contracts[j].liquidity < contracts[j + 1].liquidity) {
                    // Swap contracts
                    ContractInfo memory temp = contracts[j];
                    contracts[j] = contracts[j + 1];
                    contracts[j + 1] = temp;
                }
            }
        }

        emit ContractsOrdered(contracts);
    }

    /**
     * @dev Retrieves the list of contracts ordered by liquidity.
     * @return An array of ContractInfo structs.
     */
    function getOrderedContracts() external view returns (ContractInfo[] memory) {
        return contracts;
    }
}
```
