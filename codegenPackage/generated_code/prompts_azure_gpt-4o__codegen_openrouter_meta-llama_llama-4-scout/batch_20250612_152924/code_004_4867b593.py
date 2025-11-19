"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20en.pages.dev
Prompt: Write Solidity code for a liquidity provision mechanism that allocates 10% of the DOGE20 token supply to Uniswap, as outlined in the Dogecoin20 roadmap.
Generated: DETERMINISTIC_4867b5931464673e
Batch ID: 20250612_152924
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@uniswap/v2-periphery/contracts/UniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";

contract Dogecoin20 is ERC20, ERC20Burnable, ReentrancyGuard {
    // Uniswap router
    address public uniswapRouterAddress;
    UniswapV2Router02 public uniswapRouter;

    // Uniswap factory
    address public uniswapFactoryAddress;
    IUniswapV2Factory public uniswapFactory;

    // Mapping for liquidity provider
    mapping(address => bool) public liquidityProviders;

    // Percentage of token supply to allocate to Uniswap
    uint256 public constant UNISWAP_ALLOCATION_PERCENTAGE = 10;

    // Token supply allocated to Uniswap
    uint256 public uniswapAllocation;

    // Event emitted when liquidity is provided
    event LiquidityProvided(address indexed provider, uint256 amount);

    // Event emitted when liquidity is removed
    event LiquidityRemoved(address indexed remover, uint256 amount);

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 totalSupply_,
        address uniswapRouterAddress_,
        address uniswapFactoryAddress_
    ) ERC20(name_, symbol_) {
        // Mint total supply
        _mint(msg.sender, totalSupply_);

        // Set Uniswap router and factory addresses
        uniswapRouterAddress = uniswapRouterAddress_;
        uniswapRouter = UniswapV2Router02(uniswapRouterAddress);
        uniswapFactoryAddress = uniswapFactoryAddress_;
        uniswapFactory = IUniswapV2Factory(uniswapFactoryAddress);

        // Calculate Uniswap allocation
        uniswapAllocation = (totalSupply_ * UNISWAP_ALLOCATION_PERCENTAGE) / 100;

        // Approve Uniswap router to spend tokens
        _approve(address(this), uniswapRouterAddress, uniswapAllocation);
    }

    // Function to add liquidity to Uniswap
    function addLiquidity() external nonReentrant {
        // Check if sender is not the contract itself
        require(msg.sender != address(this), "Contract cannot add liquidity");

        // Get current balance of sender
        uint256 balance = balanceOf(msg.sender);

        // Check if sender has sufficient balance
        require(balance > 0, "Insufficient balance");

        // Calculate amount to allocate to Uniswap
        uint256 amountToAllocate = (balance * UNISWAP_ALLOCATION_PERCENTAGE) / 100;

        // Check if amount to allocate is greater than 0
        require(amountToAllocate > 0, "Amount to allocate must be greater than 0");

        // Transfer tokens to Uniswap router
        _transfer(msg.sender, address(this), amountToAllocate);

        // Approve Uniswap router to spend tokens
        _approve(address(this), uniswapRouterAddress, amountToAllocate);

        // Add liquidity to Uniswap
        (uint256 liquidity, ) = uniswapRouter.addLiquidityETH{value: 0}(
            address(this),
            amountToAllocate,
            0,
            0,
            msg.sender,
            block.timestamp
        );

        // Update liquidity provider mapping
        liquidityProviders[msg.sender] = true;

        // Emit event
        emit LiquidityProvided(msg.sender, liquidity);
    }

    // Function to remove liquidity from Uniswap
    function removeLiquidity(uint256 liquidity) external nonReentrant {
        // Check if sender is a liquidity provider
        require(liquidityProviders[msg.sender], "Sender is not a liquidity provider");

        // Get Uniswap pair address
        address pairAddress = uniswapFactory.getPair(address(this), uniswapRouter.WETH());

        // Check if pair exists
        require(pairAddress != address(0), "Pair does not exist");

        // Get liquidity balance of sender
        uint256 senderLiquidity = IUniswapV2Pair(pairAddress).balanceOf(msg.sender);

        // Check if sender has sufficient liquidity
        require(senderLiquidity >= liquidity, "Insufficient liquidity");

        // Remove liquidity from Uniswap
        (uint256 amount0, uint256 amount1) = uniswapRouter.removeLiquidityETH(
            address(this),
            liquidity,
            0,
            0,
            msg.sender,
            block.timestamp
        );

        // Update liquidity provider mapping
        liquidityProviders[msg.sender] = false;

        // Emit event
        emit LiquidityRemoved(msg.sender, liquidity);
    }
}
```
