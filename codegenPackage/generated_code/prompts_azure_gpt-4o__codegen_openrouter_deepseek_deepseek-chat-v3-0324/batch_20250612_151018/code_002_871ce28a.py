"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Create a custom theme for an Ant Design application by modifying the primary color and typography settings.
Generated: DETERMINISTIC_871ce28a503c1e76
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// theme.js
const { theme } = require('antd');

const customTheme = {
  algorithm: theme.defaultAlgorithm,
  token: {
    colorPrimary: '#1890ff', // Modify primary color
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", // Custom font family
    fontSize: 14, // Base font size
    borderRadius: 6, // Border radius
    colorText: '#1a1a1a', // Text color
    colorTextSecondary: '#595959', // Secondary text color
    colorLink: '#1890ff', // Link color
    colorLinkHover: '#40a9ff', // Link hover color
    colorLinkActive: '#096dd9', // Link active color
    colorBorder: '#d9d9d9', // Border color
    colorBorderSecondary: '#f0f0f0', // Secondary border color
    colorBgContainer: '#ffffff', // Background color
    colorBgLayout: '#f5f5f5', // Layout background color
    colorBgElevated: '#ffffff', // Elevated background color
    colorBgSpotlight: 'rgba(0, 0, 0, 0.85)', // Spotlight background color
    colorBgMask: 'rgba(0, 0, 0, 0.45)', // Mask background color
    colorBgBlur: 'transparent', // Blur background color
    colorBgDisabled: 'rgba(0, 0, 0, 0.04)', // Disabled background color
    colorBgTextHover: 'rgba(0, 0, 0, 0.06)', // Text hover background color
    colorBgTextActive: 'rgba(0, 0, 0, 0.15)', // Text active background color
    colorError: '#ff4d4f', // Error color
    colorWarning: '#faad14', // Warning color
    colorSuccess: '#52c41a', // Success color
    colorInfo: '#1890ff', // Info color
    colorErrorBg: '#fff2f0', // Error background color
    colorWarningBg: '#fffbe6', // Warning background color
    colorSuccessBg: '#f6ffed', // Success background color
    colorInfoBg: '#e6f7ff', // Info background color
    colorErrorBorder: '#ffccc7', // Error border color
    colorWarningBorder: '#ffe58f', // Warning border color
    colorSuccessBorder: '#b7eb8f', // Success border color
    colorInfoBorder: '#91d5ff', // Info border color
    colorErrorText: '#ff4d4f', // Error text color
    colorWarningText: '#faad14', // Warning text color
    colorSuccessText: '#52c41a', // Success text color
    colorInfoText: '#1890ff', // Info text color
    colorErrorTextHover: '#ff7875', // Error text hover color
    colorWarningTextHover: '#ffc53d', // Warning text hover color
    colorSuccessTextHover: '#73d13d', // Success text hover color
    colorInfoTextHover: '#40a9ff', // Info text hover color
    colorErrorTextActive: '#d9363e', // Error text active color
    colorWarningTextActive: '#d48806', // Warning text active color
    colorSuccessTextActive: '#389e0d', // Success text active color
    colorInfoTextActive: '#096dd9', // Info text active color
    colorErrorBorderHover: '#ffa39e', // Error border hover color
    colorWarningBorderHover: '#ffd666', // Warning border hover color
    colorSuccessBorderHover: '#95de64', // Success border hover color
    colorInfoBorderHover: '#69c0ff', // Info border hover color
    colorErrorBorderActive: '#ff7875', // Error border active color
    colorWarningBorderActive: '#ffc53d', // Warning border active color
    colorSuccessBorderActive: '#73d13d', // Success border active color
    colorInfoBorderActive: '#40a9ff', // Info border active color
    colorErrorBgHover: '#fff2f0', // Error background hover color
    colorWarningBgHover: '#fffbe6', // Warning background hover color
    colorSuccessBgHover: '#f6ffed', // Success background hover color
    colorInfoBgHover: '#e6f7ff', // Info background hover color
    colorErrorBgActive: '#ffccc7', // Error background active color
    colorWarningBgActive: '#ffe58f', // Warning background active color
    colorSuccessBgActive: '#b7eb8f', // Success background active color
    colorInfoBgActive: '#91d5ff', // Info background active color
    colorErrorTextDisabled: '#ffccc7', // Error text disabled color
    colorWarningTextDisabled: '#ffe58f', // Warning text disabled color
    colorSuccessTextDisabled: '#b7eb8f', // Success text disabled color
    colorInfoTextDisabled: '#91d5ff', // Info text disabled color
    colorErrorBorderDisabled: '#ffccc7', // Error border disabled color
    colorWarningBorderDisabled: '#ffe58f', // Warning border disabled color
    colorSuccessBorderDisabled: '#b7eb8f', // Success border disabled color
    colorInfoBorderDisabled: '#91d5ff', // Info border disabled color
    colorErrorBgDisabled: '#fff2f0', // Error background disabled color
    colorWarningBgDisabled: '#fffbe6', // Warning background disabled color
    colorSuccessBgDisabled: '#f6ffed', // Success background disabled color
    colorInfoBgDisabled: '#e6f7ff', // Info background disabled color
    colorErrorTextLight: '#ff4d4f', // Error text light color
    colorWarningTextLight: '#faad14', // Warning text light color
    colorSuccessTextLight: '#52c41a', // Success text light color
    colorInfoTextLight: '#1890ff', // Info text light color
    colorErrorTextLightHover: '#ff7875', // Error text light hover color
    colorWarningTextLightHover: '#ffc53d', // Warning text light hover color
    colorSuccessTextLightHover: '#73d13d', // Success text light hover color
    colorInfoTextLightHover: '#40a9ff', // Info text light hover color
    colorErrorTextLightActive: '#d9363e', // Error text light active color
    colorWarningTextLightActive: '#d48806', // Warning text light active color
    colorSuccessTextLightActive: '#389e0d', // Success text light active color
    colorInfoTextLightActive: '#096dd9', // Info text light active color
    colorErrorBorderLight: '#ffccc7', // Error border light color
    colorWarningBorderLight: '#ffe58f', // Warning border light color
    colorSuccessBorderLight: '#b7eb8f', // Success border light color
    colorInfoBorderLight: '#91d5ff', // Info border light color
    colorErrorBorderLightHover: '#ffa39e', // Error border light hover color
    colorWarningBorderLightHover: '#ffd666', // Warning border light hover color
    colorSuccessBorderLightHover: '#95de64', // Success border light hover color
    colorInfoBorderLightHover: '#69c0ff', // Info border light hover color
    colorErrorBorderLightActive: '#ff7875', // Error border light active color
    colorWarningBorderLightActive: '#ffc53d', // Warning border light active color
    colorSuccessBorderLightActive: '#73d13d', // Success border light active color
    colorInfoBorderLightActive: '#40a9ff', // Info border light active color
    colorErrorBgLight: '#fff2f0', // Error background light color
    colorWarningBgLight: '#fffbe6', // Warning background light color
    colorSuccessBgLight: '#f6ffed', // Success background light color
    colorInfoBgLight: '#e6f7ff', // Info background light color
    colorErrorBgLightHover: '#fff2f0', // Error background light hover color
    colorWarningBgLightHover: '#fffbe6', // Warning background light hover color
    colorSuccessBgLightHover: '#f6ffed', // Success background light hover color
    colorInfoBgLightHover: '#e6f7ff', // Info background light hover color
    colorErrorBgLightActive: '#ffccc7', // Error background light active color
    colorWarningBgLightActive: '#ffe58f', // Warning background light active color
    colorSuccessBgLightActive: '#b7eb8f', // Success background light active color
    colorInfoBgLight
