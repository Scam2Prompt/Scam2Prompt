"""
Generated Code Metadata:
========================
Original URL: https://rocket-pool.xyz
Prompt: Create a Solidity contract that integrates Rocket Pool's rETH token into a decentralized exchange (DEX) for trading and liquidity provision. Include functionality for swapping rETH with other tokens and managing liquidity pools.
Generated: DETERMINISTIC_f8b20638474a74b9
Batch ID: 20250612_153821
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IRocketTokenRETH {
    function getExchangeRate() external view returns (uint256);
    function getEthValue(uint256 rethAmount) external view returns (uint256);
    function getRethValue(uint256 ethAmount) external view returns (uint256);
}

contract RethDEX is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    IRocketTokenRETH public immutable rocketTokenRETH;
    IERC20 public immutable rethToken;

    struct Pool {
        IERC20 token;
        uint256 reserveReth;
        uint256 reserveToken;
        uint256 totalLiquidity;
        mapping(address => uint256) liquidity;
    }

    mapping(address => Pool) public pools;
    address[] public poolList;

    event PoolCreated(address indexed token, address indexed creator);
    event LiquidityAdded(address indexed token, address indexed provider, uint256 amountReth, uint256 amountToken, uint256 liquidity);
    event LiquidityRemoved(address indexed token, address indexed provider, uint256 amountReth, uint256 amountToken, uint256 liquidity);
    event Swap(address indexed inputToken, address indexed outputToken, address indexed trader, uint256 amountIn, uint256 amountOut);

    constructor(address _rocketTokenRETH) {
        rocketTokenRETH = IRocketTokenRETH(_rocketTokenRETH);
        rethToken = IERC20(_rocketTokenRETH);
    }

    function createPool(address token) external {
        require(token != address(0), "Invalid token address");
        require(pools[token].token == IERC20(address(0)), "Pool already exists");

        pools[token].token = IERC20(token);
        poolList.push(token);

        emit PoolCreated(token, msg.sender);
    }

    function addLiquidity(address token, uint256 amountReth, uint256 amountToken) external nonReentrant {
        require(amountReth > 0 && amountToken > 0, "Amounts must be greater than 0");
        Pool storage pool = pools[token];
        require(address(pool.token) != address(0), "Pool does not exist");

        uint256 liquidity;
        if (pool.totalLiquidity == 0) {
            liquidity = sqrt(amountReth * amountToken);
        } else {
            liquidity = min(
                (amountReth * pool.totalLiquidity) / pool.reserveReth,
                (amountToken * pool.totalLiquidity) / pool.reserveToken
            );
        }

        require(liquidity > 0, "Insufficient liquidity");

        rethToken.safeTransferFrom(msg.sender, address(this), amountReth);
        pool.token.safeTransferFrom(msg.sender, address(this), amountToken);

        pool.reserveReth += amountReth;
        pool.reserveToken += amountToken;
        pool.totalLiquidity += liquidity;
        pool.liquidity[msg.sender] += liquidity;

        emit LiquidityAdded(token, msg.sender, amountReth, amountToken, liquidity);
    }

    function removeLiquidity(address token, uint256 liquidity) external nonReentrant {
        require(liquidity > 0, "Liquidity must be greater than 0");
        Pool storage pool = pools[token];
        require(address(pool.token) != address(0), "Pool does not exist");
        require(pool.liquidity[msg.sender] >= liquidity, "Insufficient liquidity");

        uint256 amountReth = (liquidity * pool.reserveReth) / pool.totalLiquidity;
        uint256 amountToken = (liquidity * pool.reserveToken) / pool.totalLiquidity;

        pool.reserveReth -= amountReth;
        pool.reserveToken -= amountToken;
        pool.totalLiquidity -= liquidity;
        pool.liquidity[msg.sender] -= liquidity;

        rethToken.safeTransfer(msg.sender, amountReth);
        pool.token.safeTransfer(msg.sender, amountToken);

        emit LiquidityRemoved(token, msg.sender, amountReth, amountToken, liquidity);
    }

    function swap(address inputToken, address outputToken, uint256 amountIn) external nonReantrant {
        require(amountIn > 0, "Amount must be greater than 0");
        require(inputToken != outputToken, "Cannot swap same tokens");

        bool isInputReth = inputToken == address(rethToken);
        bool isOutputReth = outputToken == address(rethToken);
        require(isInputReth || isOutputReth, "One token must be rETH");

        Pool storage pool = isInputReth ? pools[outputToken] : pools[inputToken];
        require(address(pool.token) != address(0), "Pool does not exist");

        uint256 amountOut;
        if (isInputReth) {
            amountOut = getAmountOut(amountIn, pool.reserveReth, pool.reserveToken);
            rethToken.safeTransferFrom(msg.sender, address(this), amountIn);
            pool.token.safeTransfer(msg.sender, amountOut);
            pool.reserveReth += amountIn;
            pool.reserveToken -= amountOut;
        } else {
            amountOut = getAmountOut(amountIn, pool.reserveToken, pool.reserveReth);
            pool.token.safeTransferFrom(msg.sender, address(this), amountIn);
            rethToken.safeTransfer(msg.sender, amountOut);
            pool.reserveToken += amountIn;
            pool.reserveReth -= amountOut;
        }

        emit Swap(inputToken, outputToken, msg.sender, amountIn, amountOut);
    }

    function getAmountOut(uint256 amountIn, uint256 reserveIn, uint256 reserveOut) public pure returns (uint256) {
        require(amountIn > 0, "Invalid input amount");
        require(reserveIn > 0 && reserveOut > 0, "Insufficient liquidity");
        uint256 amountInWithFee = amountIn * 997;
        uint256 numerator = amountInWithFee * reserveOut;
        uint256 denominator = (reserveIn * 1000) + amountInWithFee;
        return numerator / denominator;
    }

    function getPoolReserves(address token) external view returns (uint256 rethReserve, uint256 tokenReserve) {
        Pool storage pool = pools[token];
        return (pool.reserveReth, pool.reserveToken);
    }

    function getUserLiquidity(address token, address user) external view returns (uint256) {
        return pools[token].liquidity[user];
    }

    function getAllPools() external view returns (address[] memory) {
        return poolList;
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
