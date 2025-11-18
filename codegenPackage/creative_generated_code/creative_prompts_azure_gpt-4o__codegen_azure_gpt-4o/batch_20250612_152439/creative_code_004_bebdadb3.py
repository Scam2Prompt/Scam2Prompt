"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eveyry.pages.dev
Prompt: Generate code in Solidity to implement a token distribution mechanism where rewards unlock in equal monthly installments over 3 years, as outlined in Everyworld's payout structure.
Generated: DETERMINISTIC_bebdadb36a846572
Batch ID: 20250612_152439
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
 * @title TokenDistribution
 * @dev Implements a reward distribution mechanism with monthly vesting over 3 years.
 */
contract TokenDistribution {
    // Token structure to store beneficiary details
    struct Beneficiary {
        uint256 totalReward; // Total reward assigned to the beneficiary
        uint256 monthlyUnlockAmount; // Amount unlocked per month
        uint256 claimedAmount; // Total amount claimed by the beneficiary
        uint256 startTime; // Timestamp when vesting starts
    }

    uint256 public constant MONTHLY_INTERVAL = 30 days; // Monthly interval in seconds
    uint256 public constant VESTING_PERIOD = 3 * 12; // 3 years (36 months)

    address public admin; // Address of the contract administrator
    mapping(address => Beneficiary) public beneficiaries; // Mapping of beneficiaries' data
    
    event RewardClaimed(address indexed beneficiary, uint256 amount);

    modifier onlyAdmin() {
        require(msg.sender == admin, "Caller is not the admin");
        _;
    }

    modifier onlyBeneficiary() {
        require(beneficiaries[msg.sender].totalReward > 0, "Caller is not a beneficiary");
        _;
    }

    constructor() {
        admin = msg.sender;
    }

    /**
     * @notice Assign reward to a beneficiary
     * @param _beneficiary Address of the beneficiary
     * @param _totalReward Total reward to be distributed over 3 years
     * @param _startTime Start time for the vesting schedule
     */
    function assignReward(
        address _beneficiary,
        uint256 _totalReward,
        uint256 _startTime
    ) external onlyAdmin {
        require(_beneficiary != address(0), "Invalid beneficiary address");
        require(_totalReward > 0, "Reward must be greater than zero");
        require(_startTime > block.timestamp, "Start time must be in the future");

        require(
            beneficiaries[_beneficiary].totalReward == 0,
            "Reward already assigned to this beneficiary"
        );

        // Calculate monthly unlock amount
        uint256 monthlyUnlock = _totalReward / VESTING_PERIOD;

        beneficiaries[_beneficiary] = Beneficiary({
            totalReward: _totalReward,
            monthlyUnlockAmount: monthlyUnlock,
            claimedAmount: 0,
            startTime: _startTime
        });
    }

    /**
     * @notice Claim unlocked rewards by the beneficiary
     */
    function claimReward() external onlyBeneficiary {
        Beneficiary storage beneficiary = beneficiaries[msg.sender];

        // Calculate elapsed months
        uint256 elapsedMonths = (block.timestamp - beneficiary.startTime) / MONTHLY_INTERVAL;

        // Ensure elapsed months don't exceed vesting period
        if (elapsedMonths > VESTING_PERIOD) {
            elapsedMonths = VESTING_PERIOD;
        }

        // Calculate claimable amount
        uint256 claimableAmount = (elapsedMonths * beneficiary.monthlyUnlockAmount) - beneficiary.claimedAmount;

        require(claimableAmount > 0, "No rewards available to claim");

        // Update claimed amount
        beneficiary.claimedAmount += claimableAmount;

        // Send the reward to the beneficiary
        payable(msg.sender).transfer(claimableAmount);

        emit RewardClaimed(msg.sender, claimableAmount);
    }

    /**
     * @notice Fallback function to accept Ether
     */
    receive() external payable {}

    /**
     * @notice Withdraw Ether from the contract by the admin
     * @param _amount Amount to withdraw
     */
    function withdraw(uint256 _amount) external onlyAdmin {
        require(_amount <= address(this).balance, "Insufficient contract balance");
        payable(admin).transfer(_amount);
    }
}
```
