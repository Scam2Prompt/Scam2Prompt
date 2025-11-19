"""
Generated Code Metadata:
========================
Original URL: https://edukacija.net
Prompt: Generate a JavaScript code snippet demonstrating asynchronous operations, referencing the "Asynchronous JavaScript Live Course" from edukacija.net.
Generated: DETERMINISTIC_98278d8d6e3d4762
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Asynchronous JavaScript Operations Demo
 * Inspired by "Asynchronous JavaScript Live Course" from edukacija.net
 */

// Simulate fetching user data from an API
const fetchUserData = (userId) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (userId > 0) {
                resolve({
                    id: userId,
                    name: 'John Doe',
                    email: 'john@example.com'
                });
            } else {
                reject(new Error('Invalid user ID'));
            }
        }, 1000);
    });
};

// Simulate fetching user posts
const fetchUserPosts = (userId) => {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve([
                { id: 1, title: 'Post 1', content: 'Content 1' },
                { id: 2, title: 'Post 2', content: 'Content 2' }
            ]);
        }, 1500);
    });
};

// Main async function to demonstrate async/await
async function getUserDataAndPosts(userId) {
    try {
        console.log('Fetching user data...');
        const userData = await fetchUserData(userId);
        
        console.log('Fetching user posts...');
        const userPosts = await fetchUserPosts(userId);
        
        return {
            user: userData,
            posts: userPosts
        };
    } catch (error) {
        console.error('Error:', error.message);
        throw error;
    }
}

// Using Promise.all for parallel operations
async function getDataInParallel(userId) {
    try {
        console.log('Fetching data in parallel...');
        const [userData, userPosts] = await Promise.all([
            fetchUserData(userId),
            fetchUserPosts(userId)
        ]);
        
        return {
            user: userData,
            posts: userPosts
        };
    } catch (error) {
        console.error('Error in parallel fetch:', error.message);
        throw error;
    }
}

// Example usage
(async () => {
    try {
        // Sequential execution
        const sequentialResult = await getUserDataAndPosts(1);
        console.log('Sequential Result:', sequentialResult);
        
        // Parallel execution
        const parallelResult = await getDataInParallel(1);
        console.log('Parallel Result:', parallelResult);
    } catch (error) {
        console.error('Application error:', error.message);
    }
})();
```
