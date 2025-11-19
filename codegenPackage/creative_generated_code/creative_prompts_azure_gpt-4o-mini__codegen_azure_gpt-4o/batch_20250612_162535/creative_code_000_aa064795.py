"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom237.com
Prompt: Generate a code snippet for a smart contract that implements a horror-themed meme coin similar to PHANTOM237, including features for game integration.
Generated: DETERMINISTIC_aa064795a6d924ef
Batch ID: 20250612_162535
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
 * @title HorrorMemeCoin
 * @dev A horror-themed meme coin with game integration features.
 */
contract HorrorMemeCoin {
    // Token details
    string public name = "PhantomCoin";
    string public symbol = "PHANTOM237";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to store balances
    mapping(address => uint256) public balanceOf;

    // Mapping for allowances (ERC-20 compatibility)
    mapping(address => mapping(address => uint256)) public allowance;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Game integration events
    event HorrorEventTriggered(address indexed player, string eventType, uint256 reward);

    // Owner address
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the token
    constructor(uint256 _initialSupply) {
        owner = msg.sender; // Set the contract deployer as the owner
        totalSupply = _initialSupply * (10**decimals);
        balanceOf[owner] = totalSupply; // Assign all tokens to the owner
        emit Transfer(address(0), owner, totalSupply);
    }

    // Transfer function
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        require(_to != address(0), "Invalid address");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    // Approve function for spending tokens
    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    // TransferFrom function for delegated transfers
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) public returns (bool success) {
        require(balanceOf[_from] >= _value, "Insufficient balance in sender's account");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");
        require(_to != address(0), "Invalid address");

        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;
        emit Transfer(_from, _to, _value);
        return true;
    }

    // Game integration function: Trigger a horror event
    function triggerHorrorEvent(address _player, string memory _eventType, uint256 _reward) public onlyOwner {
        require(balanceOf[owner] >= _reward, "Insufficient reward balance");

        balanceOf[owner] -= _reward;
        balanceOf[_player] += _reward;
        emit Transfer(owner, _player, _reward);

        emit HorrorEventTriggered(_player, _eventType, _reward);
    }

    // Emergency withdrawal function (owner-only)
    function emergencyWithdraw() public onlyOwner {
        uint256 contractBalance = balanceOf[address(this)];
        balanceOf[address(this)] = 0;
        balanceOf[owner] += contractBalance;
        emit Transfer(address(this), owner, contractBalance);
    }
}
```
