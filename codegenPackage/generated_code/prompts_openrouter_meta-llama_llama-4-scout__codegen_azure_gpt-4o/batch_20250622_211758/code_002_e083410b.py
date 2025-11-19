"""
Generated Code Metadata:
========================
Original URL: https://cloneforce.xyz
Prompt: Generate a smart contract code in Solidity to implement a burning utility for digital assets, similar to the one mentioned on the Clone Force website.
Generated: DETERMINISTIC_e083410b087e282c
Batch ID: 20250622_211758
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
 * @title BurnableToken
 * @dev A smart contract to implement a burning utility for digital assets.
 * Users can burn their tokens, reducing the total supply.
 */
contract BurnableToken {
    // State variables
    string public name = "BurnableToken";
    string public symbol = "BURN";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances of each address
    mapping(address => uint256) private balances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Burn(address indexed burner, uint256 value);

    // Constructor to initialize the total supply and assign it to the deployer
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the balance of a specific address.
     * @param _owner The address to query the balance of.
     * @return The balance of the specified address.
     */
    function balanceOf(address _owner) public view returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param _to The address to transfer to.
     * @param _value The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Burns a specific amount of tokens from the caller's account.
     * @param _value The amount of tokens to burn.
     * @return A boolean indicating whether the burn was successful.
     */
    function burn(uint256 _value) public returns (bool) {
        require(balances[msg.sender] >= _value, "Insufficient balance to burn");

        balances[msg.sender] -= _value;
        totalSupply -= _value;

        emit Burn(msg.sender, _value);
        return true;
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers to the contract.
     */
    fallback() external payable {
        revert("Contract does not accept Ether");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers to the contract.
     */
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
