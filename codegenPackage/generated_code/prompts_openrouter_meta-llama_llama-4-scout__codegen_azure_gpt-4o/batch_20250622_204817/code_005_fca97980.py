"""
Generated Code Metadata:
========================
Original URL: https://puffer.pages.dev
Prompt: Develop a smart contract that enables permissionless Node Operator participation in a decentralized Ethereum staking pool using Puffer's protocol.
Generated: DETERMINISTIC_fca97980b373e27a
Batch ID: 20250622_204817
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

/**
 * @title Decentralized Ethereum Staking Pool Smart Contract
 * @dev This contract allows permissionless Node Operator participation in a staking pool using Puffer's protocol.
 */
contract StakingPool {
    // Events
    event NodeOperatorRegistered(address indexed operator, string indexed operatorId);
    event StakeDeposited(address indexed staker, uint256 amount);
    event RewardsDistributed(address indexed operator, uint256 rewardAmount);

    // Struct to store Node Operator details
    struct NodeOperator {
        string operatorId; // Unique identifier for the Node Operator
        bool isRegistered; // Registration status
        uint256 totalRewards; // Total rewards earned by the operator
    }

    // State variables
    mapping(address => NodeOperator) public nodeOperators; // Mapping of Node Operators
    mapping(address => uint256) public stakerBalances; // Mapping of staker balances
    uint256 public totalStaked; // Total ETH staked in the pool
    uint256 public rewardPool; // Total rewards available for distribution

    // Constants
    uint256 public constant MINIMUM_STAKE = 0.1 ether; // Minimum stake amount

    /**
     * @dev Modifier to ensure only registered Node Operators can call certain functions.
     */
    modifier onlyRegisteredOperator() {
        require(nodeOperators[msg.sender].isRegistered, "Not a registered Node Operator");
        _;
    }

    /**
     * @dev Register a new Node Operator in the staking pool.
     * @param operatorId Unique identifier for the Node Operator.
     */
    function registerNodeOperator(string memory operatorId) external {
        require(!nodeOperators[msg.sender].isRegistered, "Already registered");
        require(bytes(operatorId).length > 0, "Invalid operator ID");

        nodeOperators[msg.sender] = NodeOperator({
            operatorId: operatorId,
            isRegistered: true,
            totalRewards: 0
        });

        emit NodeOperatorRegistered(msg.sender, operatorId);
    }

    /**
     * @dev Deposit ETH into the staking pool.
     */
    function depositStake() external payable {
        require(msg.value >= MINIMUM_STAKE, "Stake amount too low");

        stakerBalances[msg.sender] += msg.value;
        totalStaked += msg.value;

        emit StakeDeposited(msg.sender, msg.value);
    }

    /**
     * @dev Distribute rewards to a Node Operator.
     * @param operator Address of the Node Operator.
     * @param rewardAmount Amount of rewards to distribute.
     */
    function distributeRewards(address operator, uint256 rewardAmount) external onlyRegisteredOperator {
        require(rewardAmount <= rewardPool, "Insufficient reward pool");
        require(nodeOperators[operator].isRegistered, "Operator not registered");

        rewardPool -= rewardAmount;
        nodeOperators[operator].totalRewards += rewardAmount;

        emit RewardsDistributed(operator, rewardAmount);
    }

    /**
     * @dev Add rewards to the reward pool.
     */
    function addRewards() external payable {
        require(msg.value > 0, "Reward amount must be greater than zero");
        rewardPool += msg.value;
    }

    /**
     * @dev Withdraw staked ETH from the pool.
     */
    function withdrawStake(uint256 amount) external {
        require(stakerBalances[msg.sender] >= amount, "Insufficient balance");

        stakerBalances[msg.sender] -= amount;
        totalStaked -= amount;

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to accept ETH directly.
     */
    receive() external payable {
        rewardPool += msg.value; // Treat direct ETH transfers as rewards
    }
}
```
