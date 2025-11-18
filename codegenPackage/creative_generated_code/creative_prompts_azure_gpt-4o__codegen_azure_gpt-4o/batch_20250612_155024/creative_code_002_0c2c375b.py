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

```vue
<template>
  <Card>
    <template v-slot:title>
      Notifications
    </template>
    <Table
      :columns="columns"
      :data="notifications"
      border
      stripe
    />
    <div class="notification-footer">
      <Button type="primary" @click="clearNotifications">Clear Notifications</Button>
    </div>
  </Card>
</template>

<script>
export default {
  name: 'NotificationWidget',

  data() {
    return {
      notifications: [
        // Example notification data
        { id: 1, message: 'New user registered', type: 'info', timestamp: '2023-10-01 10:10:00' },
        { id: 2, message: 'Server downtime', type: 'error', timestamp: '2023-10-02 15:20:00' },
      ],
      columns: [
        // Table configuration
        {
          title: 'Type',
          key: 'type',
        },
        {
          title: 'Message',
          key: 'message',
        },
        {
          title: 'Timestamp',
          key: 'timestamp',
        },
      ],
    };
  },

  methods: {
    /**
     * Clears all notifications from the list.
     */
    clearNotifications() {
      try {
        this.notifications = [];
        this.$Message.success('Notifications cleared successfully.');
      } catch (error) {
        console.error('Error clearing notifications:', error);
        this.$Message.error('Failed to clear notifications.');
      }
    },
  },
};
</script>

<style scoped>
.notification-footer {
  margin-top: 20px;
  text-align: right;
}
</style>
```
