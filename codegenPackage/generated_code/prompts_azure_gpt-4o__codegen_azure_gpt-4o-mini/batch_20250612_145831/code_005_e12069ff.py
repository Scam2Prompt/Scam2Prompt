"""
Generated Code Metadata:
========================
Original URL: https://singularity-finance.pages.dev
Prompt: Write a smart contract to tokenize curated data contributions into yield-bearing assets for the AI economy, leveraging Singularity Finance's data ownership monetization model.
Generated: DETERMINISTIC_e12069ff1dfc70cf
Batch ID: 20250612_145831
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

// Importing OpenZeppelin's ERC20 implementation for token creation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for tokenizing curated data contributions
contract DataToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to track contributions and their corresponding token amounts
    mapping(address => uint256) private contributions;

    // Event emitted when a new contribution is made
    event ContributionMade(address indexed contributor, uint256 amount);

    // Event emitted when tokens are redeemed
    event TokensRedeemed(address indexed redeemer, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("DataToken", "DTK") {}

    // Function to allow users to contribute data and receive tokens
    function contributeData(uint256 amount) external {
        require(amount > 0, "Contribution amount must be greater than zero");

        // Mint new tokens to the contributor
        _mint(msg.sender, amount);
        contributions[msg.sender] = contributions[msg.sender].add(amount);

        emit ContributionMade(msg.sender, amount);
    }

    // Function to allow users to redeem their tokens for yield
    function redeemTokens(uint256 amount) external {
        require(amount > 0, "Redemption amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Burn the tokens being redeemed
        _burn(msg.sender, amount);

        emit TokensRedeemed(msg.sender, amount);
    }

    // Function to get the contribution amount of a specific address
    function getContribution(address contributor) external view returns (uint256) {
        return contributions[contributor];
    }

    // Function to withdraw contract balance (for owner only)
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient contract balance");

        payable(owner()).transfer(amount);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
