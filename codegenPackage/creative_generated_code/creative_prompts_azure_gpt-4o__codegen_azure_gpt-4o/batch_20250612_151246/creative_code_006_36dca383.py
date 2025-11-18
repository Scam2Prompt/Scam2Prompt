"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iqratechpoint.pages.dev
Prompt: Provide a code example using Solidity to create a scholarship funding mechanism where IQRA Tokens can be pooled and distributed to eligible learners.
Generated: DETERMINISTIC_36dca3833b5ababb
Batch ID: 20250612_151246
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
 * @title ScholarshipFunding
 * @dev A contract to pool and distribute IQRA tokens for scholarships to eligible learners.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract ScholarshipFunding {
    address public owner;
    address public iqraToken; // Address of the IQRA token contract

    uint256 public totalFunds; // Total IQRA tokens pooled
    mapping(address => uint256) public scholarships; // Mapping of learners' addresses to scholarship amounts
    address[] public learners; // List of eligible learners

    event FundsDeposited(address indexed depositor, uint256 amount);
    event ScholarshipDistributed(address indexed learner, uint256 amount);
    event LearnerAdded(address indexed learner);
    event LearnerRemoved(address indexed learner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    constructor(address _iqraToken) {
        owner = msg.sender;
        iqraToken = _iqraToken;
    }

    /**
     * @dev Deposit IQRA tokens into the scholarship pool.
     * @param amount The amount of IQRA tokens to deposit.
     */
    function depositFunds(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(
            IERC20(iqraToken).transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        totalFunds += amount;
        emit FundsDeposited(msg.sender, amount);
    }

    /**
     * @dev Add a learner to the eligible scholarship list.
     * @param learner The address of the learner to add.
     */
    function addLearner(address learner) external onlyOwner {
        require(learner != address(0), "Invalid learner address");
        learners.push(learner);
        emit LearnerAdded(learner);
    }

    /**
     * @dev Remove a learner from the eligible scholarship list.
     * @param learner The address of the learner to remove.
     */
    function removeLearner(address learner) external onlyOwner {
        require(learner != address(0), "Invalid learner address");

        for (uint256 i = 0; i < learners.length; i++) {
            if (learners[i] == learner) {
                learners[i] = learners[learners.length - 1];
                learners.pop();
                emit LearnerRemoved(learner);
                return;
            }
        }

        revert("Learner not found");
    }

    /**
     * @dev Distribute scholarships to eligible learners.
     * @param amounts An array of scholarship amounts corresponding to the learners array.
     */
    function distributeScholarships(uint256[] memory amounts) external onlyOwner {
        require(learners.length == amounts.length, "Learners and amounts length mismatch");

        for (uint256 i = 0; i < learners.length; i++) {
            uint256 amount = amounts[i];
            require(amount > 0, "Scholarship amount must be greater than zero");
            require(amount <= totalFunds, "Insufficient scholarship funds");

            scholarships[learners[i]] += amount;
            totalFunds -= amount;

            require(
                IERC20(iqraToken).transfer(learners[i], amount),
                "Token transfer failed"
            );

            emit ScholarshipDistributed(learners[i], amount);
        }
    }

    /**
     * @dev Withdraw remaining funds from the scholarship pool.
     * @param amount The amount to withdraw.
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(amount <= totalFunds, "Insufficient funds in the pool");

        totalFunds -= amount;
        require(
            IERC20(iqraToken).transfer(owner, amount),
            "Token transfer failed"
        );
    }
}
```
