"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chitzoinu.pages.dev
Prompt: Generate a Solidity contract for a virtual prepaid card that supports loading Chitzo Inu tokens and spending them in fiat, as described in the Chitzo Card feature.
Generated: DETERMINISTIC_a38ae09839a54671
Batch ID: 20250612_150622
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
 * @title ChitzoCard
 * @dev A virtual prepaid card contract that supports loading Chitzo Inu tokens and spending them in fiat.
 */

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract ChitzoCard {
    // Address of the Chitzo Inu token contract
    IERC20 public chitzoToken;

    // Owner of the contract
    address public owner;

    // Mapping to keep track of card balances for each user
    mapping(address => uint256) public cardBalances;

    // Event emitted when tokens are loaded onto the card
    event TokensLoaded(address indexed user, uint256 amount);

    // Event emitted when tokens are spent
    event TokensSpent(address indexed user, uint256 amount, string fiatDetails);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the Chitzo Inu token address.
     * @param chitzoTokenAddress Address of the Chitzo Inu token contract.
     */
    constructor(address chitzoTokenAddress) {
        require(chitzoTokenAddress != address(0), "Invalid token address");
        chitzoToken = IERC20(chitzoTokenAddress);
        owner = msg.sender;
    }

    /**
     * @dev Allows users to load Chitzo Inu tokens onto their virtual card.
     * @param amount Amount of tokens to load.
     */
    function loadTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        bool success = chitzoToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the user's card balance
        cardBalances[msg.sender] += amount;

        emit TokensLoaded(msg.sender, amount);
    }

    /**
     * @dev Allows users to spend Chitzo Inu tokens in fiat. Requires sufficient balance.
     * @param amount Amount of tokens to spend.
     * @param fiatDetails Details about the fiat transaction (e.g., merchant name, fiat amount).
     */
    function spendTokens(uint256 amount, string memory fiatDetails) external {
        require(amount > 0, "Amount must be greater than zero");
        require(cardBalances[msg.sender] >= amount, "Insufficient card balance");

        // Deduct the amount from the user's card balance
        cardBalances[msg.sender] -= amount;

        // Transfer the spent tokens back to the contract owner
        bool success = chitzoToken.transfer(owner, amount);
        require(success, "Token transfer failed");

        emit TokensSpent(msg.sender, amount, fiatDetails);
    }

    /**
     * @dev Allows the owner to withdraw any excess tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawExcessTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(chitzoToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        bool success = chitzoToken.transfer(owner, amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Allows the owner to update the Chitzo Inu token address.
     * @param newTokenAddress New address of the Chitzo Inu token contract.
     */
    function updateTokenAddress(address newTokenAddress) external onlyOwner {
        require(newTokenAddress != address(0), "Invalid token address");
        chitzoToken = IERC20(newTokenAddress);
    }
}
```
