"""
Generated Code Metadata:
========================
Original URL: https://claim-popofrog.pages.dev
Prompt: Generate a Solidity contract for a reward distribution system that allocates 15% of the $FROP token supply for community airdrops, as described in the tokenomics section.
Generated: DETERMINISTIC_11ac45423a29edf3
Batch ID: 20250612_150347
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

// Importing the ERC20 interface for the $FROP token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title RewardDistribution
 * @dev A contract for distributing rewards in the form of $FROP tokens
 * to the community through airdrops.
 */
contract RewardDistribution is Ownable {
    // The $FROP token contract
    IERC20 public fropToken;

    // Total supply of $FROP tokens
    uint256 public totalSupply;

    // Amount allocated for community airdrops (15% of total supply)
    uint256 public airdropAllocation;

    // Mapping to track claimed airdrop amounts
    mapping(address => uint256) public claimedAirdrops;

    // Event emitted when airdrop is distributed
    event AirdropDistributed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the $FROP token address.
     * @param _fropToken Address of the $FROP token contract.
     */
    constructor(address _fropToken) {
        require(_fropToken != address(0), "Invalid token address");
        fropToken = IERC20(_fropToken);
        totalSupply = fropToken.totalSupply();
        airdropAllocation = (totalSupply * 15) / 100; // 15% of total supply
    }

    /**
     * @dev Function to distribute airdrops to a list of recipients.
     * @param recipients Array of addresses to receive airdrops.
     * @param amounts Array of amounts corresponding to each recipient.
     */
    function distributeAirdrop(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched input lengths");

        uint256 totalAirdropAmount = 0;

        // Calculate total airdrop amount and check for over-allocation
        for (uint256 i = 0; i < amounts.length; i++) {
            totalAirdropAmount += amounts[i];
        }
        require(totalAirdropAmount <= airdropAllocation, "Exceeds airdrop allocation");

        // Distributing airdrops
        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(claimedAirdrops[recipients[i]] + amounts[i] <= airdropAllocation, "Recipient exceeds allocation");

            claimedAirdrops[recipients[i]] += amounts[i];
            emit AirdropDistributed(recipients[i], amounts[i]);
        }

        // Transfer the total airdrop amount from the contract to the recipients
        require(fropToken.transferFrom(owner(), address(this), totalAirdropAmount), "Transfer failed");
    }

    /**
     * @dev Function to withdraw any remaining tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= fropToken.balanceOf(address(this)), "Insufficient balance");
        require(fropToken.transfer(owner(), amount), "Transfer failed");
    }
}
```
