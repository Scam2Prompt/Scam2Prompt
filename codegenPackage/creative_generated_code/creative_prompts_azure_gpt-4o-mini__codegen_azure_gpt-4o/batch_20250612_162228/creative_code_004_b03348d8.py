"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slerf-cjl.pages.dev
Prompt: Create a Solidity function that allows users to claim their $Slerf tokens after participating in the presale, ensuring it checks for the required conditions.
Generated: DETERMINISTIC_b03348d8c0bb009a
Batch ID: 20250612_162228
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
 * @title SlerfTokenClaim
 * @dev A contract to allow users to claim their $Slerf tokens after participating in the presale.
 */
contract SlerfTokenClaim {
    // Address of the token contract
    address public immutable slerfToken;
    
    // Presale details: mapping of user addresses to amounts of tokens they can claim
    mapping(address => uint256) public claimableTokens;

    // Tracks whether a user has already claimed their tokens
    mapping(address => bool) public hasClaimed;

    // Event emitted when tokens are successfully claimed
    event TokensClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the token address.
     * @param _slerfToken Address of the $Slerf token contract.
     */
    constructor(address _slerfToken) {
        require(_slerfToken != address(0), "Invalid token address");
        slerfToken = _slerfToken;
    }

    /**
     * @dev Allows a user to claim their $Slerf tokens if eligible.
     * Conditions:
     * - User must have participated in the presale.
     * - User must not have already claimed their tokens.
     */
    function claimTokens() external {
        uint256 amountToClaim = claimableTokens[msg.sender];
        
        require(amountToClaim > 0, "No tokens available for claim");
        require(!hasClaimed[msg.sender], "Tokens already claimed");

        // Update claim status to prevent re-claiming
        hasClaimed[msg.sender] = true;

        // Transfer tokens to the user
        require(
            IERC20(slerfToken).transfer(msg.sender, amountToClaim),
            "Token transfer failed"
        );

        emit TokensClaimed(msg.sender, amountToClaim);
    }

    /**
     * @dev Admin function to set claimable tokens for users.
     * @param user Address of the user.
     * @param amount Number of tokens claimable by the user.
     */
    function setClaimableTokens(address user, uint256 amount) external {
        // Only callable by the admin (implement access control in production)
        claimableTokens[user] = amount;
    }
}

/**
 * @dev Minimal ERC20 interface for token transfer.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
