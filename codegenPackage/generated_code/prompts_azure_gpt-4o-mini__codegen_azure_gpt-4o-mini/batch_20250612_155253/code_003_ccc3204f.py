"""
Generated Code Metadata:
========================
Original URL: https://poc-dao.zetachain.io
Prompt: Generate a smart contract for a POC-DAO that channels slashed stakes to charitable causes.
Generated: DETERMINISTIC_ccc3204f2b954be4
Batch ID: 20250612_155253
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title POCDAO
 * @dev A smart contract for a Proof of Contribution Decentralized Autonomous Organization (POC-DAO)
 * that channels slashed stakes to charitable causes.
 */
contract POCDAO is Ownable {
    // Event emitted when a stake is slashed
    event StakeSlashed(address indexed user, uint256 amount, address charity);

    // Mapping to track user stakes
    mapping(address => uint256) public stakes;

    // Charity address to receive slashed stakes
    address public charityAddress;

    // ERC20 token used for staking
    IERC20 public stakingToken;

    /**
     * @dev Constructor to initialize the contract with the staking token and charity address.
     * @param _stakingToken The address of the ERC20 token used for staking.
     * @param _charityAddress The address of the charity to receive slashed stakes.
     */
    constructor(IERC20 _stakingToken, address _charityAddress) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        require(_charityAddress != address(0), "Invalid charity address");
        
        stakingToken = _stakingToken;
        charityAddress = _charityAddress;
    }

    /**
     * @dev Allows users to stake tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        
        // Transfer tokens from user to this contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user's stake
        stakes[msg.sender] += amount;
    }

    /**
     * @dev Allows the owner to slash a user's stake and send it to charity.
     * @param user The address of the user whose stake is to be slashed.
     * @param amount The amount to be slashed.
     */
    function slashStake(address user, uint256 amount) external onlyOwner {
        require(stakes[user] >= amount, "Insufficient stake to slash");
        
        // Reduce the user's stake
        stakes[user] -= amount;

        // Transfer the slashed amount to the charity
        stakingToken.transfer(charityAddress, amount);
        
        // Emit the StakeSlashed event
        emit StakeSlashed(user, amount, charityAddress);
    }

    /**
     * @dev Allows the owner to update the charity address.
     * @param newCharityAddress The new charity address.
     */
    function updateCharityAddress(address newCharityAddress) external onlyOwner {
        require(newCharityAddress != address(0), "Invalid charity address");
        charityAddress = newCharityAddress;
    }

    /**
     * @dev Allows users to withdraw their stakes.
     */
    function withdrawStake() external {
        uint256 userStake = stakes[msg.sender];
        require(userStake > 0, "No stake to withdraw");
        
        // Reset user's stake before transferring to prevent re-entrancy
        stakes[msg.sender] = 0;

        // Transfer the user's stake back to them
        stakingToken.transfer(msg.sender, userStake);
    }
}
```
