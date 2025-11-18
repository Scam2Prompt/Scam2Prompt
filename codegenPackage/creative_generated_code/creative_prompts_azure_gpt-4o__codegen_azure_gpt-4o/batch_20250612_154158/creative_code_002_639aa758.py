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

// Import interfaces for Uniswap's ERC20, Factory, and Pair contracts
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function totalSupply() external view returns (uint256);
    function decimals() external view returns (uint8);
    function symbol() external view returns (string memory);
}

interface IUniswapV2Factory {
    function getPair(address tokenA, address tokenB) external view returns (address pair);
}

interface IUniswapV2Pair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
    function token0() external view returns (address);
    function token1() external view returns (address);
    function swap(uint amount0Out, uint amount1Out, address to, bytes calldata data) external;
}

contract MempoolExplorerAndProfitWithdrawer {
    address public owner;
    IUniswapV2Factory public uniswapFactory;

    // Event for logging profits withdrawn
    event ProfitsWithdrawn(address indexed to, uint256 amount);

    // Modifier to restrict access
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to set up the contract
    constructor(address _uniswapFactory) {
        require(_uniswapFactory != address(0), "Invalid factory address");
        owner = msg.sender;
        uniswapFactory = IUniswapV2Factory(_uniswapFactory);
    }

    /**
     * @dev Allows the owner to change the Uniswap factory address if needed
     * @param _uniswapFactory The new Uniswap factory address
     */
    function setUniswapFactory(address _uniswapFactory) external onlyOwner {
        require(_uniswapFactory != address(0), "Invalid factory address");
        uniswapFactory = IUniswapV2Factory(_uniswapFactory);
    }

    /**
     * @dev Fetch reserves of a pair
     * @param tokenA Address of the first token
     * @param tokenB Address of the second token
     * @return reserveA Reserve of tokenA
     * @return reserveB Reserve of tokenB
     */
    function getPairReserves(address tokenA, address tokenB) external view returns (uint112 reserveA, uint112 reserveB) {
        address pair = uniswapFactory.getPair(tokenA, tokenB);
        require(pair != address(0), "Pair does not exist");

        IUniswapV2Pair uniPair = IUniswapV2Pair(pair);
        (uint112 reserve0, uint112 reserve1, ) = uniPair.getReserves();

        // Determine which token corresponds to reserve0 and reserve1
        if (uniPair.token0() == tokenA) {
            reserveA = reserve0;
            reserveB = reserve1;
        } else {
            reserveA = reserve1;
            reserveB = reserve0;
        }
    }

    /**
     * @dev Withdraw profits by transferring specified token balance to the owner
     * @param token Address of the ERC20 token to withdraw
     */
    function withdrawProfits(address token) external onlyOwner {
        IERC20 erc20 = IERC20(token);
        uint256 balance = erc20.balanceOf(address(this));
        require(balance > 0, "No balance to withdraw");

        // Transfer profits to the owner
        require(erc20.transfer(owner, balance), "Profit withdrawal failed");

        emit ProfitsWithdrawn(owner, balance);
    }

    /**
     * @dev Allows the contract owner to withdraw ETH
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH balance to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Fallback function to receive ETH
     */
    receive() external payable {}
}
```
