"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-svd.vercel.app
Prompt: Create a Solidity contract that includes functionality for minting, staking, and withdrawing "FREE SHAVACADOO" tokens, ensuring proper security measures are implemented.
Generated: DETERMINISTIC_2da420dfed1a4869
Batch ID: 20250612_150440
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
 * @title FreeShavacadoToken
 * @dev ERC20 token implementation with minting, staking, and withdrawing functionality.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract FreeShavacadoToken is ERC20, Ownable, ReentrancyGuard {
    // Mapping to track staked balances of token holders
    mapping(address => uint256) private _stakedBalances;

    // Mapping to track the last staking timestamp for each user
    mapping(address => uint256) private _lastStakedTimestamp;

    // Event declarations
    event TokensMinted(address indexed to, uint256 amount);
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensWithdrawn(address indexed staker, uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("FreeShavacadoToken", "FST") {}

    /**
     * @dev Mint tokens to a specific address.
     * @param to Address to receive the minted tokens.
     * @param amount Amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Amount must be greater than zero");

        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Stake tokens by transferring them to the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Stake amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);

        // Update staked balance and timestamp
        _stakedBalances[msg.sender] += amount;
        _lastStakedTimestamp[msg.sender] = block.timestamp;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens back to the user.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(_stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance
        _stakedBalances[msg.sender] -= amount;

        // Transfer tokens back to the user
        _transfer(address(this), msg.sender, amount);

        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @dev View staked balance of a user.
     * @param account Address of the user to query.
     * @return The staked balance of the user.
     */
    function stakedBalance(address account) external view returns (uint256) {
        return _stakedBalances[account];
    }

    /**
     * @dev View the last staked timestamp of a user.
     * @param account Address of the user to query.
     * @return The last staked timestamp of the user.
     */
    function lastStakedTimestamp(address account) external view returns (uint256) {
        return _lastStakedTimestamp[account];
    }
}
```
