from conan import ConanFile
from conan.tools.cmake import cmake_layout

class ExampleRecipe(ConanFile):
    name = "network-monitor"  # Add your project name here
    version = "1.0.0"  # Add your project version here
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires("boost/1.74.0")

    def layout(self):
        cmake_layout(self)
