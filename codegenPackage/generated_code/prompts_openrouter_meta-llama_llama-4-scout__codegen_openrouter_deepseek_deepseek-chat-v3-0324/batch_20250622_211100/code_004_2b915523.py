"""
Generated Code Metadata:
========================
Original URL: https://benqi.cc
Prompt: Generate a smart contract code for creating a custom Avalanche validator or subnet using BENQI's Ignite feature.
Generated: DETERMINISTIC_2b915523b7fc3e6e
Batch ID: 20250622_211100
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
 * @title BENQI Ignite Validator/Subnet Creator
 * @notice Smart contract for creating custom Avalanche validators/subnets using BENQI's Ignite feature
 * @dev Implements validator/subnet creation with staking requirements and fee distribution
 */
contract BenqiIgniteValidator is Ownable, ReentrancyGuard {
    // Token used for staking (QI token)
    IERC20 public stakingToken;
    
    // Minimum staking amount required to create a validator/subnet
    uint256 public minStakeAmount;
    
    // Duration for which tokens must be staked (in seconds)
    uint256 public stakeDuration;
    
    // Fee percentage taken by BENQI (basis points, where 10000 = 100%)
    uint256 public feeBasisPoints;
    
    // Address where fees are sent
    address public feeCollector;
    
    // Mapping of validator IDs to their details
    mapping(bytes32 => Validator) public validators;
    
    // Mapping of user addresses to their staked amounts
    mapping(address => uint256) public stakedBalances;
    
    // Mapping of user addresses to their stake unlock times
    mapping(address => uint256) public stakeUnlockTimes;
    
    // Validator details structure
    struct Validator {
        address creator;
        uint256 stakedAmount;
        uint256 creationTime;
        string name;
        string description;
        bool isActive;
    }
    
    // Events
    event ValidatorCreated(
        bytes32 indexed validatorId,
        address indexed creator,
        string name,
        uint256 stakedAmount,
        uint256 creationTime
    );
    
    event StakeDeposited(address indexed user, uint256 amount);
    event StakeWithdrawn(address indexed user, uint256 amount);
    event FeeCollected(address indexed collector, uint256 amount);
    event ParametersUpdated(
        uint256 minStakeAmount,
        uint256 stakeDuration,
        uint256 feeBasisPoints
    );
    
    /**
     * @dev Constructor initializes the contract with required parameters
     * @param _stakingToken Address of the staking token (QI)
     * @param _minStakeAmount Minimum amount required to stake
     * @param _stakeDuration Duration tokens must be staked (in seconds)
     * @param _feeBasisPoints Fee percentage in basis points
     * @param _feeCollector Address where fees are collected
     */
    constructor(
        address _stakingToken,
        uint256 _minStakeAmount,
        uint256 _stakeDuration,
        uint256 _feeBasisPoints,
        address _feeCollector
    ) {
        require(_stakingToken != address(0), "Invalid token address");
        require(_feeCollector != address(0), "Invalid fee collector");
        
        stakingToken = IERC20(_stakingToken);
        minStakeAmount = _minStakeAmount;
        stakeDuration = _stakeDuration;
        feeBasisPoints = _feeBasisPoints;
        feeCollector = _feeCollector;
    }
    
    /**
     * @notice Stake tokens to be eligible for validator/subnet creation
     * @param amount Amount of tokens to stake
     */
    function depositStake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        stakedBalances[msg.sender] += amount;
        stakeUnlockTimes[msg.sender] = block.timestamp + stakeDuration;
        
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );
        
        emit StakeDeposited(msg.sender, amount);
    }
    
    /**
     * @notice Withdraw staked tokens after lock period expires
     */
    function withdrawStake() external nonReentrant {
        require(
            stakeUnlockTimes[msg.sender] <= block.timestamp,
            "Stake is still locked"
        );
        require(stakedBalances[msg.sender] > 0, "No stake to withdraw");
        
        uint256 amount = stakedBalances[msg.sender];
        stakedBalances[msg.sender] = 0;
        stakeUnlockTimes[msg.sender] = 0;
        
        require(
            stakingToken.transfer(msg.sender, amount),
            "Token transfer failed"
        );
        
        emit StakeWithdrawn(msg.sender, amount);
    }
    
    /**
     * @notice Create a new validator/subnet
     * @param name Name of the validator/subnet
     * @param description Description of the validator/subnet
     * @param stakeAmount Amount to stake for this validator
     * @return validatorId The unique ID of the created validator
     */
    function createValidator(
        string memory name,
        string memory description,
        uint256 stakeAmount
    ) external nonReentrant returns (bytes32 validatorId) {
        require(stakeAmount >= minStakeAmount, "Insufficient stake amount");
        require(
            stakedBalances[msg.sender] >= stakeAmount,
            "Insufficient staked balance"
        );
        require(bytes(name).length > 0, "Name cannot be empty");
        
        validatorId = keccak256(abi.encodePacked(msg.sender, block.timestamp, name));
        
        uint256 feeAmount = (stakeAmount * feeBasisPoints) / 10000;
        uint256 netStakeAmount = stakeAmount - feeAmount;
        
        validators[validatorId] = Validator({
            creator: msg.sender,
            stakedAmount: netStakeAmount,
            creationTime: block.timestamp,
            name: name,
            description: description,
            isActive: true
        });
        
        stakedBalances[msg.sender] -= stakeAmount;
        
        // Transfer fee to collector
        if (feeAmount > 0) {
            require(
                stakingToken.transfer(feeCollector, feeAmount),
                "Fee transfer failed"
            );
            emit FeeCollected(feeCollector, feeAmount);
        }
        
        emit ValidatorCreated(
            validatorId,
            msg.sender,
            name,
            netStakeAmount,
            block.timestamp
        );
        
        return validatorId;
    }
    
    /**
     * @notice Update validator parameters (owner only)
     * @param _minStakeAmount New minimum stake amount
     * @param _stakeDuration New stake duration
     * @param _feeBasisPoints New fee basis points
     */
    function updateParameters(
        uint256 _minStakeAmount,
        uint256 _stakeDuration,
        uint256 _feeBasisPoints
    ) external onlyOwner {
        minStakeAmount = _minStakeAmount;
        stakeDuration = _stakeDuration;
        feeBasisPoints = _feeBasisPoints;
        
        emit ParametersUpdated(
            _minStakeAmount,
            _stakeDuration,
            _feeBasisPoints
        );
    }
    
    /**
     * @notice Update fee collector address (owner only)
     * @param _feeCollector New fee collector address
     */
    function updateFeeCollector(address _feeCollector) external onlyOwner {
        require(_feeCollector != address(0), "Invalid fee collector");
        feeCollector = _feeCollector;
    }
    
    /**
     * @notice Get validator details by ID
     * @param validatorId ID of the validator
     * @return Validator details
     */
    function getValidator(bytes32 validatorId) external view returns (Validator memory) {
        return validators[validatorId];
    }
    
    /**
     * @notice Check if a validator exists and is active
     * @param validatorId ID of the validator
     * @return True if validator exists and is active
     */
    function isValidatorActive(bytes32 validatorId) external view returns (bool) {
        return validators[validatorId].isActive;
    }
    
    /**
     * @notice Get user's staked balance
     * @param user Address of the user
     * @return Staked balance amount
     */
    function getUserStake(address user) external view returns (uint256) {
        return stakedBalances[user];
    }
    
    /**
     * @notice Get user's stake unlock time
     * @param user Address of the user
     * @return Stake unlock timestamp
     */
    function getUserUnlockTime(address user) external view returns (uint256) {
        return stakeUnlockTimes[user];
    }
}
```
