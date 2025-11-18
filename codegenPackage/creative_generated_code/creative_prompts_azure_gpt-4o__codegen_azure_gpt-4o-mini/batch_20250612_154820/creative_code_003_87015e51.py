"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimalvara.pages.dev
Prompt: Create a Solidity function to mint BTS LP tokens for contributors based on their percentage share of the fund, and burn LP tokens during withdrawals, following the ERC-7621 standard.
Generated: DETERMINISTIC_87015e51471e8da3
Batch ID: 20250612_154820
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

// Import the ERC777 interface to ensure compliance with the standard
import "@openzeppelin/contracts/token/ERC777/IERC777.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the ERC-7621 standard
interface IERC7621 {
    function mint(address to, uint256 amount) external;
    function burn(address from, uint256 amount) external;
}

// FundManager contract to manage contributions and LP tokens
contract FundManager is Ownable {
    // Mapping to track contributors and their shares
    mapping(address => uint256) public contributions;
    uint256 public totalContributions;

    // Reference to the LP token contract
    IERC777 public lpToken;

    // Event emitted when LP tokens are minted
    event LPTokensMinted(address indexed contributor, uint256 amount);
    // Event emitted when LP tokens are burned
    event LPTokensBurned(address indexed contributor, uint256 amount);

    // Constructor to initialize the LP token contract
    constructor(IERC777 _lpToken) {
        lpToken = _lpToken;
    }

    // Function to contribute to the fund
    function contribute(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Update total contributions and individual contributor's share
        contributions[msg.sender] += amount;
        totalContributions += amount;

        // Mint LP tokens based on the contribution percentage
        uint256 lpAmount = calculateLPTokens(amount);
        lpToken.mint(msg.sender, lpAmount);
        emit LPTokensMinted(msg.sender, lpAmount);
    }

    // Function to withdraw and burn LP tokens
    function withdraw(uint256 amount) external {
        uint256 contributorShare = contributions[msg.sender];
        require(contributorShare > 0, "No contributions found");
        require(amount <= contributorShare, "Not enough LP tokens to withdraw");

        // Burn LP tokens equivalent to the withdrawal request
        lpToken.burn(msg.sender, amount);
        emit LPTokensBurned(msg.sender, amount);

        // Update contributions and total contributions
        contributions[msg.sender] -= amount;
        totalContributions -= amount;
    }

    // Internal function to calculate LP tokens based on contribution
    function calculateLPTokens(uint256 amount) internal view returns (uint256) {
        if (totalContributions == 0) {
            return amount; // If no contributions, mint 1:1
        }
        return (amount * totalContributions) / totalContributions;
    }
}
```
