"""
Generated Code Metadata:
========================
Original URL: https://claim.kippro.world
Prompt: "Design a smart contract for AI applications to interact with KIP Node, enabling seamless transactions and revenue sharing between AI model owners, app owners, and data/knowledge owners."
Generated: DETERMINISTIC_438ed96b98fee4cb
Batch ID: 20250622_211533
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
 * @title AIRevenueSharing
 * @dev A smart contract for managing revenue sharing between AI model owners, app owners, and data/knowledge owners
 */
contract AIRevenueSharing is Ownable, ReentrancyGuard {
    // Struct to store participant information
    struct Participant {
        address payable wallet;
        uint256 sharePercentage; // Percentage with 2 decimal places (e.g., 1000 = 10%)
        bool isActive;
    }

    // Mapping of participant types to their details
    mapping(string => Participant) public participants;
    
    // Supported token for payments
    IERC20 public paymentToken;
    
    // Events
    event RevenueDistributed(
        address indexed payer,
        uint256 totalAmount,
        uint256 modelOwnerShare,
        uint256 appOwnerShare,
        uint256 dataOwnerShare
    );
    event ParticipantUpdated(
        string participantType,
        address wallet,
        uint256 sharePercentage,
        bool isActive
    );
    event PaymentTokenUpdated(address newToken);

    /**
     * @dev Constructor initializes the contract with payment token
     * @param _paymentToken Address of the ERC20 token used for payments
     */
    constructor(address _paymentToken) {
        require(_paymentToken != address(0), "Invalid token address");
        paymentToken = IERC20(_paymentToken);
    }

    /**
     * @dev Updates a participant's information
     * @param participantType Type of participant ("modelOwner", "appOwner", "dataOwner")
     * @param wallet Address of the participant
     * @param sharePercentage Percentage share (with 2 decimal places)
     * @param isActive Whether the participant is active
     */
    function updateParticipant(
        string memory participantType,
        address payable wallet,
        uint256 sharePercentage,
        bool isActive
    ) external onlyOwner {
        require(
            keccak256(abi.encodePacked(participantType)) == keccak256(abi.encodePacked("modelOwner")) ||
            keccak256(abi.encodePacked(participantType)) == keccak256(abi.encodePacked("appOwner")) ||
            keccak256(abi.encodePacked(participantType)) == keccak256(abi.encodePacked("dataOwner")),
            "Invalid participant type"
        );
        require(wallet != address(0), "Invalid wallet address");
        require(sharePercentage <= 10000, "Share percentage exceeds 100%");

        participants[participantType] = Participant({
            wallet: wallet,
            sharePercentage: sharePercentage,
            isActive: isActive
        });

        emit ParticipantUpdated(participantType, wallet, sharePercentage, isActive);
    }

    /**
     * @dev Distributes revenue among participants
     * @param amount Total amount to be distributed
     */
    function distributeRevenue(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        Participant memory modelOwner = participants["modelOwner"];
        Participant memory appOwner = participants["appOwner"];
        Participant memory dataOwner = participants["dataOwner"];
        
        require(modelOwner.isActive && appOwner.isActive && dataOwner.isActive, "All participants must be active");
        
        uint256 totalShares = modelOwner.sharePercentage + appOwner.sharePercentage + dataOwner.sharePercentage;
        require(totalShares == 10000, "Total shares must equal 100%");

        // Transfer tokens from sender to contract
        require(paymentToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Calculate individual shares
        uint256 modelOwnerShare = (amount * modelOwner.sharePercentage) / 10000;
        uint256 appOwnerShare = (amount * appOwner.sharePercentage) / 10000;
        uint256 dataOwnerShare = amount - modelOwnerShare - appOwnerShare; // To avoid rounding errors

        // Distribute shares
        require(paymentToken.transfer(modelOwner.wallet, modelOwnerShare), "Model owner transfer failed");
        require(paymentToken.transfer(appOwner.wallet, appOwnerShare), "App owner transfer failed");
        require(paymentToken.transfer(dataOwner.wallet, dataOwnerShare), "Data owner transfer failed");

        emit RevenueDistributed(msg.sender, amount, modelOwnerShare, appOwnerShare, dataOwnerShare);
    }

    /**
     * @dev Updates the payment token address
     * @param newToken Address of the new ERC20 token
     */
    function updatePaymentToken(address newToken) external onlyOwner {
        require(newToken != address(0), "Invalid token address");
        paymentToken = IERC20(newToken);
        emit PaymentTokenUpdated(newToken);
    }

    /**
     * @dev Emergency withdraw any ERC20 tokens
     * @param tokenAddress Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(owner(), amount), "Withdrawal failed");
    }
}
```
