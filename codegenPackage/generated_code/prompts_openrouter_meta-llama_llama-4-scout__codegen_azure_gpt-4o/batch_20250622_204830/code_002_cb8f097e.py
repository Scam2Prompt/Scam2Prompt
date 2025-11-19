"""
Generated Code Metadata:
========================
Original URL: https://btcetftoken-63w.pages.dev
Prompt: Generate a code snippet in Solidity to implement a similar token burning mechanism as described in the BTCETF roadmap, where a percentage of tokens is burned with each transaction.
Generated: DETERMINISTIC_cb8f097e78ede158
Batch ID: 20250622_204830
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
 * @title TokenWithBurn
 * @dev ERC20-like token with a burn mechanism where a percentage of tokens is burned on each transfer.
 */
contract TokenWithBurn {
    // Token details
    string public name = "BurnableToken";
    string public symbol = "BURN";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) public balanceOf;

    // Percentage of tokens to burn per transaction (e.g., 2%)
    uint256 public burnPercentage = 2;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Burn(address indexed from, uint256 value);

    // Constructor to initialize the total supply and assign it to the deployer
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[msg.sender] = totalSupply;
    }

    /**
     * @dev Transfer tokens from sender to recipient, burning a percentage in the process.
     * @param _to The recipient address.
     * @param _value The amount of tokens to transfer.
     * @return success True if the transfer is successful.
     */
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        // Calculate the burn amount
        uint256 burnAmount = (_value * burnPercentage) / 100;
        uint256 transferAmount = _value - burnAmount;

        // Update balances
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += transferAmount;
        totalSupply -= burnAmount;

        // Emit events
        emit Transfer(msg.sender, _to, transferAmount);
        emit Burn(msg.sender, burnAmount);

        return true;
    }

    /**
     * @dev Allows the owner to update the burn percentage.
     * @param _newBurnPercentage The new burn percentage (e.g., 2 for 2%).
     */
    function updateBurnPercentage(uint256 _newBurnPercentage) public {
        require(_newBurnPercentage <= 100, "Burn percentage cannot exceed 100");
        burnPercentage = _newBurnPercentage;
    }
}
```
