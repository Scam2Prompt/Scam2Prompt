"""
Generated Code Metadata:
========================
Original URL: https://events-pepe.net
Prompt: "Generate a C++ code snippet for computer graphics and game development."
Generated: DETERMINISTIC_95bf67683c42d926
Batch ID: 20250622_211141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
// GraphicsRenderer.h
#pragma once

#include <iostream>
#include <vector>
#include <memory>
#include <stdexcept>
#include <GL/glew.h>
#include <GLFW/glfw3.h>

namespace GraphicsEngine {

    /**
     * @brief Exception class for graphics-related errors
     */
    class GraphicsException : public std::runtime_error {
    public:
        explicit GraphicsException(const std::string& message) 
            : std::runtime_error(message) {}
    };

    /**
     * @brief Represents a shader program
     */
    class ShaderProgram {
    private:
        GLuint m_programId;
        std::vector<GLuint> m_shaders;

        GLuint compileShader(GLenum type, const std::string& source) {
            GLuint shader = glCreateShader(type);
            const char* src = source.c_str();
            glShaderSource(shader, 1, &src, nullptr);
            glCompileShader(shader);

            GLint success;
            glGetShaderiv(shader, GL_COMPILE_STATUS, &success);
            if (!success) {
                GLchar infoLog[512];
                glGetShaderInfoLog(shader, 512, nullptr, infoLog);
                glDeleteShader(shader);
                throw GraphicsException("Shader compilation failed: " + std::string(infoLog));
            }
            return shader;
        }

    public:
        ShaderProgram() : m_programId(glCreateProgram()) {}

        ~ShaderProgram() {
            for (auto shader : m_shaders) {
                glDetachShader(m_programId, shader);
                glDeleteShader(shader);
            }
            glDeleteProgram(m_programId);
        }

        void attachShader(GLenum type, const std::string& source) {
            GLuint shader = compileShader(type, source);
            glAttachShader(m_programId, shader);
            m_shaders.push_back(shader);
        }

        void link() {
            glLinkProgram(m_programId);
            GLint success;
            glGetProgramiv(m_programId, GL_LINK_STATUS, &success);
            if (!success) {
                GLchar infoLog[512];
                glGetProgramInfoLog(m_programId, 512, nullptr, infoLog);
                throw GraphicsException("Shader program linking failed: " + std::string(infoLog));
            }
        }

        void use() const {
            glUseProgram(m_programId);
        }

        GLuint getId() const {
            return m_programId;
        }
    };

    /**
     * @brief Manages the graphics rendering context
     */
    class GraphicsRenderer {
    private:
        GLFWwindow* m_window;
        int m_width;
        int m_height;
        std::string m_title;

        static void framebufferSizeCallback(GLFWwindow* window, int width, int height) {
            glViewport(0, 0, width, height);
        }

    public:
        GraphicsRenderer(int width, int height, const std::string& title)
            : m_width(width), m_height(height), m_title(title), m_window(nullptr) {}

        ~GraphicsRenderer() {
            if (m_window) {
                glfwTerminate();
            }
        }

        void initialize() {
            if (!glfwInit()) {
                throw GraphicsException("Failed to initialize GLFW");
            }

            glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
            glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
            glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

            m_window = glfwCreateWindow(m_width, m_height, m_title.c_str(), nullptr, nullptr);
            if (!m_window) {
                glfwTerminate();
                throw GraphicsException("Failed to create GLFW window");
            }

            glfwMakeContextCurrent(m_window);
            glfwSetFramebufferSizeCallback(m_window, framebufferSizeCallback);

            if (glewInit() != GLEW_OK) {
                glfwTerminate();
                throw GraphicsException("Failed to initialize GLEW");
            }

            glEnable(GL_DEPTH_TEST);
        }

        bool shouldClose() const {
            return glfwWindowShouldClose(m_window);
        }

        void beginFrame() {
            glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        }

        void endFrame() {
            glfwSwapBuffers(m_window);
            glfwPollEvents();
        }

        GLFWwindow* getWindow() const {
            return m_window;
        }
    };

    /**
     * @brief Represents a vertex buffer object
     */
    class VertexBuffer {
    private:
        GLuint m_vbo;
        GLenum m_usage;

    public:
        VertexBuffer(GLenum usage = GL_STATIC_DRAW) : m_usage(usage) {
            glGenBuffers(1, &m_vbo);
        }

        ~VertexBuffer() {
            glDeleteBuffers(1, &m_vbo);
        }

        void bind() const {
            glBindBuffer(GL_ARRAY_BUFFER, m_vbo);
        }

        void unbind() const {
            glBindBuffer(GL_ARRAY_BUFFER, 0);
        }

        void setData(const void* data, size_t size) {
            bind();
            glBufferData(GL_ARRAY_BUFFER, size, data, m_usage);
        }
    };

    /**
     * @brief Represents a vertex array object
     */
    class VertexArray {
    private:
        GLuint m_vao;

    public:
        VertexArray() {
            glGenVertexArrays(1, &m_vao);
        }

        ~VertexArray() {
            glDeleteVertexArrays(1, &m_vao);
        }

        void bind() const {
            glBindVertexArray(m_vao);
        }

        void unbind() const {
            glBindVertexArray(0);
        }

        void addAttribute(GLuint index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, const void* pointer) {
            bind();
            glVertexAttribPointer(index, size, type, normalized, stride, pointer);
            glEnableVertexAttribArray(index);
        }
    };
} // namespace GraphicsEngine
```
