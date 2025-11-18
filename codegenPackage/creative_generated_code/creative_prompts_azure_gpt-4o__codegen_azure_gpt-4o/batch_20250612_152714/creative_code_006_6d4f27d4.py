"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simonscat-token.com
Prompt: Develop a smart contract feature that automatically donates a portion of $CAT trades to feed hungry cats, as described in Simon's Cat Token’s mission.
Generated: DETERMINISTIC_6d4f27d4ae574355
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
 * @title SimonsCatToken
 * @dev A token contract with an automated donation feature to support feeding hungry cats.
 *      A percentage of each transfer is allocated to a donation address.
 */
contract SimonsCatToken {
    string public name = "Simons Cat Token";
    string public symbol = "CAT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Address where donations are sent
    address public donationAddress;

    // Percentage of each transfer that is donated (e.g., 5% = 500, where 10000 represents 100%)
    uint256 public donationPercentage = 500;

    // Mapping for balances
    mapping(address => uint256) public balanceOf;

    // Mapping for allowances
    mapping(address => mapping(address => uint256)) public allowance;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Donation(address indexed from, uint256 value);

    /**
     * @dev Constructor to initialize the contract with initial supply and donation address.
     * @param _initialSupply Initial supply of the token.
     * @param _donationAddress Address where donations will be sent.
     */
    constructor(uint256 _initialSupply, address _donationAddress) {
        require(_donationAddress != address(0), "Donation address cannot be zero address");
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[msg.sender] = totalSupply;
        donationAddress = _donationAddress;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Internal function to handle token transfers with donation logic.
     * @param _from Address sending the tokens.
     * @param _to Address receiving the tokens.
     * @param _value Amount of tokens to transfer.
     */
    function _transfer(
        address _from,
        address _to,
        uint256 _value
    ) internal {
        require(_from != address(0), "Transfer from zero address");
        require(_to != address(0), "Transfer to zero address");
        require(balanceOf[_from] >= _value, "Insufficient balance");

        uint256 donationAmount = (_value * donationPercentage) / 10000;
        uint256 transferAmount = _value - donationAmount;

        // Update balances
        balanceOf[_from] -= _value;
        balanceOf[_to] += transferAmount;
        balanceOf[donationAddress] += donationAmount;

        // Emit transfer events
        emit Transfer(_from, _to, transferAmount);
        emit Donation(_from, donationAmount);
    }

    /**
     * @dev Public function to transfer tokens.
     * @param _to Address receiving the tokens.
     * @param _value Amount of tokens to transfer.
     * @return Success status of the transfer.
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        _transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Public function to approve a spender to spend tokens on behalf of the sender.
     * @param _spender Address of the spender.
     * @param _value Amount of tokens to approve.
     * @return Success status of the approval.
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Public function to transfer tokens on behalf of another address.
     * @param _from Address sending the tokens.
     * @param _to Address receiving the tokens.
     * @param _value Amount of tokens to transfer.
     * @return Success status of the transfer.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) public returns (bool) {
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");
        allowance[_from][msg.sender] -= _value;
        _transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Function to update the donation address. Only the contract owner can call this.
     * @param _newDonationAddress New donation address.
     */
    function updateDonationAddress(address _newDonationAddress) public {
        require(msg.sender == donationAddress, "Only current donation address can update");
        require(_newDonationAddress != address(0), "Donation address cannot be zero address");
        donationAddress = _newDonationAddress;
    }

    /**
     * @dev Function to update the donation percentage. Only the contract owner can call this.
     * @param _newDonationPercentage New donation percentage (e.g., 5% = 500, where 10000 represents 100%).
     */
    function updateDonationPercentage(uint256 _newDonationPercentage) public {
        require(msg.sender == donationAddress, "Only current donation address can update");
        require(_newDonationPercentage <= 10000, "Donation percentage cannot exceed 100%");
        donationPercentage = _newDonationPercentage;
    }
}
```
