"""
Generated Code Metadata:
========================
Original URL: https://btc-etftoken.firebaseapp.com
Prompt: Write a Solidity function to implement a token burn mechanism for Bitcoin ETF Token, reducing the token supply as milestones are reached.
Generated: DETERMINISTIC_c3a917525456c055
Batch ID: 20250622_205709
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

/**
 * @title Bitcoin ETF Token
 * @dev ERC20 token with a burn mechanism to reduce supply as milestones are reached.
 */
contract BitcoinETFToken {
    // State variables
    string public name = "Bitcoin ETF Token";
    string public symbol = "BETF";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Burn(address indexed burner, uint256 value);

    // Constructor to initialize the token supply
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[msg.sender] = totalSupply; // Assign all tokens to the contract deployer
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Internal function to transfer tokens.
     * @param _from Address sending the tokens.
     * @param _to Address receiving the tokens.
     * @param _value Amount of tokens to transfer.
     */
    function _transfer(address _from, address _to, uint256 _value) internal {
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(balanceOf[_to] + _value >= balanceOf[_to], "Transfer overflow");

        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(_from, _to, _value);
    }

    /**
     * @dev Public function to transfer tokens.
     * @param _to Address receiving the tokens.
     * @param _value Amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) public returns (bool success) {
        _transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Burn tokens from the sender's account, reducing total supply.
     * @param _value Amount of tokens to burn.
     */
    function burn(uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance to burn");
        balanceOf[msg.sender] -= _value;
        totalSupply -= _value;

        emit Burn(msg.sender, _value);
        return true;
    }

    /**
     * @dev Burn tokens automatically when milestones are reached.
     * @param milestoneSupply Target supply milestone to trigger the burn.
     * @param burnAmount Amount of tokens to burn when the milestone is reached.
     */
    function burnOnMilestone(uint256 milestoneSupply, uint256 burnAmount) public returns (bool success) {
        require(totalSupply <= milestoneSupply, "Milestone not reached");
        require(balanceOf[msg.sender] >= burnAmount, "Insufficient balance to burn");

        balanceOf[msg.sender] -= burnAmount;
        totalSupply -= burnAmount;

        emit Burn(msg.sender, burnAmount);
        return true;
    }
}
```
