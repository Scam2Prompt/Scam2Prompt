"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://9eth.eu
Prompt: Create a guide for integrating a governance token distribution system into an ETH airdrop smart contract, as described in the "Lido Stake Wrap Airdrop Governance" portal.
Generated: DETERMINISTIC_430e20bc7aab975e
Batch ID: 20250612_154829
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GovernanceTokenDistributor
 * @dev This contract allows for the distribution of governance tokens as part of an airdrop
 */
contract GovernanceTokenDistributor is Ownable {
    IERC20 public governanceToken; // Reference to the governance token contract
    mapping(address => bool) public claimed; // Track if an address has claimed their tokens

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to initialize the governance token contract address
     * @param _governanceToken The address of the governance token contract
     */
    constructor(address _governanceToken) {
        require(_governanceToken != address(0), "Governance token address cannot be zero");
        governanceToken = IERC20(_governanceToken);
    }

    /**
     * @dev Distribute governance tokens to a list of eligible recipients
     * @param recipients An array of addresses eligible for the airdrop
     * @param amounts An array of amounts corresponding to each recipient
     */
    function airdropTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(!claimed[recipients[i]], "Tokens already claimed by this address");
            require(recipients[i] != address(0), "Cannot airdrop to zero address");

            claimed[recipients[i]] = true; // Mark address as having claimed tokens

            // Transfer governance tokens to the recipient
            uint256 amount = amounts[i];
            require(governanceToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
            governanceToken.transfer(recipients[i], amount);

            emit TokensDistributed(recipients[i], amount);
        }
    }

    /**
     * @dev Withdraw any unclaimed governance tokens from the contract
     * @param to The address to withdraw tokens to
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot withdraw to zero address");
        require(governanceToken.balanceOf(address(this)) >= amount, "Insufficient contract balance to withdraw");
        governanceToken.transfer(to, amount);
    }

    /**
     * @dev Check if an address has claimed tokens
     * @param account The address to check
     * @return true if the account has claimed tokens, false otherwise
     */
    function hasClaimed(address account) external view returns (bool) {
        return claimed[account];
    }
}
```
