"""
Generated Code Metadata:
========================
Original URL: https://monprotocol-4yq.pages.dev
Prompt: Create a simple smart contract in Solidity that could be used to manage the claiming and distribution of MON tokens post-TGE, based on the presale terms provided.
Generated: DETERMINISTIC_dcdf00a536016831
Batch ID: 20250622_205751
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MONTokenDistribution
 * @author [Your Name]
 * @notice A simple smart contract for managing the claiming and distribution of MON tokens post-TGE.
 */
contract MONTokenDistribution is ReentrancyGuard, Ownable {
    // Mapping of claim status for each user
    mapping(address => bool) public claimed;

    // Mapping of user claim amounts
    mapping(address => uint256) public claimAmounts;

    // MON token contract
    ERC20 public monToken;

    // Total MON tokens available for distribution
    uint256 public totalTokensAvailable;

    // Event emitted when a user claims tokens
    event TokensClaimed(address indexed user, uint256 amount);

    /**
     * @notice Initializes the contract.
     * @param _monTokenAddress Address of the MON token contract.
     * @param _totalTokensAvailable Total MON tokens available for distribution.
     */
    constructor(address _monTokenAddress, uint256 _totalTokensAvailable) {
        require(_monTokenAddress != address(0), "MON token address cannot be zero");
        require(_totalTokensAvailable > 0, "Total tokens available must be greater than zero");

        monToken = ERC20(_monTokenAddress);
        totalTokensAvailable = _totalTokensAvailable;
    }

    /**
     * @notice Sets the claim amount for a user.
     * @param _user Address of the user.
     * @param _amount Claim amount for the user.
     */
    function setClaimAmount(address _user, uint256 _amount) public onlyOwner {
        require(_user != address(0), "User address cannot be zero");
        require(_amount > 0, "Claim amount must be greater than zero");
        require(claimAmounts[_user] == 0, "Claim amount already set for user");

        claimAmounts[_user] = _amount;
    }

    /**
     * @notice Claims MON tokens for a user.
     */
    function claimTokens() public nonReentrant {
        require(claimed[msg.sender] == false, "Tokens already claimed by user");
        require(claimAmounts[msg.sender] > 0, "No claim amount set for user");

        uint256 claimAmount = claimAmounts[msg.sender];
        require(monToken.balanceOf(address(this)) >= claimAmount, "Insufficient tokens in contract");

        claimed[msg.sender] = true;
        claimAmounts[msg.sender] = 0;

        // Transfer tokens to user
        bool sent = monToken.transfer(msg.sender, claimAmount);
        require(sent, "Failed to transfer tokens");

        emit TokensClaimed(msg.sender, claimAmount);
    }

    /**
     * @notice Withdraws excess tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) public onlyOwner {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(monToken.balanceOf(address(this)) >= _amount, "Insufficient tokens in contract");

        // Transfer tokens to owner
        bool sent = monToken.transfer(msg.sender, _amount);
        require(sent, "Failed to transfer tokens");
    }

    /**
     * @notice Updates the total tokens available for distribution.
     * @param _newTotalTokensAvailable New total tokens available.
     */
    function updateTotalTokensAvailable(uint256 _newTotalTokensAvailable) public onlyOwner {
        require(_newTotalTokensAvailable >= 0, "New total tokens available must be non-negative");

        totalTokensAvailable = _newTotalTokensAvailable;
    }
}
```
