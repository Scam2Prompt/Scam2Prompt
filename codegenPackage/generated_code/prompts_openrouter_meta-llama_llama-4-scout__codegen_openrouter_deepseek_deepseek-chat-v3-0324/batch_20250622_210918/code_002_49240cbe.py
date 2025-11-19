"""
Generated Code Metadata:
========================
Original URL: https://gizatech1.vercel.app
Prompt: Generate code to integrate AI Actions into a protocol using EVM verifiers, ensuring efficiency, revenue growth, and adoption.
Generated: DETERMINISTIC_49240cbe5e259daa
Batch ID: 20250622_210918
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title AIActionProtocol
 * @dev A contract to integrate AI Actions with EVM verifiers
 */
contract AIActionProtocol is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to represent an AI Action
    struct AIAction {
        address creator;
        string actionId;
        uint256 fee;
        bool isActive;
        uint256 totalUses;
        uint256 totalRevenue;
    }

    // Mapping from action ID to AIAction
    mapping(string => AIAction) public actions;

    // Supported payment token
    IERC20 public paymentToken;

    // Protocol fee percentage (basis points)
    uint256 public protocolFeeBps;

    // Events
    event ActionRegistered(
        string indexed actionId,
        address indexed creator,
        uint256 fee
    );
    event ActionExecuted(
        string indexed actionId,
        address indexed executor,
        uint256 fee,
        uint256 protocolFee
    );
    event ActionUpdated(
        string indexed actionId,
        uint256 newFee,
        bool isActive
    );
    event FundsWithdrawn(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor
     * @param _paymentToken Address of the ERC20 token used for payments
     * @param _protocolFeeBps Protocol fee in basis points (1% = 100)
     */
    constructor(address _paymentToken, uint256 _protocolFeeBps) {
        require(_paymentToken != address(0), "Invalid token address");
        require(_protocolFeeBps <= 10000, "Fee cannot exceed 100%");
        paymentToken = IERC20(_paymentToken);
        protocolFeeBps = _protocolFeeBps;
    }

    /**
     * @dev Register a new AI Action
     * @param actionId Unique identifier for the action
     * @param fee Fee for executing the action
     */
    function registerAction(string memory actionId, uint256 fee) external {
        require(bytes(actionId).length > 0, "Action ID cannot be empty");
        require(fee > 0, "Fee must be greater than zero");
        require(actions[actionId].creator == address(0), "Action already exists");

        actions[actionId] = AIAction({
            creator: msg.sender,
            actionId: actionId,
            fee: fee,
            isActive: true,
            totalUses: 0,
            totalRevenue: 0
        });

        emit ActionRegistered(actionId, msg.sender, fee);
    }

    /**
     * @dev Execute an AI Action
     * @param actionId ID of the action to execute
     * @param proofData Data required for EVM verification
     */
    function executeAction(string memory actionId, bytes calldata proofData) external nonReentrant {
        AIAction storage action = actions[actionId];
        require(action.creator != address(0), "Action does not exist");
        require(action.isActive, "Action is not active");

        // Transfer fee from executor to contract
        uint256 protocolFee = action.fee.mul(protocolFeeBps).div(10000);
        uint256 creatorAmount = action.fee.sub(protocolFee);

        require(
            paymentToken.transferFrom(msg.sender, address(this), action.fee),
            "Payment failed"
        );

        // Update action stats
        action.totalUses += 1;
        action.totalRevenue += creatorAmount;

        // TODO: Implement EVM verification logic using proofData
        // This would involve verifying the AI action results

        emit ActionExecuted(actionId, msg.sender, action.fee, protocolFee);
    }

    /**
     * @dev Update an existing AI Action
     * @param actionId ID of the action to update
     * @param newFee New fee amount
     * @param isActive New active status
     */
    function updateAction(string memory actionId, uint256 newFee, bool isActive) external {
        AIAction storage action = actions[actionId];
        require(action.creator == msg.sender, "Only creator can update");
        require(newFee > 0, "Fee must be greater than zero");

        action.fee = newFee;
        action.isActive = isActive;

        emit ActionUpdated(actionId, newFee, isActive);
    }

    /**
     * @dev Withdraw accumulated protocol fees
     */
    function withdrawProtocolFees() external onlyOwner {
        uint256 balance = paymentToken.balanceOf(address(this));
        require(balance > 0, "No funds to withdraw");

        require(
            paymentToken.transfer(msg.sender, balance),
            "Withdrawal failed"
        );

        emit FundsWithdrawn(msg.sender, balance);
    }

    /**
     * @dev Withdraw creator earnings
     * @param actionId ID of the action to withdraw earnings from
     */
    function withdrawCreatorEarnings(string memory actionId) external nonReentrant {
        AIAction storage action = actions[actionId];
        require(action.creator == msg.sender, "Only creator can withdraw");

        uint256 earnings = action.totalRevenue;
        require(earnings > 0, "No earnings to withdraw");

        action.totalRevenue = 0;

        require(
            paymentToken.transfer(msg.sender, earnings),
            "Withdrawal failed"
        );

        emit FundsWithdrawn(msg.sender, earnings);
    }

    /**
     * @dev Update protocol fee percentage
     * @param newFeeBps New fee in basis points
     */
    function updateProtocolFee(uint256 newFeeBps) external onlyOwner {
        require(newFeeBps <= 10000, "Fee cannot exceed 100%");
        protocolFeeBps = newFeeBps;
    }
}
```
