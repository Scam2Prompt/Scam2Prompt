"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://runetech0.github.io
Prompt: Recommend APIs or libraries for managing archives and tags in a Jekyll blog, specifically tailored for technical blogs like Rune Tech.
Generated: DETERMINISTIC_d9bbf9a76c4ae1f9
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# Jekyll plugin to manage archives and tags in a technical blog like Rune Tech.
# This plugin generates archive pages based on year and tag.

module Jekyll
  class ArchiveGenerator < Generator
    safe true
    priority :low

    def generate(site)
      generate_yearly_archives(site)
      generate_tag_archives(site)
    end

    # Generate archive pages for each year
    def generate_yearly_archives(site)
      posts_by_year = site.posts.docs.group_by { |post| post.date.year }

      posts_by_year.each do |year, posts|
        archive_page = ArchivePage.new(site, site.source, "archives/#{year}", "year", year, posts)
        site.pages << archive_page
      end
    end

    # Generate archive pages for each tag
    def generate_tag_archives(site)
      posts_by_tags = site.posts.docs.flat_map(&:tags).uniq.group_by do |tag|
        site.posts.docs.select { |post| post.tags.include?(tag) }
      end

      posts_by_tags.each do |tag, posts|
        archive_page = ArchivePage.new(site, site.source, "tags/#{tag}", "tag", tag, posts)
        site.pages << archive_page
      end
    end
  end

  # ArchivePage class to create a custom Jekyll page for archives
  class ArchivePage < Page
    def initialize(site, base, dir, archive_type, archive_name, posts)
      @site = site
      @base = base
      @dir = dir
      @name = "index.html" # Archive pages use index.html

      self.process(@name) # Set up file name and extension
      self.read_yaml(File.join(base, '_layouts'), 'archive.html') # Use archive layout
      self.data['title'] = "#{archive_type.capitalize}: #{archive_name}" # Page title
      self.data['posts'] = posts # Pass posts to the page
      self.data['archive_type'] = archive_type # Type of archive (year/tag)
      self.data['archive_name'] = archive_name # Name of the archive (year/tag name)
    end
  end
end

# Error handling: Ensure the required variables are present
# Ensure 'archive.html' layout exists in `_layouts` folder.
raise "Missing 'archive.html' layout in `_layouts` folder!" unless File.exist?("_layouts/archive.html")

# Usage:
# 1. Place this file in the `_plugins` directory of your Jekyll project.
# 2. Create an `archive.html` layout in `_layouts` that uses `page.posts`.
# 3. Run `jekyll build` or `jekyll serve` to generate archives automatically.

# Note:
# Customize the `archive.html` layout to display posts for the archive.
```
