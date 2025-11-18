"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fr-worldcoin.web.app
Prompt: Generate Solidity code for a smart contract that verifies wallet ownership and facilitates claiming $WLD tokens, referencing the distribution process mentioned on the Worldcoin site.
Generated: DETERMINISTIC_c9a44488b6170d5d
Batch ID: 20250612_151412
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
 * @title WLDTokenClaim
 * @dev Smart contract for verifying wallet ownership and claiming $WLD tokens.
 * Based on the distribution process mentioned on the Worldcoin site.
 */
contract WLDTokenClaim {
    // Address of the token contract
    address public tokenAddress;

    // Mapping to track claimed tokens
    mapping(address => bool) public hasClaimed;

    // Event emitted when tokens are successfully claimed
    event TokensClaimed(address indexed claimant, uint256 amount);

    // Modifier to check if the caller is the wallet owner
    modifier onlyWalletOwner() {
        require(msg.sender == tx.origin, "Caller must be a wallet owner");
        _;
    }

    /**
     * @dev Constructor to set the $WLD token contract address.
     * @param _tokenAddress Address of the $WLD token contract.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        tokenAddress = _tokenAddress;
    }

    /**
     * @dev Function to claim $WLD tokens.
     * Verifies that the caller is the wallet owner and has not already claimed tokens.
     * @param amount The amount of $WLD tokens to claim.
     */
    function claimTokens(uint256 amount) external onlyWalletOwner {
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        require(amount > 0, "Invalid token amount");

        // Mark the caller as having claimed tokens
        hasClaimed[msg.sender] = true;

        // Interface to interact with the $WLD token contract
        IERC20 token = IERC20(tokenAddress);

        // Transfer $WLD tokens to the caller
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        // Emit event for successful token claim
        emit TokensClaimed(msg.sender, amount);
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
