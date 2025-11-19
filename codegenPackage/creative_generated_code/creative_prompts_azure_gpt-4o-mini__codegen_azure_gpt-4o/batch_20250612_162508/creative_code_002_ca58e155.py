"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metalcoin.vercel.app
Prompt: Create a smart contract in Solidity that implements the Proof of Hilarity mechanism for the METAL token, allowing miners to submit memes for rewards.
Generated: DETERMINISTIC_ca58e155dfd101d5
Batch ID: 20250612_162508
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
 * @title ProofOfHilarity
 * @dev A smart contract implementing the Proof of Hilarity mechanism for METAL token.
 * Miners can submit memes, and the community votes to determine rewards.
 */
contract ProofOfHilarity {
    // Token balance mapping (mock METAL token ledger)
    mapping(address => uint256) public balances;

    // Meme submission structure
    struct Meme {
        address miner; // Address of the meme's submitter
        string memeURL; // URL pointing to the meme
        uint256 votes; // Number of votes the meme has received
        bool claimed; // Whether the reward has been claimed
    }

    // Array to store submitted memes
    Meme[] public memes;

    // Voting mapping to prevent double-voting per meme
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Reward to be distributed per meme (in METAL tokens)
    uint256 public rewardAmount = 100;

    // Event emitted upon successful meme submission
    event MemeSubmitted(uint256 memeId, address indexed miner, string memeURL);

    // Event emitted upon successful voting
    event Voted(uint256 memeId, address indexed voter);

    // Event emitted upon successful reward claim
    event RewardClaimed(uint256 memeId, address indexed miner, uint256 rewardAmount);

    /**
     * @dev Submit a meme for voting.
     * @param memeURL URL pointing to the meme content.
     */
    function submitMeme(string calldata memeURL) external {
        require(bytes(memeURL).length > 0, "Meme URL cannot be empty");

        memes.push(Meme({
            miner: msg.sender,
            memeURL: memeURL,
            votes: 0,
            claimed: false
        }));

        uint256 memeId = memes.length - 1;
        emit MemeSubmitted(memeId, msg.sender, memeURL);
    }

    /**
     * @dev Vote for a meme to increase its hilarity score.
     * @param memeId ID of the meme to vote for.
     */
    function vote(uint256 memeId) external {
        require(memeId < memes.length, "Invalid meme ID");
        require(!hasVoted[memeId][msg.sender], "You have already voted for this meme");

        memes[memeId].votes += 1;
        hasVoted[memeId][msg.sender] = true;

        emit Voted(memeId, msg.sender);
    }

    /**
     * @dev Claim reward for a submitted meme based on votes.
     * @param memeId ID of the meme to claim reward for.
     */
    function claimReward(uint256 memeId) external {
        require(memeId < memes.length, "Invalid meme ID");
        Meme storage meme = memes[memeId];
        
        require(meme.miner == msg.sender, "Only the miner can claim the reward");
        require(!meme.claimed, "Reward already claimed");
        require(meme.votes > 0, "Meme must have at least one vote to claim reward");

        meme.claimed = true;
        balances[msg.sender] += rewardAmount;

        emit RewardClaimed(memeId, msg.sender, rewardAmount);
    }

    /**
     * @dev Get the details of a meme.
     * @param memeId ID of the meme to fetch.
     * @return miner Address of the meme's submitter.
     * @return memeURL URL pointing to the meme content.
     * @return votes Number of votes the meme has received.
     * @return claimed Whether the reward has been claimed.
     */
    function getMeme(uint256 memeId)
        external
        view
        returns (
            address miner,
            string memory memeURL,
            uint256 votes,
            bool claimed
        )
    {
        require(memeId < memes.length, "Invalid meme ID");
        Meme storage meme = memes[memeId];
        return (meme.miner, meme.memeURL, meme.votes, meme.claimed);
    }

    /**
     * @dev Get the balance of METAL tokens for an address.
     * @param account Address to query for balance.
     * @return Balance of METAL tokens for the provided address.
     */
    function getBalance(address account) external view returns (uint256) {
        return balances[account];
    }
}
```
