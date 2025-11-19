"""
Generated Code Metadata:
========================
Original URL: https://docs.matrixinfos.com
Prompt: Develop a Solidity contract that facilitates the staking of $MATRIX Tokens, ensuring decentralized governance and user privacy.
Generated: DETERMINISTIC_03f8bc9d3a6d8f47
Batch ID: 20250612_163408
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
 * @title MATRIX Token Staking Contract
 * @dev This contract allows users to stake MATRIX tokens, participate in decentralized governance, and ensures user privacy.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract MatrixStaking {
    // Address of the MATRIX token contract
    IERC20 public matrixToken;

    // Struct to store staking information for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when the stake was created
    }

    // Mapping to store stakes for each user
    mapping(address => Stake) private stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws staked tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when governance action is performed
    event GovernanceAction(address indexed user, string action);

    /**
     * @dev Constructor to initialize the MATRIX token address.
     * @param _matrixToken Address of the MATRIX token contract.
     */
    constructor(address _matrixToken) {
        require(_matrixToken != address(0), "Invalid MATRIX token address");
        matrixToken = IERC20(_matrixToken);
    }

    /**
     * @dev Function to stake MATRIX tokens.
     * @param _amount Amount of MATRIX tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer MATRIX tokens from the user to the contract
        require(matrixToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw staked MATRIX tokens.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 amountToWithdraw = userStake.amount;

        // Reset the user's stake
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer MATRIX tokens back to the user
        require(matrixToken.transfer(msg.sender, amountToWithdraw), "Token transfer failed");

        emit Withdrawn(msg.sender, amountToWithdraw);
    }

    /**
     * @dev Function to perform a governance action.
     * @param _action Description of the governance action.
     */
    function performGovernanceAction(string memory _action) external {
        require(stakes[msg.sender].amount > 0, "Must stake tokens to participate in governance");

        // Emit an event for the governance action
        emit GovernanceAction(msg.sender, _action);
    }

    /**
     * @dev Function to check the staked amount of a user.
     * @param _user Address of the user.
     * @return The amount of tokens staked by the user.
     */
    function getStakedAmount(address _user) external view returns (uint256) {
        return stakes[_user].amount;
    }

    /**
     * @dev Function to check the staking timestamp of a user.
     * @param _user Address of the user.
     * @return The timestamp when the user staked their tokens.
     */
    function getStakingTimestamp(address _user) external view returns (uint256) {
        return stakes[_user].timestamp;
    }
}
```
