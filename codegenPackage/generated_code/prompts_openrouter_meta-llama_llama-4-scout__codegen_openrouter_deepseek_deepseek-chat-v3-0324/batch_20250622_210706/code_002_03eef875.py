"""
Generated Code Metadata:
========================
Original URL: https://xiaoniao120.buzz
Prompt: "Write a JavaScript function to create a tag cloud or keyword filter for an adult content website, inspired by the categories and tags found on 小鸟酱.xyz."
Generated: DETERMINISTIC_03eef8755290b081
Batch ID: 20250622_210706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * TagCloudGenerator - Creates a tag cloud for adult content filtering
 * @param {Object} options - Configuration options
 * @param {string} options.containerId - ID of the container element
 * @param {Array} options.tags - Array of tag objects {name: string, count: number, category: string}
 * @param {number} options.maxFontSize - Maximum font size in pixels
 * @param {number} options.minFontSize - Minimum font size in pixels
 * @param {Function} options.onTagClick - Callback when a tag is clicked
 */
class TagCloudGenerator {
  constructor(options) {
    this.validateOptions(options);
    this.container = document.getElementById(options.containerId);
    this.tags = options.tags;
    this.maxFontSize = options.maxFontSize || 32;
    this.minFontSize = options.minFontSize || 12;
    this.onTagClick = options.onTagClick || (() => {});
    this.categories = {};
    
    if (!this.container) {
      throw new Error(`Container element with ID '${options.containerId}' not found`);
    }
    
    this.processTags();
    this.render();
  }

  validateOptions(options) {
    if (!options || typeof options !== 'object') {
      throw new Error('Options must be an object');
    }
    if (!options.containerId || typeof options.containerId !== 'string') {
      throw new Error('containerId must be a string');
    }
    if (!Array.isArray(options.tags)) {
      throw new Error('tags must be an array');
    }
  }

  processTags() {
    // Calculate min and max counts for normalization
    const counts = this.tags.map(tag => tag.count);
    const maxCount = Math.max(...counts);
    const minCount = Math.min(...counts);
    
    // Group tags by category
    this.tags.forEach(tag => {
      if (!this.categories[tag.category]) {
        this.categories[tag.category] = [];
      }
      
      // Calculate font size based on popularity
      const fontSize = this.calculateFontSize(tag.count, minCount, maxCount);
      this.categories[tag.category].push({
        ...tag,
        fontSize
      });
    });
  }

  calculateFontSize(count, minCount, maxCount) {
    if (maxCount === minCount) return (this.maxFontSize + this.minFontSize) / 2;
    
    const normalized = (count - minCount) / (maxCount - minCount);
    return Math.round(this.minFontSize + (normalized * (this.maxFontSize - this.minFontSize)));
  }

  render() {
    this.container.innerHTML = '';
    
    // Create category sections
    for (const [category, tags] of Object.entries(this.categories)) {
      const categorySection = document.createElement('div');
      categorySection.className = 'tag-category';
      
      const categoryTitle = document.createElement('h3');
      categoryTitle.textContent = category;
      categorySection.appendChild(categoryTitle);
      
      const tagContainer = document.createElement('div');
      tagContainer.className = 'tag-container';
      
      tags.forEach(tag => {
        const tagElement = document.createElement('span');
        tagElement.className = 'tag';
        tagElement.textContent = tag.name;
        tagElement.style.fontSize = `${tag.fontSize}px`;
        tagElement.style.margin = '0 5px';
        tagElement.style.cursor = 'pointer';
        tagElement.style.display = 'inline-block';
        tagElement.style.padding = '2px 8px';
        tagElement.style.borderRadius = '3px';
        tagElement.style.backgroundColor = '#f0f0f0';
        
        tagElement.addEventListener('click', () => {
          this.onTagClick(tag);
        });
        
        tagContainer.appendChild(tagElement);
      });
      
      categorySection.appendChild(tagContainer);
      this.container.appendChild(categorySection);
    }
  }

  /**
   * Update tags and re-render the cloud
   * @param {Array} newTags - New array of tags
   */
  updateTags(newTags) {
    this.tags = newTags;
    this.categories = {};
    this.processTags();
    this.render();
  }
}

// Example usage:
/*
const tags = [
  { name: 'Asian', count: 45, category: 'Ethnicity' },
  { name: 'Japanese', count: 38, category: 'Ethnicity' },
  { name: 'Chinese', count: 32, category: 'Ethnicity' },
  { name: 'Amateur', count: 28, category: 'Production' },
  { name: 'Professional', count: 22, category: 'Production' },
  { name: 'HD', count: 50, category: 'Quality' },
  { name: '4K', count: 18, category: 'Quality' },
  { name: 'Blonde', count: 25, category: 'Appearance' },
  { name: 'Brunette', count: 30, category: 'Appearance' },
];

const tagCloud = new TagCloudGenerator({
  containerId: 'tag-cloud-container',
  tags: tags,
  maxFontSize: 32,
  minFontSize: 12,
  onTagClick: (tag) => {
    console.log('Tag clicked:', tag);
    // Implement filtering logic here
  }
});
*/
```
