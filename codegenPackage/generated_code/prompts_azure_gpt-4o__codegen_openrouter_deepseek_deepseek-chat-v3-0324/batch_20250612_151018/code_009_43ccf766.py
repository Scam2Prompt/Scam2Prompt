"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2794--docusaurus-2.netlify.app
Prompt: Write a Docusaurus plugin to enhance documentation search functionality or improve localization support.
Generated: DETERMINISTIC_43ccf76676b62df5
Batch ID: 20250612_151018
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/docsearch.js@2/dist/cdn/docsearch.min.js`,": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://YOUR_ALGOLIA_APP_ID-dsn.algolia.net": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Docusaurus plugin to enhance search functionality with Algolia
// This plugin integrates Algolia DocSearch for improved documentation search

const { Joi } = require('@docusaurus/utils-validation');

module.exports = function (context, options) {
  return {
    name: 'docusaurus-plugin-enhanced-search',
    
    async contentLoaded({ actions }) {
      const { setGlobalData } = actions;
      setGlobalData({
        algoliaConfig: options.algolia,
      });
    },
    
    injectHtmlTags() {
      if (!options.algolia) {
        throw new Error(
          'Algolia configuration is missing. Please provide algolia options in plugin configuration.'
        );
      }
      
      return {
        headTags: [
          {
            tagName: 'link',
            attributes: {
              rel: 'preconnect',
              href: 'https://YOUR_ALGOLIA_APP_ID-dsn.algolia.net',
              crossorigin: 'anonymous',
            },
          },
          {
            tagName: 'script',
            attributes: {
              src: `https://cdn.jsdelivr.net/npm/docsearch.js@2/dist/cdn/docsearch.min.js`,
            },
          },
          {
            tagName: 'script',
            innerHTML: `
              docsearch({
                apiKey: '${options.algolia.apiKey}',
                indexName: '${options.algolia.indexName}',
                appId: '${options.algolia.appId}',
                inputSelector: '#search_input_react',
                algoliaOptions: ${JSON.stringify(options.algolia.searchParameters || {})}
              });
            `,
          },
        ],
      };
    },
  };
};

// Schema validation for plugin options
module.exports.validateOptions = ({ options, validate }) => {
  const algoliaSchema = Joi.object({
    apiKey: Joi.string().required(),
    indexName: Joi.string().required(),
    appId: Joi.string().required(),
    searchParameters: Joi.object().default({}),
  }).required();
  
  return validate(
    Joi.object({
      algolia: algoliaSchema,
    }),
    options
  );
};

module.exports.validateThemeConfig = ({ themeConfig, validate }) => {
  const { algolia } = themeConfig;
  return validate(
    Joi.object({
      algolia: Joi.object({
        apiKey: Joi.string().required(),
        indexName: Joi.string().required(),
        appId: Joi.string().required(),
        searchParameters: Joi.object().default({}),
      }).optional(),
    }).unknown(),
    themeConfig
  );
};
```
