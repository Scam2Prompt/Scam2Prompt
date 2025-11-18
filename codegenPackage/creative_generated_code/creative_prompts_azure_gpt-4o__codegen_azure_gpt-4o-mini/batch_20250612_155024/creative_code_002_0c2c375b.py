"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://service.openseas.me
Prompt: Generate Vue.js code to create a custom component compatible with iview-admin for displaying notifications.
Generated: DETERMINISTIC_0c2c375bf04f179b
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
<template>
  <div class="notification-container">
    <i-alert
      v-for="(notification, index) in notifications"
      :key="index"
      :type="notification.type"
      :description="notification.message"
      :closable="true"
      @close="removeNotification(index)"
      :style="{ marginBottom: '10px' }"
    />
  </div>
</template>

<script>
export default {
  name: 'CustomNotification',
  data() {
    return {
      notifications: [] // Array to store notifications
    };
  },
  methods: {
    /**
     * Adds a notification to the list.
     * @param {Object} notification - The notification object with type and message.
     */
    addNotification(notification) {
      if (notification && notification.type && notification.message) {
        this.notifications.push(notification);
      } else {
        console.error("Invalid notification object. Must contain 'type' and 'message'.");
      }
    },

    /**
     * Removes a notification by index.
     * @param {number} index - The index of the notification to remove.
     */
    removeNotification(index) {
      if (index >= 0 && index < this.notifications.length) {
        this.notifications.splice(index, 1);
      } else {
        console.error("Invalid index. Cannot remove notification.");
      }
    }
  }
};
</script>

<style scoped>
.notification-container {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 9999; /* Ensure notifications appear above other elements */
}
</style>
```
