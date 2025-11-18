"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.defily.pro
Prompt: Create a JavaScript-based solution to enable ETH mining pool management, referencing the requirements mentioned on Defily.pro.
Generated: DETERMINISTIC_efc4bb10f9a07b4f
Batch ID: 20250612_154847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ETH Mining Pool Management System

class MiningPool {
    constructor(name, owner) {
        this.name = name;
        this.owner = owner;
        this.workers = [];
        this.totalHashRate = 0;
        this.totalRewards = 0;
    }

    /**
     * Adds a worker to the mining pool
     * @param {string} workerId - Unique identifier for the worker
     * @param {number} hashRate - The hash rate of the worker in MH/s
     * @throws Will throw an error if the worker already exists
     */
    addWorker(workerId, hashRate) {
        if (this.workers.find(worker => worker.id === workerId)) {
            throw new Error(`Worker with ID ${workerId} already exists.`);
        }
        this.workers.push({ id: workerId, hashRate });
        this.totalHashRate += hashRate;
        console.log(`Worker ${workerId} added with hash rate: ${hashRate} MH/s`);
    }

    /**
     * Removes a worker from the mining pool
     * @param {string} workerId - Unique identifier for the worker
     * @throws Will throw an error if the worker does not exist
     */
    removeWorker(workerId) {
        const workerIndex = this.workers.findIndex(worker => worker.id === workerId);
        if (workerIndex === -1) {
            throw new Error(`Worker with ID ${workerId} does not exist.`);
        }
        this.totalHashRate -= this.workers[workerIndex].hashRate;
        this.workers.splice(workerIndex, 1);
        console.log(`Worker ${workerId} removed`);
    }

    /**
     * Distributes rewards to all workers based on their hash rate
     * @param {number} totalRewards - Total rewards to be distributed
     * @throws Will throw an error if totalRewards is non-positive
     */
    distributeRewards(totalRewards) {
        if (totalRewards <= 0) {
            throw new Error("Total rewards must be a positive number.");
        }
        
        this.totalRewards += totalRewards;
        this.workers.forEach(worker => {
            const workerShare = (worker.hashRate / this.totalHashRate) * totalRewards;
            console.log(`Worker ${worker.id} receives: ${workerShare}`);
        });
    }

    /**
     * Displays the mining pool status
     */
    displayStatus() {
        console.log(`Mining Pool: ${this.name}`);
        console.log(`Owner: ${this.owner}`);
        console.log(`Total Hash Rate: ${this.totalHashRate} MH/s`);
        console.log(`Total Rewards Distributed: ${this.totalRewards}`);
        console.log("Workers:");
        this.workers.forEach(worker => {
            console.log(`- Worker ID: ${worker.id}, Hash Rate: ${worker.hashRate} MH/s`);
        });
    }
}

// Example Usage
try {
    const myMiningPool = new MiningPool('MyETHPool', 'Alice');

    // Adding workers
    myMiningPool.addWorker('worker1', 100);
    myMiningPool.addWorker('worker2', 150);

    // Displaying pool status
    myMiningPool.displayStatus();

    // Distributing rewards
    myMiningPool.distributeRewards(300);

    // Removing a worker
    myMiningPool.removeWorker('worker1');

    // Displaying updated pool status
    myMiningPool.displayStatus();
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
