"""
Generated Code Metadata:
========================
Original URL: https://impresionentabloide.com
Prompt: Develop a JavaScript snippet that generates downloadable templates for business cards and flyers, similar to those available on impresionentabloide.com.
Generated: DETERMINISTIC_47a97517114084c9
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Business Card and Flyer Template Generator
 * Provides downloadable templates similar to impresionentabloide.com
 */

class TemplateGenerator {
  constructor() {
    this.templates = {
      businessCard: {
        name: 'Business Card',
        sizes: ['3.5x2', '3.5x2.5', '4x2'],
        formats: ['PDF', 'PNG', 'JPG'],
        bleed: '0.125in',
        safeZone: '0.25in'
      },
      flyer: {
        name: 'Flyer',
        sizes: ['8.5x11', '5.5x8.5', '4x6'],
        formats: ['PDF', 'PNG', 'JPG'],
        bleed: '0.25in',
        safeZone: '0.5in'
      }
    };
  }

  /**
   * Generate download links for templates
   * @param {string} type - Template type (businessCard or flyer)
   * @param {string} size - Template size
   * @param {string} format - File format
   * @returns {object} Download links object
   */
  generateTemplate(type, size, format) {
    if (!this.templates[type]) {
      throw new Error('Invalid template type');
    }

    const template = this.templates[type];
    if (!template.sizes.includes(size)) {
      throw new Error('Invalid size for selected template');
    }

    if (!template.formats.includes(format)) {
      throw new Error('Invalid format for selected template');
    }

    const fileName = `${template.name.replace(/\s+/g, '_')}_${size}_Template.${format.toLowerCase()}`;
    const templateData = this._createTemplateData(type, size, format);

    return {
      downloadLink: this._createDownloadLink(templateData, fileName, format),
      specs: {
        type: template.name,
        size,
        format,
        bleed: template.bleed,
        safeZone: template.safeZone
      }
    };
  }

  /**
   * Create mock template data (in a real app, this would generate actual files)
   * @private
   */
  _createTemplateData(type, size, format) {
    // In a real implementation, this would generate actual file data
    // For demo purposes, we return a mock object
    return {
      type,
      size,
      format,
      content: `Template for ${type}, size ${size} in ${format} format`
    };
  }

  /**
   * Create downloadable link
   * @private
   */
  _createDownloadLink(data, fileName, format) {
    const blob = new Blob([JSON.stringify(data)], { type: this._getMimeType(format) });
    const url = URL.createObjectURL(blob);
    return {
      url,
      fileName,
      click: () => {
        const a = document.createElement('a');
        a.href = url;
        a.download = fileName;
        document.body.appendChild(a);
        a.click();
        setTimeout(() => {
          document.body.removeChild(a);
          URL.revokeObjectURL(url);
        }, 100);
      }
    };
  }

  /**
   * Get MIME type for file format
   * @private
   */
  _getMimeType(format) {
    const types = {
      PDF: 'application/pdf',
      PNG: 'image/png',
      JPG: 'image/jpeg'
    };
    return types[format] || 'application/octet-stream';
  }

  /**
   * Get available template types
   * @returns {array} Array of template types
   */
  getTemplateTypes() {
    return Object.keys(this.templates);
  }

  /**
   * Get available sizes for a template type
   * @param {string} type - Template type
   * @returns {array} Array of available sizes
   */
  getSizesForType(type) {
    if (!this.templates[type]) {
      throw new Error('Invalid template type');
    }
    return [...this.templates[type].sizes];
  }

  /**
   * Get available formats for a template type
   * @param {string} type - Template type
   * @returns {array} Array of available formats
   */
  getFormatsForType(type) {
    if (!this.templates[type]) {
      throw new Error('Invalid template type');
    }
    return [...this.templates[type].formats];
  }
}

// Example usage:
/*
const generator = new TemplateGenerator();

try {
  const template = generator.generateTemplate('businessCard', '3.5x2', 'PDF');
  console.log('Template specs:', template.specs);
  template.downloadLink.click();
} catch (error) {
  console.error('Error generating template:', error.message);
}
*/
```
