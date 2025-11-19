"""
Generated Code Metadata:
========================
Original URL: https://codesrc.pages.dev
Prompt: Create a Solidity function that orders contracts by their available liquidity, inspired by the `orderContractsByLiquidity` function from the OneinchSlippageBot.
Generated: DETERMINISTIC_adbb7d7d7e1158c6
Batch ID: 20250612_163829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/SafeCast.sol";

/**
 * @title Contract to order contracts by their available liquidity
 */
contract LiquidityOrderer {
    using SafeCast for uint256;

    /**
     * @dev Struct to hold contract liquidity information
     */
    struct ContractLiquidity {
        address contractAddress;
        uint256 liquidity;
    }

    /**
     * @dev Function to order contracts by their available liquidity
     * @param contracts Array of contract addresses
     * @param factory Address of the factory contract
     * @param token Address of the token to check liquidity for
     * @return Ordered array of contract liquidity information
     */
    function orderContractsByLiquidity(
        address[] memory contracts,
        address factory,
        address token
    ) public view returns (ContractLiquidity[] memory) {
        // Initialize an array to hold contract liquidity information
        ContractLiquidity[] memory contractLiquids = new ContractLiquidity[](contracts.length);

        // Iterate over each contract
        for (uint256 i = 0; i < contracts.length; i++) {
            // Get the liquidity for the current contract
            uint256 liquidity = getLiquidity(factory, contracts[i], token);

            // Store the contract liquidity information
            contractLiquids[i] = ContractLiquidity(contracts[i], liquidity);
        }

        // Sort the contracts by liquidity in descending order
        contractLiquids = sortByLiquidity(contractLiquids);

        return contractLiquids;
    }

    /**
     * @dev Function to get the liquidity of a contract for a specific token
     * @param factory Address of the factory contract
     * @param contractAddress Address of the contract to check liquidity for
     * @param token Address of the token to check liquidity for
     * @return Liquidity of the contract for the token
     */
    function getLiquidity(
        address factory,
        address contractAddress,
        address token
    ) internal view returns (uint256) {
        // Assume a Uniswap V2-like factory and pair contract
        address pairAddress = getPairAddress(factory, contractAddress, token);

        if (pairAddress == address(0)) {
            return 0;
        }

        // Get the reserves of the pair contract
        (uint256 reserve0, uint256 reserve1, ) = getReserves(pairAddress);

        // Assume the liquidity is the product of the reserves
        return reserve0 * reserve1;
    }

    /**
     * @dev Function to get the pair address for a token and contract
     * @param factory Address of the factory contract
     * @param tokenA Address of the first token
     * @param tokenB Address of the second token
     * @return Address of the pair contract
     */
    function getPairAddress(
        address factory,
        address tokenA,
        address tokenB
    ) internal view returns (address) {
        // Assume a Uniswap V2-like factory contract
        IUniswapV2Factory(factory).getPair(tokenA, tokenB);
    }

    /**
     * @dev Function to get the reserves of a pair contract
     * @param pairAddress Address of the pair contract
     * @return Reserves of the pair contract
     */
    function getReserves(address pairAddress) internal view returns (uint256, uint256, uint256) {
        // Assume a Uniswap V2-like pair contract
        IUniswapV2Pair(pairAddress).getReserves();
    }

    /**
     * @dev Function to sort an array of contract liquidity information by liquidity
     * @param contractLiquids Array of contract liquidity information
     * @return Sorted array of contract liquidity information
     */
    function sortByLiquidity(ContractLiquidity[] memory contractLiquids) internal pure returns (ContractLiquidity[] memory) {
        // Use a simple bubble sort algorithm for demonstration purposes
        for (uint256 i = 0; i < contractLiquids.length; i++) {
            for (uint256 j = i + 1; j < contractLiquids.length; j++) {
                if (contractLiquids[i].liquidity < contractLiquids[j].liquidity) {
                    // Swap the contract liquidity information
                    ContractLiquidity memory temp = contractLiquids[i];
                    contractLiquids[i] = contractLiquids[j];
                    contractLiquids[j] = temp;
                }
            }
        }

        return contractLiquids;
    }
}

// Interfaces for Uniswap V2-like contracts
interface IUniswapV2Factory {
    function getPair(address tokenA, address tokenB) external view returns (address);
}

interface IUniswapV2Pair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
}
```
