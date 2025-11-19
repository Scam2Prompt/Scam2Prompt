"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cumcoin.io
Prompt: Generate a smart contract for a meme coin similar to CUM Coin, focusing on cross-border liquidity and zero tax on transactions.
Generated: DETERMINISTIC_ba7f3b5ca7c71626
Batch ID: 20250612_135654
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
 * @title MemeCoin
 * @dev A standard ERC20-compatible meme coin with zero tax on transactions
 *      and features promoting cross-border liquidity.
 */
contract MemeCoin {
    // Token details
    string public name = "MemeCoin";
    string public symbol = "MEME";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Balances mapping
    mapping(address => uint256) private balances;
    // Allowances mapping for ERC20 compliance
    mapping(address => mapping(address => uint256)) private allowances;

    // Owner of the contract
    address public owner;

    // Events for logging important actions
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor initializes the contract with the total supply
     * @param _initialSupply The initial token supply assigned to the owner
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender; // Set the owner of the contract
        totalSupply = _initialSupply * (10 ** uint256(decimals)); // Adjust decimals
        balances[owner] = totalSupply; // Assign the initial supply to the owner

        emit Transfer(address(0), owner, totalSupply); // Emit a transfer event from address(0)
    }

    /**
     * @notice Returns the balance of a given address
     * @param _account The address whose balance to check
     * @return The balance of the given address
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    /**
     * @notice Transfers tokens to a specified address
     * @param _to The recipient address
     * @param _value The amount of tokens to transfer
     * @return success A boolean indicating the success of the transfer
     */
    function transfer(address _to, uint256 _value) external returns (bool success) {
        require(_to != address(0), "Transfer to zero address is not allowed");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        // Perform the transfer
        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value); // Emit transfer event
        return true;
    }

    /**
     * @notice Approves an address to spend tokens on behalf of the caller
     * @param _spender The address allowed to spend the tokens
     * @param _value The amount of tokens to approve
     * @return success A boolean indicating the success of the approval
     */
    function approve(address _spender, uint256 _value) external returns (bool success) {
        require(_spender != address(0), "Approve to zero address is not allowed");

        allowances[msg.sender][_spender] = _value; // Set the allowance

        emit Approval(msg.sender, _spender, _value); // Emit approval event
        return true;
    }

    /**
     * @notice Transfers tokens from one address to another using allowance
     * @param _from The address to transfer tokens from
     * @param _to The address to transfer tokens to
     * @param _value The amount of tokens to transfer
     * @return success A boolean indicating the success of the transfer
     */
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool success) {
        require(_from != address(0), "Transfer from zero address is not allowed");
        require(_to != address(0), "Transfer to zero address is not allowed");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        // Perform the transfer
        balances[_from] -= _value;
        balances[_to] += _value;
        allowances[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value); // Emit transfer event
        return true;
    }

    /**
     * @notice Returns the remaining amount of tokens that a spender is allowed to spend
     * @param _owner The owner of the tokens
     * @param _spender The spender
     * @return The remaining amount of tokens allowed to be spent
     */
    function allowance(address _owner, address _spender) external view returns (uint256) {
        return allowances[_owner][_spender];
    }

    /**
     * @dev Prevent accidental ETH transfers to the contract
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }

    /**
     * @dev Prevent accidental ETH transfers to the contract
     */
    fallback() external payable {
        revert("Fallback function not allowed");
    }
}
```
