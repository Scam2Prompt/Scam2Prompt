"""
Generated Code Metadata:
========================
Original URL: https://overlanders-atari.com
Prompt: Create an example of a 4K intro demo code that could compete in a demoscene event, taking cues from the '4K-Memory' demo by Overlanders.
Generated: DETERMINISTIC_d0e7620dff75cee5
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```c
// 4K Intro Demo - Inspired by Overlanders' 4K-Memory
// Compile with: gcc -O3 -ffast-math -o demo demo.c -lGL -lGLU -lglut -lm

#include <GL/glut.h>
#include <math.h>
#include <time.h>

#define PI 3.141592653589793
#define WIDTH 1280
#define HEIGHT 720

// Global variables
float t = 0.0f;
int frame = 0;

// Shader-like functions
float hash(float n) { return fract(sin(n)*43758.5453); }
float noise(vec3 x) {
    vec3 p = floor(x);
    vec3 f = fract(x);
    f = f*f*(3.0-2.0*f);
    float n = p.x + p.y*57.0 + 113.0*p.z;
    return mix(mix(mix(hash(n+0.0), hash(n+1.0),f.x),
                   mix(hash(n+57.0), hash(n+58.0),f.x),f.y),
               mix(mix(hash(n+113.0), hash(n+114.0),f.x),
                   mix(hash(n+170.0), hash(n+171.0),f.x),f.y),f.z);
}

// Vector math
typedef struct { float x, y, z; } vec3;
vec3 v3(float x, float y, float z) { vec3 v = {x,y,z}; return v; }
vec3 add(vec3 a, vec3 b) { return v3(a.x+b.x, a.y+b.y, a.z+b.z); }
vec3 mul(vec3 a, float s) { return v3(a.x*s, a.y*s, a.z*s); }
float dot(vec3 a, vec3 b) { return a.x*b.x + a.y*b.y + a.z*b.z; }
vec3 norm(vec3 v) { return mul(v, 1.0f/sqrt(dot(v,v))); }

// Scene rendering
float map(vec3 p) {
    p = mul(p, 0.5f);
    float d = length(p) - 1.0f;
    d += 0.5f*noise(v3(p.x*3.0f, p.y*3.0f, p.z*3.0f + t));
    return d;
}

vec3 calcNormal(vec3 p) {
    vec3 e = v3(0.001f, 0.0f, 0.0f);
    return norm(v3(
        map(add(p, e.xyy)) - map(add(p, -e.xyy)),
        map(add(p, e.yxy)) - map(add(p, -e.yxy)),
        map(add(p, e.yyx)) - map(add(p, -e.yyx))
    ));
}

float trace(vec3 ro, vec3 rd) {
    float t = 0.0f, d;
    for (int i = 0; i < 64; i++) {
        d = map(add(ro, mul(rd, t)));
        if (d < 0.001f || t > 20.0f) break;
        t += d * 0.5f;
    }
    return t;
}

// GLUT callbacks
void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();
    
    // Camera setup
    vec3 ro = v3(4.0f*sin(t*0.2f), 2.0f*cos(t*0.3f), 4.0f*cos(t*0.2f));
    vec3 ta = v3(0.0f, 0.0f, 0.0f);
    vec3 ww = norm(add(ta, mul(ro, -1.0f)));
    vec3 uu = norm(v3(ww.y, -ww.x, 0.0f));
    vec3 vv = norm(v3(ww.z*ww.x, ww.z*ww.y, -ww.x*ww.x - ww.y*ww.y));
    
    // Render scene
    glBegin(GL_POINTS);
    for (int y = 0; y < HEIGHT; y += 2) {
        for (int x = 0; x < WIDTH; x += 2) {
            vec2 uv = v2((x-WIDTH/2.0f)/HEIGHT, (y-HEIGHT/2.0f)/HEIGHT);
            vec3 rd = norm(add(add(mul(uu, uv.x), mul(vv, uv.y)), mul(ww, 1.5f)));
            
            float t = trace(ro, rd);
            if (t < 20.0f) {
                vec3 p = add(ro, mul(rd, t));
                vec3 n = calcNormal(p);
                vec3 l = norm(v3(0.6f, 0.8f, 0.4f));
                float diff = 0.5f + 0.5f*dot(n, l);
                float ao = 1.0f - t/20.0f;
                float col = diff * ao;
                
                glColor3f(col, col*0.8f, col*0.5f);
                glVertex2i(x, y);
            }
        }
    }
    glEnd();
    
    glutSwapBuffers();
    frame++;
    t = frame * 0.016f;
}

void reshape(int w, int h) {
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(60.0, (float)w/(float)h, 0.1, 100.0);
    glMatrixMode(GL_MODELVIEW);
}

void idle() {
    glutPostRedisplay();
}

// Main function
int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(WIDTH, HEIGHT);
    glutCreateWindow("4K Intro Demo");
    
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutIdleFunc(idle);
    
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
    glEnable(GL_DEPTH_TEST);
    glPointSize(2.0f);
    
    glutMainLoop();
    return 0;
}
```
