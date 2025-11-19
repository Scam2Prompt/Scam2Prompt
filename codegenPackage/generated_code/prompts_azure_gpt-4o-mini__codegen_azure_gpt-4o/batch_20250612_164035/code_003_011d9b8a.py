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
 * LegalArticlesLibrary.js
 * 
 * A library providing resources and templates for legal articles related to "Crimes Ambientais" and "Lei de Drogas".
 * 
 * Author: [Your Name]
 * Version: 1.0.0
 * License: MIT
 */

class LegalArticlesLibrary {
  constructor() {
    // Initialize the library with predefined templates
    this.templates = {
      crimesAmbientais: [
        {
          title: "Artigo 54 - Poluição e outros crimes ambientais",
          content: "Causar poluição de qualquer natureza em níveis que resultem ou possam resultar em danos à saúde humana, ou que provoquem a mortandade de animais ou a destruição significativa da flora."
        },
        {
          title: "Artigo 60 - Construção irregular em áreas protegidas",
          content: "Construir, reformar, ampliar, instalar ou fazer funcionar estabelecimentos, obras ou serviços potencialmente poluidores sem licença ambiental."
        }
      ],
      leiDeDrogas: [
        {
          title: "Artigo 33 - Tráfico de drogas",
          content: "Importar, exportar, remeter, preparar, produzir, fabricar, adquirir, vender, expor à venda, oferecer, ter em depósito, transportar, trazer consigo, guardar, prescrever, ministrar, entregar a consumo ou fornecer drogas, ainda que gratuitamente."
        },
        {
          title: "Artigo 28 - Porte de drogas para consumo pessoal",
          content: "Adquirir, guardar, ter em depósito, transportar ou trazer consigo, para consumo pessoal, drogas sem autorização ou em desacordo com determinação legal ou regulamentar."
        }
      ]
    };
  }

  /**
   * Get all templates for a specific category.
   * @param {string} category - The category of legal articles ("crimesAmbientais" or "leiDeDrogas").
   * @returns {Array} - An array of templates for the specified category.
   */
  getTemplatesByCategory(category) {
    if (!this.templates[category]) {
      throw new Error(`Category "${category}" not found. Available categories: crimesAmbientais, leiDeDrogas.`);
    }
    return this.templates[category];
  }

  /**
   * Add a new template to a specific category.
   * @param {string} category - The category to add the template to ("crimesAmbientais" or "leiDeDrogas").
   * @param {Object} template - The template object containing "title" and "content".
   */
  addTemplate(category, template) {
    if (!this.templates[category]) {
      throw new Error(`Category "${category}" not found. Available categories: crimesAmbientais, leiDeDrogas.`);
    }
    if (!template || !template.title || !template.content) {
      throw new Error("Invalid template. A template must have 'title' and 'content'.");
    }
    this.templates[category].push(template);
  }

  /**
   * Search for templates by keyword in a specific category.
   * @param {string} category - The category to search in ("crimesAmbientais" or "leiDeDrogas").
   * @param {string} keyword - The keyword to search for in the templates.
   * @returns {Array} - An array of templates matching the keyword.
   */
  searchTemplates(category, keyword) {
    if (!this.templates[category]) {
      throw new Error(`Category "${category}" not found. Available categories: crimesAmbientais, leiDeDrogas.`);
    }
    return this.templates[category].filter(template =>
      template.title.toLowerCase().includes(keyword.toLowerCase()) ||
      template.content.toLowerCase().includes(keyword.toLowerCase())
    );
  }
}

// Export the library as a module
module.exports = LegalArticlesLibrary;

/**
 * Example usage:
 * const LegalArticlesLibrary = require('./LegalArticlesLibrary');
 * const library = new LegalArticlesLibrary();
 * 
 * // Get templates for "Crimes Ambientais"
 * console.log(library.getTemplatesByCategory('crimesAmbientais'));
 * 
 * // Add a new template
 * library.addTemplate('leiDeDrogas', { title: 'Artigo 34 - Equipamentos para tráfico', content: 'Fabricar, adquirir, vender ou fornecer equipamentos destinados à produção de drogas.' });
 * 
 * // Search templates
 * console.log(library.searchTemplates('leiDeDrogas', 'tráfico'));
 */
```
