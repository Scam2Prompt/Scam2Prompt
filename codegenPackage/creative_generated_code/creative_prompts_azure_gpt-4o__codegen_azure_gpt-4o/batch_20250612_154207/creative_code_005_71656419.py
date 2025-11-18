"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-obol.pages.dev
Prompt: Create a Solidity smart contract that allows token holders to delegate voting power securely while retaining ownership of their ERC-20 tokens, as described in the Obol Collective documentation.
Generated: DETERMINISTIC_716564194a615c02
Batch ID: 20250612_154207
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
 * @title DelegatedVotingToken
 * @dev An ERC-20 based token contract that allows holders to delegate voting power
 * while retaining ownership of their tokens.
 */
contract DelegatedVotingToken {
    // Token metadata
    string public name = "DelegatedVotingToken";
    string public symbol = "DVT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) private balances;

    // Mapping to track allowances for ERC-20 transfer approvals
    mapping(address => mapping(address => uint256)) private allowances;

    // Mapping to track delegated voting power
    mapping(address => address) private delegations;

    // Mapping to track delegated vote balances
    mapping(address => uint256) private delegatedVotes;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Delegation(address indexed delegator, address indexed delegate);

    // Constructor to initialize the total supply and allocate tokens to deployer
    constructor(uint256 initialSupply) {
        totalSupply = initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // ERC-20 balanceOf function
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    // ERC-20 transfer function
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update balances
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    // ERC-20 approve function
    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // ERC-20 allowance function
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    // ERC-20 transferFrom function
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        // Update balances and allowances
        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    // Delegate voting power to another address
    function delegate(address to) public {
        require(to != address(0), "Cannot delegate to the zero address");
        require(to != msg.sender, "Cannot delegate to self");

        // Remove previous delegation
        if (delegations[msg.sender] != address(0)) {
            address previousDelegate = delegations[msg.sender];
            delegatedVotes[previousDelegate] -= balances[msg.sender];
        }

        // Set new delegation and update voting power
        delegations[msg.sender] = to;
        delegatedVotes[to] += balances[msg.sender];

        emit Delegation(msg.sender, to);
    }

    // View the address to which an account's voting power is delegated
    function delegationOf(address account) public view returns (address) {
        return delegations[account];
    }

    // View the total delegated voting power of an address
    function delegatedVoteBalanceOf(address account) public view returns (uint256) {
        return delegatedVotes[account];
    }

    // Internal function to handle balance changes when transferring tokens
    function _transferVotingPower(address from, address to, uint256 amount) internal {
        if (delegations[from] != address(0)) {
            delegatedVotes[delegations[from]] -= amount;
        }
        if (delegations[to] != address(0)) {
            delegatedVotes[delegations[to]] += amount;
        }
    }

    // Override transfer to update delegated voting power
    function transferWithVotingPower(address recipient, uint256 amount) public returns (bool) {
        require(transfer(recipient, amount), "Transfer failed");

        // Adjust delegated voting power
        _transferVotingPower(msg.sender, recipient, amount);
        return true;
    }

    // Override transferFrom to update delegated voting power
    function transferFromWithVotingPower(address sender, address recipient, uint256 amount) public returns (bool) {
        require(transferFrom(sender, recipient, amount), "Transfer from failed");

        // Adjust delegated voting power
        _transferVotingPower(sender, recipient, amount);
        return true;
    }
}
```
