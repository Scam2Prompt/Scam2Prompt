"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdropneiro-xyz.pages.dev
Prompt: Write a smart contract in Solidity that facilitates the claiming of $NEIRO tokens, ensuring referral tracking and reward distribution.
Generated: DETERMINISTIC_d3fe601aa63fa0f8
Batch ID: 20250612_145616
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
 * @title NeiroTokenClaim
 * @dev A smart contract to facilitate claiming of $NEIRO tokens
 * with referral tracking and reward distribution.
 */
contract NeiroTokenClaim is Ownable {
    // Token to be claimed
    IERC20 public neiroToken;

    // Referral structure to track referers and their rewards
    struct Referral {
        address referrer;
        uint256 reward;
    }

    // Mapping from user address to their referral information
    mapping(address => Referral) public referrals;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed claimant, uint256 amount, address indexed referrer);

    // Constructor to initialize the contract with the NEIRO token address
    constructor(address _neiroToken) {
        require(_neiroToken != address(0), "Invalid token address");
        neiroToken = IERC20(_neiroToken);
    }

    /**
     * @dev Claim NEIRO tokens with an optional referrer
     * @param amount The amount of NEIRO tokens to claim
     * @param referrer The address of the referring user (optional)
     */
    function claimTokens(uint256 amount, address referrer) external {
        require(amount > 0, "Amount must be greater than zero");
        require(neiroToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Handle referral tracking
        if (referrer != address(0) && referrer != msg.sender) {
            // If this is the first claim from this user, set the referrer
            if (referrals[msg.sender].referrer == address(0)) {
                referrals[msg.sender].referrer = referrer;
                referrals[referrer].reward += amount / 10; // Reward referrer with 10% of the claimed amount
            }
        }

        // Transfer tokens to the claimant
        bool success = neiroToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit TokensClaimed(msg.sender, amount, referrer);
    }

    /**
     * @dev Withdraw NEIRO tokens from the contract
     * @param amount The amount of NEIRO tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(neiroToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        bool success = neiroToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Get the reward balance for a referrer
     * @param referrer The address of the referrer
     * @return The total reward for the referrer
     */
    function getReferralReward(address referrer) external view returns (uint256) {
        return referrals[referrer].reward;
    }

    /**
     * @dev Fallback function to prevent sending Ether to the contract
     */
    receive() external payable {
        revert("No Ether is accepted");
    }
}
```
