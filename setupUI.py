from cx_Freeze import setup, Executable
import sys
import os

# Determine the base for the executable
base = 'Win32GUI' if sys.platform == 'win32' else None

# Define additional options for cx_Freeze
build_exe_options = {
    "packages": ["os", "sys", "ctypes", "win32com.client"],  # Add any other packages your app uses
    "excludes": ["tkinter", "unittest"],  # Exclude unnecessary packages
    "include_files": [
        ('dwarf_ble_connect/', './dwarf_ble_connect'),
        ('Install/', '.')
    ],
    "include_msvcr": True,  # Include Visual C++ runtime files
    "optimize": 2,  # Optimize bytecode
}

# Setup function
setup(
    name="Astro Dwarf Scheduler",
    version="1.0",
    description="Dwarf Astro Scheduler",
    options={"build_exe": build_exe_options},
    executables=[Executable("astro_dwarf_session_UI.py", base=base)]
)
