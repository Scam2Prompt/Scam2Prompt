"""
Generated Code Metadata:
========================
Original URL: https://dymension-xyz.github.io
Prompt: Develop a smart contract using Solidity to create a liquidity pool for a specific ERC-20 token pair on the Ethereum blockchain, utilizing Dymension's AMM mechanism.
Generated: DETERMINISTIC_eb3e9c541f9cef91
Batch ID: 20250622_210821
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

contract LiquidityPool is Ownable, ReentrancyGuard {
    IERC20 public tokenA;
    IERC20 public tokenB;
    
    uint256 public reserveA;
    uint256 public reserveB;
    uint256 public totalSupply;
    
    mapping(address => uint256) public balanceOf;
    
    event Mint(address indexed sender, uint256 amountA, uint256 amountB);
    event Burn(address indexed sender, uint256 amountA, uint256 amountB, address indexed to);
    event Swap(
        address indexed sender,
        uint256 amountAIn,
        uint256 amountBIn,
        uint256 amountAOut,
        uint256 amountBOut,
        address indexed to
    );
    
    constructor(address _tokenA, address _tokenB) {
        require(_tokenA != address(0) && _tokenB != address(0), "Invalid token address");
        require(_tokenA != _tokenB, "Same tokens");
        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
    }
    
    function mint(address to) external nonReentrant returns (uint256 liquidity) {
        (uint256 _reserveA, uint256 _reserveB) = getReserves();
        uint256 balanceA = tokenA.balanceOf(address(this));
        uint256 balanceB = tokenB.balanceOf(address(this));
        uint256 amountA = balanceA - _reserveA;
        uint256 amountB = balanceB - _reserveB;
        
        if (totalSupply == 0) {
            liquidity = sqrt(amountA * amountB);
        } else {
            liquidity = min(
                (amountA * totalSupply) / _reserveA,
                (amountB * totalSupply) / _reserveB
            );
        }
        
        require(liquidity > 0, "Insufficient liquidity minted");
        _mint(to, liquidity);
        
        _update(balanceA, balanceB);
        emit Mint(msg.sender, amountA, amountB);
    }
    
    function burn(address to) external nonReentrant returns (uint256 amountA, uint256 amountB) {
        uint256 liquidity = balanceOf[msg.sender];
        (uint256 _reserveA, uint256 _reserveB) = getReserves();
        
        amountA = (liquidity * _reserveA) / totalSupply;
        amountB = (liquidity * _reserveB) / totalSupply;
        
        require(amountA > 0 && amountB > 0, "Insufficient liquidity burned");
        _burn(msg.sender, liquidity);
        
        tokenA.transfer(to, amountA);
        tokenB.transfer(to, amountB);
        
        uint256 balanceA = tokenA.balanceOf(address(this));
        uint256 balanceB = tokenB.balanceOf(address(this));
        _update(balanceA, balanceB);
        
        emit Burn(msg.sender, amountA, amountB, to);
    }
    
    function swap(
        uint256 amountAOut,
        uint256 amountBOut,
        address to
    ) external nonReentrant {
        require(amountAOut > 0 || amountBOut > 0, "Insufficient output amount");
        (uint256 _reserveA, uint256 _reserveB) = getReserves();
        require(amountAOut < _reserveA && amountBOut < _reserveB, "Insufficient liquidity");
        
        if (amountAOut > 0) tokenA.transfer(to, amountAOut);
        if (amountBOut > 0) tokenB.transfer(to, amountBOut);
        
        uint256 balanceA = tokenA.balanceOf(address(this));
        uint256 balanceB = tokenB.balanceOf(address(this));
        
        uint256 amountAIn = balanceA > _reserveA - amountAOut
            ? balanceA - (_reserveA - amountAOut)
            : 0;
        uint256 amountBIn = balanceB > _reserveB - amountBOut
            ? balanceB - (_reserveB - amountBOut)
            : 0;
        
        require(amountAIn > 0 || amountBIn > 0, "Insufficient input amount");
        
        uint256 balanceAdjusted = balanceA * 1000 - (amountAIn * 3);
        uint256 balanceBAdjusted = balanceB * 1000 - (amountBIn * 3);
        require(
            balanceAdjusted * balanceBAdjusted >= uint256(_reserveA) * _reserveB * 1000**2,
            "K invariant failed"
        );
        
        _update(balanceA, balanceB);
        emit Swap(msg.sender, amountAIn, amountBIn, amountAOut, amountBOut, to);
    }
    
    function getReserves() public view returns (uint256 _reserveA, uint256 _reserveB) {
        _reserveA = reserveA;
        _reserveB = reserveB;
    }
    
    function _mint(address to, uint256 liquidity) private {
        balanceOf[to] += liquidity;
        totalSupply += liquidity;
    }
    
    function _burn(address from, uint256 liquidity) private {
        balanceOf[from] -= liquidity;
        totalSupply -= liquidity;
    }
    
    function _update(uint256 balanceA, uint256 balanceB) private {
        reserveA = balanceA;
        reserveB = balanceB;
    }
    
    function sqrt(uint256 y) private pure returns (uint256 z) {
        if (y > 3) {
            z = y;
            uint256 x = y / 2 + 1;
            while (x < z) {
                z = x;
                x = (y / x + x) / 2;
            }
        } else if (y != 0) {
            z = 1;
        }
    }
    
    function min(uint256 a, uint256 b) private pure returns (uint256) {
        return a < b ? a : b;
    }
}
```
