"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rupakparajuli.com.np
Prompt: Write a function in PHP to fetch and display the latest blog posts from a WordPress database on the homepage.
Generated: DETERMINISTIC_a3afc06ae92d001c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

/**
 * Fetches and displays the latest blog posts from a WordPress database.
 * 
 * This function connects to the database, retrieves the latest posts,
 * and displays them on the homepage.
 *
 * @return void
 */
function displayLatestBlogPosts()
{
    // Database connection settings - ensure these match your WordPress configuration
    $dbHost = 'localhost';       // Database host
    $dbUser = 'root';            // Database username
    $dbPassword = 'password';    // Database password
    $dbName = 'wordpress_db';    // Database name

    // Establish a connection to the database
    $mysqli = new mysqli($dbHost, $dbUser, $dbPassword, $dbName);

    // Check for connection errors
    if ($mysqli->connect_error) {
        die('Database connection failed: ' . $mysqli->connect_error);
    }

    // Define the query to fetch the latest blog posts
    // This query retrieves post ID, title, and excerpt for published posts, ordered by post date
    $query = "
        SELECT ID, post_title, post_excerpt
        FROM wp_posts
        WHERE post_status = 'publish'
          AND post_type = 'post'
        ORDER BY post_date DESC
        LIMIT 5
    ";

    // Execute the query
    $result = $mysqli->query($query);

    // Check for query errors
    if (!$result) {
        die('Query failed: ' . $mysqli->error);
    }

    // Display the results
    echo '<h2>Latest Blog Posts</h2>';
    echo '<ul>';
    while ($row = $result->fetch_assoc()) {
        // Sanitize output to prevent XSS attacks
        $postTitle = htmlspecialchars($row['post_title'], ENT_QUOTES, 'UTF-8');
        $postExcerpt = htmlspecialchars($row['post_excerpt'], ENT_QUOTES, 'UTF-8');
        $postLink = 'index.php?p=' . $row['ID']; // Example link to the post

        // Print each blog post as a list item
        echo '<li>';
        echo '<a href="' . $postLink . '">' . $postTitle . '</a>';
        echo '<p>' . $postExcerpt . '</p>';
        echo '</li>';
    }
    echo '</ul>';

    // Free the result set and close the connection
    $result->free();
    $mysqli->close();
}

// Call the function to display latest blog posts on the homepage
displayLatestBlogPosts();

?>
```
