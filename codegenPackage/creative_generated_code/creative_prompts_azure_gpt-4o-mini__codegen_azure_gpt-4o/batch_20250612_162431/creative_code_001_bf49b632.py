"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geoins.ru
Prompt: Write a code snippet for a decentralized application that allows users to stake QI tokens and manage collateral for MAI issuance.
Generated: DETERMINISTIC_bf49b63286fecc68
Batch ID: 20250612_162431
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
 * @title QITokenStakingAndCollateralManagement
 * @notice This contract allows users to stake QI tokens and manage collateral for MAI issuance
 */
contract QITokenStakingAndCollateralManagement {
    IERC20 public qiToken; // Interface for the QI token contract
    IERC20 public maiToken; // Interface for the MAI token contract

    mapping(address => uint256) public stakes; // Tracks the QI tokens staked by each user
    mapping(address => uint256) public collateral; // Tracks collateral provided by each user

    uint256 public totalStaked; // Total amount of QI tokens staked in the contract
    uint256 public collateralFactor = 150; // Collateralization ratio in percentage (e.g., 150%)

    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event CollateralProvided(address indexed user, uint256 amount);
    event MAIIssued(address indexed user, uint256 amount);
    event MAIRepayed(address indexed user, uint256 amount);

    // Modifier: Restricts access to only the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Unauthorized: Only owner can call this function");
        _;
    }

    /**
     * @dev Initializes the contract with the QI and MAI token addresses
     * @param _qiToken Address of the QI token contract
     * @param _maiToken Address of the MAI token contract
     */
    constructor(address _qiToken, address _maiToken) {
        require(_qiToken != address(0), "Invalid QI token address");
        require(_maiToken != address(0), "Invalid MAI token address");

        qiToken = IERC20(_qiToken);
        maiToken = IERC20(_maiToken);
        owner = msg.sender;
    }

    /**
     * @notice Stake QI tokens in the contract
     * @param amount The amount of QI tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer QI tokens from the sender to the contract
        require(qiToken.transferFrom(msg.sender, address(this), amount), "Failed to transfer QI tokens");

        // Update user's stake balance and total staked
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake QI tokens from the contract
     * @param amount The amount of QI tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient staked balance");

        // Update user's stake balance and total staked
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer QI tokens from the contract to the sender
        require(qiToken.transfer(msg.sender, amount), "Failed to transfer QI tokens");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Provide collateral for MAI issuance
     * @param amount The amount of collateral to provide
     */
    function provideCollateral(uint256 amount) external {
        require(amount > 0, "Collateral amount must be greater than zero");

        // Transfer QI tokens from the sender to the contract
        require(qiToken.transferFrom(msg.sender, address(this), amount), "Failed to transfer QI tokens");

        // Update user's collateral balance
        collateral[msg.sender] += amount;

        emit CollateralProvided(msg.sender, amount);
    }

    /**
     * @notice Issue MAI tokens based on provided collateral
     * @param amount The amount of MAI tokens to issue
     */
    function issueMAI(uint256 amount) external {
        require(amount > 0, "Issue amount must be greater than zero");
        uint256 maxIssuable = collateral[msg.sender] * 100 / collateralFactor;
        require(amount <= maxIssuable, "Insufficient collateral for requested MAI issuance");

        // Mint MAI tokens to the sender
        require(maiToken.transfer(msg.sender, amount), "Failed to transfer MAI tokens");

        emit MAIIssued(msg.sender, amount);
    }

    /**
     * @notice Repay MAI tokens to free up collateral
     * @param amount The amount of MAI tokens to repay
     */
    function repayMAI(uint256 amount) external {
        require(amount > 0, "Repay amount must be greater than zero");

        // Transfer MAI tokens from the sender to the contract
        require(maiToken.transferFrom(msg.sender, address(this), amount), "Failed to transfer MAI tokens");

        uint256 collateralToFree = amount * collateralFactor / 100;
        require(collateral[msg.sender] >= collateralToFree, "Insufficient collateral balance");

        // Update collateral balance
        collateral[msg.sender] -= collateralToFree;

        emit MAIRepayed(msg.sender, amount);
    }

    /**
     * @notice Update the collateralization factor (only owner)
     * @param newFactor The new collateralization factor (in percentage)
     */
    function updateCollateralFactor(uint256 newFactor) external onlyOwner {
        require(newFactor >= 100, "Collateral factor must be at least 100%");

        collateralFactor = newFactor;
    }
}

// IERC20 interface definition
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
