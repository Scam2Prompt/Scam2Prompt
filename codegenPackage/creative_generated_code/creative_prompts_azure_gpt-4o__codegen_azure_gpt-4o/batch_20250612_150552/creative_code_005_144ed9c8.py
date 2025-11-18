"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeverse-22u.pages.dev
Prompt: Develop a Solidity smart contract that supports claiming $DOGEVERSE tokens post-presale, ensuring compatibility with multiple chains like Ethereum, Solana, and BNB Chain.
Generated: DETERMINISTIC_144ed9c889a4c7ec
Batch ID: 20250612_150552
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
 * @title DOGEVERSE Token Claim Contract
 * @dev This contract allows users to claim $DOGEVERSE tokens after a presale.
 * It is designed to support multiple EVM-compatible chains like Ethereum and BNB Chain.
 */
contract DogeverseClaim {
    // Address of the DOGEVERSE token contract
    IERC20 public dogeverseToken;

    // Owner of the contract (presale organizer)
    address public owner;

    // Mapping to track claimed tokens for users
    mapping(address => uint256) public claimedTokens;

    // Mapping to track how many tokens each user is allowed to claim
    mapping(address => uint256) public claimableTokens;

    // Event emitted when tokens are successfully claimed
    event TokensClaimed(address indexed user, uint256 amount);

    // Event emitted when claimable tokens are updated
    event ClaimableTokensUpdated(address indexed user, uint256 amount);

    // Modifier to restrict access to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the $DOGEVERSE token address.
     * @param _dogeverseToken Address of the $DOGEVERSE ERC20 token contract.
     */
    constructor(IERC20 _dogeverseToken) {
        dogeverseToken = _dogeverseToken;
        owner = msg.sender;
    }

    /**
     * @dev Updates claimable tokens for a user.
     * Can only be called by the contract owner.
     * @param user Address of the user.
     * @param amount Number of tokens that the user can claim.
     */
    function updateClaimableTokens(address user, uint256 amount) external onlyOwner {
        claimableTokens[user] = amount;
        emit ClaimableTokensUpdated(user, amount);
    }

    /**
     * @dev Allows a user to claim their $DOGEVERSE tokens.
     */
    function claimTokens() external {
        uint256 amountToClaim = claimableTokens[msg.sender];

        // Ensure the user has tokens to claim
        require(amountToClaim > 0, "No claimable tokens available");

        // Ensure the user hasn't already claimed their tokens
        require(claimedTokens[msg.sender] == 0, "Tokens already claimed");

        // Update claimed tokens mapping
        claimedTokens[msg.sender] = amountToClaim;

        // Reset the user's claimable tokens
        claimableTokens[msg.sender] = 0;

        // Transfer tokens to the user
        bool success = dogeverseToken.transfer(msg.sender, amountToClaim);
        require(success, "Token transfer failed");

        // Emit the TokensClaimed event
        emit TokensClaimed(msg.sender, amountToClaim);
    }

    /**
     * @dev Emergency withdrawal function to withdraw tokens from the contract.
     * Can only be called by the owner.
     * @param tokenAddress Address of the token to withdraw.
     * @param recipient Address to receive the withdrawn tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(
        address tokenAddress,
        address recipient,
        uint256 amount
    ) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        bool success = token.transfer(recipient, amount);
        require(success, "Withdrawal failed");
    }
}

/**
 * @dev Minimal interface for ERC20 token methods used in this contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
