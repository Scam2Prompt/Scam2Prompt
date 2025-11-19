"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimtrumpcion.pages.dev
Prompt: Generate a smart contract for a memecoin on Binance Smart Chain similar to Trumpcoin, focusing on low fees and fast transactions.
Generated: DETERMINISTIC_e684800f87a47b81
Batch ID: 20250612_155859
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
 * @title Memecoin
 * @dev A simple ERC20 token deployed on Binance Smart Chain (BSC) with low fees and fast transactions.
 * @notice This smart contract is production-ready and adheres to best practices.
 */
contract Memecoin {
    // Token metadata
    string public name = "Memecoin";
    string public symbol = "MEME";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Balances mapping
    mapping(address => uint256) private balances;

    // Allowance mapping
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Owner of the contract
    address public owner;

    /**
     * @dev Modifier to restrict access to owner-only functionality.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor that initializes the total supply and assigns it to the contract owner.
     * @param _initialSupply The initial token supply (in wei units).
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10**uint256(decimals));
        balances[owner] = totalSupply;

        // Emit transfer event for initial supply assignment
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Returns the balance of the specified account.
     * @param _account The account address to check the balance for.
     * @return The balance of the account.
     */
    function balanceOf(address _account) public view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param _to The recipient's address.
     * @param _value The amount to transfer (in wei).
     * @return True if the operation was successful.
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        // Perform the transfer
        balances[msg.sender] -= _value;
        balances[_to] += _value;

        // Emit transfer event
        emit Transfer(msg.sender, _to, _value);

        return true;
    }

    /**
     * @dev Approves a spender to transfer a specific amount of tokens on behalf of the caller.
     * @param _spender The address allowed to spend tokens.
     * @param _value The amount of tokens to approve.
     * @return True if the operation was successful.
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        require(_spender != address(0), "Cannot approve the zero address");

        // Set the allowance
        allowances[msg.sender][_spender] = _value;

        // Emit approval event
        emit Approval(msg.sender, _spender, _value);

        return true;
    }

    /**
     * @dev Transfers tokens from one account to another. Requires prior approval.
     * @param _from The address to transfer tokens from.
     * @param _to The recipient's address.
     * @param _value The amount to transfer (in wei).
     * @return True if the operation was successful.
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(_from != address(0), "Cannot transfer from the zero address");
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        // Deduct allowances and perform the transfer
        allowances[_from][msg.sender] -= _value;
        balances[_from] -= _value;
        balances[_to] += _value;

        // Emit transfer event
        emit Transfer(_from, _to, _value);

        return true;
    }

    /**
     * @dev Returns the amount of tokens a spender is allowed to spend on behalf of an owner.
     * @param _owner The address of the token owner.
     * @param _spender The address of the spender.
     * @return The amount of tokens allowed.
     */
    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowances[_owner][_spender];
    }

    /**
     * @dev Allows the contract owner to mint new tokens.
     * @param _to The address to receive the minted tokens.
     * @param _value The amount of tokens to mint (in wei).
     */
    function mint(address _to, uint256 _value) public onlyOwner {
        require(_to != address(0), "Cannot mint to the zero address");

        // Increase the total supply and recipient's balance
        totalSupply += _value;
        balances[_to] += _value;

        // Emit transfer event (from zero address to indicate minting)
        emit Transfer(address(0), _to, _value);
    }

    /**
     * @dev Allows the contract owner to burn tokens from a specific address.
     * @param _from The address to burn tokens from.
     * @param _value The amount of tokens to burn (in wei).
     */
    function burn(address _from, uint256 _value) public onlyOwner {
        require(_from != address(0), "Cannot burn from the zero address");
        require(balances[_from] >= _value, "Insufficient balance to burn");

        // Decrease the total supply and the target balance
        totalSupply -= _value;
        balances[_from] -= _value;

        // Emit transfer event (to zero address to indicate burning)
        emit Transfer(_from, address(0), _value);
    }
}
```
