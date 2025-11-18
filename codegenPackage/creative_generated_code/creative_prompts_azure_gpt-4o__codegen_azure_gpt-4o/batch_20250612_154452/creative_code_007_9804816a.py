"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://growbit.tech
Prompt: Write a Solidity contract for tokenomics similar to GrowBTC, including features like capped supply, locked tokens for a specific duration, and transparent allocation.
Generated: DETERMINISTIC_9804816a794b483a
Batch ID: 20250612_154452
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
 * @title Tokenomics Contract
 * @dev A token contract with capped supply, lock functionality, and transparent allocation.
 */
contract GrowBTC {
    // ERC20 standard variables
    string public name = "GrowBTC";
    string public symbol = "GBTC";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Maximum token supply cap
    uint256 public immutable cap;

    // Mapping for balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Locking mechanism
    struct LockedBalance {
        uint256 amount;
        uint256 unlockTime;
    }
    mapping(address => LockedBalance) private lockedBalances;

    // Owner address for administrative tasks
    address public owner;

    // Events for transparency
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event TokensLocked(address indexed account, uint256 amount, uint256 unlockTime);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier notLocked(address account, uint256 amount) {
        require(
            balances[account] - lockedBalances[account].amount >= amount,
            "Requested amount exceeds unlocked balance"
        );
        _;
    }

    /**
     * @dev Constructor to initialize the token contract.
     * @param _cap Maximum supply cap for the token.
     */
    constructor(uint256 _cap) {
        require(_cap > 0, "Cap must be greater than 0");
        cap = _cap;
        owner = msg.sender;
    }

    /**
     * @dev Mint new tokens, adhering to the supply cap.
     * @param account Address to receive the minted tokens.
     * @param amount Number of tokens to mint.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        require(totalSupply + amount <= cap, "Minting exceeds cap");
        require(account != address(0), "Cannot mint to the zero address");

        totalSupply += amount;
        balances[account] += amount;

        emit Transfer(address(0), account, amount);
    }

    /**
     * @dev Transfer tokens to another account.
     * @param to Recipient address.
     * @param amount Number of tokens to transfer.
     */
    function transfer(address to, uint256 amount)
        external
        notLocked(msg.sender, amount)
        returns (bool)
    {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Approve another account to spend tokens on behalf of the caller.
     * @param spender Address to be approved to spend tokens.
     * @param amount Number of tokens to approve.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Cannot approve the zero address");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens from one account to another, using allowance.
     * @param from Source address.
     * @param to Recipient address.
     * @param amount Number of tokens to transfer.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) external returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");
        require(balances[from] >= amount, "Insufficient balance");

        allowances[from][msg.sender] -= amount;
        balances[from] -= amount;
        balances[to] += amount;

        emit Transfer(from, to, amount);
        return true;
    }

    /**
     * @dev Lock a specific amount of tokens for a duration.
     * @param account Address whose tokens will be locked.
     * @param amount Number of tokens to lock.
     * @param duration Duration (in seconds) for which tokens will be locked.
     */
    function lockTokens(
        address account,
        uint256 amount,
        uint256 duration
    ) external onlyOwner {
        require(account != address(0), "Cannot lock tokens for the zero address");
        require(balances[account] >= amount, "Insufficient balance to lock");

        lockedBalances[account].amount += amount;
        lockedBalances[account].unlockTime = block.timestamp + duration;

        emit TokensLocked(account, amount, lockedBalances[account].unlockTime);
    }

    /**
     * @dev Check if tokens for an account are unlocked.
     * @param account Address to check.
     */
    function unlockedBalance(address account) external view returns (uint256) {
        if (block.timestamp >= lockedBalances[account].unlockTime) {
            return balances[account];
        } else {
            return balances[account] - lockedBalances[account].amount;
        }
    }

    /**
     * @dev View the balance of an account.
     * @param account Address to check.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev View the allowance between accounts.
     * @param owner Owner of the tokens.
     * @param spender Spender who is approved to use tokens.
     */
    function allowance(address owner, address spender)
        external
        view
        returns (uint256)
    {
        return allowances[owner][spender];
    }
}
```
