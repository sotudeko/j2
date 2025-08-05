from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import copy

class CompressorRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("zlib/1.3.1")

    def build_requirements(self):
        self.tool_requires("cmake/3.27.9")

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        # cmake.configure()
        # cmake.build()

    # def package(self):
        # copy(self, "compressor", src=self.build_folder, dst=self.package_folder)

        # 1. Copy headers from the build folder (or source folder) to the 'include' folder in the package
        # copy(self, "*.h", src=self.source_folder, dst=self.package_folder, keep_path=False)
        
        # 2. Copy the library files from the build folder to the 'lib' folder in the package
        # copy(self, "*.lib", src=self.build_folder, dst=self.package_folder)
        # copy(self, "*.a", src=self.build_folder, dst=self.package_folder)
        
        # 3. Copy binaries (if any) from the build folder to the 'bin' folder in the package
        # copy(self, "*.dll", src=self.build_folder, dst=self.package_folder)
        # copy(self, "*.so", src=self.build_folder, dst=self.package_folder)

        
        # Optional: Copy a license file
        # copy(self, "LICENSE.md", src=self.source_folder, dst=self.package_folder)



