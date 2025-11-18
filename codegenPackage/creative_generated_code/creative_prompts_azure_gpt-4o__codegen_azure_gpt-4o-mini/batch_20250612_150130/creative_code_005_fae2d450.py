"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim.berafi.xyz
Prompt: Develop a smart contract function to automate token vesting for users claiming tokens through the BERAFI Claim Portal.
Generated: DETERMINISTIC_fae2d45007b4dc49
Batch ID: 20250612_150130
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenVesting
 * @dev This contract automates token vesting for users through the BERAFI Claim Portal.
 */
contract TokenVesting is Ownable {
    // Structure to hold vesting details for each beneficiary
    struct Beneficiary {
        uint256 totalAmount;    // Total amount of tokens allocated
        uint256 releasedAmount;  // Amount of tokens already released
        uint256 start;           // Start time of the vesting
        uint256 duration;        // Duration of the vesting in seconds
    }

    // Mapping of beneficiaries to their vesting details
    mapping(address => Beneficiary) private beneficiaries;

    // The token that will be vested
    IERC20 public token;

    // Event to signal token release
    event TokensReleased(address beneficiary, uint256 amount);

    /**
     * @dev Constructor to set the token address.
     * @param _token Address of the ERC20 token that will be vested.
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
    }

    /**
     * @dev Adds a new beneficiary with vesting details.
     * @param _beneficiary Address of the beneficiary.
     * @param _totalAmount Total amount of tokens allocated.
     * @param _start Start time of the vesting period.
     * @param _duration Duration of the vesting period in seconds.
     */
    function addBeneficiary(
        address _beneficiary,
        uint256 _totalAmount,
        uint256 _start,
        uint256 _duration
    ) external onlyOwner {
        require(_beneficiary != address(0), "Beneficiary address cannot be zero");
        require(_totalAmount > 0, "Total amount must be greater than 0");
        require(_duration > 0, "Duration must be greater than 0");
        
        beneficiaries[_beneficiary] = Beneficiary({
            totalAmount: _totalAmount,
            releasedAmount: 0,
            start: _start,
            duration: _duration
        });
    }

    /**
     * @dev Releases vested tokens to the beneficiary.
     */
    function release() external {
        Beneficiary storage beneficiary = beneficiaries[msg.sender];

        require(beneficiary.totalAmount > 0, "No tokens to release");
        
        uint256 unreleased = _releasableAmount(beneficiary);
        require(unreleased > 0, "No releasable tokens");

        beneficiary.releasedAmount += unreleased;

        // Transfer the tokens
        require(token.transfer(msg.sender, unreleased), "Token transfer failed");

        emit TokensReleased(msg.sender, unreleased);
    }

    /**
     * @dev Calculates the amount of tokens that can be released.
     * @param beneficiary The beneficiary's vesting details.
     * @return Amount of tokens that can be released.
     */
    function _releasableAmount(Beneficiary storage beneficiary) private view returns (uint256) {
        if (block.timestamp < beneficiary.start) {
            return 0; // Vesting has not started
        } else {
            uint256 elapsedTime = block.timestamp - beneficiary.start;
            uint256 vestingAmount = (beneficiary.totalAmount * elapsedTime) / beneficiary.duration;

            return vestingAmount > beneficiary.totalAmount ? beneficiary.totalAmount - beneficiary.releasedAmount : vestingAmount - beneficiary.releasedAmount;
        }
    }

    /**
     * @dev Allows the owner to withdraw any tokens mistakenly sent to the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        
        require(token.transfer(owner(), amount), "Withdrawal transfer failed");
    }

    /**
     * @dev Check the vesting status for a specific beneficiary.
     * @param _beneficiary Address of the beneficiary.
     * @return totalAmount Total allocated tokens.
     * @return releasedAmount Amount already released.
     * @return availableAmount Amount available for release.
     */
    function vestingStatus(address _beneficiary) external view returns (uint256 totalAmount, uint256 releasedAmount, uint256 availableAmount) {
        Beneficiary storage beneficiary = beneficiaries[_beneficiary];

        totalAmount = beneficiary.totalAmount;
        releasedAmount = beneficiary.releasedAmount;
        availableAmount = _releasableAmount(beneficiary);
    }
}
```
