"""
Generated Code Metadata:
========================
Original URL: https://claim-simoncat.pages.dev
Prompt: Generate a smart contract code snippet in Solidity for a token airdrop similar to the one described for $FLOKI holders and Simon's Cat Token.
Generated: DETERMINISTIC_4af00aaebad56bd0
Batch ID: 20250622_205404
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TokenAirdrop
 * @author [Your Name]
 * @notice A simple token airdrop contract for distributing tokens to eligible holders.
 */
contract TokenAirdrop is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of eligible token holders and their claim status
    mapping(address => bool) public claimed;

    // Mapping of eligible token holders and their airdrop amounts
    mapping(address => uint256) public airdropAmounts;

    // The token being airdropped
    ERC20 public token;

    // The token required for eligibility (e.g. $FLOKI)
    ERC20 public requiredToken;

    // The total airdrop amount
    uint256 public totalAirdropAmount;

    // Event emitted when a user claims their airdrop
    event Claimed(address indexed user, uint256 amount);

    /**
     * @notice Initializes the contract.
     * @param _token The token being airdropped.
     * @param _requiredToken The token required for eligibility.
     * @param _totalAirdropAmount The total airdrop amount.
     */
    constructor(ERC20 _token, ERC20 _requiredToken, uint256 _totalAirdropAmount) public {
        token = _token;
        requiredToken = _requiredToken;
        totalAirdropAmount = _totalAirdropAmount;
    }

    /**
     * @notice Sets the airdrop amount for an eligible token holder.
     * @param _user The eligible token holder.
     * @param _amount The airdrop amount.
     */
    function setAirdropAmount(address _user, uint256 _amount) public onlyOwner {
        require(_amount > 0, "Airdrop amount must be greater than 0");
        airdropAmounts[_user] = _amount;
    }

    /**
     * @notice Claims the airdrop for an eligible token holder.
     */
    function claim() public nonReentrant {
        require(airdropAmounts[msg.sender] > 0, "No airdrop amount set");
        require(!claimed[msg.sender], "Already claimed");

        uint256 amount = airdropAmounts[msg.sender];
        claimed[msg.sender] = true;

        // Transfer the airdrop amount to the user
        require(token.transfer(msg.sender, amount), "Transfer failed");

        emit Claimed(msg.sender, amount);
    }

    /**
     * @notice Checks if a user is eligible for the airdrop based on their required token balance.
     * @param _user The user to check.
     * @return bool Whether the user is eligible.
     */
    function isEligible(address _user) public view returns (bool) {
        uint256 balance = requiredToken.balanceOf(_user);
        return balance > 0;
    }

    /**
     * @notice Distributes the airdrop to eligible token holders.
     * @param _users The eligible token holders.
     * @param _amounts The airdrop amounts.
     */
    function distributeAirdrop(address[] memory _users, uint256[] memory _amounts) public onlyOwner {
        require(_users.length == _amounts.length, "User and amount arrays must be the same length");

        for (uint256 i = 0; i < _users.length; i++) {
            address user = _users[i];
            uint256 amount = _amounts[i];

            // Check if user is eligible
            require(isEligible(user), "User is not eligible");

            // Set airdrop amount
            airdropAmounts[user] = amount;

            // Update total airdrop amount
            totalAirdropAmount = totalAirdropAmount.add(amount);
        }
    }

    // Modifier to restrict function access to the contract owner
    modifier onlyOwner {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    // Get the contract owner
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
