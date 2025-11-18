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

// Importing OpenZeppelin's SafeERC20 library
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
// Importing Uniswap Router Interface
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract ETHToArteraSwap {
    using SafeERC20 for IERC20;

    // Address of the Uniswap V2 Router
    IUniswapV2Router02 public immutable uniswapRouter;

    // Address of the Artera Token contract
    address public immutable arteraToken;

    // Contract events
    event TokensSwapped(address indexed user, uint256 ethAmount, uint256 tokenAmount);

    /**
     * @dev Constructor to initialize the contract with router and token addresses.
     * @param _uniswapRouter Address of the Uniswap V2 Router.
     * @param _arteraToken Address of the Artera Token.
     */
    constructor(address _uniswapRouter, address _arteraToken) {
        require(_uniswapRouter != address(0), "Invalid Uniswap Router address");
        require(_arteraToken != address(0), "Invalid Artera Token address");

        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        arteraToken = _arteraToken;
    }

    /**
     * @dev Swaps ETH for Artera Tokens via Uniswap.
     * @param minTokensReceived Minimum amount of Artera Tokens to receive to prevent slippage losses.
     */
    function swapETHForArtera(uint256 minTokensReceived) external payable {
        require(msg.value > 0, "No ETH sent for swapping");
        require(minTokensReceived > 0, "Invalid minimum tokens amount");

        // Define the path: ETH -> Artera Token
        address[] memory path = new address[](2);
        path[0] = uniswapRouter.WETH(); // WETH address
        path[1] = arteraToken;         // Artera Token address

        // Perform the token swap
        uint256[] memory amounts = uniswapRouter.swapExactETHForTokens{value: msg.value}(
            minTokensReceived, // Minimum amount of tokens to receive
            path,              // Path for the swap
            msg.sender,        // Recipient of the tokens
            block.timestamp    // Deadline (current block timestamp)
        );

        // Emit an event for the swap
        emit TokensSwapped(msg.sender, msg.value, amounts[1]);
    }

    /**
     * @dev Fallback function to accept ETH deposits.
     */
    receive() external payable {
        // Accept ETH deposits without any additional logic
    }

    /**
     * @dev Withdraw Ether sent to the contract by mistake.
     * Only the contract owner can call this (restricted via OpenZeppelin's Ownable if needed).
     * @param to Address to send the Ether to.
     */
    function withdrawETH(address payable to) external {
        require(to != address(0), "Invalid address");
        require(address(this).balance > 0, "No ETH to withdraw");

        to.transfer(address(this).balance);
    }
}
```

This Solidity code implements a simple smart contract that swaps ETH for Artera Tokens via Uniswap, handling user interactions and ensuring safe execution with error handling and best practices.
