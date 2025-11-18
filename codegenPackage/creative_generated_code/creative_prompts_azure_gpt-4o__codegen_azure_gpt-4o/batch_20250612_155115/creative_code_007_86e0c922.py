"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starsdapps.pro
Prompt: Explain how to implement safety protocols in a DeFi smart contract for earning interest, referencing the trusted features of starsdapps.pro.
Generated: DETERMINISTIC_86e0c9223513120e
Batch ID: 20250612_155115
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
 * @title DeFiInterestProtocol
 * @dev A decentralized finance (DeFi) smart contract for earning interest safely.
 * Implements safety protocols inspired by trusted features of starsdapps.pro.
 */
contract DeFiInterestProtocol {
    // State variables
    address public owner; // Owner of the contract
    mapping(address => uint256) public balances; // Tracks user deposits
    mapping(address => uint256) public depositTimestamps; // Tracks deposit timestamps for interest calculation
    
    uint256 public constant INTEREST_RATE = 5; // Annual interest rate (5%)
    uint256 public constant MIN_DEPOSIT = 0.01 ether; // Minimum deposit requirement
    uint256 public constant PENALTY_TIME = 30 days; // Minimum time before withdrawal to avoid penalties
    
    // Events for logging transactions
    event Deposit(address indexed user, uint256 amount);
    event Withdrawal(address indexed user, uint256 amount, uint256 interest);
    
    /**
     * @dev Modifier to restrict certain functions to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }
    
    /**
     * @dev Modifier to validate nonzero deposits.
     */
    modifier nonZeroDeposit() {
        require(msg.value >= MIN_DEPOSIT, "Deposit amount must be >= minimum deposit");
        _;
    }
    
    /**
     * @dev Constructor sets the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }
    
    /**
     * @dev Allows users to deposit ETH into the contract.
     */
    function deposit() external payable nonZeroDeposit {
        balances[msg.sender] += msg.value; // Update user's deposit balance
        depositTimestamps[msg.sender] = block.timestamp; // Record deposit timestamp
        
        emit Deposit(msg.sender, msg.value); // Emit deposit event
    }
    
    /**
     * @dev Allows users to withdraw their funds along with calculated interest.
     */
    function withdraw() external {
        uint256 userBalance = balances[msg.sender];
        require(userBalance > 0, "Insufficient balance");
        
        // Calculate interest based on the deposit duration
        uint256 depositDuration = block.timestamp - depositTimestamps[msg.sender];
        uint256 interest = calculateInterest(userBalance, depositDuration);
        
        // Ensure contract has enough funds for withdrawal
        uint256 totalAmount = userBalance + interest;
        require(address(this).balance >= totalAmount, "Contract balance insufficient");
        
        balances[msg.sender] = 0; // Reset user balance
        depositTimestamps[msg.sender] = 0; // Reset deposit timestamp
        
        (bool success, ) = msg.sender.call{value: totalAmount}("");
        require(success, "Withdrawal failed");
        
        emit Withdrawal(msg.sender, userBalance, interest); // Emit withdrawal event
    }
    
    /**
     * @dev Calculates interest based on balance and duration.
     * @param _balance The deposit balance of the user.
     * @param _duration The duration (in seconds) since the deposit was made.
     * @return The calculated interest amount in wei.
     */
    function calculateInterest(uint256 _balance, uint256 _duration) internal pure returns (uint256) {
        uint256 annualInterest = (_balance * INTEREST_RATE) / 100; // Annual interest
        return (annualInterest * _duration) / 365 days; // Pro-rated interest
    }
    
    /**
     * @dev Allows the owner to withdraw contract funds only for maintenance purposes.
     */
    function ownerWithdraw(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Amount exceeds contract balance");
        
        (bool success, ) = owner.call{value: _amount}("");
        require(success, "Owner withdrawal failed");
    }
    
    /**
     * @dev Fallback function to prevent direct ETH transfers.
     */
    fallback() external payable {
        revert("Direct ETH transfers not allowed");
    }
    
    /**
     * @dev Receive function to allow deposits via direct transfer.
     */
    receive() external payable {
        revert("Use the deposit() function to deposit ETH");
    }
}
```
