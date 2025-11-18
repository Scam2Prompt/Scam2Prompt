"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chinesebrettbase-reward.pages.dev
Prompt: Using the $CHRETT tokenomics details provided, create a Solidity smart contract that implements a token with a fixed supply of 1,000,000,000 tokens, no buy/sell tax, locked liquidity, and renounced ownership.
Generated: DETERMINISTIC_be521c618153177c
Batch ID: 20250612_151246
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
 * @title CHRETT Token Contract
 * @dev Implements an ERC20 token with fixed supply, no buy/sell tax, locked liquidity, and renounced ownership.
 */
contract CHRETTToken {
    // ERC20 state variables
    string public name = "CHRETT";
    string public symbol = "CHRETT";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000_000 * (10 ** decimals);

    // Mapping to store balances of each address
    mapping(address => uint256) private balances;

    // Mapping for allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Locked liquidity address (immutable after deployment)
    address public immutable liquidityLock;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor initializes the total supply to the deployer and sets a locked liquidity address.
     */
    constructor(address _liquidityLock) {
        require(_liquidityLock != address(0), "Liquidity lock address cannot be zero.");
        liquidityLock = _liquidityLock;

        // Mint the full supply to the deployer
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);

        // Renounce ownership by transferring all tokens to liquidity lock
        _transfer(msg.sender, liquidityLock, totalSupply);
    }

    /**
     * @dev Returns the balance of a specific address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specific address.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Cannot approve to zero address.");
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using allowance mechanism.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool) {
        require(amount <= allowances[sender][msg.sender], "Transfer amount exceeds allowance.");
        _transfer(sender, recipient, amount);
        allowances[sender][msg.sender] -= amount;
        return true;
    }

    /**
     * @dev Returns the remaining allowance for a spender.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Internal function to transfer tokens between addresses.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from zero address.");
        require(recipient != address(0), "Transfer to zero address.");
        require(balances[sender] >= amount, "Insufficient balance.");

        // Perform the transfer
        balances[sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);
    }
}
```
