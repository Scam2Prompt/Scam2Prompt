"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycoded.pages.dev
Prompt: Implement a Solidity function that orders contracts by their available liquidity using the `orderContractsByLiquidity` logic from the Oneinch Slippage Bot code.
Generated: DETERMINISTIC_24c95b709c5cad56
Batch ID: 20250612_145917
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

/**
 * @title LiquidityOrdering
 * @dev A contract to order other contracts by their available liquidity.
 */
contract LiquidityOrdering {
    struct ContractLiquidity {
        address contractAddress; // Address of the contract
        uint256 liquidity;       // Available liquidity of the contract
    }

    /**
     * @dev Orders an array of contracts by their liquidity in descending order.
     * @param contracts An array of contract addresses to be ordered.
     * @param liquidityProvider Function signature to query liquidity from each contract.
     * @return sortedContracts An array of contract addresses sorted by liquidity.
     */
    function orderContractsByLiquidity(
        address[] memory contracts,
        bytes4 liquidityProvider
    ) external view returns (address[] memory sortedContracts) {
        require(contracts.length > 0, "No contracts provided");

        // Array to hold contract liquidity data
        ContractLiquidity[] memory liquidityData = new ContractLiquidity[](contracts.length);

        // Fetch liquidity for each contract
        for (uint256 i = 0; i < contracts.length; i++) {
            address contractAddress = contracts[i];
            uint256 liquidity = getLiquidity(contractAddress, liquidityProvider);
            liquidityData[i] = ContractLiquidity(contractAddress, liquidity);
        }

        // Sort the contracts by liquidity in descending order
        for (uint256 i = 0; i < liquidityData.length; i++) {
            for (uint256 j = i + 1; j < liquidityData.length; j++) {
                if (liquidityData[j].liquidity > liquidityData[i].liquidity) {
                    ContractLiquidity memory temp = liquidityData[i];
                    liquidityData[i] = liquidityData[j];
                    liquidityData[j] = temp;
                }
            }
        }

        // Prepare the sorted address array
        sortedContracts = new address[](contracts.length);
        for (uint256 i = 0; i < liquidityData.length; i++) {
            sortedContracts[i] = liquidityData[i].contractAddress;
        }

        return sortedContracts;
    }

    /**
     * @dev Fetches the liquidity of a contract using the provided function signature.
     * @param contractAddress Address of the contract.
     * @param liquidityProvider Function signature to call for liquidity.
     * @return liquidity The liquidity of the contract.
     */
    function getLiquidity(address contractAddress, bytes4 liquidityProvider) internal view returns (uint256 liquidity) {
        require(contractAddress != address(0), "Invalid contract address");
        (bool success, bytes memory data) = contractAddress.staticcall(abi.encodePacked(liquidityProvider));
        require(success, "Failed to fetch liquidity");
        liquidity = abi.decode(data, (uint256));
    }
}
```
