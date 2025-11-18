"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-mpeppe.web.app
Prompt: Write a function in Solidity to burn $MPEPE tokens after every transaction, as described in the tokenomics section of the Mpeppe ecosystem.
Generated: DETERMINISTIC_c3873188596c82a7
Batch ID: 20250612_152426
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
 * @title MPEPE Token Contract
 * @dev Implements burning mechanism after every transaction in the MPEPE ecosystem.
 */
contract MPEPEToken {
    string public name = "MPEPE Token";
    string public symbol = "MPEPE";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    uint256 public burnRate = 2; // Burn rate percentage (2%)

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(address indexed from, uint256 value);

    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[msg.sender] = totalSupply;

        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Transfers tokens to a specified address and burns a percentage of the transferred amount.
     * @param _to Recipient address.
     * @param _value Amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_value > 0, "Transfer value must be greater than zero");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        uint256 burnAmount = (_value * burnRate) / 100;
        uint256 transferAmount = _value - burnAmount;

        // Perform the transfer and burn
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += transferAmount;
        totalSupply -= burnAmount;

        emit Transfer(msg.sender, _to, transferAmount);
        emit Burn(msg.sender, burnAmount);

        return true;
    }

    /**
     * @dev Allows spender to transfer tokens on behalf of the owner.
     * @param _spender Address allowed to spend.
     * @param _value Amount of tokens to approve.
     */
    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfers tokens on behalf of the owner and burns a percentage of the transferred amount.
     * @param _from Address from which tokens are transferred.
     * @param _to Recipient address.
     * @param _value Amount of tokens to transfer.
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(_value > 0, "Transfer value must be greater than zero");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        uint256 burnAmount = (_value * burnRate) / 100;
        uint256 transferAmount = _value - burnAmount;

        // Perform the transfer and burn
        balanceOf[_from] -= _value;
        balanceOf[_to] += transferAmount;
        allowance[_from][msg.sender] -= _value;
        totalSupply -= burnAmount;

        emit Transfer(_from, _to, transferAmount);
        emit Burn(_from, burnAmount);

        return true;
    }

    /**
     * @dev Sets the burn rate percentage for transactions.
     * @param _burnRate New burn rate percentage.
     */
    function setBurnRate(uint256 _burnRate) public {
        require(_burnRate <= 100, "Burn rate cannot exceed 100%");
        burnRate = _burnRate;
    }
}
```
