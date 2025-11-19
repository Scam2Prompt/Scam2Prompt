"""
Generated Code Metadata:
========================
Original URL: https://bafybeiewx4e2pncoxcrbd57xruotistqgiyxfakla3tb5qfpwkazlkrize.ipfs.dweb.link
Prompt: Write a smart contract in Solidity that implements ecosystem-owned liquidity on a layer 1 blockchain, referencing Mitosis as a use case.
Generated: DETERMINISTIC_eda522ceaabdd3ac
Batch ID: 20250622_205111
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

/**
 * @title EcosystemOwnedLiquidity
 * @dev Implements ecosystem-owned liquidity mechanism inspired by Mitosis
 */
contract EcosystemOwnedLiquidity is Ownable, ReentrancyGuard {
    // Token pair structure
    struct TokenPair {
        address tokenA;
        address tokenB;
        uint256 reserveA;
        uint256 reserveB;
        uint256 totalLiquidity;
    }

    // Liquidity provider information
    struct ProviderInfo {
        uint256 liquidity;
        uint256 timestamp;
    }

    // Mapping of token pairs
    mapping(bytes32 => TokenPair) public tokenPairs;

    // Mapping of liquidity providers
    mapping(address => mapping(bytes32 => ProviderInfo)) public providers;

    // Protocol fee percentage (basis points)
    uint256 public protocolFeeBps = 30; // 0.3%

    // Events
    event PairCreated(bytes32 indexed pairHash, address tokenA, address tokenB);
    event LiquidityAdded(
        bytes32 indexed pairHash,
        address provider,
        uint256 amountA,
        uint256 amountB,
        uint256 liquidity
    );
    event LiquidityRemoved(
        bytes32 indexed pairHash,
        address provider,
        uint256 amountA,
        uint256 amountB,
        uint256 liquidity
    );
    event Swapped(
        bytes32 indexed pairHash,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOut,
        uint256 protocolFee
    );

    /**
     * @dev Creates a new token pair
     * @param tokenA Address of first token
     * @param tokenB Address of second token
     */
    function createPair(address tokenA, address tokenB) external onlyOwner {
        require(tokenA != tokenB, "EOL: identical addresses");
        require(tokenA != address(0) && tokenB != address(0), "EOL: zero address");

        bytes32 pairHash = keccak256(abi.encodePacked(tokenA, tokenB));
        require(tokenPairs[pairHash].tokenA == address(0), "EOL: pair exists");

        tokenPairs[pairHash] = TokenPair({
            tokenA: tokenA,
            tokenB: tokenB,
            reserveA: 0,
            reserveB: 0,
            totalLiquidity: 0
        });

        emit PairCreated(pairHash, tokenA, tokenB);
    }

    /**
     * @dev Adds liquidity to a token pair
     * @param tokenA Address of first token
     * @param tokenB Address of second token
     * @param amountADesired Amount of tokenA to add
     * @param amountBDesired Amount of tokenB to add
     */
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint256 amountADesired,
        uint256 amountBDesired
    ) external nonReentrant {
        bytes32 pairHash = keccak256(abi.encodePacked(tokenA, tokenB));
        TokenPair storage pair = tokenPairs[pairHash];
        require(pair.tokenA != address(0), "EOL: pair doesn't exist");

        IERC20(tokenA).transferFrom(msg.sender, address(this), amountADesired);
        IERC20(tokenB).transferFrom(msg.sender, address(this), amountBDesired);

        uint256 liquidity;
        if (pair.totalLiquidity == 0) {
            liquidity = sqrt(amountADesired * amountBDesired);
        } else {
            uint256 liquidityA = (amountADesired * pair.totalLiquidity) / pair.reserveA;
            uint256 liquidityB = (amountBDesired * pair.totalLiquidity) / pair.reserveB;
            liquidity = (liquidityA < liquidityB) ? liquidityA : liquidityB;
        }

        require(liquidity > 0, "EOL: insufficient liquidity");

        pair.reserveA += amountADesired;
        pair.reserveB += amountBDesired;
        pair.totalLiquidity += liquidity;

        ProviderInfo storage provider = providers[msg.sender][pairHash];
        provider.liquidity += liquidity;
        provider.timestamp = block.timestamp;

        emit LiquidityAdded(pairHash, msg.sender, amountADesired, amountBDesired, liquidity);
    }

    /**
     * @dev Removes liquidity from a token pair
     * @param tokenA Address of first token
     * @param tokenB Address of second token
     * @param liquidity Amount of liquidity to remove
     */
    function removeLiquidity(
        address tokenA,
        address tokenB,
        uint256 liquidity
    ) external nonReentrant {
        bytes32 pairHash = keccak256(abi.encodePacked(tokenA, tokenB));
        TokenPair storage pair = tokenPairs[pairHash];
        require(pair.tokenA != address(0), "EOL: pair doesn't exist");

        ProviderInfo storage provider = providers[msg.sender][pairHash];
        require(provider.liquidity >= liquidity, "EOL: insufficient liquidity");

        uint256 amountA = (liquidity * pair.reserveA) / pair.totalLiquidity;
        uint256 amountB = (liquidity * pair.reserveB) / pair.totalLiquidity;

        pair.reserveA -= amountA;
        pair.reserveB -= amountB;
        pair.totalLiquidity -= liquidity;
        provider.liquidity -= liquidity;

        IERC20(tokenA).transfer(msg.sender, amountA);
        IERC20(tokenB).transfer(msg.sender, amountB);

        emit LiquidityRemoved(pairHash, msg.sender, amountA, amountB, liquidity);
    }

    /**
     * @dev Swaps tokens in a pair
     * @param tokenIn Address of input token
     * @param tokenOut Address of output token
     * @param amountIn Amount of input token
     * @param minAmountOut Minimum amount of output token expected
     */
    function swap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut
    ) external nonReentrant {
        bytes32 pairHash = keccak256(abi.encodePacked(tokenIn, tokenOut));
        TokenPair storage pair = tokenPairs[pairHash];
        require(pair.tokenA != address(0), "EOL: pair doesn't exist");

        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        uint256 reserveIn;
        uint256 reserveOut;
        if (tokenIn == pair.tokenA) {
            reserveIn = pair.reserveA;
            reserveOut = pair.reserveB;
        } else {
            reserveIn = pair.reserveB;
            reserveOut = pair.reserveA;
        }

        uint256 amountInWithFee = amountIn * (10000 - protocolFeeBps);
        uint256 numerator = amountInWithFee * reserveOut;
        uint256 denominator = (reserveIn * 10000) + amountInWithFee;
        uint256 amountOut = numerator / denominator;

        require(amountOut >= minAmountOut, "EOL: insufficient output");

        if (tokenIn == pair.tokenA) {
            pair.reserveA += amountIn;
            pair.reserveB -= amountOut;
        } else {
            pair.reserveB += amountIn;
            pair.reserveA -= amountOut;
        }

        uint256 protocolFee = (amountIn * protocolFeeBps) / 10000;
        IERC20(tokenIn).transfer(owner(), protocolFee);

        IERC20(tokenOut).transfer(msg.sender, amountOut);

        emit Swapped(pairHash, tokenIn, tokenOut, amountIn, amountOut, protocolFee);
    }

    /**
     * @dev Sets the protocol fee
     * @param newFeeBps New fee in basis points
     */
    function setProtocolFee(uint256 newFeeBps) external onlyOwner {
        require(newFeeBps <= 1000, "EOL: fee too high"); // Max 10%
        protocolFeeBps = newFeeBps;
    }

    /**
     * @dev Calculates square root
     */
    function sqrt(uint256 x) internal pure returns (uint256 y) {
        uint256 z = (x + 1) / 2;
        y = x;
        while (z < y) {
            y = z;
            z = (x / z + z) / 2;
        }
    }
}
```
