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

// Import OpenZeppelin's SafeERC20 library and ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

// Scholarship Fund contract
contract ScholarshipFund {
    using SafeERC20 for IERC20;

    // State variables
    IERC20 public iqraToken; // The IQRA Token contract
    address public owner; // Contract owner address
    uint256 public totalPool; // Total amount of IQRA Tokens pooled
    mapping(address => uint256) public contributions; // Contributions by each address
    mapping(address => bool) public eligibleLearners; // Eligibility status of learners

    // Events
    event ContributionMade(address indexed contributor, uint256 amount);
    event ScholarshipDistributed(address indexed learner, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier onlyEligibleLearner() {
        require(eligibleLearners[msg.sender], "Caller is not an eligible learner");
        _;
    }

    // Constructor
    constructor(IERC20 _iqraToken) {
        iqraToken = _iqraToken;
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to contribute IQRA Tokens to the pool
    function contribute(uint256 amount) external {
        require(amount > 0, "Contribution amount must be greater than zero");
        
        // Transfer tokens from contributor to the contract
        iqraToken.safeTransferFrom(msg.sender, address(this), amount);
        
        // Update total pool and contributor mapping
        totalPool += amount;
        contributions[msg.sender] += amount;

        emit ContributionMade(msg.sender, amount);
    }

    // Function to set eligibility for learners
    function setEligibility(address learner, bool isEligible) external onlyOwner {
        eligibleLearners[learner] = isEligible;
    }

    // Function to distribute scholarships to eligible learners
    function distributeScholarship(uint256 amount) external onlyOwner {
        require(totalPool >= amount, "Insufficient funds in the pool");
        
        // Distribute funds to each eligible learner
        for (uint256 i = 0; i < eligibleLearners.length; i++) {
            address learner = eligibleLearners[i];
            if (eligibleLearners[learner]) {
                iqraToken.safeTransfer(learner, amount);
                totalPool -= amount; // Deduct the amount from the pool
                emit ScholarshipDistributed(learner, amount);
            }
        }
    }

    // Function to withdraw remaining tokens (only callable by owner)
    function withdrawRemainingTokens() external onlyOwner {
        uint256 balance = iqraToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        
        // Transfer remaining tokens to the owner
        iqraToken.safeTransfer(owner, balance);
    }
}
```
