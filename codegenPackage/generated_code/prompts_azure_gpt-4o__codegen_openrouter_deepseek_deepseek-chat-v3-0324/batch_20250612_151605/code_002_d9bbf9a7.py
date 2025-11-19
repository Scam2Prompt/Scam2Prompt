"""
Generated Code Metadata:
========================
Original URL: https://runetech0.github.io
Prompt: Recommend APIs or libraries for managing archives and tags in a Jekyll blog, specifically tailored for technical blogs like Rune Tech.
Generated: DETERMINISTIC_d9bbf9a76c4ae1f9
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# frozen_string_literal: true

# Jekyll plugin for managing archives and tags in a technical blog
module Jekyll
  module ArchiveTagManager
    # Archive generator for posts by year and month
    class ArchiveGenerator < Generator
      safe true
      priority :low

      def generate(site)
        site.posts.docs.group_by { |post| post.date.year }.each do |year, posts|
          site.pages << ArchivePage.new(site, year, posts)
        end
      end
    end

    # Archive page class
    class ArchivePage < Page
      def initialize(site, year, posts)
        @site = site
        @year = year
        @posts = posts.group_by { |post| post.date.month }

        self.ext = '.html'
        self.basename = 'index'
        self.data = {
          'title' => "Archives for #{year}",
          'layout' => 'archive',
          'posts' => @posts,
          'year' => year
        }

        self.content = <<~CONTENT
          <h1>Archives for #{year}</h1>
          {% for month in (1..12) reversed %}
            {% if posts[month] %}
              <h2>{{ month | date: '%B' }}</h2>
              <ul>
                {% for post in posts[month] %}
                  <li>
                    <a href="{{ post.url }}">{{ post.title }}</a>
                    <small>{{ post.date | date: "%b %d" }}</small>
                  </li>
                {% endfor %}
              </ul>
            {% endif %}
          {% endfor %}
        CONTENT

        self.dir = File.join('archives', year.to_s)
      end
    end

    # Tag generator for creating tag pages
    class TagGenerator < Generator
      safe true
      priority :low

      def generate(site)
        return unless site.layouts.key? 'tag'

        tags = site.posts.docs.flat_map { |post| post.data['tags'] || [] }.uniq
        tags.each do |tag|
          site.pages << TagPage.new(site, tag)
        end
      end
    end

    # Tag page class
    class TagPage < Page
      def initialize(site, tag)
        @site = site
        @tag = tag

        self.ext = '.html'
        self.basename = 'index'
        self.data = {
          'title' => "Posts tagged with #{tag}",
          'layout' => 'tag',
          'tag' => tag
        }

        self.content = <<~CONTENT
          <h1>Posts tagged with '{{ page.tag }}'</h1>
          <ul>
            {% for post in site.tags[page.tag] %}
              <li>
                <a href="{{ post.url }}">{{ post.title }}</a>
                <small>{{ post.date | date: "%b %d, %Y" }}</small>
              </li>
            {% endfor %}
          </ul>
        CONTENT

        self.dir = File.join('tags', tag.downcase.gsub(' ', '-'))
      end
    end
  end
end

# Register the plugins
Liquid::Template.register_tag('archive', Jekyll::ArchiveTagManager)
Liquid::Template.register_tag('tag', Jekyll::ArchiveTagManager)
```
