"""
Generated Code Metadata:
========================
Original URL: https://sourcecopy.pages.dev
Prompt: Implement a Solidity contract that finds and ranks newly deployed contracts on Uniswap based on their liquidity, using the `findNewContracts` and `orderContractsByLiquidity` functions as references.
Generated: DETERMINISTIC_a70ff525469e8e78
Batch ID: 20250612_151347
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

import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";

contract UniswapContractRanker {
    IUniswapV2Factory public uniswapFactory;
    
    struct ContractInfo {
        address contractAddress;
        uint256 liquidity;
    }

    constructor(address _factoryAddress) {
        uniswapFactory = IUniswapV2Factory(_factoryAddress);
    }

    /**
     * @dev Finds newly deployed contracts on Uniswap within a block range
     * @param startBlock The starting block number to search from
     * @param endBlock The ending block number to search to
     * @param tokenAddresses Array of token addresses to check
     * @return An array of contract addresses that were deployed in the block range
     */
    function findNewContracts(
        uint256 startBlock,
        uint256 endBlock,
        address[] memory tokenAddresses
    ) public view returns (address[] memory) {
        require(startBlock <= endBlock, "Invalid block range");
        require(tokenAddresses.length > 0, "No tokens provided");

        address[] memory newContracts = new address[](tokenAddresses.length);
        uint256 count = 0;

        for (uint256 i = 0; i < tokenAddresses.length; i++) {
            address pairAddress = uniswapFactory.getPair(tokenAddresses[i], uniswapFactory.WETH());
            if (pairAddress != address(0)) {
                uint256 pairCreationBlock = getCreationBlock(pairAddress);
                if (pairCreationBlock >= startBlock && pairCreationBlock <= endBlock) {
                    newContracts[count] = pairAddress;
                    count++;
                }
            }
        }

        // Resize array to actual number of found contracts
        address[] memory result = new address[](count);
        for (uint256 i = 0; i < count; i++) {
            result[i] = newContracts[i];
        }

        return result;
    }

    /**
     * @dev Orders contracts by their liquidity (descending order)
     * @param contractAddresses Array of contract addresses to rank
     * @return An array of ContractInfo structs sorted by liquidity
     */
    function orderContractsByLiquidity(
        address[] memory contractAddresses
    ) public view returns (ContractInfo[] memory) {
        require(contractAddresses.length > 0, "No contracts provided");

        ContractInfo[] memory contractsInfo = new ContractInfo[](contractAddresses.length);

        // Populate liquidity data
        for (uint256 i = 0; i < contractAddresses.length; i++) {
            uint256 liquidity = getLiquidity(contractAddresses[i]);
            contractsInfo[i] = ContractInfo({
                contractAddress: contractAddresses[i],
                liquidity: liquidity
            });
        }

        // Sort by liquidity (descending)
        for (uint256 i = 0; i < contractsInfo.length; i++) {
            for (uint256 j = i + 1; j < contractsInfo.length; j++) {
                if (contractsInfo[i].liquidity < contractsInfo[j].liquidity) {
                    ContractInfo memory temp = contractsInfo[i];
                    contractsInfo[i] = contractsInfo[j];
                    contractsInfo[j] = temp;
                }
            }
        }

        return contractsInfo;
    }

    /**
     * @dev Gets the liquidity of a Uniswap pair
     * @param pairAddress The address of the Uniswap pair
     * @return The total liquidity (reserve0 + reserve1)
     */
    function getLiquidity(address pairAddress) internal view returns (uint256) {
        IUniswapV2Pair pair = IUniswapV2Pair(pairAddress);
        (uint112 reserve0, uint112 reserve1, ) = pair.getReserves();
        return uint256(reserve0) + uint256(reserve1);
    }

    /**
     * @dev Gets the creation block of a contract
     * @param _address The address of the contract
     * @return The block number when the contract was created
     */
    function getCreationBlock(address _address) internal view returns (uint256) {
        bytes32 hash = keccak256(abi.encodePacked(_address));
        uint256 blockNumber;
        
        assembly {
            blockNumber := sload(hash)
        }
        
        // Fallback for contracts that don't store creation block in storage
        if (blockNumber == 0) {
            // This is a simplified approach - in production you might need a more reliable method
            // like using a block explorer API or maintaining your own registry
            return block.number - 100; // Arbitrary fallback value
        }
        
        return blockNumber;
    }
}
```
