"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://criterio.cl
Prompt: Generate JavaScript code to enhance the blog post editor in WordPress, allowing users to preview patterns from the "Patrones" section in real time.
Generated: DETERMINISTIC_3a6abd3b9788e3d9
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Enhance the WordPress blog post editor to preview patterns from the "Patrones" section in real time.
 * This script uses the WordPress block editor API.
 */

// Ensure the script only runs when the editor is loaded
wp.domReady(() => {
    // Import required WordPress components
    const { registerPlugin } = wp.plugins;
    const { PluginSidebar, PluginSidebarMoreMenu } = wp.editPost;
    const { PanelBody, Button, Spinner } = wp.components;
    const { useState } = wp.element;
    const { withSelect } = wp.data;

    // Custom plugin for previewing "Patrones"
    const PatronesPreviewPlugin = ({ postType }) => {
        // State to track pattern data
        const [patterns, setPatterns] = useState([]);
        const [loading, setLoading] = useState(false);
        const [selectedPattern, setSelectedPattern] = useState(null);

        // Function to fetch patterns from the "Patrones" section
        const fetchPatterns = async () => {
            try {
                setLoading(true);
                const response = await wp.apiFetch({ path: '/wp/v2/patterns?context=edit' });
                setPatterns(response);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching patterns:', error);
                setLoading(false);
            }
        };

        // Handle pattern selection and preview
        const handlePatternPreview = (pattern) => {
            setSelectedPattern(pattern);
            const blocks = wp.blocks.parse(pattern.content);
            wp.data.dispatch('core/block-editor').replaceInnerBlocks(wp.data.select('core/block-editor').getBlockSelectionStart().clientId, blocks);
        };

        // Fetch patterns automatically when the plugin is loaded
        if (!patterns.length && !loading) {
            fetchPatterns();
        }

        return (
            <PluginSidebar
                name="patrones-preview-sidebar"
                title="Patrones Preview"
                icon="layout"
            >
                <PanelBody>
                    <h3>Available Patterns</h3>
                    {loading && <Spinner />}
                    {!loading && patterns.length === 0 && <p>No patterns found.</p>}
                    {!loading && patterns.map((pattern) => (
                        <Button
                            isSecondary
                            key={pattern.id}
                            onClick={() => handlePatternPreview(pattern)}
                        >
                            {pattern.title.rendered}
                        </Button>
                    ))}
                </PanelBody>
                {selectedPattern && (
                    <PanelBody>
                        <h3>Previewing: {selectedPattern.title.rendered}</h3>
                    </PanelBody>
                )}
            </PluginSidebar>
        );
    };

    // Register the plugin in the editor sidebar
    registerPlugin('patrones-preview-plugin', {
        render: withSelect((select) => {
            return {
                postType: select('core/editor').getCurrentPostType(),
            };
        })(PatronesPreviewPlugin),
        icon: 'layout',
    });
});
```
