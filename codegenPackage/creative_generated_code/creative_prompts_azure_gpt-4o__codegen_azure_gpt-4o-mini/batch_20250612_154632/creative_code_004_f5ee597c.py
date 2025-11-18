"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloud.barchin.com
Prompt: Generate code to enable JavaScript-based session management for a Nextcloud application.
Generated: DETERMINISTIC_f5ee597c055889f1
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// sessionManager.js

/**
 * Session Manager for Nextcloud Application
 * This module handles user sessions, including creation, retrieval, and destruction of sessions.
 */

class SessionManager {
    constructor() {
        this.sessions = new Map(); // Store sessions in a Map for easy access
    }

    /**
     * Create a new session for a user
     * @param {string} userId - The ID of the user
     * @returns {string} sessionId - The unique ID of the created session
     */
    createSession(userId) {
        if (!userId) {
            throw new Error('User ID is required to create a session');
        }

        const sessionId = this.generateSessionId();
        const expirationTime = Date.now() + this.getSessionExpiration();
        
        this.sessions.set(sessionId, { userId, expirationTime });
        return sessionId;
    }

    /**
     * Retrieve session data by session ID
     * @param {string} sessionId - The ID of the session
     * @returns {Object|null} sessionData - The session data or null if not found
     */
    getSession(sessionId) {
        const sessionData = this.sessions.get(sessionId);
        
        if (sessionData) {
            // Check if the session is expired
            if (Date.now() > sessionData.expirationTime) {
                this.sessions.delete(sessionId); // Remove expired session
                return null;
            }
            return sessionData;
        }
        return null; // Session not found
    }

    /**
     * Destroy a session by session ID
     * @param {string} sessionId - The ID of the session
     * @returns {boolean} - Returns true if the session was destroyed, false otherwise
     */
    destroySession(sessionId) {
        return this.sessions.delete(sessionId);
    }

    /**
     * Generate a unique session ID
     * @returns {string} - Unique session ID
     */
    generateSessionId() {
        return 'sess_' + Math.random().toString(36).substr(2, 9); // Simple random ID generation
    }

    /**
     * Get the session expiration time (default is 30 minutes)
     * @returns {number} - Expiration time in milliseconds
     */
    getSessionExpiration() {
        return 30 * 60 * 1000; // 30 minutes
    }
}

// Example usage:
try {
    const sessionManager = new SessionManager();
    const sessionId = sessionManager.createSession('user123');
    console.log(`Session Created: ${sessionId}`);
    
    const sessionData = sessionManager.getSession(sessionId);
    console.log('Session Data:', sessionData);
    
    const isDestroyed = sessionManager.destroySession(sessionId);
    console.log(`Session Destroyed: ${isDestroyed}`);
} catch (error) {
    console.error('Error:', error.message);
}

export default SessionManager;
```
