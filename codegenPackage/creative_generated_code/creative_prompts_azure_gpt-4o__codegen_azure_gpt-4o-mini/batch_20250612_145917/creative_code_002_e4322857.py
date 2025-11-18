"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycoded.pages.dev
Prompt: Create a Solidity contract that interacts with the Uniswap V2 Factory and Pair interfaces, using the `WETH_CONTRACT_ADDRESS` and `UNISWAP_CONTRACT_ADDRESS` provided in the Oneinch Slippage Bot example.
Generated: DETERMINISTIC_e4322857ef5451b4
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

// Importing the necessary interfaces
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract UniswapInteraction {
    // Constant for WETH contract address
    address public constant WETH_CONTRACT_ADDRESS = 0xC02aaa39b223FE8D0B0B51bE3E8C8F1bA7bE4D4d; // Example address
    // Constant for Uniswap V2 factory contract address
    address public constant UNISWAP_CONTRACT_ADDRESS = 0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f; // Example address

    // Reference to the Uniswap V2 factory
    IUniswapV2Factory private uniswapFactory;

    // Constructor to initialize the factory interface
    constructor() {
        uniswapFactory = IUniswapV2Factory(UNISWAP_CONTRACT_ADDRESS);
    }

    /**
     * @dev Creates a new Uniswap pair for the given tokens
     * @param tokenA Address of the first token
     * @param tokenB Address of the second token
     * @return pairAddress Address of the newly created pair
     */
    function createPair(address tokenA, address tokenB) external returns (address pairAddress) {
        require(tokenA != tokenB, "Identical addresses");
        require(tokenA != address(0) && tokenB != address(0), "Zero address");
        
        // Create the pair and return the address
        pairAddress = uniswapFactory.createPair(tokenA, tokenB);
        require(pairAddress != address(0), "Pair creation failed");
    }

    /**
     * @dev Gets the address of the Uniswap pair for the given tokens
     * @param tokenA Address of the first token
     * @param tokenB Address of the second token
     * @return pairAddress Address of the existing pair
     */
    function getPair(address tokenA, address tokenB) external view returns (address pairAddress) {
        pairAddress = uniswapFactory.getPair(tokenA, tokenB);
        require(pairAddress != address(0), "Pair does not exist");
    }

    /**
     * @dev Swaps a specified amount of WETH for another token in a given pair
     * @param pairAddress Address of the Uniswap pair
     * @param amountIn Amount of WETH to swap
     * @param amountOutMin Minimum amount of tokens to receive
     */
    function swapWETHForToken(
        address pairAddress,
        uint256 amountIn,
        uint256 amountOutMin
    ) external {
        require(amountIn > 0, "Amount in must be greater than zero");

        IUniswapV2Pair pair = IUniswapV2Pair(pairAddress);
        address tokenOut = pair.token0() == WETH_CONTRACT_ADDRESS ? pair.token1() : pair.token0();

        // Transfer WETH from user to this contract
        IERC20(WETH_CONTRACT_ADDRESS).transferFrom(msg.sender, address(this), amountIn);

        // Approve the pair contract to spend WETH
        IERC20(WETH_CONTRACT_ADDRESS).approve(pairAddress, amountIn);

        // Perform the swap
        pair.swap(0, amountOutMin, msg.sender, new bytes(0));
    }
}
```
