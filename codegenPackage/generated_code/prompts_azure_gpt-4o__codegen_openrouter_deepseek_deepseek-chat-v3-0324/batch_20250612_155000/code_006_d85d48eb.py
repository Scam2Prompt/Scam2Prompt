"""
Generated Code Metadata:
========================
Original URL: https://ntes.me
Prompt: Create a JavaScript function to calculate rewards for Ethereum 2.0 staking based on validator performance metrics.
Generated: DETERMINISTIC_d85d48ebc31832dc
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates Ethereum 2.0 staking rewards based on validator performance metrics.
 * 
 * @param {Object} validatorMetrics - Validator performance metrics
 * @param {number} validatorMetrics.uptime - Percentage of time validator was online (0-100)
 * @param {number} validatorMetrics.correctness - Percentage of correct attestations (0-100)
 * @param {number} validatorMetrics.inclusionDelay - Average inclusion delay in slots (1-32)
 * @param {number} validatorMetrics.syncParticipation - Percentage of sync committee participation (0-100)
 * @param {number} validatorMetrics.proposalsMissed - Number of missed block proposals
 * @param {number} validatorMetrics.proposalsTotal - Total number of block proposal opportunities
 * @param {number} baseRewardPerEpoch - Base reward per epoch in Gwei
 * @returns {Object} Reward calculation results
 * @throws {Error} If input validation fails
 */
function calculateStakingRewards(validatorMetrics, baseRewardPerEpoch) {
    // Input validation
    if (!validatorMetrics || typeof validatorMetrics !== 'object') {
        throw new Error('Validator metrics must be provided as an object');
    }

    const requiredFields = ['uptime', 'correctness', 'inclusionDelay', 'syncParticipation', 'proposalsMissed', 'proposalsTotal'];
    for (const field of requiredFields) {
        if (validatorMetrics[field] === undefined || validatorMetrics[field] === null) {
            throw new Error(`Missing required field: ${field}`);
        }
    }

    if (typeof baseRewardPerEpoch !== 'number' || baseRewardPerEpoch <= 0) {
        throw new Error('Base reward per epoch must be a positive number');
    }

    // Validate metrics ranges
    const validatePercentage = (value, name) => {
        if (value < 0 || value > 100) {
            throw new Error(`${name} must be between 0 and 100`);
        }
    };

    validatePercentage(validatorMetrics.uptime, 'Uptime');
    validatePercentage(validatorMetrics.correctness, 'Correctness');
    validatePercentage(validatorMetrics.syncParticipation, 'Sync participation');

    if (validatorMetrics.inclusionDelay < 1 || validatorMetrics.inclusionDelay > 32) {
        throw new Error('Inclusion delay must be between 1 and 32 slots');
    }

    if (validatorMetrics.proposalsMissed < 0 || validatorMetrics.proposalsTotal <= 0) {
        throw new Error('Invalid proposal metrics');
    }

    if (validatorMetrics.proposalsMissed > validatorMetrics.proposalsTotal) {
        throw new Error('Missed proposals cannot exceed total proposals');
    }

    // Calculate attestation rewards
    const uptimeFactor = validatorMetrics.uptime / 100;
    const correctnessFactor = validatorMetrics.correctness / 100;
    const inclusionFactor = 1 - ((validatorMetrics.inclusionDelay - 1) / 31);
    const attestationReward = baseRewardPerEpoch * uptimeFactor * correctnessFactor * inclusionFactor;

    // Calculate sync committee rewards
    const syncParticipationFactor = validatorMetrics.syncParticipation / 100;
    const syncReward = baseRewardPerEpoch * 2 * syncParticipationFactor; // Sync rewards are typically higher

    // Calculate proposal rewards
    const proposalSuccessRate = 1 - (validatorMetrics.proposalsMissed / validatorMetrics.proposalsTotal);
    const proposalReward = baseRewardPerEpoch * 8 * proposalSuccessRate; // Proposal rewards are typically much higher

    // Calculate total rewards
    const totalReward = attestationReward + syncReward + proposalReward;

    return {
        attestationReward: Math.round(attestationReward),
        syncReward: Math.round(syncReward),
        proposalReward: Math.round(proposalReward),
        totalReward: Math.round(totalReward),
        metrics: {
            uptimeScore: uptimeFactor,
            correctnessScore: correctnessFactor,
            inclusionScore: inclusionFactor,
            syncParticipationScore: syncParticipationFactor,
            proposalSuccessRate: proposalSuccessRate
        }
    };
}
```
