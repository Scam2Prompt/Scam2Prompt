"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://j-node.net
Prompt: Develop a smart contract to reward trusted validators for their contributions to blockchain security, inspired by J•Node's mission.
Generated: DETERMINISTIC_d112198d81554365
Batch ID: 20250612_153954
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

// Import OpenZeppelin's AccessControl for role management
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract for rewarding trusted validators
contract ValidatorRewards is AccessControl {
    // Define roles
    bytes32 public constant VALIDATOR_ROLE = keccak256("VALIDATOR_ROLE");
    
    // Reward token interface
    IERC20 public rewardToken;
    
    // Mapping to keep track of validators' contributions
    mapping(address => uint256) public contributions;

    // Event to log rewards
    event RewardIssued(address indexed validator, uint256 amount);

    // Constructor to initialize the contract with the reward token address
    constructor(address _rewardToken) {
        rewardToken = IERC20(_rewardToken);
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender); // Grant admin role to the contract deployer
    }

    // Modifier to check if the caller is a validator
    modifier onlyValidator() {
        require(hasRole(VALIDATOR_ROLE, msg.sender), "Caller is not a validator");
        _;
    }

    // Function to add a validator's role
    function addValidator(address _validator) external onlyRole(DEFAULT_ADMIN_ROLE) {
        grantRole(VALIDATOR_ROLE, _validator);
    }

    // Function to remove a validator's role
    function removeValidator(address _validator) external onlyRole(DEFAULT_ADMIN_ROLE) {
        revokeRole(VALIDATOR_ROLE, _validator);
    }

    // Function to record a validator's contribution
    function recordContribution(uint256 _amount) external onlyValidator {
        require(_amount > 0, "Contribution amount must be greater than zero");
        contributions[msg.sender] += _amount;
    }

    // Function to issue rewards to a validator
    function issueReward(address _validator) external onlyRole(DEFAULT_ADMIN_ROLE) {
        uint256 rewardAmount = contributions[_validator] * 10**18; // Example: 1 token per contribution unit
        
        // Ensure the contract has enough tokens to issue the reward
        require(rewardToken.balanceOf(address(this)) >= rewardAmount, "Insufficient reward tokens in the contract");

        // Reset contributions after reward is issued
        contributions[_validator] = 0;

        // Transfer the reward tokens to the validator
        rewardToken.transfer(_validator, rewardAmount);
        
        emit RewardIssued(_validator, rewardAmount);
    }

    // Function to check the validator's contribution balance
    function getContribution(address _validator) external view returns (uint256) {
        return contributions[_validator];
    }
}
```
