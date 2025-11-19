"""
Generated Code Metadata:
========================
Original URL: https://bafybeia5w6ij6k5e2i3vwagaacosirdjz6kce4q3y2thlqdaqcfnictzmu.ipfs.dweb.link
Prompt: Generate code for an automated market maker (AMM) built into Berachain's chain, leveraging its native DeFi legos and validator-powered pools.
Generated: DETERMINISTIC_d1651ab5e146cc7a
Batch ID: 20250612_152249
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Automated Market Maker (AMM) for Berachain
 * @notice Implements a constant product market maker with validator-powered liquidity pools
 */
contract BerachainAMM is ReentrancyGuard {
    using SafeMath for uint256;

    struct Pool {
        address tokenA;
        address tokenB;
        uint256 reserveA;
        uint256 reserveB;
        uint256 totalLiquidity;
        mapping(address => uint256) liquidity;
    }

    address public immutable nativeToken;
    address[] public validators;
    mapping(address => bool) public isValidator;
    mapping(bytes32 => Pool) public pools;

    event PoolCreated(
        address indexed tokenA,
        address indexed tokenB,
        bytes32 indexed poolId
    );
    event LiquidityAdded(
        address indexed provider,
        bytes32 indexed poolId,
        uint256 amountA,
        uint256 amountB,
        uint256 liquidity
    );
    event LiquidityRemoved(
        address indexed provider,
        bytes32 indexed poolId,
        uint256 amountA,
        uint256 amountB,
        uint256 liquidity
    );
    event Swap(
        address indexed sender,
        bytes32 indexed poolId,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    modifier onlyValidator() {
        require(isValidator[msg.sender], "Only validators can call this");
        _;
    }

    constructor(address _nativeToken) {
        nativeToken = _nativeToken;
    }

    /**
     * @notice Add a validator to the AMM
     * @param _validator Address of the validator to add
     */
    function addValidator(address _validator) external onlyValidator {
        require(!isValidator[_validator], "Validator already exists");
        validators.push(_validator);
        isValidator[_validator] = true;
    }

    /**
     * @notice Create a new liquidity pool
     * @param _tokenA Address of first token
     * @param _tokenB Address of second token
     */
    function createPool(address _tokenA, address _tokenB) external onlyValidator {
        require(_tokenA != _tokenB, "Cannot create pool with same tokens");
        bytes32 poolId = keccak256(abi.encodePacked(_tokenA, _tokenB));
        require(pools[poolId].tokenA == address(0), "Pool already exists");

        pools[poolId].tokenA = _tokenA;
        pools[poolId].tokenB = _tokenB;
        pools[poolId].reserveA = 0;
        pools[poolId].reserveB = 0;
        pools[poolId].totalLiquidity = 0;

        emit PoolCreated(_tokenA, _tokenB, poolId);
    }

    /**
     * @notice Add liquidity to a pool
     * @param _poolId ID of the pool
     * @param _amountA Amount of token A to add
     * @param _amountB Amount of token B to add
     */
    function addLiquidity(
        bytes32 _poolId,
        uint256 _amountA,
        uint256 _amountB
    ) external nonReentrant {
        Pool storage pool = pools[_poolId];
        require(pool.tokenA != address(0), "Pool does not exist");

        IERC20 tokenA = IERC20(pool.tokenA);
        IERC20 tokenB = IERC20(pool.tokenB);

        uint256 liquidity;
        if (pool.totalLiquidity == 0) {
            liquidity = sqrt(_amountA.mul(_amountB));
        } else {
            liquidity = min(
                _amountA.mul(pool.totalLiquidity) / pool.reserveA,
                _amountB.mul(pool.totalLiquidity) / pool.reserveB
            );
        }

        require(liquidity > 0, "Insufficient liquidity");

        tokenA.transferFrom(msg.sender, address(this), _amountA);
        tokenB.transferFrom(msg.sender, address(this), _amountB);

        pool.reserveA = pool.reserveA.add(_amountA);
        pool.reserveB = pool.reserveB.add(_amountB);
        pool.totalLiquidity = pool.totalLiquidity.add(liquidity);
        pool.liquidity[msg.sender] = pool.liquidity[msg.sender].add(liquidity);

        emit LiquidityAdded(msg.sender, _poolId, _amountA, _amountB, liquidity);
    }

    /**
     * @notice Remove liquidity from a pool
     * @param _poolId ID of the pool
     * @param _liquidity Amount of liquidity to remove
     */
    function removeLiquidity(bytes32 _poolId, uint256 _liquidity) external nonReentrant {
        Pool storage pool = pools[_poolId];
        require(pool.tokenA != address(0), "Pool does not exist");
        require(pool.liquidity[msg.sender] >= _liquidity, "Insufficient liquidity");

        uint256 amountA = _liquidity.mul(pool.reserveA) / pool.totalLiquidity;
        uint256 amountB = _liquidity.mul(pool.reserveB) / pool.totalLiquidity;

        pool.reserveA = pool.reserveA.sub(amountA);
        pool.reserveB = pool.reserveB.sub(amountB);
        pool.totalLiquidity = pool.totalLiquidity.sub(_liquidity);
        pool.liquidity[msg.sender] = pool.liquidity[msg.sender].sub(_liquidity);

        IERC20(pool.tokenA).transfer(msg.sender, amountA);
        IERC20(pool.tokenB).transfer(msg.sender, amountB);

        emit LiquidityRemoved(msg.sender, _poolId, amountA, amountB, _liquidity);
    }

    /**
     * @notice Swap tokens in a pool
     * @param _poolId ID of the pool
     * @param _tokenIn Address of input token
     * @param _amountIn Amount of input token
     * @param _minAmountOut Minimum amount of output token expected
     */
    function swap(
        bytes32 _poolId,
        address _tokenIn,
        uint256 _amountIn,
        uint256 _minAmountOut
    ) external nonReentrant {
        Pool storage pool = pools[_poolId];
        require(pool.tokenA != address(0), "Pool does not exist");
        require(
            _tokenIn == pool.tokenA || _tokenIn == pool.tokenB,
            "Invalid input token"
        );

        address tokenOut = _tokenIn == pool.tokenA ? pool.tokenB : pool.tokenA;
        uint256 reserveIn = _tokenIn == pool.tokenA ? pool.reserveA : pool.reserveB;
        uint256 reserveOut = _tokenIn == pool.tokenA ? pool.reserveB : pool.reserveA;

        uint256 amountOut = getAmountOut(_amountIn, reserveIn, reserveOut);
        require(amountOut >= _minAmountOut, "Insufficient output amount");

        IERC20(_tokenIn).transferFrom(msg.sender, address(this), _amountIn);

        if (_tokenIn == pool.tokenA) {
            pool.reserveA = pool.reserveA.add(_amountIn);
            pool.reserveB = pool.reserveB.sub(amountOut);
        } else {
            pool.reserveB = pool.reserveB.add(_amountIn);
            pool.reserveA = pool.reserveA.sub(amountOut);
        }

        IERC20(tokenOut).transfer(msg.sender, amountOut);

        emit Swap(msg.sender, _poolId, _tokenIn, tokenOut, _amountIn, amountOut);
    }

    /**
     * @notice Calculate output amount for a swap
     * @param _amountIn Amount of input token
     * @param _reserveIn Reserve of input token
     * @param _reserveOut Reserve of output token
     * @return amountOut Calculated output amount
     */
    function getAmountOut(
        uint256 _amountIn,
        uint256 _reserveIn,
        uint256 _reserveOut
    ) public pure returns (uint256 amountOut) {
        require(_amountIn > 0, "Invalid input amount");
        require(_reserveIn > 0 && _reserveOut > 0, "Insufficient liquidity");
        uint256 amountInWithFee = _amountIn.mul(997);
        uint256 numerator = amountInWithFee.mul(_reserveOut);
        uint256 denominator = _reserveIn.mul(1000).add(amountInWithFee);
        amountOut = numerator / denominator;
    }

    /**
     * @notice Get pool reserves
     * @param _poolId ID of the pool
     * @return reserveA Reserve of token A
     * @
