"""
Generated Code Metadata:
========================
Original URL: https://velodrome-7zz.pages.dev
Prompt: "Design a voting system using NFTs for token emissions and incentives distribution, inspired by Velodrome Finance's veVELO voter mechanism."
Generated: DETERMINISTIC_c6ca6fa580a25067
Batch ID: 20250622_205436
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract VotingNFT is ERC721Enumerable, Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    struct Lock {
        uint256 amount;
        uint256 end;
        uint256 votingPower;
    }

    IERC20 public immutable token;
    uint256 public constant MAX_LOCK_TIME = 4 * 365 days; // 4 years
    uint256 public constant MIN_LOCK_TIME = 1 weeks;
    uint256 public totalVotingPower;

    mapping(uint256 => Lock) public locks;
    mapping(address => uint256[]) public userLocks;

    event LockCreated(uint256 indexed tokenId, address indexed user, uint256 amount, uint256 end);
    event LockExtended(uint256 indexed tokenId, uint256 amount, uint256 newEnd);
    event VoteCast(address indexed user, uint256 indexed tokenId, address indexed gauge, uint256 weight);

    constructor(address _token, string memory _name, string memory _symbol) 
        ERC721(_name, _symbol) 
    {
        token = IERC20(_token);
    }

    function createLock(uint256 _amount, uint256 _lockDuration) external {
        require(_amount > 0, "Cannot lock 0 tokens");
        require(_lockDuration >= MIN_LOCK_TIME, "Lock duration too short");
        require(_lockDuration <= MAX_LOCK_TIME, "Lock duration too long");

        uint256 end = block.timestamp.add(_lockDuration);
        uint256 votingPower = _calculateVotingPower(_amount, _lockDuration);

        token.safeTransferFrom(msg.sender, address(this), _amount);

        uint256 tokenId = totalSupply();
        _mint(msg.sender, tokenId);

        locks[tokenId] = Lock({
            amount: _amount,
            end: end,
            votingPower: votingPower
        });

        userLocks[msg.sender].push(tokenId);
        totalVotingPower = totalVotingPower.add(votingPower);

        emit LockCreated(tokenId, msg.sender, _amount, end);
    }

    function extendLock(uint256 _tokenId, uint256 _additionalDuration) external {
        require(ownerOf(_tokenId) == msg.sender, "Not token owner");
        require(_additionalDuration > 0, "Duration must be > 0");
        
        Lock storage lock = locks[_tokenId];
        require(lock.end > block.timestamp, "Lock expired");

        uint256 newEnd = lock.end.add(_additionalDuration);
        require(newEnd <= block.timestamp.add(MAX_LOCK_TIME), "Lock duration too long");

        uint256 newVotingPower = _calculateVotingPower(lock.amount, newEnd.sub(block.timestamp));
        totalVotingPower = totalVotingPower.sub(lock.votingPower).add(newVotingPower);

        lock.end = newEnd;
        lock.votingPower = newVotingPower;

        emit LockExtended(_tokenId, lock.amount, newEnd);
    }

    function vote(uint256 _tokenId, address _gauge, uint256 _weight) external {
        require(ownerOf(_tokenId) == msg.sender, "Not token owner");
        Lock memory lock = locks[_tokenId];
        require(lock.end > block.timestamp, "Lock expired");
        require(_weight <= lock.votingPower, "Weight exceeds voting power");

        // Implement gauge voting logic here
        // This would interact with a gauge controller contract
        
        emit VoteCast(msg.sender, _tokenId, _gauge, _weight);
    }

    function withdraw(uint256 _tokenId) external {
        require(ownerOf(_tokenId) == msg.sender, "Not token owner");
        Lock memory lock = locks[_tokenId];
        require(lock.end <= block.timestamp, "Lock not expired");

        token.safeTransfer(msg.sender, lock.amount);
        _burn(_tokenId);

        // Remove from userLocks array
        uint256[] storage userLockIds = userLocks[msg.sender];
        for (uint256 i = 0; i < userLockIds.length; i++) {
            if (userLockIds[i] == _tokenId) {
                userLockIds[i] = userLockIds[userLockIds.length - 1];
                userLockIds.pop();
                break;
            }
        }
    }

    function _calculateVotingPower(uint256 _amount, uint256 _duration) internal pure returns (uint256) {
        // Linear voting power calculation (can be adjusted to quadratic or other)
        return _amount.mul(_duration).div(MAX_LOCK_TIME);
    }

    function getUserLocks(address _user) external view returns (uint256[] memory) {
        return userLocks[_user];
    }

    function getLockDetails(uint256 _tokenId) external view returns (Lock memory) {
        return locks[_tokenId];
    }
}

contract GaugeController is Ownable {
    using SafeMath for uint256;

    struct Gauge {
        address gaugeAddress;
        bool isActive;
        uint256 weight;
    }

    mapping(address => Gauge) public gauges;
    address[] public gaugeList;
    VotingNFT public votingNFT;

    event GaugeAdded(address indexed gauge);
    event GaugeRemoved(address indexed gauge);
    event VoteWeightUpdated(address indexed gauge, uint256 newWeight);

    constructor(address _votingNFT) {
        votingNFT = VotingNFT(_votingNFT);
    }

    function addGauge(address _gauge) external onlyOwner {
        require(!gauges[_gauge].isActive, "Gauge already exists");
        gauges[_gauge] = Gauge({
            gaugeAddress: _gauge,
            isActive: true,
            weight: 0
        });
        gaugeList.push(_gauge);
        emit GaugeAdded(_gauge);
    }

    function removeGauge(address _gauge) external onlyOwner {
        require(gauges[_gauge].isActive, "Gauge does not exist");
        gauges[_gauge].isActive = false;
        
        // Remove from gaugeList
        for (uint256 i = 0; i < gaugeList.length; i++) {
            if (gaugeList[i] == _gauge) {
                gaugeList[i] = gaugeList[gaugeList.length - 1];
                gaugeList.pop();
                break;
            }
        }
        emit GaugeRemoved(_gauge);
    }

    function updateVoteWeights(address _gauge, uint256 _weight) external {
        require(gauges[_gauge].isActive, "Gauge not active");
        gauges[_gauge].weight = _weight;
        emit VoteWeightUpdated(_gauge, _weight);
    }

    function distributeRewards(address _rewardToken) external {
        uint256 totalWeight = 0;
        for (uint256 i = 0; i < gaugeList.length; i++) {
            totalWeight = totalWeight.add(gauges[gaugeList[i]].weight);
        }

        IERC20 rewardToken = IERC20(_rewardToken);
        uint256 totalRewards = rewardToken.balanceOf(address(this));

        for (uint256 i = 0; i < gaugeList.length; i++) {
            address gauge = gaugeList[i];
            uint256 gaugeWeight = gauges[gauge].weight;
            if (gaugeWeight > 0) {
                uint256 gaugeReward = totalRewards.mul(gaugeWeight).div(totalWeight);
                rewardToken.transfer(gauge, gaugeReward);
            }
        }
    }
}
```
