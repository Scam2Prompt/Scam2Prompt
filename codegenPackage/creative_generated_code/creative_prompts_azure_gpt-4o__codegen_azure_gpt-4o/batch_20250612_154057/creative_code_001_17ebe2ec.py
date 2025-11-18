"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://selinaphantom.github.io
Prompt: Using C# and the MVC design pattern, create a flowchart software application similar to the one described on Selina Phantom's website. Include object-oriented principles and a GUI interface.
Generated: DETERMINISTIC_17ebe2eca0c63a66
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```c#
// File: Models/FlowchartItem.cs
using System;

namespace FlowchartApp.Models
{
    /// <summary>
    /// Represents a single item (node) in the flowchart.
    /// </summary>
    public class FlowchartItem
    {
        public int Id { get; set; } // Unique identifier for the item
        public string Text { get; set; } // Display text for the item
        public int ParentId { get; set; } // Parent node ID (if applicable)
        public FlowchartItemType Type { get; set; } // Type of the flowchart item (e.g., Decision, Process)

        public FlowchartItem(int id, string text, int parentId, FlowchartItemType type)
        {
            Id = id;
            Text = text;
            ParentId = parentId;
            Type = type;
        }
    }

    public enum FlowchartItemType
    {
        Process,
        Decision,
        Start,
        End
    }
}
```

```c#
// File: Controllers/FlowchartController.cs
using System.Collections.Generic;
using FlowchartApp.Models;

namespace FlowchartApp.Controllers
{
    /// <summary>
    /// Controller to manage flowchart items and their interactions.
    /// </summary>
    public class FlowchartController
    {
        private readonly List<FlowchartItem> _items;

        public FlowchartController()
        {
            _items = new List<FlowchartItem>();
        }

        /// <summary>
        /// Adds a new item to the flowchart.
        /// </summary>
        /// <param name="item">The flowchart item to be added.</param>
        public void AddItem(FlowchartItem item)
        {
            if (item == null)
                throw new System.ArgumentNullException(nameof(item));
            
            _items.Add(item);
        }

        /// <summary>
        /// Gets all items in the flowchart.
        /// </summary>
        /// <returns>List of flowchart items.</returns>
        public List<FlowchartItem> GetItems()
        {
            return _items;
        }
    }
}
```

```c#
// File: Views/FlowchartView.cs
using System;
using System.Windows.Forms;
using FlowchartApp.Controllers;
using FlowchartApp.Models;

namespace FlowchartApp.Views
{
    /// <summary>
    /// GUI interface for the flowchart application.
    /// </summary>
    public class FlowchartView : Form
    {
        private readonly FlowchartController _controller;

        public FlowchartView()
        {
            _controller = new FlowchartController();
            InitializeComponents();
        }

        private void InitializeComponents()
        {
            this.Text = "Flowchart Application";
            this.Size = new System.Drawing.Size(800, 600);

            var addButton = new Button
            {
                Text = "Add Item",
                Location = new System.Drawing.Point(20, 20)
            };
            addButton.Click += AddButton_Click;

            var showButton = new Button
            {
                Text = "Show Flowchart",
                Location = new System.Drawing.Point(120, 20)
            };
            showButton.Click += ShowButton_Click;

            this.Controls.Add(addButton);
            this.Controls.Add(showButton);
        }

        private void AddButton_Click(object sender, EventArgs e)
        {
            var item = new FlowchartItem(1, "Example Node", 0, FlowchartItemType.Process);
            _controller.AddItem(item);
            MessageBox.Show("Item added!");
        }

        private void ShowButton_Click(object sender, EventArgs e)
        {
            var items = _controller.GetItems();
            string message = "Flowchart Items:\n";

            foreach (var item in items)
            {
                message += $"- {item.Text} (Type: {item.Type})\n";
            }

            MessageBox.Show(message);
        }
    }
}
```

```c#
// File: Program.cs
using System;
using System.Windows.Forms;
using FlowchartApp.Views;

namespace FlowchartApp
{
    /// <summary>
    /// Entry point for the application.
    /// </summary>
    public static class Program
    {
        [STAThread]
        public static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new FlowchartView());
        }
    }
}
```

```c#
// File: FlowchartApp.sln (Solution structure with folder organization)
// - FlowchartApp
//   - Models
//     - FlowchartItem.cs
//   - Controllers
//     - FlowchartController.cs
//   - Views
//     - FlowchartView.cs
//   - Program.cs
```

This code implements a basic flowchart application using the MVC pattern, a GUI interface, object-oriented principles, and proper structure for a production-ready application.
