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

```csharp
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace FlowchartApp
{
    // Base class for all flowchart elements
    public abstract class FlowchartElement
    {
        public Guid Id { get; } = Guid.NewGuid();
        public string Name { get; set; }
        public Point Position { get; set; }
        public Size Size { get; set; } = new Size(100, 60);
        public Color Color { get; set; } = Color.LightBlue;
        public string Text { get; set; }

        public abstract void Draw(Graphics g);
        public virtual bool Contains(Point point)
        {
            return new Rectangle(Position, Size).Contains(point);
        }
    }

    // Concrete implementations of flowchart elements
    public class ProcessElement : FlowchartElement
    {
        public override void Draw(Graphics g)
        {
            using (var brush = new SolidBrush(Color))
            {
                g.FillRectangle(brush, new Rectangle(Position, Size));
            }
            using (var pen = new Pen(Color.Black, 2))
            {
                g.DrawRectangle(pen, new Rectangle(Position, Size));
            }
            if (!string.IsNullOrEmpty(Text))
            {
                using (var font = new Font("Arial", 10))
                {
                    var textSize = g.MeasureString(Text, font);
                    var textPos = new PointF(
                        Position.X + (Size.Width - textSize.Width) / 2,
                        Position.Y + (Size.Height - textSize.Height) / 2
                    );
                    g.DrawString(Text, font, Brushes.Black, textPos);
                }
            }
        }
    }

    public class DecisionElement : FlowchartElement
    {
        public override void Draw(Graphics g)
        {
            Point[] points = {
                new Point(Position.X + Size.Width / 2, Position.Y),
                new Point(Position.X + Size.Width, Position.Y + Size.Height / 2),
                new Point(Position.X + Size.Width / 2, Position.Y + Size.Height),
                new Point(Position.X, Position.Y + Size.Height / 2)
            };

            using (var brush = new SolidBrush(Color))
            {
                g.FillPolygon(brush, points);
            }
            using (var pen = new Pen(Color.Black, 2))
            {
                g.DrawPolygon(pen, points);
            }
            if (!string.IsNullOrEmpty(Text))
            {
                using (var font = new Font("Arial", 10))
                {
                    var textSize = g.MeasureString(Text, font);
                    var textPos = new PointF(
                        Position.X + (Size.Width - textSize.Width) / 2,
                        Position.Y + (Size.Height - textSize.Height) / 2
                    );
                    g.DrawString(Text, font, Brushes.Black, textPos);
                }
            }
        }

        public override bool Contains(Point point)
        {
            Point[] points = {
                new Point(Position.X + Size.Width / 2, Position.Y),
                new Point(Position.X + Size.Width, Position.Y + Size.Height / 2),
                new Point(Position.X + Size.Width / 2, Position.Y + Size.Height),
                new Point(Position.X, Position.Y + Size.Height / 2)
            };
            return IsPointInPolygon(points, point);
        }

        private bool IsPointInPolygon(Point[] polygon, Point point)
        {
            bool inside = false;
            for (int i = 0, j = polygon.Length - 1; i < polygon.Length; j = i++)
            {
                if (((polygon[i].Y > point.Y) != (polygon[j].Y > point.Y)) &&
                    (point.X < (polygon[j].X - polygon[i].X) * (point.Y - polygon[i].Y) / (polygon[j].Y - polygon[i].Y) + polygon[i].X))
                {
                    inside = !inside;
                }
            }
            return inside;
        }
    }

    // Connection between elements
    public class Connection
    {
        public Guid Id { get; } = Guid.NewGuid();
        public FlowchartElement FromElement { get; set; }
        public FlowchartElement ToElement { get; set; }
        public string Text { get; set; }
        public Color Color { get; set; } = Color.Black;

        public void Draw(Graphics g)
        {
            if (FromElement == null || ToElement == null) return;

            Point start = GetConnectionPoint(FromElement, ToElement.Position);
            Point end = GetConnectionPoint(ToElement, FromElement.Position);

            using (var pen = new Pen(Color, 2))
            {
                g.DrawLine(pen, start, end);

                // Draw arrow
                DrawArrow(g, pen, start, end);
            }

            if (!string.IsNullOrEmpty(Text))
            {
                using (var font = new Font("Arial", 10))
                {
                    var textPos = new PointF(
                        (start.X + end.X) / 2,
                        (start.Y + end.Y) / 2
                    );
                    g.DrawString(Text, font, Brushes.Black, textPos);
                }
            }
        }

        private Point GetConnectionPoint(FlowchartElement element, Point target)
        {
            Rectangle bounds = new Rectangle(element.Position, element.Size);
            Point center = new Point(bounds.X + bounds.Width / 2, bounds.Y + bounds.Height / 2);

            if (element is DecisionElement)
            {
                // For diamond shape, find intersection with perimeter
                return GetPolygonIntersection(element as DecisionElement, target);
            }

            // For rectangles, find intersection with edges
            float dx = target.X - center.X;
            float dy = target.Y - center.Y;
            float ratio = Math.Abs(dx / dy);

            float halfWidth = bounds.Width / 2f;
            float halfHeight = bounds.Height / 2f;

            if (ratio > (halfWidth / halfHeight))
            {
                // Intersect with left or right edge
                int x = dx > 0 ? bounds.Right : bounds.Left;
                int y = center.Y + (int)((x - center.X) * dy / dx);
                return new Point(x, y);
            }
            else
            {
                // Intersect with top or bottom edge
                int y = dy > 0 ? bounds.Bottom : bounds.Top;
                int x = center.X + (int)((y - center.Y) * dx / dy);
                return new Point(x, y);
            }
        }

        private Point GetPolygonIntersection(DecisionElement element, Point target)
        {
            Point[] points = {
                new Point(element.Position.X + element.Size.Width / 2, element.Position.Y),
                new Point(element.Position.X + element.Size.Width, element.Position.Y + element.Size.Height / 2),
                new Point(element.Position.X + element.Size.Width / 2, element.Position.Y + element.Size.Height),
                new Point(element.Position.X, element.Position.Y + element.Size.Height / 2)
            };

            Point center = new Point(
                element.Position.X + element.Size.Width / 2,
                element.Position.Y + element.Size.Height / 2
            );

            for (int i = 0; i < points.Length; i++)
            {
                int j = (i + 1) % points.Length;
                Point intersection;
                if (LineIntersectsLine(center, target, points[i], points[j], out intersection))
                {
                    return intersection;
                }
            }

            return center;
        }

        private bool LineIntersectsLine(Point l1p1, Point l1p2, Point l2p1, Point l2p2, out Point intersection)
        {
            intersection = Point.Empty;

            float A1 = l1p2.Y - l1p1.Y;
            float B1 = l1p1.X - l1p2.X;
            float C1 = A1 * l1p1.X + B1 * l1p1.Y;

            float A2 = l2p2.Y - l2p1.Y;
            float B2 = l2p1.X - l2p2.X;
            float C2 = A2 * l2p1.X + B2 * l2p1.Y;

            float det = A1 * B2 - A2 * B1;
            if (det == 0)
            {
                return false;
            }

            float x = (B2 * C1 - B1 * C2) / det;
            float y = (A1 * C2 - A2 * C1) / det;

            bool online1 = ((Math.Min(l1p1.X, l1p2.X) <= x) && (x <= Math.Max(l1p1.X, l1p2.X)) &&
                           (Math.Min(l1p1.Y, l1p2.Y) <= y) && (y <= Math.Max(l1p1.Y, l1p
