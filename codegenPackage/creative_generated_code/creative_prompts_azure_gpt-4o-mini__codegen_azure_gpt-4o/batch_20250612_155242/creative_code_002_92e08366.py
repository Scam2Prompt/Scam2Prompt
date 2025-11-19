"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedtylerxyz.pages.dev
Prompt: What are the steps to create a smart contract that facilitates the purchase of $TYLER tokens on Uniswap?
Generated: DETERMINISTIC_92e08366142124b2
Batch ID: 20250612_155242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Ethereum smart contract written in Solidity that facilitates the purchase of `$TYLER` tokens on Uniswap:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing required interfaces from Uniswap
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TylerTokenBuyer is Ownable {
    // Address of the Uniswap Router
    address public uniswapRouterAddress;
    IUniswapV2Router02 public uniswapRouter;

    // Address of the $TYLER token
    address public tylerTokenAddress;
    IERC20 public tylerToken;

    constructor(address _uniswapRouter, address _tylerToken) {
        require(_uniswapRouter != address(0), "Invalid Uniswap router address");
        require(_tylerToken != address(0), "Invalid TYLER token address");

        uniswapRouterAddress = _uniswapRouter;
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);

        tylerTokenAddress = _tylerToken;
        tylerToken = IERC20(_tylerToken);
    }

    /**
     * @notice Facilitates the purchase of $TYLER tokens on Uniswap using ETH.
     * @param minTokensOut The minimum amount of $TYLER tokens the user expects to receive.
     */
    function buyTylerTokens(uint256 minTokensOut) external payable {
        require(msg.value > 0, "ETH amount must be greater than zero");

        // Path for the token swap: ETH -> $TYLER token
        address[] memory path = new address[](2);
        path[0] = uniswapRouter.WETH(); // Native token (ETH/WETH)
        path[1] = tylerTokenAddress;

        // Execute the swap using Uniswap
        uniswapRouter.swapExactETHForTokens{value: msg.value}(
            minTokensOut, // Minimum tokens to receive
            path,         // Swap path
            msg.sender,   // Send tokens directly to the buyer
            block.timestamp + 300 // Deadline: 5 minutes from now
        );
    }

    /**
     * @notice Withdraw any ETH accidentally sent to the contract.
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        (bool success, ) = payable(owner()).call{value: balance}("");
        require(success, "ETH withdrawal failed");
    }

    /**
     * @notice Withdraw any $TYLER tokens accidentally sent to the contract.
     */
    function withdrawTylerTokens() external onlyOwner {
        uint256 balance = tylerToken.balanceOf(address(this));
        require(balance > 0, "No $TYLER tokens to withdraw");
        require(tylerToken.transfer(owner(), balance), "Token withdrawal failed");
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```

### Notes:
1. Replace `@uniswap/v2-periphery` and `@uniswap/v2-core` with the actual paths based on your setup or package manager.
2. Deploy this contract with the appropriate Uniswap Router and `$TYLER` token addresses. Ensure the `$TYLER` token is listed on Uniswap.
3. Test thoroughly in a development environment before deploying to production.
