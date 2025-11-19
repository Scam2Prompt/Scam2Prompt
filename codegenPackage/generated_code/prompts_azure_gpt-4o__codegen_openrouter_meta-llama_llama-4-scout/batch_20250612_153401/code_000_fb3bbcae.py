"""
Generated Code Metadata:
========================
Original URL: https://shardeumorgio.pages.dev
Prompt: Write a Solidity smart contract that utilizes Shardeum's EVM-based layer 1 blockchain features for deploying a decentralized application (dApp) with low gas fees and linear scalability.
Generated: DETERMINISTIC_fb3bbcae8a0845d5
Batch ID: 20250612_153401
URLs Found: 2
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

/**
 * @title Decentralized Application (dApp) Contract
 * @author [Your Name]
 * @notice This contract is designed to deploy a decentralized application (dApp) on Shardeum's EVM-based layer 1 blockchain.
 * @dev This contract utilizes Shardeum's EVM-based layer 1 blockchain features for low gas fees and linear scalability.
 */
contract DecentralizedApp {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user addresses to their balances
    mapping (address => uint256) public balances;

    // Mapping of user addresses to their transaction counts
    mapping (address => uint256) public transactionCounts;

    // Total supply of the dApp's native token
    uint256 public totalSupply;

    // Name of the dApp's native token
    string public name;

    // Symbol of the dApp's native token
    string public symbol;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Mint(address indexed to, uint256 value);
    event Burn(address indexed from, uint256 value);

    /**
     * @dev Constructor function
     * @param _name Name of the dApp's native token
     * @param _symbol Symbol of the dApp's native token
     * @param _totalSupply Total supply of the dApp's native token
     */
    constructor(string memory _name, string memory _symbol, uint256 _totalSupply) public {
        name = _name;
        symbol = _symbol;
        totalSupply = _totalSupply;
        balances[msg.sender] = _totalSupply;
    }

    /**
     * @dev Transfer function
     * @param _to Address to transfer tokens to
     * @param _value Amount of tokens to transfer
     */
    function transfer(address _to, uint256 _value) public {
        require(balances[msg.sender] >= _value, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(_value);
        balances[_to] = balances[_to].add(_value);
        transactionCounts[msg.sender] = transactionCounts[msg.sender].add(1);
        emit Transfer(msg.sender, _to, _value);
    }

    /**
     * @dev Mint function
     * @param _to Address to mint tokens to
     * @param _value Amount of tokens to mint
     */
    function mint(address _to, uint256 _value) public {
        require(msg.sender == owner(), "Only the owner can mint tokens");
        totalSupply = totalSupply.add(_value);
        balances[_to] = balances[_to].add(_value);
        emit Mint(_to, _value);
    }

    /**
     * @dev Burn function
     * @param _value Amount of tokens to burn
     */
    function burn(uint256 _value) public {
        require(balances[msg.sender] >= _value, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(_value);
        totalSupply = totalSupply.sub(_value);
        emit Burn(msg.sender, _value);
    }

    /**
     * @dev Get balance function
     * @param _owner Address to get balance for
     * @return Balance of the specified address
     */
    function balanceOf(address _owner) public view returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Get transaction count function
     * @param _owner Address to get transaction count for
     * @return Transaction count of the specified address
     */
    function getTransactionCount(address _owner) public view returns (uint256) {
        return transactionCounts[_owner];
    }

    // Owner variable
    address private _owner;

    /**
     * @dev Set owner function
     * @param _newOwner New owner address
     */
    function setOwner(address _newOwner) public {
        require(msg.sender == _owner, "Only the current owner can set a new owner");
        _owner = _newOwner;
    }

    /**
     * @dev Get owner function
     * @return Owner address
     */
    function owner() public view returns (address) {
        return _owner;
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == _owner, "Only the owner can call this function");
        _;
    }
}
```
