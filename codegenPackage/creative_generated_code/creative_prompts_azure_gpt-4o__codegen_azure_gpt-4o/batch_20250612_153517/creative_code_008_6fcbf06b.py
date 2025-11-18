"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mong-life-mong.pages.dev
Prompt: Write a smart contract to implement a no-tax policy for a memecoin, inspired by $MONG's no-tax feature.
Generated: DETERMINISTIC_6fcbf06bb47df08e
Batch ID: 20250612_153517
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
 * @title NoTaxMemecoin
 * @dev A simple ERC20-compliant token with no tax policy, inspired by $MONG.
 */
contract NoTaxMemecoin {
    string public name = "NoTaxMemecoin";
    string public symbol = "NTMC";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to initialize the total supply and assign it to the deployer
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** decimals);
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the balance of the specified address.
     * @param _owner Address to query the balance of.
     * @return The balance of the provided address.
     */
    function balanceOf(address _owner) external view returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param _to Address to transfer tokens to.
     * @param _value Amount of tokens to transfer.
     * @return True if the transfer is successful, false otherwise.
     */
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Invalid address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        // Perform transfer without any tax
        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approves a spender to spend tokens on behalf of the owner.
     * @param _spender Address to be approved.
     * @param _value Amount of tokens to be approved.
     * @return True if the approval is successful, false otherwise.
     */
    function approve(address _spender, uint256 _value) external returns (bool) {
        require(_spender != address(0), "Invalid address");

        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfers tokens on behalf of the owner, using allowance.
     * @param _from Address from which tokens will be transferred.
     * @param _to Address to transfer tokens to.
     * @param _value Amount of tokens to transfer.
     * @return True if the transfer is successful, false otherwise.
     */
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Invalid address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        // Perform transfer without any tax
        balances[_from] -= _value;
        balances[_to] += _value;
        allowances[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that the spender is allowed to spend.
     * @param _owner Address of the token owner.
     * @param _spender Address of the spender.
     * @return Remaining allowance for the spender.
     */
    function allowance(address _owner, address _spender) external view returns (uint256) {
        return allowances[_owner][_spender];
    }
}
```
