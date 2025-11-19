"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum.com-crypto.com
Prompt: Create an example of a Solidity contract that demonstrates token transfer functionality on the Ethereum network.
Generated: DETERMINISTIC_65859cb059a34bac
Batch ID: 20250612_140024
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

/*
 * @title ERC20 Token Contract
 * @dev A basic example of an ERC20 token contract implementing token transfer functionality.
 *      This contract follows the ERC20 standard with additional comments for clarity.
 */
contract ExampleToken {
    // Token details
    string public name = "ExampleToken";
    string public symbol = "EXT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances of each address
    mapping(address => uint256) private balances;
    // Mapping to track allowances for delegated transfers
    mapping(address => mapping(address => uint256)) private allowances;

    // Events for logging actions
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to set the total supply and assign it to the deployer
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** decimals);
        balances[msg.sender] = totalSupply; // Assign all tokens to the contract deployer
        emit Transfer(address(0), msg.sender, totalSupply); // Emit initial transfer event
    }

    /*
     * @dev Get the balance of a specific address.
     * @param _account Address to query the balance of.
     * @return The balance of the specified address.
     */
    function balanceOf(address _account) public view returns (uint256) {
        return balances[_account];
    }

    /*
     * @dev Transfer tokens from the caller's account to another address.
     * @param _to The recipient's address.
     * @param _value Number of tokens to transfer.
     * @return True if the transfer succeeds.
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid address"); // Prevent transferring to zero address
        require(balances[msg.sender] >= _value, "Insufficient balance"); // Ensure sender has enough tokens

        // Perform the transfer
        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value); // Emit transfer event
        return true;
    }

    /*
     * @dev Allow another address to spend tokens on behalf of the caller.
     * @param _spender The address allowed to spend tokens.
     * @param _value The number of tokens to allow.
     * @return True if the approval succeeds.
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        require(_spender != address(0), "Invalid address"); // Prevent approving zero address

        // Set the allowance for the spender
        allowances[msg.sender][_spender] = _value;

        emit Approval(msg.sender, _spender, _value); // Emit approval event
        return true;
    }

    /*
     * @dev Transfer tokens from one address to another using allowance.
     * @param _from The address to transfer tokens from.
     * @param _to The recipient's address.
     * @param _value Number of tokens to transfer.
     * @return True if the transfer succeeds.
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(_from != address(0) && _to != address(0), "Invalid address"); // Prevent transferring to/from zero address
        require(balances[_from] >= _value, "Insufficient balance"); // Ensure sender has enough tokens
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded"); // Ensure allowance is sufficient

        // Perform the transfer
        balances[_from] -= _value;
        balances[_to] += _value;

        // Deduct the spent allowance
        allowances[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value); // Emit transfer event
        return true;
    }

    /*
     * @dev Get the remaining allowance for a spender from a specific address.
     * @param _owner The address owning the tokens.
     * @param _spender The address allowed to spend the tokens.
     * @return The remaining allowance.
     */
    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowances[_owner][_spender];
    }
}
```
