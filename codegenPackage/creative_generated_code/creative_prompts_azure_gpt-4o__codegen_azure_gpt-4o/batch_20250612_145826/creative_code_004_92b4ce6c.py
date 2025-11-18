"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchifi-dapprotocol.pages.dev
Prompt: Create a smart contract for staking and unstaking tokens on the Fix-path platform, ensuring support for multi-chain functionality.
Generated: DETERMINISTIC_92b4ce6c4a3a6cc1
Batch ID: 20250612_145826
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
 * @title StakingContract
 * @notice A smart contract for staking and unstaking ERC20 tokens
 *         with multi-chain support.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is Ownable {
    // Struct to hold staking information
    struct StakeInfo {
        uint256 amount;      // Amount of tokens staked
        uint256 timestamp;   // Timestamp of when tokens were staked
    }

    // Mapping of user addresses to chain ID to their staking info
    mapping(address => mapping(uint256 => StakeInfo)) public stakes;

    // Token instance
    IERC20 public stakingToken;

    // Events
    event TokensStaked(address indexed user, uint256 chainId, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 chainId, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract with the token address.
     * @param _token Address of the ERC20 token used for staking.
     */
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        stakingToken = IERC20(_token);
    }

    /**
     * @notice Stake tokens on a specific chain.
     * @param _chainId ID of the chain where tokens are being staked.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _chainId, uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from user to contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staking info
        stakes[msg.sender][_chainId].amount += _amount;
        stakes[msg.sender][_chainId].timestamp = block.timestamp;

        emit TokensStaked(msg.sender, _chainId, _amount);
    }

    /**
     * @notice Unstake tokens from a specific chain.
     * @param _chainId ID of the chain where tokens are being unstaked.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _chainId, uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        StakeInfo storage stakeInfo = stakes[msg.sender][_chainId];
        require(
            stakeInfo.amount >= _amount,
            "Insufficient staked balance for unstaking"
        );

        // Update staking info
        stakeInfo.amount -= _amount;

        // Transfer tokens back to user
        require(
            stakingToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        emit TokensUnstaked(msg.sender, _chainId, _amount);
    }

    /**
     * @notice Get staking details for a user on a specific chain.
     * @param _user Address of the user.
     * @param _chainId ID of the chain.
     * @return amount Staked amount.
     * @return timestamp Timestamp when the tokens were staked.
     */
    function getStakeInfo(address _user, uint256 _chainId)
        external
        view
        returns (uint256 amount, uint256 timestamp)
    {
        StakeInfo memory stakeInfo = stakes[_user][_chainId];
        return (stakeInfo.amount, stakeInfo.timestamp);
    }
}
```
