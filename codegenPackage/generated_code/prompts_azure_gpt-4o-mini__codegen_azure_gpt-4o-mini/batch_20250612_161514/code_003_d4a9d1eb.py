"""
Generated Code Metadata:
========================
Original URL: https://usual-portal.firebaseapp.com
Prompt: Create a smart contract that utilizes the USUAL token to manage treasury control and revenue distribution in a decentralized finance setting.
Generated: DETERMINISTIC_d4a9d1ebcaee5b4b
Batch ID: 20250612_161514
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

// Importing the ERC20 interface for the USUAL token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Treasury contract for managing treasury control and revenue distribution
contract Treasury is Ownable {
    // State variables
    IERC20 public usualToken; // USUAL token contract
    address[] public beneficiaries; // List of beneficiaries
    mapping(address => uint256) public shares; // Shares of each beneficiary
    uint256 public totalShares; // Total shares for distribution

    // Events
    event BeneficiaryAdded(address indexed beneficiary, uint256 shares);
    event BeneficiaryRemoved(address indexed beneficiary);
    event RevenueDistributed(uint256 amount);

    // Constructor to set the USUAL token address
    constructor(address _usualToken) {
        require(_usualToken != address(0), "Invalid token address");
        usualToken = IERC20(_usualToken);
    }

    // Function to add a beneficiary with shares
    function addBeneficiary(address _beneficiary, uint256 _shares) external onlyOwner {
        require(_beneficiary != address(0), "Invalid beneficiary address");
        require(_shares > 0, "Shares must be greater than zero");
        require(shares[_beneficiary] == 0, "Beneficiary already exists");

        beneficiaries.push(_beneficiary);
        shares[_beneficiary] = _shares;
        totalShares += _shares;

        emit BeneficiaryAdded(_beneficiary, _shares);
    }

    // Function to remove a beneficiary
    function removeBeneficiary(address _beneficiary) external onlyOwner {
        require(shares[_beneficiary] > 0, "Beneficiary does not exist");

        // Remove beneficiary from the list
        for (uint256 i = 0; i < beneficiaries.length; i++) {
            if (beneficiaries[i] == _beneficiary) {
                beneficiaries[i] = beneficiaries[beneficiaries.length - 1];
                beneficiaries.pop();
                break;
            }
        }

        totalShares -= shares[_beneficiary];
        delete shares[_beneficiary];

        emit BeneficiaryRemoved(_beneficiary);
    }

    // Function to distribute revenue to beneficiaries
    function distributeRevenue(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(usualToken.balanceOf(address(this)) >= _amount, "Insufficient balance");

        // Transfer the specified amount to the contract
        usualToken.transferFrom(msg.sender, address(this), _amount);

        // Distribute the revenue based on shares
        for (uint256 i = 0; i < beneficiaries.length; i++) {
            address beneficiary = beneficiaries[i];
            uint256 share = (shares[beneficiary] * _amount) / totalShares;
            if (share > 0) {
                usualToken.transfer(beneficiary, share);
            }
        }

        emit RevenueDistributed(_amount);
    }

    // Function to withdraw tokens from the treasury
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(usualToken.balanceOf(address(this)) >= _amount, "Insufficient balance");

        usualToken.transfer(msg.sender, _amount);
    }

    // Function to get the list of beneficiaries
    function getBeneficiaries() external view returns (address[] memory) {
        return beneficiaries;
    }

    // Function to get the shares of a beneficiary
    function getShares(address _beneficiary) external view returns (uint256) {
        return shares[_beneficiary];
    }
}
```
