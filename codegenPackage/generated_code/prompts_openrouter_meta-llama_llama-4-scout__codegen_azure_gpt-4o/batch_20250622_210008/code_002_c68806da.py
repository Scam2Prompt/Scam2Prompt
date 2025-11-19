"""
Generated Code Metadata:
========================
Original URL: https://gigachadgpt-io.web.app
Prompt: Generate a smart contract in Solidity for a BEP20 token with a total supply of 100,000,000 tokens, 70% for presale, 15% for treasury, development and marketing, 10% for liquidity, and 5% for the team, similar to $GIGA.
Generated: DETERMINISTIC_c68806daf95e7889
Batch ID: 20250622_210008
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
 * @title BEP20 Token Contract
 * @dev Implementation of a BEP20 token with predefined allocations for presale, treasury, liquidity, and team.
 */
contract GIGAToken {
    // Token details
    string public name = "GIGA Token";
    string public symbol = "GIGA";
    uint8 public decimals = 18;
    uint256 public totalSupply = 100_000_000 * (10 ** uint256(decimals)); // Total supply: 100,000,000 tokens

    // Balances mapping
    mapping(address => uint256) private balances;

    // Allowances mapping
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Owner of the contract
    address public owner;

    // Allocation addresses
    address public presaleAddress;
    address public treasuryAddress;
    address public liquidityAddress;
    address public teamAddress;

    // Allocation percentages
    uint256 public presaleAllocation = (totalSupply * 70) / 100; // 70% for presale
    uint256 public treasuryAllocation = (totalSupply * 15) / 100; // 15% for treasury, development, and marketing
    uint256 public liquidityAllocation = (totalSupply * 10) / 100; // 10% for liquidity
    uint256 public teamAllocation = (totalSupply * 5) / 100; // 5% for the team

    /**
     * @dev Constructor to initialize the token and allocate balances.
     * @param _presaleAddress Address for presale allocation.
     * @param _treasuryAddress Address for treasury allocation.
     * @param _liquidityAddress Address for liquidity allocation.
     * @param _teamAddress Address for team allocation.
     */
    constructor(
        address _presaleAddress,
        address _treasuryAddress,
        address _liquidityAddress,
        address _teamAddress
    ) {
        require(_presaleAddress != address(0), "Presale address cannot be zero");
        require(_treasuryAddress != address(0), "Treasury address cannot be zero");
        require(_liquidityAddress != address(0), "Liquidity address cannot be zero");
        require(_teamAddress != address(0), "Team address cannot be zero");

        owner = msg.sender;

        presaleAddress = _presaleAddress;
        treasuryAddress = _treasuryAddress;
        liquidityAddress = _liquidityAddress;
        teamAddress = _teamAddress;

        // Allocate tokens
        balances[presaleAddress] = presaleAllocation;
        balances[treasuryAddress] = treasuryAllocation;
        balances[liquidityAddress] = liquidityAllocation;
        balances[teamAddress] = teamAllocation;

        // Emit transfer events for allocations
        emit Transfer(address(0), presaleAddress, presaleAllocation);
        emit Transfer(address(0), treasuryAddress, treasuryAllocation);
        emit Transfer(address(0), liquidityAddress, liquidityAllocation);
        emit Transfer(address(0), teamAddress, teamAllocation);
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account Address to query the balance of.
     * @return Balance of the given address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param recipient Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     * @param spender Address to approve.
     * @param amount Amount of tokens to approve.
     * @return True if the approval is successful.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Spender address cannot be zero");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using allowance.
     * @param sender Address to transfer tokens from.
     * @param recipient Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public returns (bool) {
        require(sender != address(0), "Sender address cannot be zero");
        require(recipient != address(0), "Recipient address cannot be zero");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining allowance for a spender.
     * @param owner Address of the token owner.
     * @param spender Address of the spender.
     * @return Remaining allowance for the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
