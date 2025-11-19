"""
Generated Code Metadata:
========================
Original URL: https://galaxyfox-en.web.app
Prompt: Generate a smart contract in Solidity for a token with a deflationary process, similar to $GFOX, including a burn mechanism and staking rewards.
Generated: DETERMINISTIC_39c21adafdf4ceca
Batch ID: 20250622_210348
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract DeflationaryToken is ERC20, ERC20Burnable, Ownable, Pausable {
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant BURN_RATE = 100; // 1% burn rate (100 basis points)
    uint256 public constant REWARD_RATE = 200; // 2% staking reward (200 basis points)
    uint256 public constant BASIS_POINTS = 10_000; // 100% in basis points

    mapping(address => uint256) public stakedBalance;
    mapping(address => uint256) public lastStakeTime;
    mapping(address => bool) public isExcludedFromFee;

    event TokensBurned(address indexed burner, uint256 amount);
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensUnstaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 amount);

    constructor() ERC20("DeflationaryToken", "DFT") {
        _mint(msg.sender, MAX_SUPPLY);
        isExcludedFromFee[msg.sender] = true;
    }

    function transfer(address recipient, uint256 amount) 
        public 
        override 
        whenNotPaused
        returns (bool) 
    {
        _transferWithFees(_msgSender(), recipient, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) 
        public 
        override 
        whenNotPaused
        returns (bool) 
    {
        _spendAllowance(sender, _msgSender(), amount);
        _transferWithFees(sender, recipient, amount);
        return true;
    }

    function _transferWithFees(address sender, address recipient, uint256 amount) internal {
        if (isExcludedFromFee[sender] || isExcludedFromFee[recipient]) {
            _transfer(sender, recipient, amount);
        } else {
            uint256 burnAmount = (amount * BURN_RATE) / BASIS_POINTS;
            uint256 rewardAmount = (amount * REWARD_RATE) / BASIS_POINTS;
            uint256 transferAmount = amount - burnAmount - rewardAmount;

            _transfer(sender, recipient, transferAmount);
            _burn(sender, burnAmount);
            _distributeRewards(rewardAmount);
            
            emit TokensBurned(sender, burnAmount);
        }
    }

    function _distributeRewards(uint256 amount) internal {
        uint256 totalStaked = totalStakedTokens();
        if (totalStaked == 0) {
            _burn(_msgSender(), amount);
            return;
        }

        // Distribute rewards proportionally to stakers
        // Note: In a production environment, consider using a more gas-efficient method
        for (uint256 i = 0; i < _getStakerCount(); i++) {
            address staker = _getStakerAtIndex(i);
            uint256 stakerShare = (stakedBalance[staker] * amount) / totalStaked;
            if (stakerShare > 0) {
                _mint(staker, stakerShare);
            }
        }
    }

    function stake(uint256 amount) external whenNotPaused {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(_msgSender()) >= amount, "Insufficient balance");

        _transfer(_msgSender(), address(this), amount);
        stakedBalance[_msgSender()] += amount;
        lastStakeTime[_msgSender()] = block.timestamp;

        emit TokensStaked(_msgSender(), amount);
    }

    function unstake(uint256 amount) external whenNotPaused {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedBalance[_msgSender()] >= amount, "Insufficient staked balance");

        stakedBalance[_msgSender()] -= amount;
        _transfer(address(this), _msgSender(), amount);

        emit TokensUnstaked(_msgSender(), amount);
    }

    function claimRewards() external whenNotPaused {
        uint256 rewards = calculateRewards(_msgSender());
        require(rewards > 0, "No rewards available");

        lastStakeTime[_msgSender()] = block.timestamp;
        _mint(_msgSender(), rewards);

        emit RewardsClaimed(_msgSender(), rewards);
    }

    function calculateRewards(address staker) public view returns (uint256) {
        if (stakedBalance[staker] == 0) return 0;
        
        uint256 timeStaked = block.timestamp - lastStakeTime[staker];
        uint256 rewardPerSecond = (REWARD_RATE * totalSupply()) / (BASIS_POINTS * 365 days);
        return (stakedBalance[staker] * rewardPerSecond * timeStaked) / totalSupply();
    }

    function totalStakedTokens() public view returns (uint256) {
        uint256 total;
        for (uint256 i = 0; i < _getStakerCount(); i++) {
            total += stakedBalance[_getStakerAtIndex(i)];
        }
        return total;
    }

    function excludeFromFee(address account, bool excluded) external onlyOwner {
        isExcludedFromFee[account] = excluded;
    }

    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }

    // Helper functions (in a production environment, consider using a more efficient data structure)
    function _getStakerCount() internal pure returns (uint256) {
        // Simplified for example - in production use an enumerable set
        return 0;
    }

    function _getStakerAtIndex(uint256) internal pure returns (address) {
        // Simplified for example - in production use an enumerable set
        return address(0);
    }
}
```
