"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.news
Prompt: Write a smart contract using the Moxie Protocol to programmatically reward Farcaster members for specific on-chain actions, ensuring payouts are split according to the protocol's predefined percentages.
Generated: DETERMINISTIC_6454ef7bc6c6cf7a
Batch ID: 20250612_150715
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
 * @title FarcasterRewards
 * @dev A smart contract to reward Farcaster members based on the Moxie Protocol for specific on-chain actions.
 *      Payouts are split according to the protocol's predefined percentages.
 */
contract FarcasterRewards {
    // Struct to define an action and its reward percentage split
    struct Action {
        string name; // Name of the action
        uint256 totalReward; // Total reward for the action in Wei
        mapping(address => uint256) percentages; // Address to percentage mapping for reward distribution
        address[] recipients; // Array of recipients for reward distribution
    }

    // Mapping to store the predefined actions and their respective reward splits
    mapping(string => Action) public actions;

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action.");
        _;
    }

    /**
     * @dev Event emitted when an action is rewarded.
     * @param actionName Name of the rewarded action.
     * @param totalReward Total amount of rewards distributed.
     */
    event ActionRewarded(string indexed actionName, uint256 totalReward);

    /**
     * @dev Event emitted when a new action is added.
     * @param actionName Name of the added action.
     */
    event ActionAdded(string indexed actionName);

    /**
     * @dev Constructor sets the initial owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to add a predefined action and its reward split.
     * @param _name Name of the action.
     * @param _totalReward Total reward amount for the action.
     * @param _recipients Array of recipients' addresses.
     * @param _percentages Array of percentages corresponding to each recipient.
     */
    function addAction(
        string memory _name,
        uint256 _totalReward,
        address[] memory _recipients,
        uint256[] memory _percentages
    ) external onlyOwner {
        require(_recipients.length == _percentages.length, "Recipients and percentages length mismatch.");

        // Create the action and set its reward details
        Action storage newAction = actions[_name];
        newAction.name = _name;
        newAction.totalReward = _totalReward;
        newAction.recipients = _recipients;

        uint256 totalPercentage;

        for (uint256 i = 0; i < _recipients.length; i++) {
            newAction.percentages[_recipients[i]] = _percentages[i];
            totalPercentage += _percentages[i];
        }

        require(totalPercentage == 100, "Total percentage must equal 100.");

        emit ActionAdded(_name);
    }

    /**
     * @dev Function to reward recipients for a specific action.
     * @param _name Name of the action to reward.
     */
    function rewardAction(string memory _name) external payable {
        Action storage action = actions[_name];

        require(action.totalReward > 0, "Action does not exist.");
        require(msg.value == action.totalReward, "Incorrect reward amount sent.");

        for (uint256 i = 0; i < action.recipients.length; i++) {
            address recipient = action.recipients[i];
            uint256 rewardAmount = (msg.value * action.percentages[recipient]) / 100;

            // Transfer reward amount to the recipient
            (bool success, ) = recipient.call{value: rewardAmount}("");
            require(success, "Transfer failed.");
        }

        emit ActionRewarded(_name, msg.value);
    }

    /**
     * @dev Function to withdraw funds from the contract (for emergencies or unused balances).
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance.");

        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdrawal failed.");
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Function to retrieve contract balance.
     * @return Contract balance in Wei.
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
