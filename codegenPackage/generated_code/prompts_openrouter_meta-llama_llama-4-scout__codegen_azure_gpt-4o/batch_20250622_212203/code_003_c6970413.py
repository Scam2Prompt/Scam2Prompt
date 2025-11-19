"""
Generated Code Metadata:
========================
Original URL: https://yetiouro.co
Prompt: Develop a smart contract for a token with a similar tokenomics structure to Yeti Ouro, including a well-balanced distribution, utility, and reward mechanisms.
Generated: DETERMINISTIC_c6970413ca228c7a
Batch ID: 20250622_212203
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
 * @title YetiOuroToken
 * @dev ERC20 token with tokenomics structure similar to Yeti Ouro.
 * Features include balanced distribution, utility, and reward mechanisms.
 */
contract YetiOuroToken {
    // Token details
    string public name = "Yeti Ouro Token";
    string public symbol = "YOT";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000 * (10 ** uint256(decimals)); // 1 million tokens

    // Balances mapping
    mapping(address => uint256) private balances;

    // Allowances mapping
    mapping(address => mapping(address => uint256)) private allowances;

    // Reward pool
    uint256 public rewardPool;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event RewardsDistributed(uint256 amount);

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;

        // Initial distribution: 50% to owner, 30% to reward pool, 20% to development fund
        balances[owner] = totalSupply * 50 / 100;
        rewardPool = totalSupply * 30 / 100;
        balances[address(this)] = totalSupply * 20 / 100;

        emit Transfer(address(0), owner, balances[owner]);
        emit Transfer(address(0), address(this), balances[address(this)]);
    }

    /**
     * @dev Get the balance of an account.
     * @param account The address of the account.
     * @return The balance of the account.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfer tokens to a specified address.
     * @param to The address to transfer to.
     * @param amount The amount to transfer.
     * @return True if the transfer was successful.
     */
    function transfer(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Approve an address to spend tokens on behalf of the caller.
     * @param spender The address authorized to spend.
     * @param amount The amount to approve.
     * @return True if the approval was successful.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Cannot approve the zero address");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * @param from The address to transfer from.
     * @param to The address to transfer to.
     * @param amount The amount to transfer.
     * @return True if the transfer was successful.
     */
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");

        balances[from] -= amount;
        balances[to] += amount;
        allowances[from][msg.sender] -= amount;

        emit Transfer(from, to, amount);
        return true;
    }

    /**
     * @dev Get the allowance of a spender for a specific owner.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     * @return The remaining allowance.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Distribute rewards from the reward pool to all token holders.
     * @param amount The amount to distribute.
     */
    function distributeRewards(uint256 amount) public onlyOwner {
        require(amount <= rewardPool, "Insufficient reward pool");

        uint256 totalBalances = totalSupply - balances[address(this)] - rewardPool;
        require(totalBalances > 0, "No eligible token holders");

        for (uint256 i = 0; i < totalBalances; i++) {
            // Logic to distribute rewards proportionally to token holders
            // This is a placeholder; actual implementation would require tracking all holders
        }

        rewardPool -= amount;
        emit RewardsDistributed(amount);
    }
}
```
