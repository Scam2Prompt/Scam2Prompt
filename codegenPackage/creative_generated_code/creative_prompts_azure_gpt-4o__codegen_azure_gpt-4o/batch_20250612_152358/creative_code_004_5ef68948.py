"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiaww6ymqhro76hrjq6l5h4ninbd2hn7ysd6vsyffswhvg5btz4vb4.ipfs.dweb.link
Prompt: Write a smart contract in Solidity that supports EigenLayer's "Restake" feature and adheres to its staking requirements.
Generated: DETERMINISTIC_5ef6894848479993
Batch ID: 20250612_152358
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
 * @title EigenLayerRestakeContract
 * @dev A smart contract for supporting EigenLayer's "Restake" feature.
 *      This contract adheres to the staking requirements defined by EigenLayer.
 */
contract EigenLayerRestakeContract {
    // State variables
    mapping(address => uint256) private stakedBalances; // Tracks the staked balance of each user
    mapping(address => bool) private isRestaked;        // Tracks whether a user has restaked their funds

    address public immutable admin;                     // Admin of the contract
    uint256 public immutable minimumStakeAmount;        // Minimum stake amount required to restake

    event Staked(address indexed staker, uint256 amount);       // Event emitted when staking occurs
    event Restaked(address indexed staker, uint256 amount);     // Event emitted when restaking occurs
    event Unstaked(address indexed staker, uint256 amount);     // Event emitted when unstaking occurs

    /**
     * @dev Constructor to initialize the contract.
     * @param _minimumStakeAmount Minimum amount required for staking.
     */
    constructor(uint256 _minimumStakeAmount) {
        require(_minimumStakeAmount > 0, "Minimum stake amount must be greater than zero");
        admin = msg.sender;
        minimumStakeAmount = _minimumStakeAmount;
    }

    /**
     * @dev Modifier to restrict access to admin-only functions.
     */
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call this function");
        _;
    }

    /**
     * @dev Allows a user to stake funds.
     * @notice The amount staked must be greater than or equal to the minimum stake amount.
     */
    function stake() external payable {
        require(msg.value >= minimumStakeAmount, "Stake amount must meet the minimum requirement");

        stakedBalances[msg.sender] += msg.value;

        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Allows a user to restake their funds.
     * @notice The user must have an existing stake and cannot restake twice.
     */
    function restake() external {
        uint256 userBalance = stakedBalances[msg.sender];
        require(userBalance > 0, "No staked balance available to restake");
        require(!isRestaked[msg.sender], "Already restaked");

        isRestaked[msg.sender] = true;

        emit Restaked(msg.sender, userBalance);
    }

    /**
     * @dev Allows a user to unstake their funds.
     * @notice The user must have staked funds to unstake.
     */
    function unstake() external {
        uint256 userBalance = stakedBalances[msg.sender];
        require(userBalance > 0, "No staked balance available to unstake");

        stakedBalances[msg.sender] = 0;
        isRestaked[msg.sender] = false;

        // Transfer the staked funds back to the user
        (bool success, ) = msg.sender.call{value: userBalance}("");
        require(success, "Transfer failed");

        emit Unstaked(msg.sender, userBalance);
    }

    /**
     * @dev Allows the admin to withdraw contract funds.
     * @notice This is restricted to admin only.
     */
    function withdrawContractFunds(uint256 amount) external onlyAdmin {
        require(address(this).balance >= amount, "Insufficient contract balance");

        (bool success, ) = admin.call{value: amount}("");
        require(success, "Admin withdrawal failed");
    }

    /**
     * @dev Retrieves the staked balance of a user.
     * @param user Address of the user to query.
     * @return The staked balance of the user.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    /**
     * @dev Checks whether a user has restaked their funds.
     * @param user Address of the user to query.
     * @return True if the user has restaked, false otherwise.
     */
    function hasRestaked(address user) external view returns (bool) {
        return isRestaked[user];
    }

    /**
     * @dev Fallback function to accept ether.
     */
    receive() external payable {
        // Allow direct deposits to the contract
    }
}
```
