"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumbull.pages.dev
Prompt: Develop a Solidity function to implement airdrop mechanics for a meme coin, inspired by $EBULL's roadmap events like "Bull Stampede" and "Bull Party."
Generated: DETERMINISTIC_7b7777d66ea06388
Batch ID: 20250612_150226
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
 * @title MemeCoinAirdrop
 * @dev Implements airdrop mechanics for a meme coin.
 * Inspired by $EBULL's roadmap events like "Bull Stampede" and "Bull Party".
 */
contract MemeCoinAirdrop {
    // State variables
    address public owner; // Owner of the contract
    mapping(address => uint256) public balances; // Token balances of users

    // Events
    event TokensAirdropped(address indexed recipient, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor() {
        // Initialize contract with the deployer as the owner
        owner = msg.sender;
    }

    /**
     * @dev Transfers ownership of the contract to a new address.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Airdrops tokens to multiple addresses.
     * @param recipients An array of recipient addresses.
     * @param amounts An array of token amounts corresponding to each recipient.
     */
    function airdropTokens(address[] memory recipients, uint256[] memory amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts arrays must have the same length");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint256 amount = amounts[i];

            require(recipient != address(0), "Recipient address cannot be zero");
            require(amount > 0, "Amount must be greater than zero");

            // Update recipient balance (assuming the contract holds the tokens)
            balances[recipient] += amount;

            // Emit event
            emit TokensAirdropped(recipient, amount);
        }
    }

    /**
     * @dev Gets the balance of a specific address.
     * @param account The address to query the balance of.
     * @return The balance of the account.
     */
    function getBalance(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Fallback function to accept Ether (not used in the airdrop logic).
     */
    receive() external payable {}

    /**
     * @dev Withdraw Ether from the contract. Only accessible by the owner.
     * @param amount The amount of Ether to withdraw.
     */
    function withdrawEther(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        payable(owner).transfer(amount);
    }
}
```
