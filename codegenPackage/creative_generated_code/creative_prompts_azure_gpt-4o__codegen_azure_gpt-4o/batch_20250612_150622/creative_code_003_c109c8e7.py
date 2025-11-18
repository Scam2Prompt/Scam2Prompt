"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stklido.com
Prompt: Create a smart contract that integrates with the Lido protocol to automatically stake Ethereum and distribute rewards to multiple users.
Generated: DETERMINISTIC_c109c8e73df44bfd
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the smart contract code written in Solidity to interact with the Lido protocol for staking Ethereum and distributing rewards to multiple users. The contract assumes familiarity with the Lido protocol's API and follows best practices.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Import OpenZeppelin libraries for safe math and access control
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Interface for interacting with the Lido staking contract
interface ILido {
    function submit(address _referral) external payable returns (uint256 stETHAmount);
    function balanceOf(address account) external view returns (uint256);
}

/**
 * @title LidoAutoStake
 * @dev A smart contract that stakes Ethereum into the Lido protocol
 *      and distributes staking rewards to multiple beneficiaries.
 */
contract LidoAutoStake is Ownable, ReentrancyGuard {
    ILido public lido; // Lido contract instance
    IERC20 public stETH; // stETH token contract instance

    // Mapping to track user shares for reward distribution
    mapping(address => uint256) public userShares;
    uint256 public totalShares;

    event Staked(address indexed staker, uint256 amountETH, uint256 amountStETH);
    event RewardsDistributed(uint256 totalRewards, uint256 timestamp);
    event BeneficiaryAdded(address indexed beneficiary, uint256 shares);
    event BeneficiaryRemoved(address indexed beneficiary);

    /**
     * @dev Constructor to set Lido contract and stETH token.
     * @param _lido Address of the Lido staking contract.
     * @param _stETH Address of the stETH token.
     */
    constructor(address _lido, address _stETH) {
        require(_lido != address(0), "Invalid Lido contract address");
        require(_stETH != address(0), "Invalid stETH token address");

        lido = ILido(_lido);
        stETH = IERC20(_stETH);
    }

    /**
     * @dev Stake Ethereum into the Lido protocol and receive stETH.
     * @notice Automatically distributes stETH rewards to beneficiaries.
     */
    function stakeETH() external payable nonReentrant {
        require(msg.value > 0, "Invalid ETH amount");

        // Stake ETH into Lido
        uint256 stETHReceived = lido.submit{ value: msg.value }(address(0)); // No referral used

        emit Staked(msg.sender, msg.value, stETHReceived);

        // Distribute stETH rewards among beneficiaries
        distributeRewards();
    }

    /**
     * @dev Distribute stETH rewards proportionally to beneficiaries based on shares.
     */
    function distributeRewards() public nonReentrant {
        uint256 totalBalance = stETH.balanceOf(address(this));
        require(totalBalance > 0, "No rewards available for distribution");

        for (uint256 i = 0; i < totalShares; i++) {
            address beneficiary = address(i); // Assume beneficiaries are pre-indexed for simplicity
            uint256 beneficiaryShare = userShares[beneficiary];
            uint256 rewards = beneficiaryShareportion calculation logic..
