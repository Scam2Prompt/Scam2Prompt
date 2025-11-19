"""
Generated Code Metadata:
========================
Original URL: https://canopusem.com
Prompt: Develop a Max for Live patch to create a custom instrument or effect, using the principles of music production and sound design.
Generated: DETERMINISTIC_a5e5fff4143517b3
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Custom Max for Live Patch: Granulator Effect**
```max
{
  "patcher" :   {
    "file_version" : 1,
    "app_version" : 1,
    "blocks" :     [
      {
        "box" :        {
          "patching_rect" : [ 10.0, 10.0, 256.0, 24.0 ],
          "rpatching_rect" : [ 10.0, 10.0, 256.0, 24.0 ],
          "file_version" : 1,
          "app_version" : 1,
          "inlets" :     [
            {
              "patching_rect" : [ 10.0, 3.0, 20.0, 20.0 ],
              "rpatching_rect" : [ 10.0, 3.0, 20.0, 20.0 ],
              "file_version" : 1,
              "app_version" : 1
            }
          ],
          "outlets" :    [
            {
              "patching_rect" : [ 240.0, 3.0, 20.0, 20.0 ],
              "rpatching_rect" : [ 240.0, 3.0, 20.0, 20.0 ],
              "file_version" : 1,
              "app_version" : 1
            }
          ],
          "file_version" : 1,
          "app_version" : 1,
          "object_class" : "p",
          "objectname" : "granulator",
          "patching_rect" : [ 10.0, 10.0, 256.0, 24.0 ],
          "rpatching_rect" : [ 10.0, 10.0, 256.0, 24.0 ]
        }
      },
      {
        "box" :        {
          "patching_rect" : [ 20.0, 40.0, 100.0, 40.0 ],
          "rpatching_rect" : [ 20.0, 40.0, 100.0, 40.0 ],
          "file_version" : 1,
          "app_version" : 1,
          "object_class" : "flonum",
          "objectname" : "grain-size",
          "patching_rect" : [ 20.0, 40.0, 100.0, 40.0 ],
          "rpatching_rect" : [ 20.0, 40.0, 100.0, 40.0 ],
          "value" : 10.0
        }
      },
      {
        "box" :        {
          "patching_rect" : [ 20.0, 90.0, 100.0, 40.0 ],
          "rpatching_rect" : [ 20.0, 90.0, 100.0, 40.0 ],
          "file_version" : 1,
          "app_version" : 1,
          "object_class" : "flonum",
          "objectname" : "overlap",
          "patching_rect" : [ 20.0, 90.0, 100.0, 40.0 ],
          "rpatching_rect" : [ 20.0, 90.0, 100.0, 40.0 ],
          "value" : 0.5
        }
      },
      {
        "box" :        {
          "patching_rect" : [ 20.0, 140.0, 100.0, 40.0 ],
          "rpatching_rect" : [ 20.0, 140.0, 100.0, 40.0 ],
          "file_version" : 1,
          "app_version" : 1,
          "object_class" : "flonum",
          "objectname" : "random-range",
          "patching_rect" : [ 20.0, 140.0, 100.0, 40.0 ],
          "rpatching_rect" : [ 20.0, 140.0, 100.0, 40.0 ],
          "value" : 100.0
        }
      },
      {
        "box" :        {
          "patching_rect" : [ 150.0, 40.0, 69.0, 20.0 ],
          "rpatching_rect" : [ 150.0, 40.0, 69.0, 20.0 ],
          "file_version" : 1,
          "app_version" : 1,
          "object_class" : "number",
          "objectname" : "buffer-size",
          "patching_rect" : [ 150.0, 40.0, 69.0, 20.0 ],
          "rpatching_rect" : [ 150.0, 40.0, 69.0, 20.0 ],
          "value" : 1024
        }
      },
      {
        "box" :        {
          "patching_rect" : [ 150.0, 70.0, 130.0, 20.0 ],
          "rpatching_rect" : [ 150.0, 70.0, 130.0, 20.0 ],
          "file_version" : 1,
          "app_version" : 1,
          "object_class" : "toggle",
          "objectname" : "trigger",
          "patching_rect" : [ 150.0, 70.0, 130.0, 20.0 ],
          "rpatching_rect" : [ 150.0, 70.0, 130.0, 20.0 ]
        }
      },
      {
        "box" :        {
          "patching_rect" : [ 10.0, 190.0, 230.0, 46.0 ],
          "rpatching_rect" : [ 10.0, 190.0, 230.0, 46.0 ],
          "file_version" : 1,
          "app_version" : 1,
          "object_class" : "pfft~",
          "objectname" : "pfft~",
          "patching_rect" : [ 10.0, 190.0, 230.0, 46.0 ],
          "rpatching_rect" : [ 10.0, 190.0, 230.0, 46.0 ],
          "parameters" : [ 0.0, 0.0, 0.0, 0.0, 0.0 ]
        }
      },
      {
        "box" :        {
          "patching_rect" : [ 250.0, 40.0, 100.0, 40.0 ],
          "rpatching_rect" : [ 250.0, 40.0, 100.0, 40.0 ],
          "file_version" : 1,
          "app_version" : 1,
          "object_class" : "button",
          "objectname" : "refresh",
          "patching_rect" : [ 250.0, 40.0, 100.0, 40.0 ],
          "rpatching_rect" : [ 250.0, 40.0, 100.0, 40.0 ]
        }
      },
      {
        "box" :        {
          "patching_rect" : [ 10.0, 250.0, 340.0, 20.0 ],
          "rpatching_rect" : [ 10.0, 250.0, 340.0, 20.0 ],
          "file_version" : 1,
          "app_version" : 1,
          "object_class" : "ezadc~",
          "objectname" : "ezadc~",
          "patching_rect" : [ 10.0, 250.0, 340.0, 20.0 ],
          "rpatching_rect" : [ 10.0, 250.0, 340.0, 20.0 ]
        }
      },
      {
        "box" :        {
          "patching_rect" : [ 10.0, 280.0, 340.0, 20.0 ],
          "rpatching_rect" : [ 10.0, 280.0, 340.0, 20.0 ],
          "file_version" : 1,
          "app_version" : 1,
          "object_class" : "ezdac~",
          "objectname" : "ezdac~",
          "patching_rect" : [ 10.0, 280.0, 340.0, 20.0 ],
          "rpatching_rect" : [ 10.0, 280.0, 340.0, 20.0 ]
        }
      }
    ],
    "connections" :   [
      {
        "patchline" :    {
          "source" : [ "ezadc~", 0 ],
          "destination" :
