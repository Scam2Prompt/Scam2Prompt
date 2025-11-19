"""
Generated Code Metadata:
========================
Original URL: https://selinaphantom.github.io
Prompt: Using C# and the MVC design pattern, create a flowchart software application similar to the one described on Selina Phantom's website. Include object-oriented principles and a GUI interface.
Generated: DETERMINISTIC_17ebe2eca0c63a66
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Flowchart Software Application in C# using MVC Design Pattern**

### Models
```csharp
// FlowchartModel.cs
namespace FlowchartSoftware
{
    public class Node
    {
        public int Id { get; set; }
        public string Text { get; set; }
        public NodeType Type { get; set; }
        public List<Edge> Edges { get; set; }

        public Node(int id, string text, NodeType type)
        {
            Id = id;
            Text = text;
            Type = type;
            Edges = new List<Edge>();
        }
    }

    public enum NodeType
    {
        Start,
        Process,
        Decision,
        End
    }

    public class Edge
    {
        public int Id { get; set; }
        public Node Source { get; set; }
        public Node Target { get; set; }
        public string Condition { get; set; }

        public Edge(int id, Node source, Node target, string condition)
        {
            Id = id;
            Source = source;
            Target = target;
            Condition = condition;
        }
    }

    public class Flowchart
    {
        public List<Node> Nodes { get; set; }
        public List<Edge> Edges { get; set; }

        public Flowchart()
        {
            Nodes = new List<Node>();
            Edges = new List<Edge>();
        }
    }
}
```

### Controllers
```csharp
// FlowchartController.cs
using System.Collections.Generic;
using System.Windows.Forms;

namespace FlowchartSoftware
{
    public class FlowchartController
    {
        private Flowchart _flowchart;
        private FlowchartView _view;

        public FlowchartController(FlowchartView view)
        {
            _view = view;
            _flowchart = new Flowchart();
        }

        public void AddNode(Node node)
        {
            _flowchart.Nodes.Add(node);
            _view.UpdateNodeList(_flowchart.Nodes);
        }

        public void AddEdge(Edge edge)
        {
            _flowchart.Edges.Add(edge);
            _view.UpdateEdgeList(_flowchart.Edges);
        }

        public void RemoveNode(Node node)
        {
            _flowchart.Nodes.Remove(node);
            _view.UpdateNodeList(_flowchart.Nodes);
        }

        public void RemoveEdge(Edge edge)
        {
            _flowchart.Edges.Remove(edge);
            _view.UpdateEdgeList(_flowchart.Edges);
        }
    }
}
```

### Views
```csharp
// FlowchartView.cs
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace FlowchartSoftware
{
    public class FlowchartView : Form
    {
        private FlowchartController _controller;
        private ListBox _nodeListBox;
        private ListBox _edgeListBox;
        private TextBox _nodeTextBox;
        private ComboBox _nodeTypeComboBox;
        private Button _addNodeButton;
        private Button _removeNodeButton;
        private Button _addEdgeButton;
        private Button _removeEdgeButton;

        public FlowchartView()
        {
            _controller = new FlowchartController(this);

            // Initialize UI components
            _nodeListBox = new ListBox { Width = 200, Height = 200 };
            _edgeListBox = new ListBox { Width = 200, Height = 200 };
            _nodeTextBox = new TextBox { Width = 200 };
            _nodeTypeComboBox = new ComboBox { Width = 200 };
            _addNodeButton = new Button { Text = "Add Node" };
            _removeNodeButton = new Button { Text = "Remove Node" };
            _addEdgeButton = new Button { Text = "Add Edge" };
            _removeEdgeButton = new Button { Text = "Remove Edge" };

            // Layout UI components
            _nodeListBox.Location = new Point(10, 10);
            _edgeListBox.Location = new Point(220, 10);
            _nodeTextBox.Location = new Point(10, 220);
            _nodeTypeComboBox.Location = new Point(10, 250);
            _addNodeButton.Location = new Point(10, 280);
            _removeNodeButton.Location = new Point(120, 280);
            _addEdgeButton.Location = new Point(220, 280);
            _removeEdgeButton.Location = new Point(330, 280);

            // Add UI components to form
            Controls.Add(_nodeListBox);
            Controls.Add(_edgeListBox);
            Controls.Add(_nodeTextBox);
            Controls.Add(_nodeTypeComboBox);
            Controls.Add(_addNodeButton);
            Controls.Add(_removeNodeButton);
            Controls.Add(_addEdgeButton);
            Controls.Add(_removeEdgeButton);

            // Add event handlers
            _addNodeButton.Click += AddNodeButton_Click;
            _removeNodeButton.Click += RemoveNodeButton_Click;
            _addEdgeButton.Click += AddEdgeButton_Click;
            _removeEdgeButton.Click += RemoveEdgeButton_Click;

            // Initialize node type combo box
            _nodeTypeComboBox.DataSource = Enum.GetValues(typeof(NodeType));
        }

        private void AddNodeButton_Click(object sender, EventArgs e)
        {
            try
            {
                Node node = new Node(_flowchart.Nodes.Count + 1, _nodeTextBox.Text, (NodeType)_nodeTypeComboBox.SelectedItem);
                _controller.AddNode(node);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void RemoveNodeButton_Click(object sender, EventArgs e)
        {
            try
            {
                if (_nodeListBox.SelectedItem is Node node)
                {
                    _controller.RemoveNode(node);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void AddEdgeButton_Click(object sender, EventArgs e)
        {
            try
            {
                // TO DO: implement add edge logic
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void RemoveEdgeButton_Click(object sender, EventArgs e)
        {
            try
            {
                // TO DO: implement remove edge logic
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        public void UpdateNodeList(List<Node> nodes)
        {
            _nodeListBox.DataSource = nodes;
        }

        public void UpdateEdgeList(List<Edge> edges)
        {
            _edgeListBox.DataSource = edges;
        }
    }
}
```

### Program
```csharp
// Program.cs
using System;
using System.Windows.Forms;

namespace FlowchartSoftware
{
    public class Program
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
