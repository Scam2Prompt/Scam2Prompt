"""
Generated Code Metadata:
========================
Original URL: https://usual-portal.web.app
Prompt: Write a Solidity code to implement a 4-year cash flow scarcity advantage for a token, similar to Usual's mechanism.
Generated: DETERMINISTIC_951a1c335e597d77
Batch ID: 20250622_212323
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

/**
 * @title ScarcityToken
 * @dev Implements a 4-year cash flow scarcity advantage mechanism for a token.
 */
contract ScarcityToken {
    // Token details
    string public name = "ScarcityToken";
    string public symbol = "SCT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) public balanceOf;

    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) public allowance;

    // Scarcity mechanism variables
    uint256 public immutable startTime;
    uint256 public immutable scarcityDuration = 4 * 365 days; // 4 years
    uint256 public immutable scarcityFactor = 2; // Reduction factor (e.g., 50% reduction)

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than zero");
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[msg.sender] = totalSupply; // Assign all tokens to the deployer
        startTime = block.timestamp; // Record the start time
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Internal function to apply scarcity mechanism.
     * Reduces the token amount based on the elapsed time since the start.
     * @param _amount The original token amount.
     * @return The adjusted token amount after applying scarcity.
     */
    function _applyScarcity(uint256 _amount) internal view returns (uint256) {
        if (block.timestamp > startTime + scarcityDuration) {
            // Scarcity period has ended, no adjustment needed
            return _amount;
        }

        // Calculate the reduction factor based on elapsed time
        uint256 elapsedTime = block.timestamp - startTime;
        uint256 reduction = (scarcityFactor * elapsedTime) / scarcityDuration;

        // Apply reduction to the amount
        return _amount - ((_amount * reduction) / 100);
    }

    /**
     * @dev Transfer tokens from the sender to a recipient.
     * Applies the scarcity mechanism to the transferred amount.
     * @param _to The recipient address.
     * @param _value The amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        // Apply scarcity mechanism
        uint256 adjustedValue = _applyScarcity(_value);

        // Perform the transfer
        balanceOf[msg.sender] -= adjustedValue;
        balanceOf[_to] += adjustedValue;

        emit Transfer(msg.sender, _to, adjustedValue);
        return true;
    }

    /**
     * @dev Approve a spender to transfer tokens on behalf of the sender.
     * @param _spender The address of the spender.
     * @param _value The amount of tokens to approve.
     * @return True if the approval is successful.
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        require(_spender != address(0), "Cannot approve the zero address");

        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * Applies the scarcity mechanism to the transferred amount.
     * @param _from The address to transfer tokens from.
     * @param _to The recipient address.
     * @param _value The amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) public returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        // Apply scarcity mechanism
        uint256 adjustedValue = _applyScarcity(_value);

        // Perform the transfer
        balanceOf[_from] -= adjustedValue;
        balanceOf[_to] += adjustedValue;
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, adjustedValue);
        return true;
    }
}
```
