"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-beam-token.pages.dev
Prompt: Write a smart contract to manage BEAM token rewards distribution, ensuring accountability and real-time tracking of funds.
Generated: DETERMINISTIC_f094b012ff25d746
Batch ID: 20250612_150604
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

/*
 * @title BEAM Token Rewards Distribution Smart Contract
 * @dev This contract manages the distribution of BEAM token rewards to recipients,
 *      ensuring accountability and real-time tracking of funds.
 *      Designed using OpenZeppelin libraries for security and best practices.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BeamRewardsDistributor is Ownable {
    // Address of the BEAM token contract
    IERC20 public beamToken;

    // Total rewards distributed
    uint256 public totalDistributed;

    // Event emitted after successful reward distribution
    event RewardDistributed(address indexed recipient, uint256 amount);

    // Event emitted in case of withdrawal of unused tokens
    event UnusedTokensWithdrawn(address indexed owner, uint256 amount);

    /*
     * @notice Constructor to initialize the smart contract
     * @param _beamToken The address of the BEAM token contract
     */
    constructor(IERC20 _beamToken) {
        require(address(_beamToken) != address(0), "Invalid token address");
        beamToken = _beamToken;
    }

    /*
     * @notice Distribute rewards to a list of recipients
     * @param recipients Array of recipient addresses
     * @param amounts Array of reward amounts corresponding to each recipient
     */
    function distributeRewards(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched recipients and amounts");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint256 amount = amounts[i];

            require(recipient != address(0), "Invalid recipient address");
            require(amount > 0, "Reward amount must be greater than zero");

            // Transfer BEAM tokens to the recipient
            require(beamToken.transfer(recipient, amount), "Token transfer failed");

            // Update total distributed
            totalDistributed += amount;

            // Emit the reward distribution event
            emit RewardDistributed(recipient, amount);
        }
    }

    /*
     * @notice Withdraw unused tokens from the contract (owner-only)
     * @param amount Amount of tokens to withdraw
     */
    function withdrawUnusedTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer unused tokens to the owner
        require(beamToken.transfer(msg.sender, amount), "Token transfer failed");

        emit UnusedTokensWithdrawn(msg.sender, amount);
    }

    /*
     * @notice Get the balance of BEAM tokens in the contract
     * @return Balance of BEAM tokens
     */
    function getContractBalance() external view returns (uint256) {
        return beamToken.balanceOf(address(this));
    }
}
```
