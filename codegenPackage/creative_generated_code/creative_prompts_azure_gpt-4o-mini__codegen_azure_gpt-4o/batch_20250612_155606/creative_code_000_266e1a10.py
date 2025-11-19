"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-rectify-presale-url.pages.dev
Prompt: Generate a smart contract in Solidity that implements a token similar to $EARNM, focusing on converting mobile activity into rewards.
Generated: DETERMINISTIC_266e1a10ee3755f6
Batch ID: 20250612_155606
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
 * @title EarnMobileToken
 * @dev A smart contract to implement a token that rewards users for mobile activity.
 */
contract EarnMobileToken {
    // Token details
    string public name = "EarnMobileToken";
    string public symbol = "EARNM";
    uint8 public decimals = 18;

    // Total supply of the token
    uint256 public totalSupply;

    // Balances mapping to track token holdings
    mapping(address => uint256) private balances;

    // Allowances mapping for token approvals
    mapping(address => mapping(address => uint256)) private allowances;

    // Owner of the contract
    address public owner;

    // Event emitted when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Event emitted when an allowance is set
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with a total supply.
     * @param _initialSupply Initial supply of the tokens.
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply; // Assign the entire supply to the owner
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Get the balance of an account.
     * @param _account The address to query the balance of.
     * @return The balance of the account.
     */
    function balanceOf(address _account) public view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Transfer tokens to a specified address.
     * @param _to The address to transfer tokens to.
     * @param _value The amount of tokens to transfer.
     * @return Whether the transfer was successful.
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid recipient address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approve an account to spend tokens on behalf of the caller.
     * @param _spender The address to approve.
     * @param _value The amount of tokens to approve.
     * @return Whether the approval was successful.
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens on behalf of an account.
     * @param _from The address to transfer tokens from.
     * @param _to The address to transfer tokens to.
     * @param _value The amount of tokens to transfer.
     * @return Whether the transfer was successful.
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid recipient address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        balances[_from] -= _value;
        balances[_to] += _value;
        allowances[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Check the allowance of a spender for a given owner.
     * @param _owner The address of the token owner.
     * @param _spender The address of the approved spender.
     * @return The remaining allowance.
     */
    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowances[_owner][_spender];
    }

    /**
     * @dev Reward users for mobile activity. Restricted to owner only.
     * @param _to The address to reward.
     * @param _value The amount of tokens to reward.
     */
    function rewardMobileActivity(address _to, uint256 _value) public onlyOwner {
        require(_to != address(0), "Invalid recipient address");
        require(totalSupply + _value >= totalSupply, "Overflow error");

        totalSupply += _value;
        balances[_to] += _value;

        emit Transfer(address(0), _to, _value);
    }
}
```
