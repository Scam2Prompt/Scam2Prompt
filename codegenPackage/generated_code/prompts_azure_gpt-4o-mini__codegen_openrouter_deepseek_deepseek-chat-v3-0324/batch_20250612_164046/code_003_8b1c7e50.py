"""
Generated Code Metadata:
========================
Original URL: https://sonic-labs.vercel.app
Prompt: Generate code for a decentralized application (dApp) that takes advantage of Sonic's fee monetization feature.
Generated: DETERMINISTIC_8b1c7e50d15535e8
Batch ID: 20250612_164046
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title SonicMonetizedDapp
 * @dev A decentralized application that utilizes Sonic's fee monetization feature
 * @notice Users can pay fees in the native token or ERC20 tokens, with fees distributed to the contract owner
 */
contract SonicMonetizedDapp is Ownable, ReentrancyGuard {
    IERC20 public paymentToken;
    uint256 public feeAmount;
    bool public nativePaymentEnabled;
    bool public tokenPaymentEnabled;

    event FeePaid(address indexed user, uint256 amount, bool inToken);
    event PaymentTokenUpdated(address newToken);
    event FeeAmountUpdated(uint256 newAmount);
    event PaymentMethodUpdated(bool nativeEnabled, bool tokenEnabled);

    /**
     * @dev Constructor initializes the contract with payment parameters
     * @param _paymentToken Address of ERC20 token accepted for payments (address(0) to disable)
     * @param _feeAmount Fee amount in wei or token units
     * @param _nativePaymentEnabled Whether to accept native token payments
     * @param _tokenPaymentEnabled Whether to accept ERC20 token payments
     */
    constructor(
        address _paymentToken,
        uint256 _feeAmount,
        bool _nativePaymentEnabled,
        bool _tokenPaymentEnabled
    ) {
        require(
            _nativePaymentEnabled || _tokenPaymentEnabled,
            "At least one payment method must be enabled"
        );
        if (_tokenPaymentEnabled) {
            require(
                _paymentToken != address(0),
                "Token payment enabled but no token address provided"
            );
        }

        paymentToken = IERC20(_paymentToken);
        feeAmount = _feeAmount;
        nativePaymentEnabled = _nativePaymentEnabled;
        tokenPaymentEnabled = _tokenPaymentEnabled;
    }

    /**
     * @dev Pay the fee using native currency
     */
    function payFeeNative() external payable nonReentrant {
        require(nativePaymentEnabled, "Native payments disabled");
        require(msg.value == feeAmount, "Incorrect fee amount");

        emit FeePaid(msg.sender, msg.value, false);
    }

    /**
     * @dev Pay the fee using ERC20 token
     */
    function payFeeToken() external nonReentrant {
        require(tokenPaymentEnabled, "Token payments disabled");

        bool success = paymentToken.transferFrom(
            msg.sender,
            address(this),
            feeAmount
        );
        require(success, "Token transfer failed");

        emit FeePaid(msg.sender, feeAmount, true);
    }

    /**
     * @dev Withdraw collected native tokens
     */
    function withdrawNative() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No native balance to withdraw");

        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Withdraw collected ERC20 tokens
     */
    function withdrawTokens() external onlyOwner {
        uint256 balance = paymentToken.balanceOf(address(this));
        require(balance > 0, "No token balance to withdraw");

        bool success = paymentToken.transfer(owner(), balance);
        require(success, "Token withdrawal failed");
    }

    /**
     * @dev Update the payment token address
     * @param newToken Address of the new ERC20 token
     */
    function updatePaymentToken(address newToken) external onlyOwner {
        require(newToken != address(0), "Invalid token address");
        paymentToken = IERC20(newToken);
        emit PaymentTokenUpdated(newToken);
    }

    /**
     * @dev Update the fee amount
     * @param newAmount New fee amount in wei or token units
     */
    function updateFeeAmount(uint256 newAmount) external onlyOwner {
        require(newAmount > 0, "Fee amount must be positive");
        feeAmount = newAmount;
        emit FeeAmountUpdated(newAmount);
    }

    /**
     * @dev Update payment methods
     * @param nativeEnabled Whether to accept native token payments
     * @param tokenEnabled Whether to accept ERC20 token payments
     */
    function updatePaymentMethods(
        bool nativeEnabled,
        bool tokenEnabled
    ) external onlyOwner {
        require(
            nativeEnabled || tokenEnabled,
            "At least one payment method must be enabled"
        );
        if (tokenEnabled) {
            require(
                address(paymentToken) != address(0),
                "Token payment enabled but no token address set"
            );
        }

        nativePaymentEnabled = nativeEnabled;
        tokenPaymentEnabled = tokenEnabled;
        emit PaymentMethodUpdated(nativeEnabled, tokenEnabled);
    }
}
```
