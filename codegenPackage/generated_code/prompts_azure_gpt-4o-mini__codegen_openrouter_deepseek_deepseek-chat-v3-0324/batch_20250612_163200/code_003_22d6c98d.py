"""
Generated Code Metadata:
========================
Original URL: https://mazza.pages.dev
Prompt: Develop a decentralized application (dApp) on the Mazze blockchain that facilitates cross-border transactions, utilizing its high throughput capabilities.
Generated: DETERMINISTIC_22d6c98d5a9fce54
Batch ID: 20250612_163200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Solidity smart contract for a cross-border payment dApp on an Ethereum-compatible blockchain (assuming "Mazze" is similar). The code includes token transfers, fee calculations, and basic access control:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title CrossBorderPayment
 * @dev Facilitates cross-border transactions with fee calculations.
 */
contract CrossBorderPayment is Ownable, ReentrancyGuard {
    IERC20 public paymentToken;
    uint256 public constant FEE_BASIS_POINTS = 50; // 0.5% fee (50 basis points)
    address public feeCollector;

    event PaymentSent(
        address indexed sender,
        address indexed recipient,
        uint256 amount,
        uint256 fee,
        string referenceId
    );

    event FeeCollectorUpdated(address newCollector);

    /**
     * @dev Constructor initializes the payment token and fee collector.
     * @param _paymentToken Address of the ERC20 token used for payments.
     * @param _feeCollector Address where fees will be sent.
     */
    constructor(address _paymentToken, address _feeCollector) {
        require(_paymentToken != address(0), "Invalid token address");
        require(_feeCollector != address(0), "Invalid fee collector address");
        
        paymentToken = IERC20(_paymentToken);
        feeCollector = _feeCollector;
    }

    /**
     * @dev Send cross-border payment with a reference ID.
     * @param recipient Address of the recipient.
     * @param amount Amount to send (before fee deduction).
     * @param referenceId Unique reference for the transaction.
     */
    function sendPayment(
        address recipient,
        uint256 amount,
        string calldata referenceId
    ) external nonReentrant {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be positive");

        uint256 fee = (amount * FEE_BASIS_POINTS) / 10000;
        uint256 amountAfterFee = amount - fee;

        require(
            paymentToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        // Transfer amount after fee to recipient
        require(
            paymentToken.transfer(recipient, amountAfterFee),
            "Recipient transfer failed"
        );

        // Transfer fee to collector
        if (fee > 0) {
            require(
                paymentToken.transfer(feeCollector, fee),
                "Fee transfer failed"
            );
        }

        emit PaymentSent(
            msg.sender,
            recipient,
            amountAfterFee,
            fee,
            referenceId
        );
    }

    /**
     * @dev Update the fee collector address.
     * @param newCollector Address of the new fee collector.
     */
    function setFeeCollector(address newCollector) external onlyOwner {
        require(newCollector != address(0), "Invalid fee collector address");
        feeCollector = newCollector;
        emit FeeCollectorUpdated(newCollector);
    }

    /**
     * @dev Emergency withdraw tokens from contract (owner only).
     * @param tokenAddress Address of the token to withdraw.
     * @param amount Amount to withdraw.
     */
    function emergencyWithdraw(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(
            token.transfer(msg.sender, amount),
            "Emergency withdraw failed"
        );
    }
}
```

And here's a JavaScript (web3.js) interaction script for the frontend:

```javascript
const CrossBorderPayment = artifacts.require("CrossBorderPayment");

module.exports = async function (callback) {
    try {
        const paymentContract = await CrossBorderPayment.deployed();
        
        // Example: Send payment
        const recipient = "0xRecipientAddress";
        const amount = web3.utils.toWei("100", "ether"); // 100 tokens
        const referenceId = "INV12345";
        
        // Approve first
        const tokenAddress = await paymentContract.paymentToken();
        const tokenInstance = new web3.eth.Contract(
            [
                {
                    constant: false,
                    inputs: [
                        { name: "spender", type: "address" },
                        { name: "amount", type: "uint256" },
                    ],
                    name: "approve",
                    outputs: [{ name: "", type: "bool" }],
                    payable: false,
                    stateMutability: "nonpayable",
                    type: "function",
                },
            ],
            tokenAddress
        );
        
        await tokenInstance.methods
            .approve(paymentContract.address, amount)
            .send({ from: web3.eth.defaultAccount });
        
        // Send payment
        const tx = await paymentContract.sendPayment(
            recipient,
            amount,
            referenceId,
            { from: web3.eth.defaultAccount }
        );
        
        console.log(`Transaction hash: ${tx.tx}`);
        callback();
    } catch (error) {
        console.error("Error:", error);
        callback(error);
    }
};
```

Note: This assumes Mazze blockchain is Ethereum-compatible (EVM-based). For actual production, you would need to:
1. Adjust for Mazze's specific chain ID
2. Use Mazze's preferred libraries
3. Add Mazze-specific gas optimizations
4. Include Mazze's native token handling if needed
