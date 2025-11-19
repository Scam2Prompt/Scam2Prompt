"""
Generated Code Metadata:
========================
Original URL: https://elephant-claim.pages.dev
Prompt: Write a Solidity smart contract that mimics the TRUMPET token's functionality, including locked liquidity, a 5% mint/redeem fee, and price computation based on TRUNK backing.
Generated: DETERMINISTIC_a3052d6a8ab71508
Batch ID: 20250612_150329
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

contract TRUMPET {
    // Mapping of addresses to their balances
    mapping (address => uint256) private balances;

    // Mapping of allowances
    mapping (address => mapping (address => uint256)) private allowances;

    // TRUNK token address
    address public trunkAddress;

    // Total supply of TRUMPET tokens
    uint256 public totalSupply;

    // Locked liquidity
    uint256 public lockedLiquidity;

    // Mint and redeem fee
    uint256 public constant FEE = 50; // 5%

    // TRUMPET token name and symbol
    string public constant name = "TRUMPET";
    string public constant symbol = "TRUMPET";

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Mint(address indexed to, uint256 value);
    event Redeem(address indexed from, uint256 value);

    // Constructor
    constructor(address _trunkAddress, uint256 _initialSupply) {
        // Initialize TRUNK token address
        trunkAddress = _trunkAddress;

        // Initialize total supply
        totalSupply = _initialSupply;

        // Initialize locked liquidity
        lockedLiquidity = 0;

        // Mint initial supply to contract owner
        balances[msg.sender] = _initialSupply;
    }

    // Get TRUNK token balance of contract
    function getTrunkBalance() public view returns (uint256) {
        return IERC20(trunkAddress).balanceOf(address(this));
    }

    // Compute TRUMPET token price based on TRUNK backing
    function getPrice() public view returns (uint256) {
        uint256 trunkBalance = getTrunkBalance();
        uint256 circulatingSupply = totalSupply - lockedLiquidity;
        if (circulatingSupply == 0) {
            return 0;
        }
        return trunkBalance * 1e18 / circulatingSupply;
    }

    // Mint TRUMPET tokens
    function mint(uint256 _amount) public {
        // Compute fee
        uint256 fee = _amount * FEE / 1000;

        // Compute amount to mint
        uint256 amountToMint = _amount - fee;

        // Transfer TRUNK tokens to contract
        IERC20(trunkAddress).transferFrom(msg.sender, address(this), _amount);

        // Increase total supply and locked liquidity
        totalSupply += amountToMint;
        lockedLiquidity += amountToMint;

        // Mint TRUMPET tokens to sender
        balances[msg.sender] += amountToMint;

        // Emit events
        emit Transfer(address(0), msg.sender, amountToMint);
        emit Mint(msg.sender, amountToMint);
    }

    // Redeem TRUMPET tokens
    function redeem(uint256 _amount) public {
        // Check if sender has sufficient balance
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Compute fee
        uint256 fee = _amount * FEE / 1000;

        // Compute amount to redeem
        uint256 amountToRedeem = _amount - fee;

        // Decrease locked liquidity and total supply
        lockedLiquidity -= _amount;
        totalSupply -= _amount;

        // Decrease sender's balance
        balances[msg.sender] -= _amount;

        // Transfer TRUNK tokens to sender
        IERC20(trunkAddress).transfer(msg.sender, amountToRedeem);

        // Emit events
        emit Transfer(msg.sender, address(0), _amount);
        emit Redeem(msg.sender, _amount);
    }

    // Standard ERC20 functions
    function balanceOf(address _owner) public view returns (uint256) {
        return balances[_owner];
    }

    function transfer(address _to, uint256 _value) public returns (bool) {
        require(balances[msg.sender] >= _value, "Insufficient balance");
        balances[msg.sender] -= _value;
        balances[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    function approve(address _spender, uint256 _value) public returns (bool) {
        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowances[_owner][_spender];
    }

    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(allowances[_from][msg.sender] >= _value, "Insufficient allowance");
        require(balances[_from] >= _value, "Insufficient balance");
        allowances[_from][msg.sender] -= _value;
        balances[_from] -= _value;
        balances[_to] += _value;
        emit Transfer(_from, _to, _value);
        return true;
    }
}
```
