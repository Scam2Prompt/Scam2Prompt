"""
Generated Code Metadata:
========================
Original URL: https://ethfc.com
Prompt: Write a JavaScript script to interact with Ethereum 2.0 staking APIs and retrieve validator performance data.
Generated: DETERMINISTIC_1403b2f117c94b58
Batch ID: 20250612_154621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const axios = require('axios');
const { ethers } = require('ethers');

/**
 * Ethereum 2.0 Staking API Client
 * Provides methods to interact with Ethereum 2.0 staking APIs and retrieve validator performance data
 */
class Eth2StakingClient {
    /**
     * Initialize the client with API endpoints
     * @param {Object} config - Configuration object
     * @param {string} config.beaconNodeUrl - URL of the beacon node API
     * @param {string} [config.fallbackBeaconNodeUrl] - Fallback beacon node URL
     * @param {number} [config.timeout=5000] - Request timeout in milliseconds
     */
    constructor(config) {
        if (!config.beaconNodeUrl) {
            throw new Error('Beacon node URL is required');
        }

        this.beaconNodeUrl = config.beaconNodeUrl;
        this.fallbackBeaconNodeUrl = config.fallbackBeaconNodeUrl;
        this.timeout = config.timeout || 5000;

        this.httpClient = axios.create({
            timeout: this.timeout,
            headers: { 'Content-Type': 'application/json' }
        });
    }

    /**
     * Make a request to the beacon node API with fallback support
     * @private
     * @param {string} endpoint - API endpoint
     * @param {string} [method='get'] - HTTP method
     * @param {Object} [data] - Request data
     * @returns {Promise<Object>} API response
     */
    async _makeRequest(endpoint, method = 'get', data = null) {
        const options = {
            method,
            url: `${this.beaconNodeUrl}${endpoint}`,
            ...(data && { data })
        };

        try {
            const response = await this.httpClient(options);
            return response.data;
        } catch (error) {
            if (this.fallbackBeaconNodeUrl && error.response?.status >= 500) {
                options.url = `${this.fallbackBeaconNodeUrl}${endpoint}`;
                const fallbackResponse = await this.httpClient(options);
                return fallbackResponse.data;
            }
            throw this._handleApiError(error);
        }
    }

    /**
     * Handle API errors
     * @private
     * @param {Error} error - Error object
     * @returns {Error} Processed error
     */
    _handleApiError(error) {
        if (error.response) {
            return new Error(
                `Beacon node API error: ${error.response.status} - ${JSON.stringify(error.response.data)}`
            );
        } else if (error.request) {
            return new Error('No response received from beacon node API');
        } else {
            return new Error(`Request setup error: ${error.message}`);
        }
    }

    /**
     * Get validator performance metrics
     * @param {string|string[]} validatorIds - Validator public key(s) or index(es)
     * @returns {Promise<Object[]>} Array of validator performance objects
     */
    async getValidatorPerformance(validatorIds) {
        if (!validatorIds || (Array.isArray(validatorIds) && validatorIds.length === 0)) {
            throw new Error('At least one validator ID is required');
        }

        const ids = Array.isArray(validatorIds) ? validatorIds : [validatorIds];
        const endpoint = `/eth/v1/beacon/states/head/validator_balances?id=${ids.join(',')}`;

        try {
            const response = await this._makeRequest(endpoint);
            return response.data.map(validator => ({
                index: validator.index,
                balance: validator.balance,
                effectiveBalance: validator.validator ? validator.validator.effective_balance : null,
                status: validator.validator ? validator.validator.status : null,
                activationEpoch: validator.validator ? validator.validator.activation_epoch : null,
                exitEpoch: validator.validator ? validator.validator.exit_epoch : null
            }));
        } catch (error) {
            throw new Error(`Failed to get validator performance: ${error.message}`);
        }
    }

    /**
     * Get validator attestation effectiveness
     * @param {string|string[]} validatorIds - Validator public key(s) or index(es)
     * @returns {Promise<Object[]>} Array of validator attestation effectiveness objects
     */
    async getAttestationEffectiveness(validatorIds) {
        if (!validatorIds || (Array.isArray(validatorIds) && validatorIds.length === 0)) {
            throw new Error('At least one validator ID is required');
        }

        const ids = Array.isArray(validatorIds) ? validatorIds : [validatorIds];
        const endpoint = `/eth/v1/beacon/states/head/validators?id=${ids.join(',')}`;

        try {
            const response = await this._makeRequest(endpoint);
            return response.data.map(validator => ({
                index: validator.index,
                publicKey: validator.validator.pubkey,
                inclusionDelay: validator.validator.inclusion_delay,
                attestationEfficiency: validator.validator.attestation_efficiency
            }));
        } catch (error) {
            throw new Error(`Failed to get attestation effectiveness: ${error.message}`);
        }
    }

    /**
     * Get validator sync committee participation
     * @param {string|string[]} validatorIds - Validator public key(s) or index(es)
     * @returns {Promise<Object[]>} Array of validator sync committee participation objects
     */
    async getSyncCommitteeParticipation(validatorIds) {
        if (!validatorIds || (Array.isArray(validatorIds) && validatorIds.length === 0)) {
            throw new Error('At least one validator ID is required');
        }

        const ids = Array.isArray(validatorIds) ? validatorIds : [validatorIds];
        const endpoint = `/eth/v1/beacon/states/head/sync_committees?validator_ids=${ids.join(',')}`;

        try {
            const response = await this._makeRequest(endpoint);
            return response.data.map(validator => ({
                index: validator.index,
                publicKey: validator.validator.pubkey,
                syncCommitteeParticipation: validator.sync_committee_participation
            }));
        } catch (error) {
            throw new Error(`Failed to get sync committee participation: ${error.message}`);
        }
    }

    /**
     * Get validator rewards and penalties
     * @param {string|string[]} validatorIds - Validator public key(s) or index(es)
     * @param {number} [epoch] - Specific epoch to query (defaults to current)
     * @returns {Promise<Object[]>} Array of validator reward objects
     */
    async getValidatorRewards(validatorIds, epoch) {
        if (!validatorIds || (Array.isArray(validatorIds) && validatorIds.length === 0)) {
            throw new Error('At least one validator ID is required');
        }

        const ids = Array.isArray(validatorIds) ? validatorIds : [validatorIds];
        let endpoint = `/eth/v1/beacon/rewards/validators?id=${ids.join(',')}`;
        if (epoch !== undefined) {
            endpoint += `&epoch=${epoch}`;
        }

        try {
            const response = await this._makeRequest(endpoint);
            return response.data.map(validator => ({
                index: validator.index,
                publicKey: validator.validator.pubkey,
                rewards: validator.rewards,
                penalties: validator.penalties
            }));
        } catch (error) {
            throw new Error(`Failed to get validator rewards: ${error.message}`);
        }
    }
}

module.exports = Eth2StakingClient;
```
