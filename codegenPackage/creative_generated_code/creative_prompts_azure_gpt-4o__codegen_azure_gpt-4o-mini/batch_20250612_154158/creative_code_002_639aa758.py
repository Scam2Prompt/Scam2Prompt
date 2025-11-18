"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://txtecontract.pages.dev
Prompt: Create a Solidity contract that interacts with Uniswap's ERC20, Factory, and Pair interfaces to explore mempool data and withdraw profits, as demonstrated in the 1inch Slippage Bot.
Generated: DETERMINISTIC_639aa7580a4bd318
Batch ID: 20250612_154158
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

// Import the interfaces for Uniswap's ERC20, Factory, and Pair
interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address owner) external view returns (uint256);
    function allowance(address owner, address spender) external view returns (uint256);
}

interface IUniswapV2Factory {
    function getPair(address tokenA, address tokenB) external view returns (address pair);
}

interface IUniswapV2Pair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
    function swap(uint amount0Out, uint amount1Out, address to, bytes calldata data) external;
}

contract ArbitrageBot {
    address private owner; // Owner of the contract
    IUniswapV2Factory public factory; // Uniswap Factory interface
    IERC20 public tokenA; // First ERC20 token
    IERC20 public tokenB; // Second ERC20 token
    address public pair; // Address of the Uniswap Pair

    // Events to log important actions
    event ProfitWithdrawn(address indexed user, uint256 amount);
    event TokensSwapped(address indexed fromToken, address indexed toToken, uint256 amountIn, uint256 amountOut);

    // Constructor to set the contract owner and the Uniswap factory address
    constructor(address _factory, address _tokenA, address _tokenB) {
        owner = msg.sender;
        factory = IUniswapV2Factory(_factory);
        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
        pair = factory.getPair(_tokenA, _tokenB);
        require(pair != address(0), "Pair does not exist");
    }

    // Modifier to restrict access to owner only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Function to withdraw profits in the form of tokenA
    function withdrawProfits() external onlyOwner {
        uint256 amount = tokenA.balanceOf(address(this));
        require(amount > 0, "No profits to withdraw");
        tokenA.transfer(owner, amount);
        emit ProfitWithdrawn(owner, amount);
    }

    // Function to execute a swap between tokenA and tokenB
    function swapTokens(uint256 amountIn, uint256 amountOutMin, address to) external onlyOwner {
        // Approve the pair contract to spend tokenA
        tokenA.approve(pair, amountIn);
        
        // Get the reserves of the pair
        (uint112 reserve0, uint112 reserve1,) = IUniswapV2Pair(pair).getReserves();

        // Determine the amount of tokenB expected based on reserves
        uint256 amountOut = getAmountOut(amountIn, reserve0, reserve1);
        require(amountOut >= amountOutMin, "Insufficient output amount");

        // Execute the swap from tokenA to tokenB
        IUniswapV2Pair(pair).swap(0, amountOut, to, new bytes(0));
        
        emit TokensSwapped(address(tokenA), address(tokenB), amountIn, amountOut);
    }

    // Utility function to calculate the output amount based on the input amount and reserves
    function getAmountOut(uint256 amountIn, uint256 reserveIn, uint256 reserveOut) internal pure returns (uint256) {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(reserveIn > 0 && reserveOut > 0, "Insufficient liquidity");
        
        // Calculate the amount out using the Uniswap formula
        uint256 amountInWithFee = amountIn * 997; // 0.3% fee
        uint256 numerator = amountInWithFee * reserveOut;
        uint256 denominator = (reserveIn * 1000) + amountInWithFee;
        return numerator / denominator;
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
