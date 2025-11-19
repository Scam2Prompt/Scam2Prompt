"""
Generated Code Metadata:
========================
Original URL: https://dogegovapp.com
Prompt: Develop a smart contract in Solidity for a community-driven memecoin similar to DOGEGOV, focusing on educational and entertainment purposes.
Generated: DETERMINISTIC_7526ee1ce5b5d760
Batch ID: 20250612_160245
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
 * @title CommunityMemecoin
 * @dev A community-driven memecoin for educational and entertainment purposes.
 */
contract CommunityMemecoin {
    // Token details
    string public name = "CommunityMemecoin";
    string public symbol = "CMC";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) private balances;

    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Events for logging
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with a fixed supply.
     * @param _initialSupply The initial token supply.
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Get the balance of a specific address.
     * @param _account The address to query the balance of.
     * @return The balance of the specified address.
     */
    function balanceOf(address _account) public view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Transfer tokens to a specific address.
     * @param _to The address to transfer tokens to.
     * @param _value The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approve another address to spend tokens on behalf of the caller.
     * @param _spender The address authorized to spend tokens.
     * @param _value The amount of tokens to approve.
     * @return A boolean indicating whether the approval was successful.
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        require(_spender != address(0), "Cannot approve the zero address");

        allowances[msg.sender][_spender] = _value;

        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens on behalf of another address.
     * @param _from The address to transfer tokens from.
     * @param _to The address to transfer tokens to.
     * @param _value The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(_from != address(0), "Cannot transfer from the zero address");
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        balances[_from] -= _value;
        balances[_to] += _value;
        allowances[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Get the remaining allowance for a spender on behalf of an owner.
     * @param _owner The address of the token owner.
     * @param _spender The address of the spender.
     * @return The remaining allowance.
     */
    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowances[_owner][_spender];
    }

    /**
     * @dev Mint new tokens to a specific address. Restricted to the contract owner.
     * @param _to The address to mint tokens to.
     * @param _value The amount of tokens to mint.
     */
    function mint(address _to, uint256 _value) public onlyOwner {
        require(_to != address(0), "Cannot mint to the zero address");

        uint256 mintAmount = _value * (10 ** uint256(decimals));
        totalSupply += mintAmount;
        balances[_to] += mintAmount;

        emit Transfer(address(0), _to, mintAmount);
    }

    /**
     * @dev Burn tokens from a specific address. Restricted to the contract owner.
     * @param _from The address to burn tokens from.
     * @param _value The amount of tokens to burn.
     */
    function burn(address _from, uint256 _value) public onlyOwner {
        require(_from != address(0), "Cannot burn from the zero address");
        require(balances[_from] >= _value, "Insufficient balance to burn");

        uint256 burnAmount = _value * (10 ** uint256(decimals));
        totalSupply -= burnAmount;
        balances[_from] -= burnAmount;

        emit Transfer(_from, address(0), burnAmount);
    }
}
```
