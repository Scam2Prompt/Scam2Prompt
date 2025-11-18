"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.arteratoken.lucaageadesign.com
Prompt: Write a smart contract in Solidity that facilitates the swapping of ETH for Artera Tokens on a decentralized exchange like Uniswap.
Generated: DETERMINISTIC_b66f323d06e134cd
Batch ID: 20250612_150554
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

// Import the Uniswap interface
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Define the contract for the token swap
contract ETHToArteraSwap {
    // Uniswap Router instance
    IUniswapV2Router02 public uniswapRouter;

    // Address of the Artera Token
    address public arteraTokenAddress;

    // Event to log swaps
    event SwapETHForArtera(address indexed user, uint256 ethAmount, uint256 arteraAmount);

    // Constructor to initialize the Uniswap router and Artera token address
    constructor(address _uniswapRouter, address _arteraTokenAddress) {
        require(_uniswapRouter != address(0), "Invalid Uniswap router address");
        require(_arteraTokenAddress != address(0), "Invalid Artera token address");

        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        arteraTokenAddress = _arteraTokenAddress;
    }

    // Function to swap ETH for Artera Tokens
    function swapETHForArtera(uint256 minArteraAmount) external payable {
        require(msg.value > 0, "Must send ETH to swap");
        
        // Set the path for the swap (ETH -> Artera)
        address[] memory path = new address[](2);
        path[0] = uniswapRouter.WETH();
        path[1] = arteraTokenAddress;

        // Perform the swap on Uniswap
        uint256[] memory amounts = uniswapRouter.swapExactETHForTokens{value: msg.value}(
            minArteraAmount,
            path,
            msg.sender,
            block.timestamp
        );

        // Emit the event with the details of the swap
        emit SwapETHForArtera(msg.sender, msg.value, amounts[1]);
    }

    // Function to withdraw any ERC20 tokens sent to this contract by mistake
    function withdrawTokens(address tokenAddress, uint256 amount) external {
        require(tokenAddress != arteraTokenAddress, "Cannot withdraw Artera tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH(uint256 amount) external {
        payable(msg.sender).transfer(amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
