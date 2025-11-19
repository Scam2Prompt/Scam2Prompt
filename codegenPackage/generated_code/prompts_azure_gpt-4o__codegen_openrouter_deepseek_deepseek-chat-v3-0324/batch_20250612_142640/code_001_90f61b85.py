"""
Generated Code Metadata:
========================
Original URL: https://lido-hi.github.io
Prompt: Generate Solidity code for an oracle contract that integrates with Lido Finance to track stETH balances based on Ethereum Beacon Chain data.
Generated: DETERMINISTIC_90f61b85100b3fee
Batch ID: 20250612_142640
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface ILido {
    function getTotalPooledEther() external view returns (uint256);
    function getTotalShares() external view returns (uint256);
    function sharesOf(address _account) external view returns (uint256);
    function balanceOf(address _account) external view returns (uint256);
}

contract LidoOracle is Ownable {
    using SafeMath for uint256;

    // Lido stETH contract address
    address public lidoContract;

    // Events
    event LidoContractUpdated(address indexed oldAddress, address indexed newAddress);
    event OracleQuery(address indexed requester, uint256 stEthBalance, uint256 timestamp);

    /**
     * @dev Constructor initializes the Lido contract address
     * @param _lidoContract Address of the Lido stETH contract
     */
    constructor(address _lidoContract) {
        require(_lidoContract != address(0), "Invalid Lido contract address");
        lidoContract = _lidoContract;
    }

    /**
     * @dev Updates the Lido contract address
     * @param _newLidoContract New Lido contract address
     */
    function updateLidoContract(address _newLidoContract) external onlyOwner {
        require(_newLidoContract != address(0), "Invalid Lido contract address");
        emit LidoContractUpdated(lidoContract, _newLidoContract);
        lidoContract = _newLidoContract;
    }

    /**
     * @dev Gets the total pooled ETH in Lido
     * @return Total pooled ETH amount
     */
    function getTotalPooledEther() external view returns (uint256) {
        return ILido(lidoContract).getTotalPooledEther();
    }

    /**
     * @dev Gets the total shares in Lido
     * @return Total shares amount
     */
    function getTotalShares() external view returns (uint256) {
        return ILido(lidoContract).getTotalShares();
    }

    /**
     * @dev Gets the stETH balance for an account
     * @param _account Address to query
     * @return stETH balance
     */
    function getStEthBalance(address _account) external view returns (uint256) {
        require(_account != address(0), "Invalid account address");
        return ILido(lidoContract).balanceOf(_account);
    }

    /**
     * @dev Gets the shares for an account
     * @param _account Address to query
     * @return Shares amount
     */
    function getShares(address _account) external view returns (uint256) {
        require(_account != address(0), "Invalid account address");
        return ILido(lidoContract).sharesOf(_account);
    }

    /**
     * @dev Gets the exchange rate between stETH and ETH
     * @return Exchange rate (stETH per ETH)
     */
    function getExchangeRate() external view returns (uint256) {
        uint256 totalPooledEther = ILido(lidoContract).getTotalPooledEther();
        uint256 totalShares = ILido(lidoContract).getTotalShares();
        
        require(totalShares > 0, "No shares minted yet");
        return totalPooledEther.mul(1e18).div(totalShares);
    }

    /**
     * @dev Query oracle for stETH balance and emit event
     * @param _account Address to query
     * @return stETH balance
     */
    function queryStEthBalance(address _account) external returns (uint256) {
        require(_account != address(0), "Invalid account address");
        uint256 balance = ILido(lidoContract).balanceOf(_account);
        emit OracleQuery(_account, balance, block.timestamp);
        return balance;
    }
}
```
