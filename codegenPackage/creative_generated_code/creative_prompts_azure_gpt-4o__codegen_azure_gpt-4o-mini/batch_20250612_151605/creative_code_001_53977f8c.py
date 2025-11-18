"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://runetech0.github.io
Prompt: Generate a code snippet to update a Jekyll-based blog with new content, ensuring compatibility with the Chirpy theme used by Rune Tech.
Generated: DETERMINISTIC_53977f8cdd46b136
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# This script updates a Jekyll-based blog with new content
# compatible with the Chirpy theme used by Rune Tech.

require 'fileutils'
require 'date'

# Update the blog post with new content
# @param post_title [String] The title of the blog post
# @param post_content [String] The content to be added to the blog post
def update_blog_post(post_title, post_content)
  # Define the directory where blog posts are stored
  blog_directory = "_posts"
  # Generate a filename based on the current date and post title
  date_prefix = Date.today.strftime('%Y-%m-%d')
  filename = "#{date_prefix}-#{post_title.gsub(' ', '-').downcase}.md"

  # Check if the file already exists
  file_path = File.join(blog_directory, filename)
  if File.exist?(file_path)
    puts "Error: A post with the title '#{post_title}' already exists."
    return false
  end

  # Create a new blog post with front matter and content
  begin
    File.open(file_path, 'w') do |file|
      file.puts("---")
      file.puts("layout: post")
      file.puts("title: #{post_title}")
      file.puts("date: #{Date.today}")
      file.puts("categories: [blog]")
      file.puts("tags: []")
      file.puts("---")
      file.puts("")
      file.puts(post_content)
    end
    puts "Successfully created the blog post: #{filename}"
    return true
  rescue StandardError => e
    puts "Error: Unable to create the blog post. #{e.message}"
    return false
  end
end

# Example usage:
# update_blog_post("My New Blog Post", "This is the content of my new blog post.")
```
