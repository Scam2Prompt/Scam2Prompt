"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://officialcocoro.xyz
Prompt: Create a smart contract in Solidity for an IP token like Cocoro Token that includes functionality for automatic charitable donations based on transaction volume.
Generated: DETERMINISTIC_fb1a7c3a5642cd16
Batch ID: 20250612_154752
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
 * @title Cocoro Token
 * @dev ERC-20 token with automatic charitable donation functionality
 */
contract CocoroToken {
    // Token details
    string public constant name = "Cocoro Token";
    string public constant symbol = "COCO";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Address of the charity fund
    address public charityAddress;

    // Percentage of transaction volume to donate (e.g., 2% donation rate)
    uint8 public donationRate;

    // Mapping of balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Events for transfer and approval
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Modifier to ensure valid addresses
    modifier validAddress(address _address) {
        require(_address != address(0), "Address cannot be the zero address");
        _;
    }

    /**
     * @dev Constructor to initialize the token
     * @param _initialSupply Initial supply of tokens
     * @param _charityAddress Address of the charity fund
     * @param _donationRate Donation percentage rate (e.g., 2 for 2%)
     */
    constructor(uint256 _initialSupply, address _charityAddress, uint8 _donationRate) validAddress(_charityAddress) {
        require(_donationRate <= 100, "Donation rate must be between 0 and 100");
        
        charityAddress = _charityAddress;
        donationRate = _donationRate;
        totalSupply = _initialSupply;
        balances[msg.sender] = _initialSupply;
        
        emit Transfer(address(0), msg.sender, _initialSupply);
    }

    /**
     * @dev Returns the balance of an account
     * @param _account Address of the account
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Transfers tokens to a recipient
     * @param _recipient Address of the recipient
     * @param _amount Amount of tokens to transfer
     */
    function transfer(address _recipient, uint256 _amount) external validAddress(_recipient) returns (bool) {
        _transfer(msg.sender, _recipient, _amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the sender
     * @param _spender Address of the spender
     * @param _amount Amount of tokens to approve
     */
    function approve(address _spender, uint256 _amount) external validAddress(_spender) returns (bool) {
        allowances[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one account to another using allowance
     * @param _sender Address of the sender
     * @param _recipient Address of the recipient
     * @param _amount Amount of tokens to transfer
     */
    function transferFrom(address _sender, address _recipient, uint256 _amount) external validAddress(_recipient) returns (bool) {
        require(allowances[_sender][msg.sender] >= _amount, "Transfer amount exceeds allowance");

        allowances[_sender][msg.sender] -= _amount;
        _transfer(_sender, _recipient, _amount);
        return true;
    }

    /**
     * @dev Internal function to handle token transfers and donation logic
     * @param _sender Address of the sender
     * @param _recipient Address of the recipient
     * @param _amount Amount of tokens to transfer
     */
    function _transfer(address _sender, address _recipient, uint256 _amount) internal {
        require(balances[_sender] >= _amount, "Insufficient balance");

        // Calculate donation amount
        uint256 donationAmount = (_amount * donationRate) / 100;
        uint256 transferAmount = _amount - donationAmount;

        // Adjust balances
        balances[_sender] -= _amount;
        balances[_recipient] += transferAmount;
        balances[charityAddress] += donationAmount;

        emit Transfer(_sender, _recipient, transferAmount);
        emit Transfer(_sender, charityAddress, donationAmount);
    }

    /**
     * @dev Returns the allowance for a spender given an owner
     * @param _owner Address of the token owner
     * @param _spender Address of the spender
     */
    function allowance(address _owner, address _spender) external view returns (uint256) {
        return allowances[_owner][_spender];
    }

    /**
     * @dev Updates the charity address
     * @param _newCharityAddress Address of the new charity fund
     */
    function updateCharityAddress(address _newCharityAddress) external validAddress(_newCharityAddress) {
        require(msg.sender == charityAddress, "Only the current charity address can update");
        charityAddress = _newCharityAddress;
    }
}
```
