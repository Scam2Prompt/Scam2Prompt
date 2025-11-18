"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bsc-info.mdex.com
Prompt: Write a Solidity smart contract example for adding liquidity to Mdex pools on the BSC network.
Generated: DETERMINISTIC_1f9072b82ed0ead2
Batch ID: 20250612_151525
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
 * @title MdexLiquidityAdder
 * @dev A smart contract to add liquidity to Mdex pools on the Binance Smart Chain (BSC).
 * This contract interacts with Mdex's Router for adding liquidity.
 */
interface IMdexRouter {
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB, uint liquidity);

    function WBNB() external pure returns (address);
}

interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract MdexLiquidityAdder {
    address public owner;
    IMdexRouter public mdexRouter;

    // Events for monitoring liquidity addition
    event LiquidityAdded(address indexed user, address tokenA, address tokenB, uint liquidity);

    constructor(address _mdexRouter) {
        require(_mdexRouter != address(0), "Invalid Mdex Router address");
        mdexRouter = IMdexRouter(_mdexRouter);
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    /**
     * @notice Adds liquidity to Mdex pools using the provided token amounts.
     * @param tokenA Address of the first token.
     * @param tokenB Address of the second token.
     * @param amountADesired Desired amount of the first token.
     * @param amountBDesired Desired amount of the second token.
     * @param amountAMin Minimum amount of the first token.
     * @param amountBMin Minimum amount of the second token.
     * @param deadline Deadline timestamp by which the transaction must execute.
     */
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        uint deadline
    ) external {
        require(tokenA != address(0) && tokenB != address(0), "Invalid token addresses");
        require(amountADesired > 0 && amountBDesired > 0, "Invalid token amounts");

        // Transfer tokens from sender to this contract
        IERC20(tokenA).transferFrom(msg.sender, address(this), amountADesired);
        IERC20(tokenB).transferFrom(msg.sender, address(this), amountBDesired);

        // Approve Mdex Router to spend tokens
        IERC20(tokenA).approve(address(mdexRouter), amountADesired);
        IERC20(tokenB).approve(address(mdexRouter), amountBDesired);

        // Add liquidity via Mdex Router
        (uint amountA, uint amountB, uint liquidity) = mdexRouter.addLiquidity(
            tokenA,
            tokenB,
            amountADesired,
            amountBDesired,
            amountAMin,
            amountBMin,
            msg.sender,
            deadline
        );

        // Emit event for logging
        emit LiquidityAdded(msg.sender, tokenA, tokenB, liquidity);
    }

    /**
     * @notice Updates the Mdex Router address. Restricted to the owner.
     * @param _mdexRouter New Mdex Router address.
     */
    function updateRouter(address _mdexRouter) external onlyOwner {
        require(_mdexRouter != address(0), "Invalid Mdex Router address");
        mdexRouter = IMdexRouter(_mdexRouter);
    }

    /**
     * @notice Withdraws ERC20 tokens from the contract. Restricted to the owner.
     * @param token Address of the token to withdraw.
     * @param amount Amount to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Invalid amount");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
