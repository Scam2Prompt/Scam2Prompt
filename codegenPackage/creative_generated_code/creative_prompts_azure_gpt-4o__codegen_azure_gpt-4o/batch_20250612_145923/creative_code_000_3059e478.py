"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://groovesup.pages.dev
Prompt: Write a smart contract in Solidity that enables artists to distribute $GROOVE token rewards to fans based on streaming activity, as described in the GrooveUP ecosystem.
Generated: DETERMINISTIC_3059e4787cbebdb9
Batch ID: 20250612_145923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

/**
 * @title GrooveUP Reward Distribution Smart Contract
 * @dev Enables artists to distribute $GROOVE token rewards to fans based on streaming activity.
 * @author Your Name
 */
contract GrooveUPRewards {
    // ERC20 interface for $GROOVE token
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // $GROOVE token address
    IERC20 public grooveToken;

    // Owner of the contract (typically the artist or ecosystem manager)
    address public owner;

    // Mapping of fans to their rewards
    mapping(address => uint256) public rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed fan, uint256 amount);

    // Event emitted when ownership is transferred
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to the owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize the smart contract
     * @param _grooveToken Address of the $GROOVE token contract
     */
    constructor(address _grooveToken) {
        require(_grooveToken != address(0), "Invalid token address");
        grooveToken = IERC20(_grooveToken);
        owner = msg.sender;
    }

    /**
     * @dev Function to set rewards for a fan based on their streaming activity
     * @param _fan Address of the fan
     * @param _rewardAmount Amount of $GROOVE tokens to reward
     */
    function setReward(address _fan, uint256 _rewardAmount) external onlyOwner {
        require(_fan != address(0), "Invalid fan address");
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        rewards[_fan] += _rewardAmount;
    }

    /**
     * @dev Function for fans to claim their $GROOVE token rewards
     */
    function claimReward() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");
        require(grooveToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");

        rewards[msg.sender] = 0; // Reset reward balance for the fan
        require(grooveToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");

        emit RewardsDistributed(msg.sender, rewardAmount);
    }

    /**
     * @dev Function to transfer ownership of the contract to a new owner
     * @param _newOwner Address of the new owner
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @dev Function to withdraw any remaining $GROOVE tokens from the contract
     * @param _recipient Address to receive the remaining tokens
     */
    function withdrawTokens(address _recipient) external onlyOwner {
        require(_recipient != address(0), "Invalid recipient address");
        uint256 contractBalance = grooveToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");
        require(grooveToken.transfer(_recipient, contractBalance), "Withdrawal failed");
    }
}
```
