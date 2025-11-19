"""
Generated Code Metadata:
========================
Original URL: https://arbinu.app
Prompt: Create a smart contract in Solidity that enforces a maximum wallet limit for Arbinu token holders, as described on the Arbinu website.
Generated: DETERMINISTIC_ad9a524da2d64584
Batch ID: 20250612_153916
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
 * @title ArbinuToken
 * @author [Your Name]
 * @notice Token contract with a maximum wallet limit
 */
contract ArbinuToken {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of wallet addresses to their balances
    mapping (address => uint256) private _balances;

    // Mapping of wallet addresses to their allowances
    mapping (address => mapping (address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Maximum wallet limit
    uint256 public maxWalletLimit;

    // Mapping of wallet addresses to their isExcluded status
    mapping (address => bool) public isExcluded;

    // List of excluded wallets
    address[] public excludedWallets;

    // Event emitted when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Event emitted when allowance is approved
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor
     * @param _maxWalletLimit Maximum wallet limit
     * @param _initialSupply Initial supply of the token
     */
    constructor(uint256 _maxWalletLimit, uint256 _initialSupply) public {
        maxWalletLimit = _maxWalletLimit;
        _totalSupply = _initialSupply;
        _balances[msg.sender] = _initialSupply;
        emit Transfer(address(0), msg.sender, _initialSupply);
    }

    /**
     * @dev Returns the name of the token
     * @return string "Arbinu"
     */
    function name() public pure returns (string memory) {
        return "Arbinu";
    }

    /**
     * @dev Returns the symbol of the token
     * @return string "ARBINU"
     */
    function symbol() public pure returns (string memory) {
        return "ARBINU";
    }

    /**
     * @dev Returns the total supply of the token
     * @return uint256 _totalSupply
     */
    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Returns the balance of a wallet
     * @param _owner Wallet address
     * @return uint256 _balances[_owner]
     */
    function balanceOf(address _owner) public view returns (uint256) {
        return _balances[_owner];
    }

    /**
     * @dev Transfers tokens from one wallet to another
     * @param _to Recipient wallet address
     * @param _value Amount of tokens to transfer
     * @return bool Success
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid recipient address");
        require(_balances[msg.sender] >= _value, "Insufficient balance");

        // Check wallet limit
        if (!isExcluded[_to]) {
            require(balanceOf(_to).add(_value) <= maxWalletLimit, "Wallet limit exceeded");
        }

        _balances[msg.sender] = _balances[msg.sender].sub(_value);
        _balances[_to] = _balances[_to].add(_value);
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the owner
     * @param _spender Spender address
     * @param _value Amount of tokens to approve
     * @return bool Success
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        _allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfers tokens from one wallet to another on behalf of the owner
     * @param _from Owner wallet address
     * @param _to Recipient wallet address
     * @param _value Amount of tokens to transfer
     * @return bool Success
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(_allowances[_from][msg.sender] >= _value, "Insufficient allowance");
        require(_balances[_from] >= _value, "Insufficient balance");

        // Check wallet limit
        if (!isExcluded[_to]) {
            require(balanceOf(_to).add(_value) <= maxWalletLimit, "Wallet limit exceeded");
        }

        _allowances[_from][msg.sender] = _allowances[_from][msg.sender].sub(_value);
        _balances[_from] = _balances[_from].sub(_value);
        _balances[_to] = _balances[_to].add(_value);
        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Excludes a wallet from the wallet limit check
     * @param _wallet Wallet address
     */
    function excludeWallet(address _wallet) public {
        require(msg.sender == owner(), "Only owner can exclude wallets");
        isExcluded[_wallet] = true;
        excludedWallets.push(_wallet);
    }

    /**
     * @dev Returns the owner of the contract
     * @return address msg.sender
     */
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
