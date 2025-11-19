"""
Generated Code Metadata:
========================
Original URL: https://moonbag-org.pages.dev
Prompt: Design a smart contract in Solidity that handles token locking and vesting for a team, similar to MoonBag's tokenomics.
Generated: DETERMINISTIC_234b307743876d9b
Batch ID: 20250622_211330
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenVesting
 * @dev A smart contract for token locking and vesting for a team.
 */
contract TokenVesting is Ownable {
    // Struct to hold vesting information for each beneficiary
    struct Beneficiary {
        uint256 totalAmount; // Total amount of tokens allocated
        uint256 releasedAmount; // Amount of tokens already released
        uint256 start; // Start time of the vesting period
        uint256 duration; // Duration of the vesting period
        bool revoked; // Indicates if the vesting has been revoked
    }

    // Mapping of beneficiaries to their vesting information
    mapping(address => Beneficiary) public beneficiaries;

    // The token being vested
    IERC20 public token;

    // Event emitted when tokens are released
    event TokensReleased(address indexed beneficiary, uint256 amount);

    // Event emitted when vesting is revoked
    event VestingRevoked(address indexed beneficiary);

    /**
     * @dev Constructor to initialize the contract with the token address.
     * @param _token The address of the ERC20 token to be vested.
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Adds a new beneficiary with vesting details.
     * @param _beneficiary The address of the beneficiary.
     * @param _totalAmount The total amount of tokens allocated to the beneficiary.
     * @param _start The start time of the vesting period.
     * @param _duration The duration of the vesting period in seconds.
     */
    function addBeneficiary(
        address _beneficiary,
        uint256 _totalAmount,
        uint256 _start,
        uint256 _duration
    ) external onlyOwner {
        require(_beneficiary != address(0), "Beneficiary cannot be the zero address");
        require(beneficiaries[_beneficiary].totalAmount == 0, "Beneficiary already exists");
        require(_totalAmount > 0, "Total amount must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        beneficiaries[_beneficiary] = Beneficiary({
            totalAmount: _totalAmount,
            releasedAmount: 0,
            start: _start,
            duration: _duration,
            revoked: false
        });
    }

    /**
     * @dev Releases vested tokens to the beneficiary.
     */
    function release() external {
        Beneficiary storage beneficiary = beneficiaries[msg.sender];
        require(beneficiary.totalAmount > 0, "No tokens to release");
        require(!beneficiary.revoked, "Vesting revoked");

        uint256 unreleased = _releasableAmount(beneficiary);
        require(unreleased > 0, "No tokens are due");

        beneficiary.releasedAmount += unreleased;
        token.transfer(msg.sender, unreleased);

        emit TokensReleased(msg.sender, unreleased);
    }

    /**
     * @dev Revokes vesting for a beneficiary.
     * @param _beneficiary The address of the beneficiary.
     */
    function revoke(address _beneficiary) external onlyOwner {
        Beneficiary storage beneficiary = beneficiaries[_beneficiary];
        require(beneficiary.totalAmount > 0, "No vesting to revoke");
        require(!beneficiary.revoked, "Vesting already revoked");

        beneficiary.revoked = true;

        emit VestingRevoked(_beneficiary);
    }

    /**
     * @dev Calculates the amount of tokens that can be released.
     * @param beneficiary The beneficiary's vesting information.
     * @return The amount of tokens that can be released.
     */
    function _releasableAmount(Beneficiary memory beneficiary) private view returns (uint256) {
        if (block.timestamp < beneficiary.start) {
            return 0;
        } else if (block.timestamp >= beneficiary.start + beneficiary.duration) {
            return beneficiary.totalAmount - beneficiary.releasedAmount;
        } else {
            uint256 vestedAmount = (beneficiary.totalAmount * (block.timestamp - beneficiary.start)) / beneficiary.duration;
            return vestedAmount - beneficiary.releasedAmount;
        }
    }

    /**
     * @dev Allows the owner to withdraw any tokens sent to the contract by mistake.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= _amount, "Insufficient balance");

        token.transfer(owner(), _amount);
    }
}
```
