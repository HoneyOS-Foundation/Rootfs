"""
Setup the rootfs
"""

import tempfile
import shutil

# Create a temp dir
temp = tempfile.TemporaryDirectory()

print("Creating the root directories")
shutil.copytree("rootfs", temp.name + "/rootfs")

print("Create the archive")
shutil.make_archive("dist/rootfs", 'zip', temp.name + "/rootfs")

# Clear the temp dir
temp.cleanup()
