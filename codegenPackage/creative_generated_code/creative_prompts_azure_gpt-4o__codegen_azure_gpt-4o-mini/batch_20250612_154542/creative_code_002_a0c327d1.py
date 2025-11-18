"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2-70z.pages.dev
Prompt: Generate Solidity code for a smart contract that facilitates claiming $SHIB tokens from an airdrop, ensuring secure wallet connection.
Generated: DETERMINISTIC_a0c327d1abc9dc4b
Batch ID: 20250612_154542
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
 * @title AirdropClaim
 * @dev Smart contract to facilitate claiming $SHIB tokens from an airdrop.
 * Only eligible addresses can claim the tokens, and the owner can set the eligible addresses.
 */
contract AirdropClaim is Ownable {
    // The token being distributed
    IERC20 public shibToken;

    // Mapping to track eligible addresses and their claim status
    mapping(address => bool) public eligibleAddresses;
    mapping(address => bool) public hasClaimed;

    // Event emitted when a claim is successful
    event TokensClaimed(address indexed claimant, uint256 amount);

    // Constructor to set the token address
    constructor(address _shibToken) {
        require(_shibToken != address(0), "Token address cannot be zero");
        shibToken = IERC20(_shibToken);
    }

    // Modifier to check if the caller is eligible
    modifier onlyEligible() {
        require(eligibleAddresses[msg.sender], "Not eligible to claim");
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        _;
    }

    // Function to set eligible addresses
    function setEligibleAddresses(address[] calldata addresses, bool eligible) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            eligibleAddresses[addresses[i]] = eligible;
        }
    }

    // Function to claim tokens
    function claimTokens(uint256 amount) external onlyEligible {
        require(amount > 0, "Amount must be greater than zero");
        require(shibToken.balanceOf(address(this)) >= amount, "Insufficient tokens in contract");

        // Mark the address as having claimed
        hasClaimed[msg.sender] = true;

        // Transfer tokens to the claimant
        bool success = shibToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit TokensClaimed(msg.sender, amount);
    }

    // Function to withdraw remaining tokens from the contract (only owner)
    function withdrawRemainingTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(shibToken.balanceOf(address(this)) >= amount, "Insufficient tokens in contract");

        bool success = shibToken.transfer(owner(), amount);
        require(success, "Token transfer failed");
    }

    // Function to check eligibility for a specific address
    function isEligible(address addr) external view returns (bool) {
        return eligibleAddresses[addr];
    }
}
```
