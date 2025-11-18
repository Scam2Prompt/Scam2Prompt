"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge-coin20.pages.dev
Prompt: Write code to launch an ERC-20 token on Uniswap, including liquidity pool provisioning, similar to the DOGE20 roadmap's DEX launch.
Generated: DETERMINISTIC_eaf3737516a5ecda
Batch ID: 20250612_152827
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
 * @title ERC20TokenWithUniswapLaunch
 * @dev A contract that launches an ERC-20 token and sets up a liquidity pool on Uniswap.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract ERC20TokenWithUniswapLaunch is ERC20, Ownable {
    // Address of the Uniswap V2 Router
    IUniswapV2Router02 public uniswapRouter;

    // Address of the pair created on Uniswap
    address public uniswapPair;

    // Track whether liquidity has been added to Uniswap
    bool public liquidityAdded;

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply_,
        address uniswapRouterAddress_
    ) ERC20(name_, symbol_) {
        // Mint the initial supply to the contract deployer
        _mint(msg.sender, initialSupply_);

        // Set the Uniswap V2 Router instance
        uniswapRouter = IUniswapV2Router02(uniswapRouterAddress_);

        liquidityAdded = false; // Liquidity has not been added yet
    }

    /**
     * @notice Adds liquidity to Uniswap for this token and ETH.
     * @dev Requires the contract to hold sufficient tokens and ETH.
     * @param tokenAmount The amount of tokens to add to the liquidity pool.
     */
    function addLiquidity(uint256 tokenAmount) external payable onlyOwner {
        require(!liquidityAdded, "Liquidity already added");

        // Approve the Uniswap Router to spend the token
        _approve(address(this), address(uniswapRouter), tokenAmount);

        // Add liquidity to Uniswap
        (uint256 amountToken, uint256 amountETH, ) = uniswapRouter.addLiquidityETH{
            value: msg.value
        }(
            address(this), // Token address
            tokenAmount,   // Amount of tokens to add
            0,             // Minimum token amount (slippage tolerance)
            0,             // Minimum ETH amount (slippage tolerance)
            owner(),       // Address to receive liquidity tokens
            block.timestamp // Deadline for transaction
        );

        // Ensure liquidity was successfully added
        require(amountToken > 0 && amountETH > 0, "Liquidity addition failed");

        // Update the liquidity-added flag
        liquidityAdded = true;

        // Emit event for liquidity provision
        emit LiquidityAdded(amountToken, amountETH);
    }

    /**
     * @dev Fallback function to receive ETH when sent directly to the contract.
     */
    receive() external payable {}

    /**
     * @notice Event emitted when liquidity is successfully added to Uniswap.
     * @param amountToken The amount of tokens added to the liquidity pool.
     * @param amountETH The amount of ETH added to the liquidity pool.
     */
    event LiquidityAdded(uint256 amountToken, uint256 amountETH);
}
```

### Deployment Notes
1. Deploy the contract with the `name_`, `symbol_`, `initialSupply_`, and `uniswapRouterAddress_` parameters. The `uniswapRouterAddress_` should be the address of the Uniswap V2 Router (e.g., for Ethereum mainnet, `0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D`).
2. Use the `addLiquidity` function to provide initial liquidity. Ensure the contract holds enough tokens and ETH to do so.
