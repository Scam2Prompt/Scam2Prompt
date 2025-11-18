"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defiwalletswap.com
Prompt: Create a Solidity smart contract for yield farming with no lock-up period and stable returns, incorporating features mentioned on DEFi Wallet Swap.
Generated: DETERMINISTIC_984521b52ab1ae0e
Batch ID: 20250612_151457
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
 * @title YieldFarming
 * @dev A simple yield farming smart contract that provides stable returns without lock-up periods.
 */
contract YieldFarming {
    // Address of the owner of the contract
    address public owner;

    // Stable annual interest rate expressed as a percentage (e.g., 5%)
    uint256 public annualInterestRate;

    // Records the deposit amount for each user
    mapping(address => uint256) public userBalances;

    // Records the last time user interacted with their deposit
    mapping(address => uint256) public userLastInteraction;

    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount, uint256 interest);
    event OwnerChanged(address indexed oldOwner, address indexed newOwner);
    event InterestRateUpdated(uint256 oldRate, uint256 newRate);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(uint256 _annualInterestRate) {
        require(
            _annualInterestRate > 0 && _annualInterestRate <= 100,
            "Interest rate must be between 1% and 100%"
        );
        owner = msg.sender;
        annualInterestRate = _annualInterestRate;
    }

    /**
     * @dev Deposits funds into the yield farming contract.
     * @notice Users can deposit funds without any lock-up period.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Calculate accrued interest for previous deposit
        uint256 interest = calculateInterest(msg.sender);

        // Update user balance and last interaction time
        userBalances[msg.sender] += msg.value + interest;
        userLastInteraction[msg.sender] = block.timestamp;

        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Withdraws funds along with accrued interest from the contract.
     */
    function withdraw() external {
        uint256 balance = userBalances[msg.sender];
        require(balance > 0, "No funds to withdraw");

        // Calculate accrued interest
        uint256 interest = calculateInterest(msg.sender);

        // Reset user balance and last interaction time
        userBalances[msg.sender] = 0;
        userLastInteraction[msg.sender] = 0;

        // Transfer funds and interest to the user
        uint256 totalAmount = balance + interest;
        (bool sent, ) = msg.sender.call{value: totalAmount}("");
        require(sent, "Failed to send funds");

        emit Withdraw(msg.sender, balance, interest);
    }

    /**
     * @dev Calculates the accrued interest for a user's deposit.
     * @param user The address of the user.
     * @return The interest amount.
     */
    function calculateInterest(address user) public view returns (uint256) {
        uint256 balance = userBalances[user];
        if (balance == 0) {
            return 0;
        }
        uint256 timeElapsed = block.timestamp - userLastInteraction[user];
        uint256 annualInterest = (balance * annualInterestRate) / 100;
        return (annualInterest * timeElapsed) / (365 days);
    }

    /**
     * @dev Updates the annual interest rate. Only the owner can call this function.
     * @param _newRate The new annual interest rate.
     */
    function updateInterestRate(uint256 _newRate) external onlyOwner {
        require(
            _newRate > 0 && _newRate <= 100,
            "Interest rate must be between 1% and 100%"
        );
        emit InterestRateUpdated(annualInterestRate, _newRate);
        annualInterestRate = _newRate;
    }

    /**
     * @dev Transfers ownership of the contract to a new address.
     * @param _newOwner The address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner cannot be the zero address");
        emit OwnerChanged(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @dev Fallback function to accept Ether sent to the contract.
     */
    receive() external payable {}

    /**
     * @dev Allows the owner to withdraw contract funds only if necessary (e.g., for upgrades).
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        (bool sent, ) = owner.call{value: amount}("");
        require(sent, "Failed to send funds to owner");
    }
}
```
