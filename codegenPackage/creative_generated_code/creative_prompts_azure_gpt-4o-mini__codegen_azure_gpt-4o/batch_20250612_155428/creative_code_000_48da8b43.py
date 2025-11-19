"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-is.web.app
Prompt: Generate a smart contract for the $MPEPE token that includes a burn mechanism after every transaction, as described in the Mpeppe presale details.
Generated: DETERMINISTIC_48da8b431bf10095
Batch ID: 20250612_155428
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
 * @notice ERC20-compliant token with a burn mechanism after every transaction.
 * @dev Implements basic ERC20 functionality with a custom burn feature.
 */
contract MPEPEToken {
    // Token details
    string public name = "$MPEPE Token";
    string public symbol = "MPEPE";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances and allowances
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Events to log transactions
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Burn percentage (e.g., 2%)
    uint256 public burnRate = 2;

    /**
     * @dev Constructor to initialize total supply and assign to owner.
     * @param _initialSupply Initial supply of the token (in wei).
     */
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply;
        balanceOf[msg.sender] = _initialSupply; // Assign entire supply to contract deployer
        emit Transfer(address(0), msg.sender, _initialSupply);
    }

    /**
     * @dev Internal function to handle token transfer and burn logic.
     * @param _from Sender address.
     * @param _to Recipient address.
     * @param _value Amount of tokens to transfer.
     */
    function _transfer(address _from, address _to, uint256 _value) internal {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balanceOf[_from] >= _value, "Insufficient balance");

        // Calculate burn amount
        uint256 burnAmount = (_value * burnRate) / 100;
        uint256 transferAmount = _value - burnAmount;

        // Update balances
        balanceOf[_from] -= _value;
        balanceOf[_to] += transferAmount;

        // Burn the tokens
        totalSupply -= burnAmount;

        // Emit events
        emit Transfer(_from, _to, transferAmount);
        emit Transfer(_from, address(0), burnAmount); // Burned tokens
    }

    /**
     * @dev Public function to transfer tokens.
     * @param _to Recipient address.
     * @param _value Amount of tokens to transfer.
     * @return success Boolean indicating success of the operation.
     */
    function transfer(address _to, uint256 _value) public returns (bool success) {
        _transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Public function to approve token allowance.
     * @param _spender Address allowed to spend tokens.
     * @param _value Amount of tokens to approve.
     * @return success Boolean indicating success of the operation.
     */
    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Public function to transfer tokens on behalf of another address.
     * @param _from Sender address.
     * @param _to Recipient address.
     * @param _value Amount of tokens to transfer.
     * @return success Boolean indicating success of the operation.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) public returns (bool success) {
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");
        allowance[_from][msg.sender] -= _value;
        _transfer(_from, _to, _value);
        return true;
    }
}
```
