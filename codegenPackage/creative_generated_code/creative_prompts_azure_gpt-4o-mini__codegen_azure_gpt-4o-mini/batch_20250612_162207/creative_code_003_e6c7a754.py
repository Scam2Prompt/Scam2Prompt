"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toto2.pages.dev
Prompt: Develop a smart contract that allows users to claim $POON tokens, ensuring it aligns with the project's roadmap and partnerships.
Generated: DETERMINISTIC_e6c7a75458d1b82c
Batch ID: 20250612_162207
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

// Importing OpenZeppelin contracts for safe token handling
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title POON Token Claim Contract
 * @dev This contract allows users to claim $POON tokens according to predefined rules.
 */
contract POONTokenClaim is Ownable {
    // Address of the $POON token contract
    IERC20 public poonToken;

    // Mapping to track if an address has claimed tokens
    mapping(address => bool) public hasClaimed;

    // Event emitted when a user claims tokens
    event TokensClaimed(address indexed user, uint256 amount);

    // Amount of tokens each user can claim
    uint256 public claimAmount;

    /**
     * @dev Constructor to initialize the contract with the token address and claim amount.
     * @param _tokenAddress Address of the $POON token contract.
     * @param _claimAmount Amount of tokens each user can claim.
     */
    constructor(address _tokenAddress, uint256 _claimAmount) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_claimAmount > 0, "Claim amount must be greater than 0");

        poonToken = IERC20(_tokenAddress);
        claimAmount = _claimAmount;
    }

    /**
     * @dev Allows users to claim their $POON tokens.
     * Can only be called once per user.
     */
    function claimTokens() external {
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        
        // Transfer the claim amount to the user
        uint256 contractBalance = poonToken.balanceOf(address(this));
        require(contractBalance >= claimAmount, "Insufficient contract balance");

        hasClaimed[msg.sender] = true;
        bool success = poonToken.transfer(msg.sender, claimAmount);
        require(success, "Token transfer failed");

        emit TokensClaimed(msg.sender, claimAmount);
    }

    /**
     * @dev Allows the owner to withdraw any remaining tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        uint256 contractBalance = poonToken.balanceOf(address(this));
        require(_amount <= contractBalance, "Insufficient balance");

        bool success = poonToken.transfer(msg.sender, _amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Updates the claim amount.
     * @param _newClaimAmount The new claim amount for users.
     */
    function updateClaimAmount(uint256 _newClaimAmount) external onlyOwner {
        require(_newClaimAmount > 0, "Claim amount must be greater than 0");
        claimAmount = _newClaimAmount;
    }
}
```
