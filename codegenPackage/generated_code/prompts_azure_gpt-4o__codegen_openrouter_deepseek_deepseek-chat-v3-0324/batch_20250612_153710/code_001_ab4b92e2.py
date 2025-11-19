"""
Generated Code Metadata:
========================
Original URL: https://trumpmeme.net
Prompt: Create a Solidity smart contract that integrates with the TRUMP MEME token and allows users to automatically swap ETH for $MEME tokens based on the steps outlined in the "How to Buy" section.
Generated: DETERMINISTIC_ab4b92e2a0ea823c
Batch ID: 20250612_153710
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IUniswapV2Router {
    function swapExactETHForTokens(
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external payable returns (uint[] memory amounts);
}

contract TrumpMemeSwapper is Ownable, ReentrancyGuard {
    IERC20 public memeToken;
    IUniswapV2Router public uniswapRouter;
    
    // Events
    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);
    event RouterUpdated(address newRouter);
    event TokenUpdated(address newToken);

    constructor(address _memeToken, address _uniswapRouter) {
        require(_memeToken != address(0), "Invalid token address");
        require(_uniswapRouter != address(0), "Invalid router address");
        
        memeToken = IERC20(_memeToken);
        uniswapRouter = IUniswapV2Router(_uniswapRouter);
    }

    /**
     * @notice Swap ETH for MEME tokens automatically
     * @param amountOutMin Minimum amount of tokens expected from the swap
     * @param deadline Deadline for the swap transaction
     */
    function swapETHForMeme(uint256 amountOutMin, uint256 deadline) external payable nonReentrant {
        require(msg.value > 0, "Must send ETH to swap");
        require(deadline >= block.timestamp, "Deadline has passed");

        address[] memory path = new address[](2);
        path[0] = uniswapRouter.WETH();
        path[1] = address(memeToken);

        uint256 initialBalance = memeToken.balanceOf(address(this));
        
        // Perform the swap
        uniswapRouter.swapExactETHForTokens{value: msg.value}(
            amountOutMin,
            path,
            address(this),
            deadline
        );

        uint256 tokensReceived = memeToken.balanceOf(address(this)) - initialBalance;
        require(tokensReceived >= amountOutMin, "Insufficient output amount");

        // Transfer tokens to sender
        require(memeToken.transfer(msg.sender, tokensReceived), "Token transfer failed");

        emit TokensPurchased(msg.sender, msg.value, tokensReceived);
    }

    /**
     * @notice Update the Uniswap router address
     * @param newRouter Address of the new router
     */
    function updateRouter(address newRouter) external onlyOwner {
        require(newRouter != address(0), "Invalid router address");
        uniswapRouter = IUniswapV2Router(newRouter);
        emit RouterUpdated(newRouter);
    }

    /**
     * @notice Update the MEME token address
     * @param newToken Address of the new token
     */
    function updateToken(address newToken) external onlyOwner {
        require(newToken != address(0), "Invalid token address");
        memeToken = IERC20(newToken);
        emit TokenUpdated(newToken);
    }

    /**
     * @notice Withdraw any accidentally sent ETH
     */
    function withdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @notice Withdraw any ERC20 tokens (except MEME token) accidentally sent to contract
     * @param token Address of the token to withdraw
     */
    function withdrawERC20(address token) external onlyOwner {
        require(token != address(memeToken), "Cannot withdraw MEME token");
        IERC20(token).transfer(owner(), IERC20(token).balanceOf(address(this)));
    }

    // Fallback function to reject direct ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
