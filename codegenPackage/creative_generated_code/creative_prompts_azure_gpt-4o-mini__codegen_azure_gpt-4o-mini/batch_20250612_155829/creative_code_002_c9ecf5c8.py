"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://txtecontract.pages.dev
Prompt: Generate a Solidity function that orders contracts by their available liquidity, using the logic from the `orderContractsByLiquidity` function found in the OneinchSlippageBot code.
Generated: DETERMINISTIC_c9ecf5c83ab7f792
Batch ID: 20250612_155829
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
    // Structure to hold contract information
    struct ContractInfo {
        address contractAddress;  // Address of the contract
        uint256 availableLiquidity; // Available liquidity in the contract
    }

    // Array to store contract information
    ContractInfo[] private contracts;

    // Event to emit when contracts are ordered
    event ContractsOrdered(ContractInfo[] orderedContracts);

    /**
     * @dev Adds a contract and its available liquidity to the list.
     * @param _contractAddress The address of the contract to add.
     * @param _liquidity The available liquidity of the contract.
     */
    function addContract(address _contractAddress, uint256 _liquidity) external {
        require(_contractAddress != address(0), "Invalid contract address");
        require(_liquidity > 0, "Liquidity must be greater than zero");

        contracts.push(ContractInfo({
            contractAddress: _contractAddress,
            availableLiquidity: _liquidity
        }));
    }

    /**
     * @dev Orders contracts by their available liquidity in descending order.
     * @return orderedContracts An array of ordered contract information.
     */
    function orderContractsByLiquidity() external returns (ContractInfo[] memory) {
        uint256 length = contracts.length;

        // Perform a simple bubble sort to order contracts by liquidity
        for (uint256 i = 0; i < length; i++) {
            for (uint256 j = 0; j < length - 1; j++) {
                if (contracts[j].availableLiquidity < contracts[j + 1].availableLiquidity) {
                    // Swap contracts
                    ContractInfo memory temp = contracts[j];
                    contracts[j] = contracts[j + 1];
                    contracts[j + 1] = temp;
                }
            }
        }

        emit ContractsOrdered(contracts);
        return contracts;
    }

    /**
     * @dev Gets the list of contracts with their available liquidity.
     * @return contractsList An array of contract info.
     */
    function getContracts() external view returns (ContractInfo[] memory) {
        return contracts;
    }
}
```
