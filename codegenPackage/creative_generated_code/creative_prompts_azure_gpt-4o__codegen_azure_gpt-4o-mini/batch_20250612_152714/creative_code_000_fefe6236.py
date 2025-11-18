"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vestings-scapesmania.pages.dev
Prompt: Write a smart contract in Solidity for a token vesting system tailored for ScapesMania's $MANIA token, ensuring compatibility with the project's Web3 gaming ecosystem.
Generated: DETERMINISTIC_fefe6236912ee6bb
Batch ID: 20250612_152714
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
 * @title ScapesMania Token Vesting Contract
 * @dev This contract allows for the vesting of $MANIA tokens in a structured manner.
 */
contract ManiaTokenVesting {
    // State variables
    address public tokenAddress; // Address of the $MANIA token
    address public beneficiary;   // Address of the beneficiary receiving the tokens
    uint256 public start;         // Start time of the vesting period
    uint256 public cliff;         // Cliff duration in seconds
    uint256 public duration;      // Total duration of the vesting period in seconds
    uint256 public released;      // Amount of tokens released so far

    // Event to log token releases
    event TokensReleased(uint256 amount);

    // Modifier to check if the caller is the beneficiary
    modifier onlyBeneficiary() {
        require(msg.sender == beneficiary, "Caller is not the beneficiary");
        _;
    }

    /**
     * @dev Constructor to initialize the contract
     * @param _tokenAddress The address of the $MANIA token
     * @param _beneficiary The address of the beneficiary
     * @param _start The start timestamp of the vesting period
     * @param _cliff The duration of the cliff in seconds
     * @param _duration The total duration of the vesting period in seconds
     */
    constructor(
        address _tokenAddress,
        address _beneficiary,
        uint256 _start,
        uint256 _cliff,
        uint256 _duration
    ) {
        require(_beneficiary != address(0), "Beneficiary cannot be zero address");
        require(_duration > 0, "Duration must be greater than 0");
        require(_cliff <= _duration, "Cliff must not be longer than duration");

        tokenAddress = _tokenAddress;
        beneficiary = _beneficiary;
        start = _start;
        cliff = _start + _cliff;
        duration = _duration;
    }

    /**
     * @dev Returns the amount of tokens that can be released
     * @return The amount of releasable tokens
     */
    function releasableAmount() public view returns (uint256) {
        uint256 vestedAmount = vestedAmount(block.timestamp);
        return vestedAmount - released;
    }

    /**
     * @dev Returns the amount of tokens that have been vested
     * @param _timestamp The timestamp to check vesting amount
     * @return The amount of vested tokens
     */
    function vestedAmount(uint256 _timestamp) public view returns (uint256) {
        if (_timestamp < cliff) {
            return 0;
        } else if (_timestamp >= start + duration) {
            return IERC20(tokenAddress).balanceOf(address(this));
        } else {
            return (IERC20(tokenAddress).balanceOf(address(this)) * (_timestamp - start)) / duration;
        }
    }

    /**
     * @dev Releases the releasable tokens to the beneficiary
     */
    function release() public onlyBeneficiary {
        uint256 amount = releasableAmount();
        require(amount > 0, "No tokens are due for release");

        released += amount;
        IERC20(tokenAddress).transfer(beneficiary, amount);
        
        emit TokensReleased(amount);
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
