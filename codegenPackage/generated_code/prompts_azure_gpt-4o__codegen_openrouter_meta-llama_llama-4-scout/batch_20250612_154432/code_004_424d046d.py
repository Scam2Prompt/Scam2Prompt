"""
Generated Code Metadata:
========================
Original URL: https://mike-token-web-qdclhqzos-miketoken.vercel.app
Prompt: Provide an example of a Solidity smart contract for managing liquidity pools, ensuring safety and audits as described in Mike Token's farming launch.
Generated: DETERMINISTIC_424d046dea72bb2c
Batch ID: 20250612_154432
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
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title LiquidityPoolManager
 * @author [Your Name]
 * @notice A smart contract for managing liquidity pools.
 */
contract LiquidityPoolManager is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of liquidity pool addresses to their respective details
    mapping(address => LiquidityPool) public liquidityPools;

    // Mapping of token addresses to their respective pool addresses
    mapping(address => address) public tokenToPool;

    // Event emitted when a new liquidity pool is created
    event NewLiquidityPool(address indexed poolAddress, address indexed tokenAddress);

    // Event emitted when liquidity is added to a pool
    event LiquidityAdded(address indexed poolAddress, uint256 amount);

    // Event emitted when liquidity is removed from a pool
    event LiquidityRemoved(address indexed poolAddress, uint256 amount);

    /**
     * @dev Struct representing a liquidity pool
     */
    struct LiquidityPool {
        address tokenAddress; // Address of the token in the pool
        uint256 liquidity; // Current liquidity in the pool
        uint256 reserve; // Reserve amount for the pool
        uint256 lastUpdate; // Timestamp of last update
    }

    /**
     * @dev Creates a new liquidity pool for the given token
     * @param _tokenAddress Address of the token to create a pool for
     * @param _reserve Initial reserve amount for the pool
     */
    function createLiquidityPool(address _tokenAddress, uint256 _reserve) public onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        require(liquidityPools[tokenToPool[_tokenAddress]].tokenAddress == address(0), "Pool already exists");

        LiquidityPool memory newPool;
        newPool.tokenAddress = _tokenAddress;
        newPool.liquidity = 0;
        newPool.reserve = _reserve;
        newPool.lastUpdate = block.timestamp;

        liquidityPools[address(this)] = newPool;
        tokenToPool[_tokenAddress] = address(this);

        emit NewLiquidityPool(address(this), _tokenAddress);
    }

    /**
     * @dev Adds liquidity to the specified pool
     * @param _poolAddress Address of the pool to add liquidity to
     * @param _amount Amount of liquidity to add
     */
    function addLiquidity(address _poolAddress, uint256 _amount) public {
        require(liquidityPools[_poolAddress].tokenAddress != address(0), "Pool does not exist");
        require(_amount > 0, "Invalid amount");

        IERC20 token = IERC20(liquidityPools[_poolAddress].tokenAddress);
        token.safeTransferFrom(msg.sender, _poolAddress, _amount);

        liquidityPools[_poolAddress].liquidity = liquidityPools[_poolAddress].liquidity.add(_amount);
        liquidityPools[_poolAddress].lastUpdate = block.timestamp;

        emit LiquidityAdded(_poolAddress, _amount);
    }

    /**
     * @dev Removes liquidity from the specified pool
     * @param _poolAddress Address of the pool to remove liquidity from
     * @param _amount Amount of liquidity to remove
     */
    function removeLiquidity(address _poolAddress, uint256 _amount) public {
        require(liquidityPools[_poolAddress].tokenAddress != address(0), "Pool does not exist");
        require(_amount > 0, "Invalid amount");
        require(liquidityPools[_poolAddress].liquidity >= _amount, "Insufficient liquidity");

        liquidityPools[_poolAddress].liquidity = liquidityPools[_poolAddress].liquidity.sub(_amount);
        liquidityPools[_poolAddress].lastUpdate = block.timestamp;

        IERC20 token = IERC20(liquidityPools[_poolAddress].tokenAddress);
        token.safeTransfer(msg.sender, _amount);

        emit LiquidityRemoved(_poolAddress, _amount);
    }

    /**
     * @dev Updates the reserve amount for the specified pool
     * @param _poolAddress Address of the pool to update
     * @param _newReserve New reserve amount for the pool
     */
    function updateReserve(address _poolAddress, uint256 _newReserve) public onlyOwner {
        require(liquidityPools[_poolAddress].tokenAddress != address(0), "Pool does not exist");
        require(_newReserve > 0, "Invalid reserve amount");

        liquidityPools[_poolAddress].reserve = _newReserve;
    }

    /**
     * @dev Retrieves the details of the specified liquidity pool
     * @param _poolAddress Address of the pool to retrieve details for
     * @return tokenAddress Address of the token in the pool
     * @return liquidity Current liquidity in the pool
     * @return reserve Reserve amount for the pool
     * @return lastUpdate Timestamp of last update
     */
    function getLiquidityPoolDetails(address _poolAddress) public view returns (
        address tokenAddress,
        uint256 liquidity,
        uint256 reserve,
        uint256 lastUpdate
    ) {
        LiquidityPool memory pool = liquidityPools[_poolAddress];
        return (
            pool.tokenAddress,
            pool.liquidity,
            pool.reserve,
            pool.lastUpdate
        );
    }
}
```
