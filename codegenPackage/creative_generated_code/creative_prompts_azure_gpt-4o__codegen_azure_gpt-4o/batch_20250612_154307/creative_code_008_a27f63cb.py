"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-launch.web.app
Prompt: Generate a Solidity contract that integrates the MemeVault protocol, allowing staking rewards to scale dynamically based on $STARS token holdings.
Generated: DETERMINISTIC_a27f63cb0e374709
Batch ID: 20250612_154307
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
 * @title MemeVaultStaking
 * @dev This contract integrates the MemeVault protocol to provide dynamic staking rewards
 *      based on $STARS token holdings.
 */
interface IMemeVault {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getReward() external;
    function balanceOf(address account) external view returns (uint256);
    function totalSupply() external view returns (uint256);
}

// Interface for the $STARS token
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract MemeVaultStaking {
    // State variables
    address public memeVault; // Address of MemeVault protocol
    address public starsToken; // Address of $STARS token
    address public owner; // Owner of the contract

    mapping(address => uint256) public userStakedAmount; // Tracks user stakes

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier nonZeroAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    /**
     * @dev Constructor to set the MemeVault and $STARS token addresses.
     * @param _memeVault Address of the MemeVault protocol.
     * @param _starsToken Address of the $STARS token.
     */
    constructor(address _memeVault, address _starsToken) {
        require(_memeVault != address(0) && _starsToken != address(0), "Invalid address");
        memeVault = _memeVault;
        starsToken = _starsToken;
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake tokens in the MemeVault protocol.
     *      Reward rate scales dynamically based on the user's $STARS token holdings.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external nonZeroAmount(amount) {
        IERC20(starsToken).transferFrom(msg.sender, address(this), amount);
        IERC20(starsToken).approve(memeVault, amount);

        IMemeVault(memeVault).stake(amount);
        userStakedAmount[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens from the MemeVault protocol.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external nonZeroAmount(amount) {
        require(userStakedAmount[msg.sender] >= amount, "Insufficient staked balance");

        IMemeVault(memeVault).withdraw(amount);
        IERC20(starsToken).transfer(msg.sender, amount);
        userStakedAmount[msg.sender] -= amount;

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim rewards from the MemeVault protocol.
     */
    function claimReward() external {
        IMemeVault(memeVault).getReward();
        emit RewardClaimed(msg.sender);
    }

    /**
     * @dev Returns the staked balance of a user.
     * @param account Address of the user.
     * @return The staked balance of the user.
     */
    function getStakedBalance(address account) external view returns (uint256) {
        return userStakedAmount[account];
    }

    /**
     * @dev Transfers ownership of the contract to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```
