"""
Generated Code Metadata:
========================
Original URL: https://growbit.tech
Prompt: Write a smart contract in Solidity for a token similar to GrowBTC, ensuring it includes features like capped supply, token locking for a specified duration, and interoperability with other blockchains.
Generated: DETERMINISTIC_8bed6f59cdc5cb5f
Batch ID: 20250612_154452
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
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
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
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title GrowBTC Token Contract
 * @author [Your Name]
 * @notice A token contract similar to GrowBTC with capped supply, token locking, and interoperability features.
 */
contract GrowBTCToken {
    // Using SafeMath for uint256 operations
    using SafeMath for uint256;
    // Using SafeERC20 for ERC20 token operations
    using SafeERC20 for IERC20;

    // Token details
    string public name = "GrowBTC";
    string public symbol = "GBTC";
    uint8 public decimals = 8;
    uint256 public totalSupply;

    // Mapping of token balances
    mapping(address => uint256) public balances;
    // Mapping of token allowances
    mapping(address => mapping(address => uint256)) public allowances;

    // Token cap
    uint256 public cap = 10**9 * 10**8; // 1 billion tokens with 8 decimals

    // Token locking details
    mapping(address => uint256) public lockEndTimes;
    mapping(address => uint256) public lockedBalances;

    // Interoperability bridge
    mapping(address => bool) public bridges;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Lock(address indexed account, uint256 endTime);
    event Unlock(address indexed account);
    event BridgeUpdated(address indexed bridge, bool status);

    // Errors
    error InvalidAmount();
    error ExceedsCap();
    error TokenLocked();
    error InvalidBridge();

    /**
     * @notice Initializes the token contract
     * @param _initialSupply Initial token supply
     */
    constructor(uint256 _initialSupply) public {
        require(_initialSupply <= cap, "Exceeds cap");
        totalSupply = _initialSupply;
        balances[msg.sender] = _initialSupply;
        emit Transfer(address(0), msg.sender, _initialSupply);
    }

    /**
     * @notice Transfers tokens from one account to another
     * @param _to Recipient address
     * @param _value Amount to transfer
     * @return bool Success status
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_value > 0, "Invalid amount");
        require(balances[msg.sender] >= _value, "Insufficient balance");
        require(lockEndTimes[msg.sender] == 0 || block.timestamp >= lockEndTimes[msg.sender], "Token locked");

        balances[msg.sender] = balances[msg.sender].sub(_value);
        balances[_to] = balances[_to].add(_value);
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @notice Approves a spender to transfer tokens on behalf of the owner
     * @param _spender Spender address
     * @param _value Amount to approve
     * @return bool Success status
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @notice Transfers tokens from one account to another using an allowance
     * @param _from Sender address
     * @param _to Recipient address
     * @param _value Amount to transfer
     * @return bool Success status
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(_value > 0, "Invalid amount");
        require(allowances[_from][msg.sender] >= _value, "Insufficient allowance");
        require(balances[_from] >= _value, "Insufficient balance");
        require(lockEndTimes[_from] == 0 || block.timestamp >= lockEndTimes[_from], "Token locked");

        allowances[_from][msg.sender] = allowances[_from][msg.sender].sub(_value);
        balances[_from] = balances[_from].sub(_value);
        balances[_to] = balances[_to].add(_value);
        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @notice Locks tokens for a specified duration
     * @param _endTime Lock end time
     */
    function lock(uint256 _endTime) public {
        require(lockEndTimes[msg.sender] == 0, "Already locked");
        require(_endTime > block.timestamp, "Invalid end time");

        lockEndTimes[msg.sender] = _endTime;
        lockedBalances[msg.sender] = balances[msg.sender];
        emit Lock(msg.sender, _endTime);
    }

    /**
     * @notice Unlocks tokens
     */
    function unlock() public {
        require(lockEndTimes[msg.sender] != 0 && block.timestamp >= lockEndTimes[msg.sender], "Not locked");

        lockEndTimes[msg.sender] = 0;
        lockedBalances[msg.sender] = 0;
        emit Unlock(msg.sender);
    }

    /**
     * @notice Updates the interoperability bridge
     * @param _bridge Bridge address
     * @param _status Bridge status
     */
    function updateBridge(address _bridge, bool _status) public onlyOwner {
        bridges[_bridge] = _status;
        emit BridgeUpdated(_bridge, _status);
    }

    /**
     * @notice Mints additional tokens
     * @param _amount Amount to mint
     */
    function mint(uint256 _amount) public onlyOwner {
        require(totalSupply.add(_amount) <= cap, "Exceeds cap");

        totalSupply = totalSupply.add(_amount);
        balances[msg.sender] = balances[msg.sender].add(_amount);
        emit Transfer(address(0), msg.sender, _amount);
    }

    modifier onlyOwner {
        require(msg.sender == owner, "Only owner");
        _;
    }

    address private owner;

    constructor() public {
        owner = msg.sender;
    }
}
```
