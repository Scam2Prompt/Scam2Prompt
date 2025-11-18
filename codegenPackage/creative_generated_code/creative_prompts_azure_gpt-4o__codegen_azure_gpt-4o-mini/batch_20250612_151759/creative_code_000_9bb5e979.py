"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owy-wtf.web.app
Prompt: Write a smart contract in Solidity for an Ethereum-based memecoin similar to "Owy," ensuring it includes functionality for token airdrops and manual token connections.
Generated: DETERMINISTIC_9bb5e979f1d738e7
Batch ID: 20250612_151759
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

// Importing OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract OwyCoin is ERC20, Ownable {
    // Event to log the airdrop transaction
    event Airdrop(address indexed recipient, uint256 amount);

    // Mapping to keep track of airdrop eligibility
    mapping(address => bool) public airdropEligible;

    // Constructor to set the token name and symbol
    constructor() ERC20("OwyCoin", "OWY") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    /**
     * @dev Allows the owner to airdrop tokens to multiple addresses
     * @param recipients List of recipient addresses
     * @param amounts List of amounts to send to each recipient
     */
    function airdropTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched arrays length");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid address");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer tokens to each recipient
            _transfer(msg.sender, recipients[i], amounts[i]);
            emit Airdrop(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Allows the owner to mark an address as eligible for the airdrop
     * @param recipient The address to mark as eligible
     */
    function setAirdropEligibility(address recipient) external onlyOwner {
        airdropEligible[recipient] = true;
    }

    /**
     * @dev Allows the owner to remove an address's airdrop eligibility
     * @param recipient The address to remove eligibility
     */
    function removeAirdropEligibility(address recipient) external onlyOwner {
        airdropEligible[recipient] = false;
    }

    /**
     * @dev Allows eligible recipients to claim their airdrop
     * @param amount Amount of tokens to claim
     */
    function claimAirdrop(uint256 amount) external {
        require(airdropEligible[msg.sender], "Not eligible for airdrop");
        require(amount > 0, "Claim amount must be greater than zero");
        require(balanceOf(address(this)) >= amount, "Insufficient airdrop funds");

        // Transfer tokens from the contract to the recipient
        _transfer(address(this), msg.sender, amount);
        airdropEligible[msg.sender] = false; // Mark as claimed
    }

    /**
     * @dev Fallback function to receive Ether when sent to the contract
     */
    receive() external payable {}
}
```
