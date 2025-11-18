"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimbtc20.pages.dev
Prompt: Develop a Solidity contract for BTC20 that integrates a fair presale mechanism, locking unsold tokens into a staking pool for long-term rewards distribution.
Generated: DETERMINISTIC_745549da0d634e92
Batch ID: 20250612_151333
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
 * @title BTC20 Token Contract with Fair Presale and Staking Pool
 * @notice This contract implements a fair presale mechanism for BTC20 tokens,
 *         and locks unsold tokens in a staking pool for long-term rewards distribution.
 */
contract BTC20Presale {
    // Token details
    string public constant name = "BTC20";
    string public constant symbol = "BTC20";
    uint8 public constant decimals = 18;

    uint256 public totalSupply; // Total supply of BTC20 tokens
    uint256 public presaleSupply; // Tokens allocated for presale
    uint256 public pricePerToken; // Token price during presale
    uint256 public stakingPoolSupply; // Tokens locked in staking pool

    // Presale details
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    bool public presaleEnded;

    // Staking pool
    mapping(address => uint256) public stakingBalances;
    uint256 public totalStaked;

    // Owner of the contract
    address public owner;

    // Mapping to track user balances
    mapping(address => uint256) public balances;

    // Events
    event PresalePurchase(address indexed buyer, uint256 amount);
    event TokensStaked(address indexed staker, uint256 amount);
    event RewardsDistributed(address indexed staker, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp >= presaleStartTime, "Presale has not started");
        require(block.timestamp <= presaleEndTime, "Presale has ended");
        require(!presaleEnded, "Presale has ended");
        _;
    }

    /**
     * @dev Constructor to initialize the BTC20 contract.
     * @param _totalSupply Total supply of BTC20 tokens.
     * @param _presaleSupply Tokens allocated for presale.
     * @param _pricePerToken Price per token during presale (in wei).
     * @param _presaleStartTime Start time of presale (UNIX timestamp).
     * @param _presaleEndTime End time of presale (UNIX timestamp).
     */
    constructor(
        uint256 _totalSupply,
        uint256 _presaleSupply,
        uint256 _pricePerToken,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime
    ) {
        require(_presaleSupply <= _totalSupply, "Presale supply exceeds total supply");
        require(_presaleStartTime < _presaleEndTime, "Invalid presale time range");

        owner = msg.sender;
        totalSupply = _totalSupply;
        presaleSupply = _presaleSupply;
        pricePerToken = _pricePerToken;
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;

        balances[address(this)] = totalSupply; // All tokens start in contract
    }

    /**
     * @dev Buy tokens during presale.
     * @notice Sends ETH to purchase BTC20 tokens during the presale period.
     */
    function buyPresaleTokens() external payable presaleActive {
        uint256 tokensToBuy = msg.value / pricePerToken;
        require(tokensToBuy > 0, "Insufficient ETH sent for purchase");
        require(tokensToBuy <= presaleSupply, "Not enough tokens available");

        balances[address(this)] -= tokensToBuy;
        balances[msg.sender] += tokensToBuy;
        presaleSupply -= tokensToBuy;

        emit PresalePurchase(msg.sender, tokensToBuy);
    }

    /**
     * @dev End the presale and lock unsold tokens into the staking pool.
     * @notice Only callable by the owner, after presale ends.
     */
    function endPresale() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale has not ended yet");
        require(!presaleEnded, "Presale already ended");

        presaleEnded = true;
        stakingPoolSupply = presaleSupply; // Lock unsold tokens into staking pool
        presaleSupply = 0; // Reset presale token count
    }

    /**
     * @dev Stake tokens in the staking pool.
     * @param _amount Amount of tokens to stake.
     */
    function stakeTokens(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");
        require(balances[msg.sender] >= _amount, "Insufficient token balance");

        balances[msg.sender] -= _amount;
        stakingBalances[msg.sender] += _amount;
        totalStaked += _amount;

        emit TokensStaked(msg.sender, _amount);
    }

    /**
     * @dev Distribute rewards proportionally to stakers.
     * @notice Only callable by the owner.
     */
    function distributeRewards() external onlyOwner {
        require(totalStaked > 0, "No staked tokens to distribute rewards");

        for (uint256 i = 0; i < totalStaked; i++) {
            address staker = address(i);
            uint256 reward = stakingBalances[staker] * stakingPoolSupply / totalStaked; // Proportional reward
            balances[staker] += reward;
            stakingPoolSupply -= reward;

            emit RewardsDistributed(staker, reward);
        }
    }

    /**
     * @dev Withdraw tokens.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external {
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(balances[msg.sender] >= _amount, "Insufficient token balance");

        balances[msg.sender] -= _amount;
        payable(msg.sender).transfer(_amount);
    }
}
```
