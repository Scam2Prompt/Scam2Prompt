"""
Generated Code Metadata:
========================
Original URL: https://sardagnapoeta.com.br
Prompt: Develop a library in JavaScript that provides resources and templates for legal articles related to "Crimes Ambientais" and "Lei de Drogas."
Generated: DETERMINISTIC_011d9b8a71a18d4c
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * LegalArticlesLibrary - A library for managing legal articles related to "Crimes Ambientais" and "Lei de Drogas".
 * 
 * @module LegalArticlesLibrary
 */

class LegalArticlesLibrary {
    constructor() {
        this.articles = [];
    }

    /**
     * Adds a new legal article to the library.
     * 
     * @param {Object} article - The article to be added.
     * @param {string} article.title - The title of the article.
     * @param {string} article.content - The content of the article.
     * @param {string} article.category - The category of the article (e.g., "Crimes Ambientais", "Lei de Drogas").
     * @throws {Error} Throws an error if the article is missing required fields.
     */
    addArticle(article) {
        if (!article.title || !article.content || !article.category) {
            throw new Error('Article must have a title, content, and category.');
        }
        this.articles.push(article);
    }

    /**
     * Retrieves all articles in the library.
     * 
     * @returns {Array} An array of all articles.
     */
    getAllArticles() {
        return this.articles;
    }

    /**
     * Retrieves articles by category.
     * 
     * @param {string} category - The category to filter articles by.
     * @returns {Array} An array of articles that belong to the specified category.
     * @throws {Error} Throws an error if the category is not provided.
     */
    getArticlesByCategory(category) {
        if (!category) {
            throw new Error('Category must be provided.');
        }
        return this.articles.filter(article => article.category === category);
    }

    /**
     * Updates an existing article by title.
     * 
     * @param {string} title - The title of the article to update.
     * @param {Object} updatedArticle - The updated article data.
     * @throws {Error} Throws an error if the article is not found or if required fields are missing.
     */
    updateArticle(title, updatedArticle) {
        const index = this.articles.findIndex(article => article.title === title);
        if (index === -1) {
            throw new Error('Article not found.');
        }
        if (!updatedArticle.title || !updatedArticle.content || !updatedArticle.category) {
            throw new Error('Updated article must have a title, content, and category.');
        }
        this.articles[index] = { ...this.articles[index], ...updatedArticle };
    }

    /**
     * Deletes an article by title.
     * 
     * @param {string} title - The title of the article to delete.
     * @throws {Error} Throws an error if the article is not found.
     */
    deleteArticle(title) {
        const index = this.articles.findIndex(article => article.title === title);
        if (index === -1) {
            throw new Error('Article not found.');
        }
        this.articles.splice(index, 1);
    }
}

// Example usage
const legalLibrary = new LegalArticlesLibrary();

try {
    legalLibrary.addArticle({
        title: 'Impact of Environmental Crimes',
        content: 'This article discusses the impact of environmental crimes...',
        category: 'Crimes Ambientais'
    });

    legalLibrary.addArticle({
        title: 'Understanding Drug Laws',
        content: 'This article provides an overview of drug laws...',
        category: 'Lei de Drogas'
    });

    console.log(legalLibrary.getAllArticles());
    console.log(legalLibrary.getArticlesByCategory('Crimes Ambientais'));

    legalLibrary.updateArticle('Impact of Environmental Crimes', {
        content: 'Updated content discussing the impact of environmental crimes...'
    });

    legalLibrary.deleteArticle('Understanding Drug Laws');
} catch (error) {
    console.error('Error:', error.message);
}
```
