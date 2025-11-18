"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe20-vip.web.app
Prompt: Write a Solidity script to implement a "Dev Fee" mechanism for a token contract, similar to the PEPE 2.0 token.
Generated: DETERMINISTIC_f7aece8679c4245d
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
 * @title DevFeeToken
 * @notice A simple ERC20 Token with a "Dev Fee" mechanism implemented for transfers.
 */
contract DevFeeToken {
    // State variables
    string public name = "DevFeeToken";
    string public symbol = "DFT";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000 * (10 ** uint256(decimals)); // 1 million tokens

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    uint256 public devFeePercent = 2; // Fee percentage (2%)
    address public devWallet; // Wallet where fees are sent

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Modifier to ensure non-zero addresses
    modifier validAddress(address _address) {
        require(_address != address(0), "Invalid address");
        _;
    }

    /**
     * @dev Constructor to initialize the token contract.
     * @param _devWallet Address of the developer wallet where fees will be sent.
     */
    constructor(address _devWallet) validAddress(_devWallet) {
        devWallet = _devWallet;
        balances[msg.sender] = totalSupply; // Assign all tokens to the deployer
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Transfers tokens from sender to recipient, deducting the dev fee.
     * @param _to Recipient address.
     * @param _amount Amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transfer(address _to, uint256 _amount) public validAddress(_to) returns (bool) {
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Calculate the dev fee
        uint256 fee = (_amount * devFeePercent) / 100;
        uint256 transferAmount = _amount - fee;

        // Perform the transfer
        balances[msg.sender] -= _amount;
        balances[_to] += transferAmount;
        balances[devWallet] += fee;

        emit Transfer(msg.sender, _to, transferAmount);
        emit Transfer(msg.sender, devWallet, fee);

        return true;
    }

    /**
     * @dev Allows the spender to transfer tokens from the owner's account.
     * @param _spender Address of the spender.
     * @param _amount Amount of tokens to approve.
     * @return True if the approval is successful.
     */
    function approve(address _spender, uint256 _amount) public validAddress(_spender) returns (bool) {
        allowances[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one account to another, deducting the dev fee.
     * @param _from Sender address.
     * @param _to Recipient address.
     * @param _amount Amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transferFrom(address _from, address _to, uint256 _amount) public validAddress(_to) returns (bool) {
        require(allowances[_from][msg.sender] >= _amount, "Allowance exceeded");
        require(balances[_from] >= _amount, "Insufficient balance");

        // Calculate the dev fee
        uint256 fee = (_amount * devFeePercent) / 100;
        uint256 transferAmount = _amount - fee;

        // Perform the transfer
        balances[_from] -= _amount;
        allowances[_from][msg.sender] -= _amount;
        balances[_to] += transferAmount;
        balances[devWallet] += fee;

        emit Transfer(_from, _to, transferAmount);
        emit Transfer(_from, devWallet, fee);

        return true;
    }

    /**
     * @dev Returns the token balance of a specific account.
     * @param _account Address of the account to query.
     * @return Token balance of the account.
     */
    function balanceOf(address _account) public view validAddress(_account) returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Returns the allowance for a spender on an owner's account.
     * @param _owner Address of the token owner.
     * @param _spender Address of the spender.
     * @return Remaining allowance for the spender.
     */
    function allowance(address _owner, address _spender) public view validAddress(_spender) returns (uint256) {
        return allowances[_owner][_spender];
    }

    /**
     * @dev Updates the developer wallet address.
     * @param _newDevWallet Address of the new developer wallet.
     */
    function setDevWallet(address _newDevWallet) external validAddress(_newDevWallet) {
        require(msg.sender == devWallet, "Only devWallet can update");
        devWallet = _newDevWallet;
    }

    /**
     * @dev Updates the dev fee percentage.
     * @param _newDevFeePercent New fee percentage.
     */
    function setDevFeePercent(uint256 _newDevFeePercent) external {
        require(msg.sender == devWallet, "Only devWallet can update");
        require(_newDevFeePercent <= 10, "Fee too high"); // Prevent excessive fees
        devFeePercent = _newDevFeePercent;
    }
}
```
