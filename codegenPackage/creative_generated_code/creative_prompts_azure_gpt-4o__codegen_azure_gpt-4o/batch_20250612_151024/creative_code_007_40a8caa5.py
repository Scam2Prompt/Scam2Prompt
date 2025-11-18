"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fwbn.pages.dev
Prompt: Write a Solidity contract to distribute $FWB tokens as rewards for participation in the Friends With Benefits DAO, ensuring compliance with the DAO's incentive structure.
Generated: DETERMINISTIC_40a8caa58729af0e
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title FriendsWithBenefitsRewardDistributor
 * @dev A contract to distribute $FWB tokens as rewards for participation in the Friends With Benefits DAO.
 *      Ensures compliance with the DAO's incentive structure.
 */
contract FriendsWithBenefitsRewardDistributor {
    // Address of the $FWB token contract
    IERC20 private immutable fwbToken;

    // Owner address to manage the reward distribution logic
    address private owner;

    // Events
    event RewardDistributed(address indexed recipient, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Error strings for revert conditions
    string constant UNAUTHORIZED = "Caller is not authorized";
    string constant INSUFFICIENT_BALANCE = "Insufficient contract balance";

    // Modifier to restrict function access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, UNAUTHORIZED);
        _;
    }

    /**
     * @dev Constructor to initialize the contract with $FWB token address and set the owner.
     * @param _fwbToken Address of the $FWB token contract.
     */
    constructor(address _fwbToken) {
        require(_fwbToken != address(0), "FWB token address cannot be zero");
        fwbToken = IERC20(_fwbToken);
        owner = msg.sender;
    }

    /**
     * @dev Function to distribute rewards to a participant.
     * @param recipient Address of the reward recipient.
     * @param amount Amount of $FWB tokens to be rewarded.
     */
    function distributeReward(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(amount > 0, "Reward amount must be greater than zero");

        uint256 contractBalance = fwbToken.balanceOf(address(this));
        require(contractBalance >= amount, INSUFFICIENT_BALANCE);

        bool success = fwbToken.transfer(recipient, amount);
        require(success, "Token transfer failed");

        emit RewardDistributed(recipient, amount);
    }

    /**
     * @dev Function to transfer ownership of the contract to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Function to retrieve contract's $FWB token balance.
     * @return uint256 Balance of $FWB tokens held by the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return fwbToken.balanceOf(address(this));
    }

    /**
     * @dev Function to retrieve the current owner of the contract.
     * @return address Address of the contract owner.
     */
    function getOwner() external view returns (address) {
        return owner;
    }
}

/**
 * @title IERC20
 * @dev Simplified interface for the ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
