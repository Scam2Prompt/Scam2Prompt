"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fliud.io
Prompt: Develop a smart contract that integrates the Instadapp Protocol to multiply FLUID token holdings through lending and borrowing strategies.
Generated: DETERMINISTIC_62de2625f9d092fe
Batch ID: 20250612_154333
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

// Interface for the Instadapp Protocol
interface IInstadapp {
    function supply(address asset, uint256 amount) external;
    function withdraw(address asset, uint256 amount) external;
    function borrow(address asset, uint256 amount) external;
    function repay(address asset, uint256 amount) external;
}

// Smart contract to manage FLUID token lending and borrowing strategies
contract FluidInvestment is Ownable {
    IERC20 public fluidToken;
    IInstadapp public instadapp;
    IUniswapV2Router02 public uniswapRouter;

    // Events for logging actions
    event Supplied(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);

    constructor(
        address _fluidToken,
        address _instadapp,
        address _uniswapRouter
    ) {
        require(_fluidToken != address(0), "Invalid FLUID token address");
        require(_instadapp != address(0), "Invalid Instadapp address");
        require(_uniswapRouter != address(0), "Invalid Uniswap router address");

        fluidToken = IERC20(_fluidToken);
        instadapp = IInstadapp(_instadapp);
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
    }

    // Supply FLUID tokens to Instadapp
    function supplyFLUID(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(fluidToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer FLUID tokens to contract
        fluidToken.transferFrom(msg.sender, address(this), amount);
        // Supply tokens to Instadapp
        instadapp.supply(address(fluidToken), amount);

        emit Supplied(msg.sender, amount);
    }

    // Withdraw FLUID tokens from Instadapp
    function withdrawFLUID(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Withdraw tokens from Instadapp
        instadapp.withdraw(address(fluidToken), amount);
        // Transfer tokens back to owner
        fluidToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Borrow tokens from Instadapp
    function borrowFLUID(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Borrow tokens from Instadapp
        instadapp.borrow(address(fluidToken), amount);

        emit Borrowed(msg.sender, amount);
    }

    // Repay borrowed tokens to Instadapp
    function repayFLUID(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(fluidToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer FLUID tokens to contract
        fluidToken.transferFrom(msg.sender, address(this), amount);
        // Repay tokens to Instadapp
        instadapp.repay(address(fluidToken), amount);

        emit Repaid(msg.sender, amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
