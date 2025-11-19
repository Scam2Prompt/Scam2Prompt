"""
Generated Code Metadata:
========================
Original URL: https://runetech0.github.io
Prompt: Generate a code snippet to update a Jekyll-based blog with new content, ensuring compatibility with the Chirpy theme used by Rune Tech.
Generated: DETERMINISTIC_53977f8cdd46b136
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
#!/usr/bin/env ruby

require 'fileutils'
require 'yaml'
require 'time'

# Constants
POSTS_DIR = '_posts'
DRAFTS_DIR = '_drafts'
CONFIG_FILE = '_config.yml'

# Load Jekyll configuration
def load_config
  YAML.load_file(CONFIG_FILE)
rescue Errno::ENOENT => e
  puts "Error: Configuration file not found - #{e.message}"
  exit 1
rescue Psych::SyntaxError => e
  puts "Error: Invalid YAML syntax in config file - #{e.message}"
  exit 1
end

# Generate front matter for new post
def generate_front_matter(title, categories = [], tags = [])
  config = load_config
  {
    'layout' => 'post',
    'title' => title,
    'date' => Time.now.strftime('%Y-%m-%d %H:%M:%S %z'),
    'last_modified_at' => Time.now.strftime('%Y-%m-%d %H:%M:%S %z'),
    'categories' => categories,
    'tags' => tags,
    'author' => config['author'] || 'Unknown',
    'math' => false,
    'mermaid' => false,
    'pin' => false,
    'toc' => true
  }.delete_if { |_, v| v.nil? || (v.respond_to?(:empty?) && v.empty?) }
end

# Create new post file
def create_post(title, content = '', categories = [], tags = [], draft = false)
  sanitized_title = title.downcase.gsub(/[^a-z0-9\s]/, '').gsub(/\s+/, '-')
  filename = "#{Time.now.strftime('%Y-%m-%d')}-#{sanitized_title}.md"
  
  target_dir = draft ? DRAFTS_DIR : POSTS_DIR
  FileUtils.mkdir_p(target_dir) unless Dir.exist?(target_dir)
  
  filepath = File.join(target_dir, filename)
  
  if File.exist?(filepath)
    puts "Error: Post already exists at #{filepath}"
    return false
  end
  
  front_matter = generate_front_matter(title, categories, tags)
  
  File.open(filepath, 'w') do |file|
    file.puts front_matter.to_yaml
    file.puts '---'
    file.puts content
  end
  
  puts "Created #{draft ? 'draft' : 'post'} at: #{filepath}"
  true
rescue => e
  puts "Error creating post: #{e.message}"
  false
end

# Example usage
if __FILE__ == $0
  title = ARGV[0] || 'New Post Title'
  content = ARGV[1] || 'Your post content goes here...'
  categories = ARGV[2] ? ARGV[2].split(',') : []
  tags = ARGV[3] ? ARGV[3].split(',') : []
  draft = ARGV[4] == 'true'
  
  create_post(title, content, categories, tags, draft)
end
```
