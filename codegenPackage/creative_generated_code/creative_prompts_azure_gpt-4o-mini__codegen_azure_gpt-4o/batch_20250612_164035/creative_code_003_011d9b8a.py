"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sardagnapoeta.com.br
Prompt: Develop a library in JavaScript that provides resources and templates for legal articles related to "Crimes Ambientais" and "Lei de Drogas."
Generated: DETERMINISTIC_011d9b8a71a18d4c
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * LegalResources Library
 * Provides resources and templates for legal articles related to "Crimes Ambientais" and "Lei de Drogas".
 *
 * This library is designed to be easily extensible and reusable.
 * It includes templates for generating legal documents and articles with appropriate error handling.
 */

// Define the LegalResources module
const LegalResources = (() => {
  // Private data: Legal templates
  const templates = {
    crimesAmbientais: `
      <h1>Crimes Ambientais</h1>
      <p>
        Os crimes ambientais estão regulados pela Lei nº 9.605/1998,
        conhecida como <strong>Lei de Crimes Ambientais</strong>. Esta legislação estabelece
        sanções penais e administrativas derivadas de condutas e atividades
        lesivas ao meio ambiente.
      </p>
      <p>
        Exemplos de crimes ambientais incluem desmatamento ilegal, poluição,
        tráfico de animais silvestres e pesca predatória.
      </p>
    `,
    leiDeDrogas: `
      <h1>Lei de Drogas</h1>
      <p>
        A Lei nº 11.343/2006, conhecida como <strong>Lei de Drogas</strong>, regula as
        políticas públicas sobre prevenção ao uso de drogas e estabelece normas
        para repressão à produção não autorizada e tráfico de substâncias ilícitas.
      </p>
      <p>
        Esta lei também define diferenças nas penalidades para usuários e
        traficantes, buscando um equilíbrio entre prevenção e punição.
      </p>
    `,
  };

  // Public methods
  return {
    /**
     * Get a legal article template by key.
     * @param {string} key - The key for the desired template ("crimesAmbientais" or "leiDeDrogas").
     * @returns {string} - The requested template HTML string.
     * @throws Will throw an error if the key is invalid.
     */
    getTemplate: (key) => {
      if (!templates[key]) {
        throw new Error(`Template not found for key: "${key}". Available keys are: ${Object.keys(templates).join(', ')}.`);
      }
      return templates[key];
    },

    /**
     * List all available template keys.
     * @returns {string[]} - An array of template keys.
     */
    listTemplates: () => {
      return Object.keys(templates);
    },

    /**
     * Add a new legal article template.
     * @param {string} key - The key to identify the new template.
     * @param {string} content - The content of the template (HTML string).
     * @throws Will throw an error if the key already exists.
     */
    addTemplate: (key, content) => {
      if (templates[key]) {
        throw new Error(`Template with key "${key}" already exists. Use a unique key.`);
      }
      templates[key] = content;
    },

    /**
     * Remove an existing legal article template by key.
     * @param {string} key - The key of the template to remove.
     * @throws Will throw an error if the key does not exist.
     */
    removeTemplate: (key) => {
      if (!templates[key]) {
        throw new Error(`Template with key "${key}" does not exist.`);
      }
      delete templates[key];
    },
  };
})();

// Example usage (uncomment for use in production):
try {
  console.log('Available templates:', LegalResources.listTemplates());
  const crimesAmbientaisTemplate = LegalResources.getTemplate('crimesAmbientais');
  console.log('Crimes Ambientais Template:', crimesAmbientaisTemplate);

  // Adding a new template
  LegalResources.addTemplate('newTemplate', '<h1>New Legal Template</h1><p>Example content.</p>');
  console.log('New template added. Updated templates:', LegalResources.listTemplates());

  // Removing a template
  LegalResources.removeTemplate('newTemplate');
  console.log('Template removed. Updated templates:', LegalResources.listTemplates());
} catch (error) {
  console.error('Error:', error.message);
}

// Export the LegalResources module for use in other files (Node.js environment)
// module.exports = LegalResources;
```
