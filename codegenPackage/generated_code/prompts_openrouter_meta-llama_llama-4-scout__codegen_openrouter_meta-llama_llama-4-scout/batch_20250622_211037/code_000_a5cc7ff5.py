"""
Generated Code Metadata:
========================
Original URL: https://restaking-puffer.app
Prompt: Write a smart contract for a restaking protocol using Puffer's staking mechanism.
Generated: DETERMINISTIC_a5cc7ff5f41d2b17
Batch ID: 20250622_211037
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PufferRestakingProtocol
 * @author [Your Name]
 * @notice A smart contract for a restaking protocol using Puffer's staking mechanism.
 */
contract PufferRestakingProtocol is ReentrancyGuard {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Mapping of user addresses to their staked balances
    mapping(address => uint256) public stakedBalances;

    // Mapping of user addresses to their restaked balances
    mapping(address => uint256) public restakedBalances;

    // Mapping of puffer pool IDs to their corresponding staking contracts
    mapping(uint256 => address) public pufferPoolContracts;

    // Puffer staking contract address
    address public pufferStakingContract;

    // ERC20 token used for staking
    IERC20 public stakingToken;

    /**
     * @notice Emitted when a user stakes tokens
     * @param user The user's address
     * @param amount The amount staked
     */
    event Staked(address indexed user, uint256 amount);

    /**
     * @notice Emitted when a user restakes tokens
     * @param user The user's address
     * @param amount The amount restaked
     */
    event Restaked(address indexed user, uint256 amount);

    /**
     * @notice Emitted when a user unstakes tokens
     * @param user The user's address
     * @param amount The amount unstaked
     */
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @param _pufferStakingContract The address of Puffer's staking contract
     * @param _stakingToken The address of the ERC20 token used for staking
     */
    constructor(address _pufferStakingContract, address _stakingToken) {
        pufferStakingContract = _pufferStakingContract;
        stakingToken = IERC20(_stakingToken);
    }

    /**
     * @notice Stake tokens
     * @param _amount The amount to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid stake amount");

        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user's staked balance
        stakedBalances[msg.sender] = stakedBalances[msg.sender].add(_amount);

        // Emit event
        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Restake tokens
     * @param _pufferPoolId The ID of the Puffer pool
     * @param _amount The amount to restake
     */
    function restake(uint256 _pufferPoolId, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid restake amount");
        require(pufferPoolContracts[_pufferPoolId] != address(0), "Invalid Puffer pool");

        // Check if user has sufficient staked balance
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Update user's staked balance
        stakedBalances[msg.sender] = stakedBalances[msg.sender].sub(_amount);

        // Update user's restaked balance
        restakedBalances[msg.sender] = restakedBalances[msg.sender].add(_amount);

        // Call Puffer staking contract to restake tokens
        IStakingContract(pufferPoolContracts[_pufferPoolId]).restake(msg.sender, _amount);

        // Emit event
        emit Restaked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens
     * @param _amount The amount to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid unstake amount");

        // Check if user has sufficient staked balance
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Update user's staked balance
        stakedBalances[msg.sender] = stakedBalances[msg.sender].sub(_amount);

        // Transfer tokens from contract to user
        stakingToken.safeTransfer(msg.sender, _amount);

        // Emit event
        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Add a Puffer pool contract
     * @param _pufferPoolId The ID of the Puffer pool
     * @param _contractAddress The address of the Puffer pool contract
     */
    function addPufferPoolContract(uint256 _pufferPoolId, address _contractAddress) external onlyOwner {
        pufferPoolContracts[_pufferPoolId] = _contractAddress;
    }

    /**
     * @notice Modifier for only the owner
     */
    modifier onlyOwner {
        require(msg.sender == owner(), "Only the owner can call this function");
        _;
    }

    /**
     * @notice Get the owner address
     * @return The owner address
     */
    function owner() public view returns (address) {
        return msg.sender;
    }
}

// Example IStakingContract interface
interface IStakingContract {
    function restake(address _user, uint256 _amount) external;
}
```
