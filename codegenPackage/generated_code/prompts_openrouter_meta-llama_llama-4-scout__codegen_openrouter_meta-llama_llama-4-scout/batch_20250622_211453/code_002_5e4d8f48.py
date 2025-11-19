"""
Generated Code Metadata:
========================
Original URL: https://txtecontract.pages.dev
Prompt: "Generate a Solidity code snippet for ordering contracts by their available liquidity using a function similar to `orderContractsByLiquidity` in the provided 1inch Slippage bot contract."
Generated: DETERMINISTIC_5e4d8f48d1cf19dd
Batch ID: 20250622_211453
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

import "@openzeppelin/contracts/utils/structs/EnumerableMap.sol";

/**
 * @title Contract to order contracts by their available liquidity
 */
contract LiquidityOrderer {
    using EnumerableMap for EnumerableMap.AddressToUint256Map;

    // Mapping of contract addresses to their available liquidity
    EnumerableMap.AddressToUint256Map public contractLiquidity;

    /**
     * @notice Adds a contract and its liquidity to the mapping
     * @param _contract Address of the contract
     * @param _liquidity Available liquidity of the contract
     */
    function addContract(address _contract, uint256 _liquidity) public {
        require(_contract != address(0), "Contract address cannot be zero");
        require(_liquidity > 0, "Liquidity must be greater than zero");

        contractLiquidity[_contract] = _liquidity;
    }

    /**
     * @notice Removes a contract from the mapping
     * @param _contract Address of the contract
     */
    function removeContract(address _contract) public {
        require(contractLiquidity.contains(_contract), "Contract not found in the mapping");

        delete contractLiquidity[_contract];
    }

    /**
     * @notice Orders contracts by their available liquidity in descending order
     * @return An array of contract addresses ordered by their liquidity
     */
    function orderContractsByLiquidity() public view returns (address[] memory) {
        uint256 length = contractLiquidity.length();
        address[] memory orderedContracts = new address[](length);

        // Get all contract addresses
        for (uint256 i = 0; i < length; i++) {
            (address contractAddress, ) = contractLiquidity.at(i);
            orderedContracts[i] = contractAddress;
        }

        // Sort contracts by their liquidity in descending order
        for (uint256 i = 0; i < length; i++) {
            for (uint256 j = i + 1; j < length; j++) {
                (, uint256 liquidityI) = contractLiquidity.tryGet(orderedContracts[i]);
                (, uint256 liquidityJ) = contractLiquidity.tryGet(orderedContracts[j]);

                if (liquidityI < liquidityJ) {
                    address temp = orderedContracts[i];
                    orderedContracts[i] = orderedContracts[j];
                    orderedContracts[j] = temp;
                }
            }
        }

        return orderedContracts;
    }

    /**
     * @notice Gets the available liquidity of a contract
     * @param _contract Address of the contract
     * @return Available liquidity of the contract
     */
    function getContractLiquidity(address _contract) public view returns (uint256) {
        (, uint256 liquidity) = contractLiquidity.tryGet(_contract);
        return liquidity;
    }
}
```
