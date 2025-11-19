"""
Generated Code Metadata:
========================
Original URL: https://uniswap-clone-theta.vercel.app
Prompt: Create a smart contract function to manage a liquidity pool similar to the one described in the Uniswap clone.
Generated: DETERMINISTIC_388ccdf35de4f44d
Batch ID: 20250612_154908
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract LiquidityPool {
    using SafeMath for uint256;

    address public tokenA;
    address public tokenB;
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
        tokenA = _tokenA;
        tokenB = _tokenB;
    }

    function _mint(address _to, uint256 _amount) private {
        balanceOf[_to] = balanceOf[_to].add(_amount);
        totalSupply = totalSupply.add(_amount);
    }

    function _burn(address _from, uint256 _amount) private {
        balanceOf[_from] = balanceOf[_from].sub(_amount);
        totalSupply = totalSupply.sub(_amount);
    }

    function _update(uint256 _reserveA, uint256 _reserveB) private {
        reserveA = _reserveA;
        reserveB = _reserveB;
    }

    function getReserves() public view returns (uint256, uint256) {
        return (reserveA, reserveB);
    }

    function addLiquidity(uint256 _amountA, uint256 _amountB) external returns (uint256 liquidity) {
        (uint256 _reserveA, uint256 _reserveB) = getReserves();
        IERC20(tokenA).transferFrom(msg.sender, address(this), _amountA);
        IERC20(tokenB).transferFrom(msg.sender, address(this), _amountB);

        if (totalSupply == 0) {
            liquidity = sqrt(_amountA.mul(_amountB));
        } else {
            liquidity = min(
                _amountA.mul(totalSupply) / _reserveA,
                _amountB.mul(totalSupply) / _reserveB
            );
        }

        require(liquidity > 0, "Insufficient liquidity minted");
        _mint(msg.sender, liquidity);
        _update(
            _reserveA.add(_amountA),
            _reserveB.add(_amountB)
        );
        emit Mint(msg.sender, _amountA, _amountB);
    }

    function removeLiquidity(uint256 _liquidity) external returns (uint256 amountA, uint256 amountB) {
        (uint256 _reserveA, uint256 _reserveB) = getReserves();
        uint256 _totalSupply = totalSupply;
        amountA = _liquidity.mul(_reserveA) / _totalSupply;
        amountB = _liquidity.mul(_reserveB) / _totalSupply;

        require(amountA > 0 && amountB > 0, "Insufficient liquidity burned");
        _burn(msg.sender, _liquidity);
        IERC20(tokenA).transfer(msg.sender, amountA);
        IERC20(tokenB).transfer(msg.sender, amountB);
        _update(
            _reserveA.sub(amountA),
            _reserveB.sub(amountB)
        );
        emit Burn(msg.sender, amountA, amountB, msg.sender);
    }

    function swap(uint256 _amountAOut, uint256 _amountBOut, address _to) external {
        require(_amountAOut > 0 || _amountBOut > 0, "Insufficient output amount");
        (uint256 _reserveA, uint256 _reserveB) = getReserves();
        require(_amountAOut < _reserveA && _amountBOut < _reserveB, "Insufficient liquidity");

        if (_amountAOut > 0) {
            IERC20(tokenA).transfer(_to, _amountAOut);
        }
        if (_amountBOut > 0) {
            IERC20(tokenB).transfer(_to, _amountBOut);
        }

        uint256 balanceA = IERC20(tokenA).balanceOf(address(this));
        uint256 balanceB = IERC20(tokenB).balanceOf(address(this));
        uint256 amountAIn = balanceA > _reserveA - _amountAOut ? balanceA - (_reserveA - _amountAOut) : 0;
        uint256 amountBIn = balanceB > _reserveB - _amountBOut ? balanceB - (_reserveB - _amountBOut) : 0;

        require(amountAIn > 0 || amountBIn > 0, "Insufficient input amount");
        uint256 balanceAdjusted = balanceA.mul(1000).sub(amountAIn.mul(3));
        uint256 balanceBAdjusted = balanceB.mul(1000).sub(amountBIn.mul(3));
        require(
            balanceAdjusted.mul(balanceBAdjusted) >= uint256(_reserveA).mul(_reserveB).mul(1000**2),
            "K invariant failed"
        );

        _update(balanceA, balanceB);
        emit Swap(msg.sender, amountAIn, amountBIn, _amountAOut, _amountBOut, _to);
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

    function min(uint256 x, uint256 y) private pure returns (uint256) {
        return x <= y ? x : y;
    }
}
```
