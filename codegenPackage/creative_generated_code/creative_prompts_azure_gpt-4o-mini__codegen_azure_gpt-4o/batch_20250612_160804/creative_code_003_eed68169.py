"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sale-humanizedai.web.app
Prompt: Develop a smart contract function to stake $HMZ tokens as described in the HumanizedAi presale documentation.
Generated: DETERMINISTIC_eed6816932fe1a9e
Batch ID: 20250612_160804
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
 * @title HMZTokenStaking
 * @dev Smart contract for staking $HMZ tokens during the HumanizedAi presale.
 * Users can stake $HMZ tokens and later retrieve them along with any rewards.
 * Ensure the contract is deployed after the HMZ token contract is live.
 */
contract HMZTokenStaking {
    // Token interface
    IERC20 public hmzToken;

    // Event declarations
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 timestamp);

    // Mapping to store staked balances
    mapping(address => uint256) public stakes;

    // Contract owner address
    address public owner;

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to set the $HMZ token address and contract owner.
     * @param _hmzToken Address of the HMZ token contract.
     */
    constructor(address _hmzToken) {
        require(_hmzToken != address(0), "Invalid HMZ token address");
        hmzToken = IERC20(_hmzToken);
        owner = msg.sender;
    }

    /**
     * @dev Stake $HMZ tokens into the contract.
     * @param _amount Amount of $HMZ tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Staking amount must be greater than zero");

        // Transfer $HMZ tokens from the user to the contract
        bool success = hmzToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update the user's staked balance
        stakes[msg.sender] += _amount;

        // Emit the staking event
        emit Staked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Unstake $HMZ tokens from the contract.
     */
    function unstake() external {
        uint256 stakedAmount = stakes[msg.sender];
        require(stakedAmount > 0, "No staked tokens to unstake");

        // Reset the user's staked balance
        stakes[msg.sender] = 0;

        // Transfer $HMZ tokens back to the user
        bool success = hmzToken.transfer(msg.sender, stakedAmount);
        require(success, "Token transfer failed");

        // Emit the unstaking event
        emit Unstaked(msg.sender, stakedAmount, block.timestamp);
    }

    /**
     * @dev Emergency withdrawal for the contract owner in case of issues.
     * Allows the owner to withdraw all tokens staked in the contract.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = hmzToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");

        bool success = hmzToken.transfer(owner, contractBalance);
        require(success, "Token transfer failed");
    }
}

// Minimal IERC20 interface to interact with $HMZ token
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
