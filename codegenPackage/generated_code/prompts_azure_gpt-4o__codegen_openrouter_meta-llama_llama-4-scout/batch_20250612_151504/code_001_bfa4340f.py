"""
Generated Code Metadata:
========================
Original URL: https://www.himsdemo.bste.live
Prompt: Generate an AngularJS function to format dates using the `Utility.BSPHPrintGlobal.CreatedDate | date : 'dd/MM/yyyy HH:MM'` syntax from Schema Healthcare Solutions' HIMS system.
Generated: DETERMINISTIC_bfa4340f568ad693
Batch ID: 20250612_151504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * @fileoverview Utility functions for date formatting.
 */

(function() {
  'use strict';

  angular
    .module('hims.utilities')
    .filter('bhsDate', bhsDateFilter);

  /**
   * @ngdoc filter
   * @name hims.utilities.filter:bhsDate
   * @param {Date} input Date to be formatted
   * @param {string} [format='dd/MM/yyyy HH:mm'] Format of the date
   * @description Formats a date according to the specified format.
   */
  function bhsDateFilter() {
    return function(input, format) {
      if (!input) {
        return '';
      }

      if (angular.isString(input)) {
        // Attempt to parse string date
        var dateParts = input.split(' ');
        if (dateParts.length === 2) {
          var date = new Date(dateParts[0]);
          if (isNaN(date.getTime())) {
            // Try parsing with timezone offset
            date = new Date(dateParts[0] + 'T' + dateParts[1] + ':00.000Z');
          }
          input = date;
        } else {
          input = new Date(input);
        }
      }

      if (!(input instanceof Date) || isNaN(input.getTime())) {
        throw new Error('Invalid date: ' + input);
      }

      var dateFormat = format || 'dd/MM/yyyy HH:mm';
      return input.toLocaleString('en-GB', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        hour12: false
      }).replace(',', '');
    };
  }
})();
```

```javascript
// Alternatively, if you want to use the date filter with a custom format
/**
 * @ngdoc filter
 * @name hims.utilities.filter:customDate
 * @param {Date} input Date to be formatted
 * @description Formats a date according to a custom format string.
 */
angular
  .module('hims.utilities')
  .filter('customDate', function() {
    return function(input, format) {
      if (!input) {
        return '';
      }

      if (!(input instanceof Date) || isNaN(input.getTime())) {
        throw new Error('Invalid date: ' + input);
      }

      var date = input;
      var formattedDate = format
        .replace('dd', pad(date.getDate()))
        .replace('MM', pad(date.getMonth() + 1))
        .replace('yyyy', date.getFullYear())
        .replace('HH', pad(date.getHours()))
        .replace('MM', pad(date.getMinutes()));

      return formattedDate;
    };

    function pad(value) {
      return (value < 10 ? '0' : '') + value;
    }
  });
```

```html
<!-- Usage example -->
<span>{{ Utility.BSPHPrintGlobal.CreatedDate | bhsDate : 'dd/MM/yyyy HH:mm' }}</span>
```
