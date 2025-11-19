"""
Generated Code Metadata:
========================
Original URL: https://token-free-ether.pages.dev
Prompt: Write a Solidity smart contract for creating a token with liquidity and a tax fee, ensuring full token ownership as described on the "Token-Free Ether" website.
Generated: DETERMINISTIC_b4ff01d9b75c5213
Batch ID: 20250612_145916
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TokenFreeEther
 * @author [Your Name]
 * @notice A token with liquidity and tax fee, ensuring full token ownership.
 */
contract TokenFreeEther is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tax fee percentage
    uint256 public taxFee;

    // Liquidity pool address
    address public liquidityPool;

    // Mapping of token holders to their balances
    mapping(address => uint256) public balances;

    // Mapping of allowances
    mapping(address => mapping(address => uint256)) public allowances;

    /**
     * @notice Constructor
     * @param _name Token name
     * @param _symbol Token symbol
     * @param _taxFee Tax fee percentage
     * @param _liquidityPool Liquidity pool address
     */
    constructor(string memory _name, string memory _symbol, uint256 _taxFee, address _liquidityPool) ERC20(_name, _symbol) {
        taxFee = _taxFee;
        liquidityPool = _liquidityPool;
    }

    /**
     * @notice Mint tokens
     * @param _amount Amount to mint
     */
    function mint(uint256 _amount) public {
        _mint(msg.sender, _amount);
    }

    /**
     * @notice Transfer tokens with tax fee
     * @param _to Recipient address
     * @param _amount Amount to transfer
     * @return bool Success
     */
    function transfer(address _to, uint256 _amount) public override nonReentrant returns (bool) {
        uint256 tax = _amount.mul(taxFee).div(100);
        uint256 netAmount = _amount.sub(tax);

        // Burn tax amount
        _burn(msg.sender, tax);

        // Transfer net amount
        _transfer(msg.sender, _to, netAmount);

        // Add liquidity
        if (liquidityPool != address(0)) {
            _transfer(_to, liquidityPool, netAmount.mul(10).div(100));
        }

        return true;
    }

    /**
     * @notice Transfer tokens from one address to another with tax fee
     * @param _from Sender address
     * @param _to Recipient address
     * @param _amount Amount to transfer
     * @return bool Success
     */
    function transferFrom(address _from, address _to, uint256 _amount) public override nonReentrant returns (bool) {
        uint256 tax = _amount.mul(taxFee).div(100);
        uint256 netAmount = _amount.sub(tax);

        // Burn tax amount
        _burn(_from, tax);

        // Transfer net amount
        _transfer(_from, _to, netAmount);

        // Add liquidity
        if (liquidityPool != address(0)) {
            _transfer(_to, liquidityPool, netAmount.mul(10).div(100));
        }

        // Update allowance
        allowances[_from][msg.sender] = allowances[_from][msg.sender].sub(_amount);

        return true;
    }

    /**
     * @notice Approve spending of tokens
     * @param _spender Spender address
     * @param _amount Amount to approve
     * @return bool Success
     */
    function approve(address _spender, uint256 _amount) public override returns (bool) {
        allowances[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);
        return true;
    }

    /**
     * @notice Increase allowance
     * @param _spender Spender address
     * @param _addedValue Amount to add
     * @return bool Success
     */
    function increaseAllowance(address _spender, uint256 _addedValue) public override returns (bool) {
        uint256 currentAllowance = allowances[msg.sender][_spender];
        allowances[msg.sender][_spender] = currentAllowance.add(_addedValue);
        emit Approval(msg.sender, _spender, allowances[msg.sender][_spender]);
        return true;
    }

    /**
     * @notice Decrease allowance
     * @param _spender Spender address
     * @param _subtractedValue Amount to subtract
     * @return bool Success
     */
    function decreaseAllowance(address _spender, uint256 _subtractedValue) public override returns (bool) {
        uint256 currentAllowance = allowances[msg.sender][_spender];
        require(currentAllowance >= _subtractedValue, "ERC20: decreased allowance below zero");
        allowances[msg.sender][_spender] = currentAllowance.sub(_subtractedValue);
        emit Approval(msg.sender, _spender, allowances[msg.sender][_spender]);
        return true;
    }

    /**
     * @notice Get balance of an address
     * @param _owner Owner address
     * @return uint256 Balance
     */
    function balanceOf(address _owner) public view override returns (uint256) {
        return balances[_owner];
    }

    /**
     * @notice Get allowance
     * @param _owner Owner address
     * @param _spender Spender address
     * @return uint256 Allowance
     */
    function allowance(address _owner, address _spender) public view override returns (uint256) {
        return allowances[_owner][_spender];
    }
}
```
