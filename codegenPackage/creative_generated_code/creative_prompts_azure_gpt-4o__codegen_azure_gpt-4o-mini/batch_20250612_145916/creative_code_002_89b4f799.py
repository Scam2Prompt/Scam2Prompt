"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-screator-ethereum-free.pages.dev
Prompt: Provide a Solidity smart contract template for creating a token with full ownership and automatic liquidity pool transfer, as described on the "Tokens Creator" site.
Generated: DETERMINISTIC_89b4f7990cd2e71f
Batch ID: 20250612_145916
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

// Import the OpenZeppelin ERC20 token standard and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Contract for creating a token with ownership and automatic liquidity pool transfer
contract CustomToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Events
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount);

    // Liquidity pool settings
    address public uniswapV2Router; // Address of the Uniswap router for liquidity
    address public uniswapV2Pair; // Address of the Uniswap pair for the token
    bool public isLiquidityAdded; // Flag to check if liquidity is added

    // Constructor to initialize the token
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address _uniswapV2Router
    ) ERC20(name, symbol) {
        // Mint initial supply to the owner
        _mint(msg.sender, initialSupply * (10 ** decimals()));
        
        // Set Uniswap router address
        uniswapV2Router = _uniswapV2Router;
    }

    // Function to add liquidity to the Uniswap pool
    function addLiquidity(uint256 tokenAmount) external payable onlyOwner {
        require(!isLiquidityAdded, "Liquidity has already been added");
        
        // Approve the transfer of tokens to the Uniswap router
        _approve(address(this), uniswapV2Router, tokenAmount);

        // Add the liquidity to the Uniswap pool
        (uint256 amountToken, uint256 amountETH, ) = IUniswapV2Router(uniswapV2Router).addLiquidityETH{value: msg.value}(
            address(this),
            tokenAmount,
            0,
            0,
            owner(),
            block.timestamp
        );

        emit LiquidityAdded(amountToken, amountETH);
        
        // Set liquidity added flag to true
        isLiquidityAdded = true;
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        // Transfer tokens from contract to owner
        require(balanceOf(address(this)) >= amount, "Insufficient token balance");
        _transfer(address(this), msg.sender, amount);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient ETH balance");
        payable(owner()).transfer(amount);
    }

    // Function to receive Ether. msg.data must be empty
    receive() external payable {}

    // Function to fallback on receiving Ether
    fallback() external payable {}
}

// Interface for the Uniswap V2 Router
interface IUniswapV2Router {
    function addLiquidityETH(
        address token,
        uint256 tokenAmount,
        uint256 minToken,
        uint256 minETH,
        address to,
        uint256 deadline
    ) external payable returns (uint256 amountToken, uint256 amountETH, uint256 liquidity);
}
```
