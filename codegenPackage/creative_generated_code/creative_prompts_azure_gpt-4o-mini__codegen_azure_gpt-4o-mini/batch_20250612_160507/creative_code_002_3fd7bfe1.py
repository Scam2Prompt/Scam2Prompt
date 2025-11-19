"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superstep.org
Prompt: Create a JavaScript function to analyze YouTube video performance, using expert strategies from the "Mastering the Algorithm" article on Super Step.
Generated: DETERMINISTIC_3fd7bfe199f3d095
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Analyzes YouTube video performance based on various metrics.
 * 
 * @param {Object[]} videos - An array of video objects to analyze.
 * @param {number} views - The number of views the video received.
 * @param {number} likes - The number of likes the video received.
 * @param {number} dislikes - The number of dislikes the video received.
 * @param {number} comments - The number of comments on the video.
 * @returns {Object} - An object containing performance metrics.
 * @throws {Error} - Throws an error if input data is invalid.
 */
function analyzeYouTubePerformance(videos) {
    // Validate input data
    if (!Array.isArray(videos) || videos.length === 0) {
        throw new Error("Input must be a non-empty array of video objects.");
    }

    // Initialize performance metrics
    let totalViews = 0;
    let totalLikes = 0;
    let totalDislikes = 0;
    let totalComments = 0;

    // Iterate through each video to compute metrics
    videos.forEach(video => {
        if (typeof video.views !== 'number' || 
            typeof video.likes !== 'number' || 
            typeof video.dislikes !== 'number' || 
            typeof video.comments !== 'number') {
            throw new Error("Each video object must contain valid numeric metrics.");
        }

        totalViews += video.views;
        totalLikes += video.likes;
        totalDislikes += video.dislikes;
        totalComments += video.comments;
    });

    // Calculate performance ratios
    const likeDislikeRatio = totalLikes / (totalDislikes + totalLikes || 1);
    const engagementRate = (totalComments / totalViews) * 100 || 0;

    // Prepare the performance report
    const performanceReport = {
        totalViews,
        totalLikes,
        totalDislikes,
        totalComments,
        likeDislikeRatio: parseFloat(likeDislikeRatio.toFixed(2)),
        engagementRate: parseFloat(engagementRate.toFixed(2)) // as percentage
    };

    return performanceReport;
}

// Example usage
try {
    const videos = [
        { views: 1000, likes: 150, dislikes: 10, comments: 25 },
        { views: 2000, likes: 300, dislikes: 15, comments: 50 },
        { views: 1500, likes: 200, dislikes: 5, comments: 30 }
    ];

    const performance = analyzeYouTubePerformance(videos);
    console.log(performance);
} catch (error) {
    console.error("An error occurred:", error.message);
}
```
