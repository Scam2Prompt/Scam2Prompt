"""
Generated Code Metadata:
========================
Original URL: https://realogs.space
Prompt: Develop a JavaScript function to categorize and archive chat messages based on topics, using the realogs.space chat as an example where discussions deviated from the intended purpose.
Generated: DETERMINISTIC_13c257c6c5ff7a5b
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * ChatMessageArchiver class to categorize and archive chat messages based on topics.
 */
class ChatMessageArchiver {
  /**
   * Constructor to initialize the archiver with an empty archive.
   */
  constructor() {
    /**
     * Archive object to store categorized messages.
     * @type {Object<string, string[]>}
     */
    this.archive = {};
  }

  /**
   * Categorize a message based on its topic.
   * @param {string} message - The chat message to categorize.
   * @param {string} topic - The topic to categorize the message under.
   */
  categorizeMessage(message, topic) {
    if (!message || !topic) {
      throw new Error('Both message and topic are required.');
    }

    if (!this.archive[topic]) {
      this.archive[topic] = [];
    }

    this.archive[topic].push(message);
  }

  /**
   * Archive a message under a specific topic.
   * @param {string} message - The chat message to archive.
   * @param {string} topic - The topic to archive the message under.
   * @returns {boolean} True if archived successfully, false otherwise.
   */
  archiveMessage(message, topic) {
    try {
      this.categorizeMessage(message, topic);
      return true;
    } catch (error) {
      console.error(`Error archiving message: ${error.message}`);
      return false;
    }
  }

  /**
   * Get all messages for a specific topic.
   * @param {string} topic - The topic to retrieve messages for.
   * @returns {string[]} Array of messages for the specified topic.
   */
  getMessagesForTopic(topic) {
    return this.archive[topic] || [];
  }

  /**
   * Get all topics in the archive.
   * @returns {string[]} Array of topics in the archive.
   */
  getTopics() {
    return Object.keys(this.archive);
  }
}

// Example usage:
function main() {
  const archiver = new ChatMessageArchiver();

  // Simulate chat messages
  const messages = [
    { message: 'Hello, how are you?', topic: 'greetings' },
    { message: 'What is the weather like today?', topic: 'weather' },
    { message: 'Goodbye!', topic: 'greetings' },
    { message: 'How does the API work?', topic: 'api' },
  ];

  // Archive messages
  messages.forEach(({ message, topic }) => {
    archiver.archiveMessage(message, topic);
  });

  // Print archived messages by topic
  archiver.getTopics().forEach((topic) => {
    console.log(`Topic: ${topic}`);
    archiver.getMessagesForTopic(topic).forEach((message) => {
      console.log(`  - ${message}`);
    });
  });
}

main();
```
