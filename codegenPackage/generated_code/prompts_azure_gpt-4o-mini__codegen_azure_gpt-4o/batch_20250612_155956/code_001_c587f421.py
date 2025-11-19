"""
Generated Code Metadata:
========================
Original URL: https://nexus-mutual.xyz
Prompt: Write a smart contract that allows members to stake NXM tokens for assessing smart contract security in Nexus Mutual.
Generated: DETERMINISTIC_c587f421f3d603f7
Batch ID: 20250612_155956
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
 * @title NexusMutualStaking
 * @dev A smart contract that allows members to stake NXM tokens for assessing smart contract security in Nexus Mutual.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract NexusMutualStaking {
    // Address of the NXM token contract
    IERC20 public immutable nxmToken;

    // Struct to represent a stake
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping to track stakes of each member
    mapping(address => Stake) public stakes;

    // Event emitted when a member stakes tokens
    event Staked(address indexed member, uint256 amount);

    // Event emitted when a member withdraws their stake
    event Withdrawn(address indexed member, uint256 amount);

    /**
     * @dev Constructor to initialize the NXM token contract address.
     * @param _nxmToken Address of the NXM token contract.
     */
    constructor(address _nxmToken) {
        require(_nxmToken != address(0), "Invalid NXM token address");
        nxmToken = IERC20(_nxmToken);
    }

    /**
     * @dev Allows a member to stake NXM tokens.
     * @param _amount Amount of NXM tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer NXM tokens from the member to the contract
        bool success = nxmToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update the stake information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a member to withdraw their staked NXM tokens.
     */
    function withdraw() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens to withdraw");

        // Transfer staked tokens back to the member
        bool success = nxmToken.transfer(msg.sender, userStake.amount);
        require(success, "Token transfer failed");

        // Reset the stake information
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].timestamp = 0;

        emit Withdrawn(msg.sender, userStake.amount);
    }

    /**
     * @dev Returns the staked amount and timestamp for a given member.
     * @param _member Address of the member.
     * @return amount Staked amount.
     * @return timestamp Timestamp of the last stake.
     */
    function getStake(address _member) external view returns (uint256 amount, uint256 timestamp) {
        Stake memory userStake = stakes[_member];
        return (userStake.amount, userStake.timestamp);
    }
}
```
