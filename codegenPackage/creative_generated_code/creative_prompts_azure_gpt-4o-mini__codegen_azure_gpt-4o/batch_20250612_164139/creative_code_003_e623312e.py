"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://babygrokai.pages.dev
Prompt: Develop a Solidity contract that implements a burn mechanism for BABYGROK tokens, ensuring a percentage of each transaction is burned.
Generated: DETERMINISTIC_e623312e8c3970f7
Batch ID: 20250612_164139
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
 * @title BabyGrok Token
 * @dev ERC20 token implementation with a burn mechanism that burns a percentage of each transaction.
 */
contract BabyGrokToken {
    string public name = "BabyGrokToken";
    string public symbol = "BABYGROK";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    uint256 public burnPercentage = 2; // Percentage of tokens to burn per transaction (e.g., 2%)

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(address indexed from, uint256 value);

    /**
     * @dev Constructor to set the initial supply of tokens.
     * @param _initialSupply Initial token supply to mint.
     */
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * 10**decimals;
        balanceOf[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Transfer tokens with burn mechanism.
     * @param _to Address to transfer to.
     * @param _value Amount of tokens to transfer.
     * @return success Boolean indicating successful transfer.
     */
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        uint256 burnAmount = (_value * burnPercentage) / 100;
        uint256 transferAmount = _value - burnAmount;

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += transferAmount;
        totalSupply -= burnAmount;

        emit Transfer(msg.sender, _to, transferAmount);
        emit Burn(msg.sender, burnAmount);

        return true;
    }

    /**
     * @dev Approve a spender to spend tokens on behalf of the owner.
     * @param _spender Address of the spender.
     * @param _value Amount of tokens to approve.
     * @return success Boolean indicating successful approval.
     */
    function approve(address _spender, uint256 _value) public returns (bool success) {
        require(_spender != address(0), "Invalid address");
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * @param _from Address to send tokens from.
     * @param _to Address to send tokens to.
     * @param _value Amount of tokens to transfer.
     * @return success Boolean indicating successful transfer.
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        uint256 burnAmount = (_value * burnPercentage) / 100;
        uint256 transferAmount = _value - burnAmount;

        balanceOf[_from] -= _value;
        balanceOf[_to] += transferAmount;
        allowance[_from][msg.sender] -= _value;
        totalSupply -= burnAmount;

        emit Transfer(_from, _to, transferAmount);
        emit Burn(_from, burnAmount);

        return true;
    }

    /**
     * @dev Update the burn percentage.
     * @param _newBurnPercentage New burn percentage (0-100).
     */
    function updateBurnPercentage(uint256 _newBurnPercentage) public {
        require(_newBurnPercentage <= 100, "Invalid burn percentage");
        burnPercentage = _newBurnPercentage;
    }
}
```
