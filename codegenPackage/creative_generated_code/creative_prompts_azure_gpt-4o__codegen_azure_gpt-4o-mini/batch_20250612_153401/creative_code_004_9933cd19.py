"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giftclaim-04.web.app
Prompt: Write a Solidity smart contract that verifies wallet ownership and facilitates claiming DUST tokens from the DUST protocol.
Generated: DETERMINISTIC_9933cd19475a7b77
Batch ID: 20250612_153401
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

// Importing the interface for ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title DUSTClaim
 * @dev A smart contract to verify wallet ownership and facilitate claiming DUST tokens from the DUST protocol.
 */
contract DUSTClaim {
    // Address of the DUST token contract
    IERC20 public dustToken;

    // Mapping to track claimed tokens per address
    mapping(address => bool) public hasClaimed;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed claimant, uint256 amount);

    /**
     * @dev Constructor to set the DUST token contract address.
     * @param _dustToken The address of the DUST token contract.
     */
    constructor(address _dustToken) {
        require(_dustToken != address(0), "Invalid token address");
        dustToken = IERC20(_dustToken);
    }

    /**
     * @dev Function to claim DUST tokens.
     * Only callable by owners of the wallet who have not yet claimed.
     * @param amount The amount of DUST tokens to claim.
     */
    function claimTokens(uint256 amount) external {
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer the tokens from the contract to the claimant
        bool success = dustToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Mark that the address has claimed the tokens
        hasClaimed[msg.sender] = true;

        // Emit the TokensClaimed event
        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @dev Function to check if an address has claimed tokens.
     * @param claimant The address to check the claim status for.
     * @return bool indicating whether the address has claimed tokens.
     */
    function hasClaimedTokens(address claimant) external view returns (bool) {
        return hasClaimed[claimant];
    }
}
```
