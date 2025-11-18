"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigachadgpt-io.web.app
Prompt: Create a Solidity contract for vesting team tokens, ensuring compliance with the $GIGA tokenomics (5% allocation with locked tokens).
Generated: DETERMINISTIC_4b702b5299ec2e14
Batch ID: 20250612_152422
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

// Import the OpenZeppelin Contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Vesting contract for team tokens
contract TeamTokenVesting is Ownable {
    // Token to be vested
    IERC20 public token;
    
    // Vesting details
    uint256 public vestingStart;
    uint256 public vestingDuration;
    uint256 public totalVestingAmount;
    uint256 public releasedAmount;
    uint256 public constant ALLOCATION_PERCENTAGE = 5; // 5% allocation for team
    
    // Event for logging token release
    event TokensReleased(address indexed beneficiary, uint256 amount);

    // Mapping to store beneficiary addresses and their vested amounts
    mapping(address => uint256) private _beneficiaries;

    // Constructor to initialize the contract
    constructor(
        address _tokenAddress,
        uint256 _totalAmount,
        uint256 _vestingDurationInDays
    ) {
        require(_totalAmount > 0, "Total amount must be greater than 0");
        require(_vestingDurationInDays > 0, "Vesting duration must be greater than 0");

        token = IERC20(_tokenAddress);
        totalVestingAmount = _totalAmount;
        vestingDuration = _vestingDurationInDays * 1 days; // Convert days to seconds
        vestingStart = block.timestamp; // Set vesting start time

        // Calculate the total amount to be allocated for the vesting
        uint256 allocationAmount = (totalVestingAmount * ALLOCATION_PERCENTAGE) / 100;
        
        // Ensure the contract has enough tokens for the vesting
        require(token.balanceOf(address(this)) >= allocationAmount, "Insufficient token balance for vesting");
        
        // Allocate tokens to beneficiaries
        _beneficiaries[msg.sender] = allocationAmount; // For simplicity, assigning to the contract owner
    }

    // Function to release vested tokens
    function releaseTokens() external {
        uint256 releasable = _releasableAmount();
        require(releasable > 0, "No tokens to release");

        releasedAmount += releasable;
        token.transfer(msg.sender, releasable);

        emit TokensReleased(msg.sender, releasable);
    }

    // Internal function to calculate releasable amount
    function _releasableAmount() internal view returns (uint256) {
        uint256 elapsedTime = block.timestamp - vestingStart;
        if (elapsedTime >= vestingDuration) {
            return totalVestingAmount - releasedAmount; // All tokens are releasable at the end
        } else {
            uint256 vestedAmount = (totalVestingAmount * elapsedTime) / vestingDuration;
            return vestedAmount - releasedAmount; // Calculate releasable tokens
        }
    }

    // Function to withdraw tokens in case of emergency
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= token.balanceOf(address(this)), "Insufficient contract balance");
        token.transfer(owner(), amount);
    }

    // Function to view the vested amount for a beneficiary
    function vestedAmount() external view returns (uint256) {
        return totalVestingAmount - releasedAmount;
    }
}
```
