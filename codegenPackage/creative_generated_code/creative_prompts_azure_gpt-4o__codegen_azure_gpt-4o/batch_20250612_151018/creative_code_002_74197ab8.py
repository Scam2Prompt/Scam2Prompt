"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drift-2kl.pages.dev
Prompt: Create a smart contract function that allows users to claim DRIFT tokens before the deadline of August 16, 2024, 09:00 PM, based on the eligibility criteria.
Generated: DETERMINISTIC_74197ab82ebbdae6
Batch ID: 20250612_151018
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
 * @title DRIFT Token Claim Contract
 * @dev This contract allows users to claim DRIFT tokens based on eligibility criteria
 *      before the deadline of August 16, 2024, 09:00 PM UTC.
 */
contract DriftTokenClaim {
    // DRIFT token address
    IERC20 public driftToken;

    // Deadline for claiming tokens (August 16, 2024, 09:00 PM UTC)
    uint256 public constant CLAIM_DEADLINE = 1729123200;

    // Mapping to store eligibility and claim status
    mapping(address => uint256) public claimableTokens;
    mapping(address => bool) public hasClaimed;

    // Owner of the contract
    address public owner;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed user, uint256 amount);

    /**
     * @dev Modifier to check if the sender is the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Modifier to ensure claim deadline is not over.
     */
    modifier beforeDeadline() {
        require(block.timestamp <= CLAIM_DEADLINE, "Claim deadline has passed");
        _;
    }

    constructor(address _driftToken) {
        require(_driftToken != address(0), "Invalid token address");
        driftToken = IERC20(_driftToken);
        owner = msg.sender;
    }

    /**
     * @dev Function to set claimable token amounts for users.
     * @param users List of user addresses.
     * @param amounts List of token amounts corresponding to the users.
     */
    function setClaimableTokens(address[] calldata users, uint256[] calldata amounts) external onlyOwner {
        require(users.length == amounts.length, "Mismatched input arrays");

        for (uint256 i = 0; i < users.length; i++) {
            claimableTokens[users[i]] = amounts[i];
        }
    }

    /**
     * @dev Function for users to claim their DRIFT tokens.
     */
    function claimTokens() external beforeDeadline {
        require(claimableTokens[msg.sender] > 0, "No tokens available for claim");
        require(!hasClaimed[msg.sender], "Tokens already claimed");

        uint256 claimAmount = claimableTokens[msg.sender];

        // Mark tokens as claimed
        hasClaimed[msg.sender] = true;
        claimableTokens[msg.sender] = 0;

        // Transfer DRIFT tokens to the user
        require(driftToken.transfer(msg.sender, claimAmount), "Token transfer failed");

        emit TokensClaimed(msg.sender, claimAmount);
    }

    /**
     * @dev Emergency function for the owner to withdraw tokens from the contract.
     * @param amount Number of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(driftToken.transfer(owner, amount), "Token transfer failed");
    }
}

// Interface for ERC20 token compliance
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
