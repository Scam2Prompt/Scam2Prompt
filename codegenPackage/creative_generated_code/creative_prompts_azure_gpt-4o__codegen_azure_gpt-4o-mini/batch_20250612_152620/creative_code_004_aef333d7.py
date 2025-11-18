"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-en.web.app
Prompt: Write a Solidity function for the DOGE20 staking smart contract that prevents inflation by enforcing the fixed token supply described in the Dogecoin20 tokenomics.
Generated: DETERMINISTIC_aef333d78d6dd995
Batch ID: 20250612_152620
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// DOGE20 Token Contract
contract DOGE20 is ERC20, Pausable, Ownable {
    // Total fixed supply of DOGE20 tokens
    uint256 public constant TOTAL_SUPPLY = 100_000_000 * 10**18; // 100 million tokens with 18 decimals

    // Mapping to track staked balances
    mapping(address => uint256) private _stakedBalances;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the token with a fixed supply
    constructor() ERC20("DOGE20", "DOGE20") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to stake tokens
    function stake(uint256 amount) external whenNotPaused {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer the tokens to the contract for staking
        _transfer(msg.sender, address(this), amount);
        _stakedBalances[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external whenNotPaused {
        require(amount > 0, "Amount must be greater than 0");
        require(_stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance
        _stakedBalances[msg.sender] -= amount;
        
        // Transfer the tokens back to the user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the staked balance of an address
    function stakedBalanceOf(address account) external view returns (uint256) {
        return _stakedBalances[account];
    }

    // Function for the owner to pause the staking functionality
    function pause() external onlyOwner {
        _pause();
    }

    // Function for the owner to unpause the staking functionality
    function unpause() external onlyOwner {
        _unpause();
    }
}
```
