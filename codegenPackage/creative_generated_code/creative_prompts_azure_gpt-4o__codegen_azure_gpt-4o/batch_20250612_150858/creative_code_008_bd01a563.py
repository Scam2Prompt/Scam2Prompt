"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealy-io.github.io
Prompt: Write a Solidity smart contract for managing liquidity pools on Zealy, including ORB/USDT and ORB/DAI trading pairs.
Generated: DETERMINISTIC_bd01a5637f3d3993
Batch ID: 20250612_150858
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
 * @title LiquidityPoolManager
 * @dev Smart contract for managing liquidity pools on Zealy for ORB/USDT and ORB/DAI trading pairs.
 */
contract LiquidityPoolManager {
    // Events for logging deposits, withdrawals, and other activity
    event LiquidityAdded(address indexed provider, uint256 amountORB, uint256 amountToken, string pool);
    event LiquidityRemoved(address indexed provider, uint256 amountORB, uint256 amountToken, string pool);

    // Struct representing a liquidity pool
    struct LiquidityPool {
        uint256 totalORB;
        uint256 totalToken;
        mapping(address => uint256) orbBalance;
        mapping(address => uint256) tokenBalance;
    }

    // Liquidity pools (ORB/USDT and ORB/DAI)
    LiquidityPool public orbUsdtPool;
    LiquidityPool public orbDaiPool;

    // Admin address for contract management
    address public admin;

    // Modifier to restrict access to admin functions
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    // Constructor to set the admin address
    constructor() {
        admin = msg.sender;
    }

    /**
     * @dev Add liquidity to a pool.
     * @param _poolName The name of the pool ("ORB/USDT" or "ORB/DAI").
     * @param _amountORB Amount of ORB tokens to deposit.
     * @param _amountToken Amount of USDT or DAI tokens to deposit.
     */
    function addLiquidity(
        string memory _poolName,
        uint256 _amountORB,
        uint256 _amountToken
    ) external {
        require(_amountORB > 0, "ORB amount must be greater than 0");
        require(_amountToken > 0, "Token amount must be greater than 0");

        LiquidityPool storage selectedPool = _getPoolByName(_poolName);

        // Update pool balances
        selectedPool.totalORB += _amountORB;
        selectedPool.totalToken += _amountToken;

        // Update provider balances
        selectedPool.orbBalance[msg.sender] += _amountORB;
        selectedPool.tokenBalance[msg.sender] += _amountToken;

        emit LiquidityAdded(msg.sender, _amountORB, _amountToken, _poolName);
    }

    /**
     * @dev Remove liquidity from a pool.
     * @param _poolName The name of the pool ("ORB/USDT" or "ORB/DAI").
     * @param _amountORB Amount of ORB tokens to withdraw.
     * @param _amountToken Amount of USDT or DAI tokens to withdraw.
     */
    function removeLiquidity(
        string memory _poolName,
        uint256 _amountORB,
        uint256 _amountToken
    ) external {
        require(_amountORB > 0, "ORB amount must be greater than 0");
        require(_amountToken > 0, "Token amount must be greater than 0");

        LiquidityPool storage selectedPool = _getPoolByName(_poolName);

        // Ensure sufficient balances in the pool and user account
        require(
            selectedPool.orbBalance[msg.sender] >= _amountORB,
            "Insufficient ORB balance"
        );
        require(
            selectedPool.tokenBalance[msg.sender] >= _amountToken,
            "Insufficient Token balance"
        );

        // Update pool balances
        selectedPool.totalORB -= _amountORB;
        selectedPool.totalToken -= _amountToken;

        // Update provider balances
        selectedPool.orbBalance[msg.sender] -= _amountORB;
        selectedPool.tokenBalance[msg.sender] -= _amountToken;

        emit LiquidityRemoved(msg.sender, _amountORB, _amountToken, _poolName);
    }

    /**
     * @dev Get the balances of a user in a given pool.
     * @param _poolName The name of the pool ("ORB/USDT" or "ORB/DAI").
     * @param _user The address of the user.
     * @return orbBalance The user's ORB balance in the pool.
     * @return tokenBalance The user's USDT or DAI balance in the pool.
     */
    function getUserBalances(string memory _poolName, address _user)
        external
        view
        returns (uint256 orbBalance, uint256 tokenBalance)
    {
        LiquidityPool storage selectedPool = _getPoolByName(_poolName);
        return (
            selectedPool.orbBalance[_user],
            selectedPool.tokenBalance[_user]
        );
    }

    /**
     * @dev Get pool liquidity details.
     * @param _poolName The name of the pool ("ORB/USDT" or "ORB/DAI").
     * @return totalORB Total ORB liquidity in the pool.
     * @return totalToken Total USDT or DAI liquidity in the pool.
     */
    function getPoolDetails(string memory _poolName)
        external
        view
        returns (uint256 totalORB, uint256 totalToken)
    {
        LiquidityPool storage selectedPool = _getPoolByName(_poolName);
        return (selectedPool.totalORB, selectedPool.totalToken);
    }

    /**
     * @dev Internal function to retrieve the correct pool based on the name.
     * @param _poolName The name of the pool ("ORB/USDT" or "ORB/DAI").
     * @return The liquidity pool struct.
     */
    function _getPoolByName(string memory _poolName)
        internal
        view
        returns (LiquidityPool storage)
    {
        if (keccak256(abi.encodePacked(_poolName)) == keccak256(abi.encodePacked("ORB/USDT"))) {
            return orbUsdtPool;
        } else if (keccak256(abi.encodePacked(_poolName)) == keccak256(abi.encodePacked("ORB/DAI"))) {
            return orbDaiPool;
        } else {
            revert("Invalid pool name");
        }
    }

    /**
     * @dev Update the admin address.
     * @param _newAdmin The new admin address.
     */
    function updateAdmin(address _newAdmin) external onlyAdmin {
        require(_newAdmin != address(0), "Invalid admin address");
        admin = _newAdmin;
    }
}
```
