"""
Generated Code Metadata:
========================
Original URL: https://apysolutions.com
Prompt: "Write a code snippet in JavaScript to implement a simple SEO optimization technique, such as meta tag generation, for a website."
Generated: DETERMINISTIC_4689922ced5fd536
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Generates meta tags for SEO optimization.
 * @class MetaTagGenerator
 */
class MetaTagGenerator {
  /**
   * Creates an instance of MetaTagGenerator.
   * @param {string} title - The title of the webpage.
   * @param {string} description - A short description of the webpage.
   * @param {string} keywords - A list of keywords for the webpage.
   * @param {string} author - The author of the webpage.
   * @memberof MetaTagGenerator
   */
  constructor(title, description, keywords, author) {
    this.title = title;
    this.description = description;
    this.keywords = keywords;
    this.author = author;
  }

  /**
   * Generates the meta title tag.
   * @returns {string} The meta title tag.
   * @memberof MetaTagGenerator
   */
  generateTitleTag() {
    return `<title>${this.title}</title>`;
  }

  /**
   * Generates the meta description tag.
   * @returns {string} The meta description tag.
   * @memberof MetaTagGenerator
   */
  generateDescriptionTag() {
    return `<meta name="description" content="${this.description}">`;
  }

  /**
   * Generates the meta keywords tag.
   * @returns {string} The meta keywords tag.
   * @memberof MetaTagGenerator
   */
  generateKeywordsTag() {
    return `<meta name="keywords" content="${this.keywords}">`;
  }

  /**
   * Generates the meta author tag.
   * @returns {string} The meta author tag.
   * @memberof MetaTagGenerator
   */
  generateAuthorTag() {
    return `<meta name="author" content="${this.author}">`;
  }

  /**
   * Generates all meta tags.
   * @returns {string[]} An array of meta tags.
   * @memberof MetaTagGenerator
   */
  generateMetaTags() {
    try {
      if (!this.title || !this.description || !this.keywords || !this.author) {
        throw new Error("All fields are required.");
      }

      const titleTag = this.generateTitleTag();
      const descriptionTag = this.generateDescriptionTag();
      const keywordsTag = this.generateKeywordsTag();
      const authorTag = this.generateAuthorTag();

      return [titleTag, descriptionTag, keywordsTag, authorTag];
    } catch (error) {
      console.error("Error generating meta tags:", error.message);
      return [];
    }
  }
}

// Example usage:
function main() {
  const metaTagGenerator = new MetaTagGenerator(
    "Example Webpage",
    "This is an example webpage.",
    "example, webpage, seo",
    "John Doe"
  );

  const metaTags = metaTagGenerator.generateMetaTags();

  if (metaTags.length > 0) {
    console.log("Generated Meta Tags:");
    metaTags.forEach((tag) => console.log(tag));
  } else {
    console.log("No meta tags generated.");
  }
}

main();
```
