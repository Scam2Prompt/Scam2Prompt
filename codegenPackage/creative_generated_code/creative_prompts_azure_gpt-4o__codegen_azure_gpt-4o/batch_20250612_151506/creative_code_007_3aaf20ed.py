"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimmoonbag.pages.dev
Prompt: Write a Solidity function to calculate and distribute bonus tokens to users who make purchases of $25 or more using a referral code, as described in MoonBag's referral program.
Generated: DETERMINISTIC_3aaf20edbbd6eb74
Batch ID: 20250612_151506
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
 * @title MoonBagReferralBonus
 * @dev Contract to calculate and distribute bonus tokens to users who make purchases of $25 or more using a referral code.
 */
contract MoonBagReferralBonus {
    // Address of the token contract
    IERC20 public bonusToken;

    // Exchange rate: 1 USD = X tokens (set by the contract owner)
    uint256 public tokenExchangeRate;

    // Minimum purchase amount to qualify for a bonus (in USD)
    uint256 public constant MIN_PURCHASE_AMOUNT = 25;

    // Event emitted when bonus tokens are distributed
    event BonusDistributed(address indexed user, uint256 purchaseAmount, uint256 bonusTokens);

    /**
     * @dev Sets the token contract and exchange rate during deployment.
     * @param _bonusToken Address of the token contract.
     * @param _tokenExchangeRate Token exchange rate (tokens per USD).
     */
    constructor(IERC20 _bonusToken, uint256 _tokenExchangeRate) {
        require(address(_bonusToken) != address(0), "Invalid token contract");
        require(_tokenExchangeRate > 0, "Exchange rate must be positive");

        bonusToken = _bonusToken;
        tokenExchangeRate = _tokenExchangeRate;
    }

    /**
     * @dev Distribute bonus tokens to users who make qualifying purchases.
     * @param _user Address of the user making the purchase.
     * @param _purchaseAmount Purchase amount in USD (scaled to 18 decimals).
     * @param _referralCode Referral code used during the purchase.
     */
    function distributeBonus(
        address _user,
        uint256 _purchaseAmount,
        string calldata _referralCode
    ) external {
        require(_user != address(0), "Invalid user address");
        require(_purchaseAmount > 0, "Purchase amount must be greater than zero");
        require(bytes(_referralCode).length > 0, "Referral code cannot be empty");

        // Ensure purchase meets the minimum qualifying amount
        if (_purchaseAmount >= MIN_PURCHASE_AMOUNT) {
            // Calculate bonus tokens
            uint256 bonusTokens = _purchaseAmount * tokenExchangeRate;

            // Transfer bonus tokens to the user
            require(bonusToken.transfer(_user, bonusTokens), "Token transfer failed");

            // Emit event
            emit BonusDistributed(_user, _purchaseAmount, bonusTokens);
        }
    }

    /**
     * @dev Allows the contract owner to update the token exchange rate.
     * @param _newExchangeRate New token exchange rate (tokens per USD).
     */
    function updateExchangeRate(uint256 _newExchangeRate) external {
        require(_newExchangeRate > 0, "Exchange rate must be positive");

        tokenExchangeRate = _newExchangeRate;
    }
}

/**
 * @dev Interface for ERC20 token interactions.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
