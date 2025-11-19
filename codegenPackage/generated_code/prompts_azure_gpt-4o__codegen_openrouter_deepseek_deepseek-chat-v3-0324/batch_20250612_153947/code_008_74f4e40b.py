"""
Generated Code Metadata:
========================
Original URL: https://claires.pages.dev
Prompt: Write a Solidity contract that leverages Symbiotic's scalable architecture for maximally capital-efficient sourcing of node operators.
Generated: DETERMINISTIC_74f4e40b2cdbeae6
Batch ID: 20250612_153947
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

/**
 * @title SymbioticNodeOperatorRegistry
 * @dev A capital-efficient registry for node operators leveraging Symbiotic's architecture
 */
contract SymbioticNodeOperatorRegistry is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct Operator {
        address operatorAddress;
        uint256 stakedAmount;
        uint256 commissionRate; // Basis points (1/100 of a percent)
        uint256 minDelegation;
        uint256 maxDelegation;
        bool active;
    }

    // Token used for staking
    IERC20 public stakingToken;

    // Operator ID to Operator mapping
    mapping(uint256 => Operator) public operators;
    uint256 public operatorCount;

    // Operator address to ID mapping
    mapping(address => uint256) public operatorIds;

    // Delegator to operator mapping
    mapping(address => uint256) public delegations;

    // Total staked amount across all operators
    uint256 public totalStaked;

    // Events
    event OperatorRegistered(
        uint256 indexed operatorId,
        address indexed operatorAddress,
        uint256 commissionRate,
        uint256 minDelegation,
        uint256 maxDelegation
    );
    event OperatorActivated(uint256 indexed operatorId);
    event OperatorDeactivated(uint256 indexed operatorId);
    event StakeDeposited(uint256 indexed operatorId, uint256 amount);
    event StakeWithdrawn(uint256 indexed operatorId, uint256 amount);
    event Delegated(address indexed delegator, uint256 indexed operatorId, uint256 amount);
    event Undelegated(address indexed delegator, uint256 indexed operatorId, uint256 amount);

    /**
     * @dev Constructor
     * @param _stakingToken Address of the ERC20 token used for staking
     */
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
    }

    /**
     * @dev Register a new node operator
     * @param _operatorAddress Address of the operator
     * @param _commissionRate Operator's commission rate in basis points
     * @param _minDelegation Minimum delegation amount
     * @param _maxDelegation Maximum delegation amount
     */
    function registerOperator(
        address _operatorAddress,
        uint256 _commissionRate,
        uint256 _minDelegation,
        uint256 _maxDelegation
    ) external onlyOwner {
        require(_operatorAddress != address(0), "Invalid operator address");
        require(_commissionRate <= 10000, "Commission rate too high");
        require(_minDelegation <= _maxDelegation, "Invalid delegation bounds");

        operatorCount++;
        operators[operatorCount] = Operator({
            operatorAddress: _operatorAddress,
            stakedAmount: 0,
            commissionRate: _commissionRate,
            minDelegation: _minDelegation,
            maxDelegation: _maxDelegation,
            active: true
        });
        operatorIds[_operatorAddress] = operatorCount;

        emit OperatorRegistered(
            operatorCount,
            _operatorAddress,
            _commissionRate,
            _minDelegation,
            _maxDelegation
        );
        emit OperatorActivated(operatorCount);
    }

    /**
     * @dev Activate an operator
     * @param _operatorId ID of the operator to activate
     */
    function activateOperator(uint256 _operatorId) external onlyOwner {
        require(_operatorId <= operatorCount, "Invalid operator ID");
        require(!operators[_operatorId].active, "Operator already active");

        operators[_operatorId].active = true;
        emit OperatorActivated(_operatorId);
    }

    /**
     * @dev Deactivate an operator
     * @param _operatorId ID of the operator to deactivate
     */
    function deactivateOperator(uint256 _operatorId) external onlyOwner {
        require(_operatorId <= operatorCount, "Invalid operator ID");
        require(operators[_operatorId].active, "Operator already inactive");

        operators[_operatorId].active = false;
        emit OperatorDeactivated(_operatorId);
    }

    /**
     * @dev Stake tokens as an operator
     * @param _operatorId ID of the operator
     * @param _amount Amount to stake
     */
    function stake(uint256 _operatorId, uint256 _amount) external nonReentrant {
        require(_operatorId <= operatorCount, "Invalid operator ID");
        Operator storage operator = operators[_operatorId];
        require(msg.sender == operator.operatorAddress, "Not operator");
        require(operator.active, "Operator inactive");

        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
        operator.stakedAmount += _amount;
        totalStaked += _amount;

        emit StakeDeposited(_operatorId, _amount);
    }

    /**
     * @dev Withdraw staked tokens as an operator
     * @param _operatorId ID of the operator
     * @param _amount Amount to withdraw
     */
    function withdrawStake(uint256 _operatorId, uint256 _amount) external nonReentrant {
        require(_operatorId <= operatorCount, "Invalid operator ID");
        Operator storage operator = operators[_operatorId];
        require(msg.sender == operator.operatorAddress, "Not operator");
        require(operator.stakedAmount >= _amount, "Insufficient stake");

        operator.stakedAmount -= _amount;
        totalStaked -= _amount;
        stakingToken.safeTransfer(msg.sender, _amount);

        emit StakeWithdrawn(_operatorId, _amount);
    }

    /**
     * @dev Delegate tokens to an operator
     * @param _operatorId ID of the operator
     * @param _amount Amount to delegate
     */
    function delegate(uint256 _operatorId, uint256 _amount) external nonReentrant {
        require(_operatorId <= operatorCount, "Invalid operator ID");
        Operator storage operator = operators[_operatorId];
        require(operator.active, "Operator inactive");
        require(_amount >= operator.minDelegation, "Amount below minimum");
        require(
            operator.stakedAmount + _amount <= operator.maxDelegation,
            "Amount exceeds maximum"
        );

        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
        operator.stakedAmount += _amount;
        totalStaked += _amount;
        delegations[msg.sender] = _operatorId;

        emit Delegated(msg.sender, _operatorId, _amount);
    }

    /**
     * @dev Undelegate tokens from an operator
     * @param _amount Amount to undelegate
     */
    function undelegate(uint256 _amount) external nonReentrant {
        uint256 operatorId = delegations[msg.sender];
        require(operatorId != 0, "No delegation found");
        Operator storage operator = operators[operatorId];
        require(operator.stakedAmount >= _amount, "Insufficient delegation");

        operator.stakedAmount -= _amount;
        totalStaked -= _amount;
        stakingToken.safeTransfer(msg.sender, _amount);

        if (operator.stakedAmount == 0) {
            delete delegations[msg.sender];
        }

        emit Undelegated(msg.sender, operatorId, _amount);
    }

    /**
     * @dev Get operator details
     * @param _operatorId ID of the operator
     * @return Operator details
     */
    function getOperator(uint256 _operatorId) external view returns (Operator memory) {
        require(_operatorId <= operatorCount, "Invalid operator ID");
        return operators[_operatorId];
    }

    /**
     * @dev Get current delegation for a delegator
     * @param _delegator Address of the delegator
     * @return operatorId ID of the delegated operator
     */
    function getDelegation(address _delegator) external view returns (uint256 operatorId) {
        return delegations[_delegator];
    }
}
```
