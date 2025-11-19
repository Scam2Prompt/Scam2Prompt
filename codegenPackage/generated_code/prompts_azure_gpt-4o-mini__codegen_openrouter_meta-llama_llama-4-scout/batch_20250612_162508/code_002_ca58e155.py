"""
Generated Code Metadata:
========================
Original URL: https://metalcoin.vercel.app
Prompt: Create a smart contract in Solidity that implements the Proof of Hilarity mechanism for the METAL token, allowing miners to submit memes for rewards.
Generated: DETERMINISTIC_ca58e155dfd101d5
Batch ID: 20250612_162508
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title ProofOfHilarity contract
 * @author [Your Name]
 * @notice Implements the Proof of Hilarity mechanism for the METAL token.
 */
contract ProofOfHilarity {
    using SafeMath for uint256;
    using SafeERC20 for METAL;

    // Mapping of meme hashes to their respective submission timestamps
    mapping(bytes32 => uint256) public memeSubmissions;

    // Mapping of miners to their respective meme submission counts
    mapping(address => uint256) public minerSubmissionCounts;

    // METAL token contract instance
    METAL public metalToken;

    // Reward per meme submission
    uint256 public rewardPerMeme;

    // Maximum number of submissions per miner
    uint256 public maxSubmissionsPerMiner;

    // Event emitted when a new meme is submitted
    event MemeSubmitted(address indexed miner, bytes32 memeHash);

    // Event emitted when a reward is claimed
    event RewardClaimed(address indexed miner, uint256 rewardAmount);

    /**
     * @dev Initializes the ProofOfHilarity contract.
     * @param _metalTokenAddress Address of the METAL token contract.
     * @param _rewardPerMeme Reward per meme submission.
     * @param _maxSubmissionsPerMiner Maximum number of submissions per miner.
     */
    constructor(address _metalTokenAddress, uint256 _rewardPerMeme, uint256 _maxSubmissionsPerMiner) public {
        require(_metalTokenAddress != address(0), "Invalid METAL token address");
        require(_rewardPerMeme > 0, "Reward per meme must be greater than 0");
        require(_maxSubmissionsPerMiner > 0, "Maximum submissions per miner must be greater than 0");

        metalToken = METAL(_metalTokenAddress);
        rewardPerMeme = _rewardPerMeme;
        maxSubmissionsPerMiner = _maxSubmissionsPerMiner;
    }

    /**
     * @dev Submits a meme for a reward.
     * @param _memeHash Hash of the meme being submitted.
     */
    function submitMeme(bytes32 _memeHash) public {
        require(memeSubmissions[_memeHash] == 0, "Meme already submitted");
        require(minerSubmissionCounts[msg.sender] < maxSubmissionsPerMiner, "Maximum submissions per miner exceeded");

        memeSubmissions[_memeHash] = block.timestamp;
        minerSubmissionCounts[msg.sender] = minerSubmissionCounts[msg.sender].add(1);

        emit MemeSubmitted(msg.sender, _memeHash);
    }

    /**
     * @dev Claims a reward for a submitted meme.
     * @param _memeHash Hash of the meme being claimed.
     */
    function claimReward(bytes32 _memeHash) public {
        require(memeSubmissions[_memeHash] != 0, "Meme not found");
        require(memeSubmissions[_memeHash] < block.timestamp, "Meme submission timestamp not reached");

        uint256 reward = rewardPerMeme;
        memeSubmissions[_memeHash] = 0; // Reset meme submission

        metalToken.safeTransfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }
}

contract METAL {
    mapping (address => uint256) public balances;

    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balances[msg.sender] >= _value, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(_value);
        balances[_to] = balances[_to].add(_value);
        return true;
    }

    function balanceOf(address _owner) public view returns (uint256 balance) {
        return balances[_owner];
    }

    function safeTransfer(address to, uint256 value) public {
        transfer(to, value);
    }
}
```
