"""
Generated Code Metadata:
========================
Original URL: https://bafybeib57x2i3wjq47prbs73dicwjrqmh4z6xefonlbo3qd3bojsesqjra.ipfs.dweb.link
Prompt: Explain how to delegate to selected operators in the EigenLayer ecosystem for securing new protocols.
Generated: DETERMINISTIC_d7b61f954a7f0517
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready code example demonstrating how to delegate to selected operators in the EigenLayer ecosystem:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IEigenLayerStrategyManager {
    function depositIntoStrategy(address strategy, address token, uint256 amount) external returns (bytes32);
    function withdrawShares(address strategy, address withdrawer, uint256 shares) external;
}

interface IEigenLayerDelegationManager {
    function delegateTo(address operator, bytes32 approverSalt, uint256 approverExpiry) external;
    function undelegate(address staker) external;
}

contract EigenLayerDelegator is Ownable, ReentrancyGuard {
    IEigenLayerStrategyManager public immutable strategyManager;
    IEigenLayerDelegationManager public immutable delegationManager;
    IERC20 public immutable stakingToken;
    address public immutable strategy;

    mapping(address => bool) public approvedOperators;

    event OperatorApproved(address indexed operator);
    event OperatorRevoked(address indexed operator);
    event Delegated(address indexed operator, uint256 amount);
    event Undelegated(address indexed operator, uint256 amount);

    constructor(
        address _strategyManager,
        address _delegationManager,
        address _stakingToken,
        address _strategy
    ) {
        require(_strategyManager != address(0), "Invalid strategy manager");
        require(_delegationManager != address(0), "Invalid delegation manager");
        require(_stakingToken != address(0), "Invalid staking token");
        require(_strategy != address(0), "Invalid strategy");

        strategyManager = IEigenLayerStrategyManager(_strategyManager);
        delegationManager = IEigenLayerDelegationManager(_delegationManager);
        stakingToken = IERC20(_stakingToken);
        strategy = _strategy;
    }

    /**
     * @notice Approve an operator for delegation
     * @param operator Address of the operator to approve
     */
    function approveOperator(address operator) external onlyOwner {
        require(operator != address(0), "Invalid operator");
        require(!approvedOperators[operator], "Operator already approved");
        
        approvedOperators[operator] = true;
        emit OperatorApproved(operator);
    }

    /**
     * @notice Revoke approval for an operator
     * @param operator Address of the operator to revoke
     */
    function revokeOperator(address operator) external onlyOwner {
        require(approvedOperators[operator], "Operator not approved");
        
        approvedOperators[operator] = false;
        emit OperatorRevoked(operator);
    }

    /**
     * @notice Delegate stake to an approved operator
     * @param operator Address of the operator to delegate to
     * @param amount Amount of tokens to stake and delegate
     * @param approverSalt Salt for the approver signature
     * @param approverExpiry Expiry time for the approver signature
     */
    function delegateToOperator(
        address operator,
        uint256 amount,
        bytes32 approverSalt,
        uint256 approverExpiry
    ) external nonReentrant {
        require(approvedOperators[operator], "Operator not approved");
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve strategy manager to spend tokens
        stakingToken.approve(address(strategyManager), amount);

        // Deposit into strategy
        strategyManager.depositIntoStrategy(strategy, address(stakingToken), amount);

        // Delegate to operator
        delegationManager.delegateTo(operator, approverSalt, approverExpiry);

        emit Delegated(operator, amount);
    }

    /**
     * @notice Undelegate from an operator
     * @param shares Amount of shares to undelegate
     */
    function undelegate(uint256 shares) external nonReentrant {
        require(shares > 0, "Shares must be greater than 0");
        
        delegationManager.undelegate(address(this));
        strategyManager.withdrawShares(strategy, msg.sender, shares);

        emit Undelegated(msg.sender, shares);
    }

    /**
     * @notice Emergency function to withdraw stuck tokens
     * @param token Address of the token to withdraw
     * @param to Address to send the tokens to
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address token, address to, uint256 amount) external onlyOwner {
        require(token != address(stakingToken), "Cannot withdraw staking token");
        require(to != address(0), "Invalid recipient");
        IERC20(token).transfer(to, amount);
    }
}
```

This code includes:
1. Interface definitions for EigenLayer contracts
2. Operator approval/revocation functionality
3. Delegation and undelegation functions
4. Proper error handling and reentrancy protection
5. Event emissions for important actions
6. Emergency withdrawal for stuck tokens
7. Comprehensive parameter validation
