"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdc.sbs
Prompt: Generate a Solidity smart contract that facilitates swapping ETH for USDC in a DeFi application.
Generated: DETERMINISTIC_e331c610c38acb9e
Batch ID: 20250612_154002
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

/**
 * @title ETH to USDC Swapping Contract
 * @dev This contract allows users to swap ETH for USDC using a decentralized exchange like Uniswap.
 * It uses the Uniswap Router interface to execute token swaps.
 */
interface IUniswapV2Router {
    function swapExactETHForTokens(
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external payable returns (uint[] memory amounts);
}

contract ETHToUSDCDeFiSwap {
    address public owner; // Owner of the contract
    address public immutable uniswapRouterAddress; // Address of Uniswap V2 Router
    address public immutable usdcTokenAddress; // Address of USDC token

    IUniswapV2Router private uniswapRouter;

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with Uniswap Router and USDC token addresses.
     * @param _uniswapRouterAddress Address of the Uniswap V2 Router.
     * @param _usdcTokenAddress Address of the USDC token.
     */
    constructor(address _uniswapRouterAddress, address _usdcTokenAddress) {
        require(_uniswapRouterAddress != address(0), "Uniswap Router address cannot be zero");
        require(_usdcTokenAddress != address(0), "USDC token address cannot be zero");

        owner = msg.sender;
        uniswapRouterAddress = _uniswapRouterAddress;
        usdcTokenAddress = _usdcTokenAddress;
        uniswapRouter = IUniswapV2Router(_uniswapRouterAddress);
    }

    /**
     * @dev Function to swap ETH for USDC using Uniswap.
     * @param amountOutMin Minimum amount of USDC to receive from the swap.
     * @param deadline Deadline by which the swap must be completed.
     */
    function swapETHForUSDC(uint amountOutMin, uint deadline) external payable {
        require(msg.value > 0, "You must send ETH to perform the swap");

        // Define the swap path: ETH -> USDC
        address[] memory path = new address[](2);
        path[0] = uniswapRouter.WETH(); // Wrapped ETH (WETH) address
        path[1] = usdcTokenAddress;

        // Execute the swap
        try uniswapRouter.swapExactETHForTokens{value: msg.value}(
            amountOutMin,
            path,
            msg.sender,
            deadline
        ) {
            // Swap successful
        } catch {
            revert("Swap failed: Check parameters and try again");
        }
    }

    /**
     * @dev Function for the owner to withdraw ETH from the contract.
     * @param amount Amount of ETH to withdraw.
     */
    function withdrawETH(uint amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient contract balance");
        payable(owner).transfer(amount);
    }

    /**
     * @dev Fallback function to receive ETH directly.
     */
    receive() external payable {}

    /**
     * @dev Function to change the contract owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        owner = newOwner;
    }
}
```
