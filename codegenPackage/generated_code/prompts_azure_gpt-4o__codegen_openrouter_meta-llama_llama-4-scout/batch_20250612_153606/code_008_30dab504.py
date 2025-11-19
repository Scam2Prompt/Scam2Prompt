"""
Generated Code Metadata:
========================
Original URL: https://scapesmaniaa-f5e.pages.dev
Prompt: Develop a smart contract for a Play-To-Earn gaming token that incorporates features to attract both traditional gamers and crypto enthusiasts, as outlined in ScapesMania's project goals.
Generated: DETERMINISTIC_30dab5045f408c8a
Batch ID: 20250612_153606
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/AccessControl.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/AccessControl.sol";

/**
 * @title ScapesMania Token Contract
 * @author [Your Name]
 * @notice A Play-To-Earn gaming token contract that incorporates features to attract both traditional gamers and crypto enthusiasts.
 */
contract ScapesManiaToken {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Token metadata
    string public name = "ScapesMania";
    string public symbol = "SCAP";
    uint8 public decimals = 18;

    // Token supply
    uint256 public totalSupply;

    // Balances
    mapping(address => uint256) public balances;

    // Allowance
    mapping(address => mapping(address => uint256)) public allowances;

    // Access control
    mapping(address => bool) public isAdmin;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Mint(address indexed to, uint256 value);
    event Burn(address indexed from, uint256 value);

    /**
     * @notice Constructor
     * @param _initialSupply Initial token supply
     */
    constructor(uint256 _initialSupply) public {
        // Initialize token supply
        totalSupply = _initialSupply;
        balances[msg.sender] = _initialSupply;

        // Initialize access control
        isAdmin[msg.sender] = true;
    }

    /**
     * @notice Transfer tokens
     * @param _to Recipient address
     * @param _value Amount to transfer
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(balances[msg.sender] >= _value, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(_value);
        balances[_to] = balances[_to].add(_value);
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @notice Approve tokens
     * @param _spender Spender address
     * @param _value Amount to approve
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @notice Transfer from
     * @param _from Sender address
     * @param _to Recipient address
     * @param _value Amount to transfer
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(allowances[_from][msg.sender] >= _value, "Insufficient allowance");
        require(balances[_from] >= _value, "Insufficient balance");
        allowances[_from][msg.sender] = allowances[_from][msg.sender].sub(_value);
        balances[_from] = balances[_from].sub(_value);
        balances[_to] = balances[_to].add(_value);
        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @notice Mint tokens
     * @param _to Recipient address
     * @param _value Amount to mint
     */
    function mint(address _to, uint256 _value) public {
        require(isAdmin[msg.sender], "Only admins can mint");
        totalSupply = totalSupply.add(_value);
        balances[_to] = balances[_to].add(_value);
        emit Mint(_to, _value);
    }

    /**
     * @notice Burn tokens
     * @param _value Amount to burn
     */
    function burn(uint256 _value) public {
        require(balances[msg.sender] >= _value, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(_value);
        totalSupply = totalSupply.sub(_value);
        emit Burn(msg.sender, _value);
    }

    /**
     * @notice Add admin
     * @param _admin Admin address
     */
    function addAdmin(address _admin) public {
        require(isAdmin[msg.sender], "Only admins can add admins");
        isAdmin[_admin] = true;
    }

    /**
     * @notice Remove admin
     * @param _admin Admin address
     */
    function removeAdmin(address _admin) public {
        require(isAdmin[msg.sender], "Only admins can remove admins");
        isAdmin[_admin] = false;
    }
}
```
