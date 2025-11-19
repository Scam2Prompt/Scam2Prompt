"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Write a Solidity contract to implement Ziber's token distribution rules, ensuring 80% of tokens are available for open sale, 10% are allocated to the team, and 10% are distributed as bonuses to Bitcoin and Ethereum owners.
Generated: DETERMINISTIC_695e97d62b6d8fa4
Batch ID: 20250612_151531
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ZiberToken
 * @dev Implementation of a token with specific distribution rules.
 */
contract ZiberToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals

    // Allocation percentages
    uint256 public constant SALE_ALLOCATION = 80; // 80%
    uint256 public constant TEAM_ALLOCATION = 10; // 10%
    uint256 public constant BONUS_ALLOCATION = 10; // 10%

    // Addresses for team and bonus distribution
    address public teamAddress;
    address public bonusAddress;

    // Event for token distribution
    event TokensDistributed(address indexed to, uint256 amount);

    /**
     * @dev Constructor that sets the token name and symbol, and allocates tokens.
     * @param _teamAddress Address to receive team allocation.
     * @param _bonusAddress Address to receive bonus allocation.
     */
    constructor(address _teamAddress, address _bonusAddress) ERC20("ZiberToken", "ZIBER") {
        require(_teamAddress != address(0), "Invalid team address");
        require(_bonusAddress != address(0), "Invalid bonus address");

        teamAddress = _teamAddress;
        bonusAddress = _bonusAddress;

        // Minting the total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);

        // Distributing tokens according to the allocation rules
        distributeTokens();
    }

    /**
     * @dev Distributes tokens according to the defined allocation rules.
     */
    function distributeTokens() internal {
        uint256 saleAmount = (TOTAL_SUPPLY * SALE_ALLOCATION) / 100;
        uint256 teamAmount = (TOTAL_SUPPLY * TEAM_ALLOCATION) / 100;
        uint256 bonusAmount = (TOTAL_SUPPLY * BONUS_ALLOCATION) / 100;

        // Transfer team allocation
        _transfer(msg.sender, teamAddress, teamAmount);
        emit TokensDistributed(teamAddress, teamAmount);

        // Transfer bonus allocation
        _transfer(msg.sender, bonusAddress, bonusAmount);
        emit TokensDistributed(bonusAddress, bonusAmount);

        // Remaining tokens are available for open sale
        // The saleAmount is already accounted for in the owner's balance
    }

    /**
     * @dev Allows the owner to withdraw any tokens mistakenly sent to the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount <= balanceOf(address(this)), "Insufficient balance");
        _transfer(address(this), msg.sender, _amount);
    }
}
```
