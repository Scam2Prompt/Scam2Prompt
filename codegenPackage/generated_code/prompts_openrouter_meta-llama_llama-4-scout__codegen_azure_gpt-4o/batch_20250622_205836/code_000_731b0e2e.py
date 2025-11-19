"""
Generated Code Metadata:
========================
Original URL: https://pawthereum.pages.dev
Prompt: Write a smart contract in Solidity for a token distribution system similar to Pawthereum's $PAWTH on the BASE network.
Generated: DETERMINISTIC_731b0e2e183129a4
Batch ID: 20250622_205836
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
 * @title TokenDistribution
 * @dev A smart contract for token distribution similar to Pawthereum's $PAWTH.
 * This contract is designed for the BASE network and follows best practices.
 */
contract TokenDistribution {
    // Token details
    string public name = "Pawthereum Token";
    string public symbol = "PAWTH";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) public balanceOf;

    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) public allowance;

    // Events for logging
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfer tokens from the caller to a recipient.
     * @param _to The recipient address.
     * @param _value The amount of tokens to transfer.
     * @return success True if the transfer is successful.
     */
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approve a spender to transfer tokens on behalf of the caller.
     * @param _spender The address authorized to spend.
     * @param _value The amount of tokens to approve.
     * @return success True if the approval is successful.
     */
    function approve(address _spender, uint256 _value) public returns (bool success) {
        require(_spender != address(0), "Invalid spender address");

        allowance[msg.sender][_spender] = _value;

        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * @param _from The address to transfer from.
     * @param _to The recipient address.
     * @param _value The amount of tokens to transfer.
     * @return success True if the transfer is successful.
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Mint new tokens to a specified address. Only callable by the owner.
     * @param _to The address to receive the minted tokens.
     * @param _value The amount of tokens to mint.
     */
    function mint(address _to, uint256 _value) public onlyOwner {
        require(_to != address(0), "Invalid recipient address");

        uint256 mintAmount = _value * (10 ** uint256(decimals));
        totalSupply += mintAmount;
        balanceOf[_to] += mintAmount;

        emit Transfer(address(0), _to, mintAmount);
    }

    /**
     * @dev Burn tokens from a specified address. Only callable by the owner.
     * @param _from The address whose tokens will be burned.
     * @param _value The amount of tokens to burn.
     */
    function burn(address _from, uint256 _value) public onlyOwner {
        require(_from != address(0), "Invalid address");
        require(balanceOf[_from] >= _value, "Insufficient balance");

        uint256 burnAmount = _value * (10 ** uint256(decimals));
        totalSupply -= burnAmount;
        balanceOf[_from] -= burnAmount;

        emit Transfer(_from, address(0), burnAmount);
    }
}
```
