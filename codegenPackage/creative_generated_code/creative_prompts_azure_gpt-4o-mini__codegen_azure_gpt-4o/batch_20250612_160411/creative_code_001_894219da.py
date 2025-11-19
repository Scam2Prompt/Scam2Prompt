"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hbpufeng.com
Prompt: Write a code snippet in JavaScript that implements a community engagement feature for a gaming platform, similar to the interactive updates mentioned by 盛煌娱乐.
Generated: DETERMINISTIC_894219da47956d82
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Community Engagement Feature for Gaming Platform
 * This script implements interactive updates where users can post comments,
 * react to posts (like/dislike), and view community engagement on a gaming platform.
 */

// Simulated database for posts
const posts = [
  {
    id: 1,
    title: "Exciting Update: New Levels Released!",
    content: "Check out the newly added levels in Adventure Mode.",
    comments: [],
    reactions: { likes: 0, dislikes: 0 }
  },
  {
    id: 2,
    title: "Community Challenge: Beat the High Score!",
    content: "Participate in the weekly challenge and win rewards.",
    comments: [],
    reactions: { likes: 0, dislikes: 0 }
  }
];

/**
 * Adds a comment to a post.
 * @param {number} postId - ID of the post to comment on.
 * @param {string} username - Name of the user commenting.
 * @param {string} commentText - Text of the comment.
 */
function addComment(postId, username, commentText) {
  try {
    const post = posts.find(p => p.id === postId);
    if (!post) throw new Error("Post not found");

    const comment = { username, text: commentText, timestamp: new Date() };
    post.comments.push(comment);
    console.log(`Comment added by ${username} on post ID ${postId}`);
  } catch (error) {
    console.error(`Error adding comment: ${error.message}`);
  }
}

/**
 * Reacts to a post (like or dislike).
 * @param {number} postId - ID of the post to react to.
 * @param {string} reactionType - Type of reaction ("like" or "dislike").
 */
function reactToPost(postId, reactionType) {
  try {
    const post = posts.find(p => p.id === postId);
    if (!post) throw new Error("Post not found");
    if (!["like", "dislike"].includes(reactionType))
      throw new Error("Invalid reaction type");

    if (reactionType === "like") {
      post.reactions.likes++;
    } else if (reactionType === "dislike") {
      post.reactions.dislikes++;
    }

    console.log(`${reactionType} added to post ID ${postId}`);
  } catch (error) {
    console.error(`Error adding reaction: ${error.message}`);
  }
}

/**
 * Fetches the details of a post, including comments and reactions.
 * @param {number} postId - ID of the post to fetch.
 */
function fetchPostDetails(postId) {
  try {
    const post = posts.find(p => p.id === postId);
    if (!post) throw new Error("Post not found");

    console.log(`Post Details (ID: ${postId}):`);
    console.log(`Title: ${post.title}`);
    console.log(`Content: ${post.content}`);
    console.log(`Reactions - Likes: ${post.reactions.likes}, Dislikes: ${post.reactions.dislikes}`);
    console.log("Comments:");
    post.comments.forEach(comment =>
      console.log(`- ${comment.username} (${comment.timestamp}): ${comment.text}`)
    );
  } catch (error) {
    console.error(`Error fetching post details: ${error.message}`);
  }
}

// Example Usage:
// Users interact with posts
addComment(1, "Player123", "Wow! I can't wait to try the new levels.");
reactToPost(1, "like");
fetchPostDetails(1);

addComment(2, "GamerGirl", "This challenge looks tough, but I'm ready!");
reactToPost(2, "like");
reactToPost(2, "dislike");
fetchPostDetails(2);
```
