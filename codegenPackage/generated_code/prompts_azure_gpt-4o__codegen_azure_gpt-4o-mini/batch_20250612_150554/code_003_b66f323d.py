"""
Generated Code Metadata:
========================
Original URL: https://www.arteratoken.lucaageadesign.com
Prompt: Write a smart contract in Solidity that facilitates the swapping of ETH for Artera Tokens on a decentralized exchange like Uniswap.
Generated: DETERMINISTIC_b66f323d06e134cd
Batch ID: 20250612_150554
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

// Importing the interface for Uniswap's Router
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract EthToArteraSwap {
    // Address of the Uniswap Router
    IUniswapV2Router02 public uniswapRouter;
    // Address of the Artera Token
    address public arteraTokenAddress;

    // Event to log swaps
    event SwapETHForArtera(address indexed user, uint256 ethAmount, uint256 arteraAmount);

    // Constructor to set the Uniswap Router and Artera Token address
    constructor(address _uniswapRouter, address _arteraTokenAddress) {
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        arteraTokenAddress = _arteraTokenAddress;
    }

    // Function to swap ETH for Artera Tokens
    function swapETHForArtera() external payable {
        require(msg.value > 0, "Must send ETH to swap");

        // Define the path for the swap (ETH -> Artera)
        address[] memory path = new address[](2);
        path[0] = uniswapRouter.WETH(); // Wrapped ETH address
        path[1] = arteraTokenAddress;    // Artera Token address

        // Approve the router to spend the ETH
        // Note: This is not necessary for ETH, but included for clarity
        // (ETH does not require approval)

        // Perform the swap
        uint256[] memory amounts = uniswapRouter.swapExactETHForTokens{value: msg.value}(
            0, // Accept any amount of Artera Tokens
            path,
            msg.sender, // Send tokens to the user
            block.timestamp // Deadline for the swap
        );

        // Emit an event for the swap
        emit SwapETHForArtera(msg.sender, msg.value, amounts[1]);
    }

    // Function to withdraw any tokens accidentally sent to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external {
        require(tokenAddress != arteraTokenAddress, "Cannot withdraw Artera Tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH(uint256 amount) external {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(msg.sender).transfer(amount);
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
