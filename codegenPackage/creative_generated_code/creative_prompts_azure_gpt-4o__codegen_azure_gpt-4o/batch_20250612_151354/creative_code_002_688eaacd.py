"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pablo-defis.web.app
Prompt: Generate a smart contract in Solidity for staking $PABLO tokens, ensuring revenue-sharing features where rewards are distributed in both $PABLO and USDT, as outlined in the website's staking pools.
Generated: DETERMINISTIC_688eaacdc2f5b2d8
Batch ID: 20250612_151354
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
 * @title PabloStaking
 * @dev Smart contract for staking $PABLO tokens with revenue-sharing rewards (in $PABLO and USDT).
 */
contract PabloStaking {
    // Struct to store user's staking information
    struct Stake {
        uint256 amount; // Amount of $PABLO tokens staked
        uint256 timestamp; // Timestamp of when the stake was made
    }

    // Mapping of user address to their staking information
    mapping(address => Stake) public stakes;

    // $PABLO token address (ERC20)
    address public pabloToken;

    // USDT token address (ERC20)
    address public usdtToken;

    // Admin address
    address public admin;

    // Total $PABLO staked in the contract
    uint256 public totalStaked;

    // Events for logging activities
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 pabloReward, uint256 usdtReward);

    // Modifier to restrict access to admin functions
    modifier onlyAdmin() {
        require(msg.sender == admin, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _pabloToken Address of the $PABLO token contract.
     * @param _usdtToken Address of the USDT token contract.
     */
    constructor(address _pabloToken, address _usdtToken) {
        require(_pabloToken != address(0), "Invalid $PABLO token address");
        require(_usdtToken != address(0), "Invalid USDT token address");
        pabloToken = _pabloToken;
        usdtToken = _usdtToken;
        admin = msg.sender;
    }

    /**
     * @dev Function to stake $PABLO tokens.
     * @param _amount Amount of $PABLO tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Transfer $PABLO tokens from user to this contract
        require(IERC20(pabloToken).transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user's staking information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to unstake $PABLO tokens.
     */
    function unstake() external {
        // Get user's staking information
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Transfer $PABLO tokens back to user
        require(IERC20(pabloToken).transfer(msg.sender, userStake.amount), "Token transfer failed");

        // Update total staked amount
        totalStaked -= userStake.amount;

        // Clear user's staking information
        delete stakes[msg.sender];

        emit Unstaked(msg.sender, userStake.amount);
    }

    /**
     * @dev Function to distribute rewards to a staker.
     * @param _user Address of the user to distribute rewards to.
     * @param _pabloReward Amount of $PABLO rewards.
     * @param _usdtReward Amount of USDT rewards.
     */
    function distributeRewards(address _user, uint256 _pabloReward, uint256 _usdtReward) external onlyAdmin {
        require(_user != address(0), "Invalid user address");
        require(stakes[_user].amount > 0, "User has no active stake");

        // Distribute $PABLO rewards
        if (_pabloReward > 0) {
            require(IERC20(pabloToken).transfer(_user, _pabloReward), "$PABLO reward transfer failed");
        }

        // Distribute USDT rewards
        if (_usdtReward > 0) {
            require(IERC20(usdtToken).transfer(_user, _usdtReward), "USDT reward transfer failed");
        }

        emit RewardsDistributed(_user, _pabloReward, _usdtReward);
    }

    /**
     * @dev Function to update the admin address.
     * @param _newAdmin New admin address.
     */
    function updateAdmin(address _newAdmin) external onlyAdmin {
        require(_newAdmin != address(0), "Invalid admin address");
        admin = _newAdmin;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
