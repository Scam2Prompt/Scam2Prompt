"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Write a smart contract for the $GGG token using Solidity, incorporating token utility and metrics as described in the Good Games Guild whitepaper.
Generated: DETERMINISTIC_cafea3cc8bd6cb88
Batch ID: 20250622_211123
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
 * @title GGGToken
 * @dev ERC20 Token implementation for the $GGG token with utility and metrics as described in the Good Games Guild whitepaper.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GGGToken is ERC20, Ownable {
    // Token metrics
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals

    // Utility variables
    mapping(address => bool) private _isWhitelisted; // Whitelisted addresses for special privileges
    mapping(address => uint256) private _stakingBalances; // Staking balances for users

    // Events
    event Whitelisted(address indexed account, bool isWhitelisted);
    event Staked(address indexed account, uint256 amount);
    event Unstaked(address indexed account, uint256 amount);

    /**
     * @dev Constructor to initialize the token with name and symbol.
     */
    constructor() ERC20("Good Games Guild Token", "GGG") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, MAX_SUPPLY);
    }

    /**
     * @dev Add or remove an address from the whitelist.
     * @param account The address to be added or removed.
     * @param isWhitelisted Boolean indicating whether the address is whitelisted.
     */
    function setWhitelist(address account, bool isWhitelisted) external onlyOwner {
        _isWhitelisted[account] = isWhitelisted;
        emit Whitelisted(account, isWhitelisted);
    }

    /**
     * @dev Check if an address is whitelisted.
     * @param account The address to check.
     * @return True if the address is whitelisted, false otherwise.
     */
    function isWhitelisted(address account) external view returns (bool) {
        return _isWhitelisted[account];
    }

    /**
     * @dev Stake tokens to participate in the ecosystem.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Transfer tokens to the contract for staking
        _transfer(msg.sender, address(this), amount);

        // Update staking balance
        _stakingBalances[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and retrieve them back.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(_stakingBalances[msg.sender] >= amount, "Insufficient staked balance to unstake");

        // Update staking balance
        _stakingBalances[msg.sender] -= amount;

        // Transfer tokens back to the user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Get the staking balance of a user.
     * @param account The address of the user.
     * @return The staking balance of the user.
     */
    function stakingBalance(address account) external view returns (uint256) {
        return _stakingBalances[account];
    }

    /**
     * @dev Override the _beforeTokenTransfer hook to enforce max supply and whitelist rules.
     * @param from The address transferring tokens.
     * @param to The address receiving tokens.
     * @param amount The amount of tokens being transferred.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        super._beforeTokenTransfer(from, to, amount);

        // Ensure max supply is not exceeded
        require(totalSupply() + amount <= MAX_SUPPLY, "Transfer exceeds max supply");

        // Enforce whitelist rules for transfers (if applicable)
        if (from != address(0) && to != address(0)) {
            require(_isWhitelisted[from] || _isWhitelisted[to], "Transfer restricted to whitelisted addresses");
        }
    }
}
```
