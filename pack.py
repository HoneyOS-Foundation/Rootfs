"""
Setup the rootfs
"""
import tomllib
import tempfile
import shutil
import os

# Create a temp dir
temp = tempfile.TemporaryDirectory()

print("Creating the root directories")
shutil.copytree("rootfs", temp.name + "/rootfs")

print("Compiling sys apps")
# Read tbe workspace to figure out what crates there are
workspace_file = open("sys-apps/workspace.toml")
workspace_toml = tomllib.loads(workspace_file.read())
workspace_file.close()
# Load the members from the workspace
members: list = workspace_toml["members"]

# Compile each crate and copy it;s binary to the temp dir
for crate in members:
    os.system("cd " + "sys-apps/" + crate +
              " && cargo build --release --target wasm32-unknown-unknown")
    shutil.copyfile(
        "sys-apps/" + crate + "/target/wasm32-unknown-unknown/release/" + crate + ".wasm", temp.name + "/rootfs/bin/" + crate + ".wasm")


print("Create the archive")
shutil.make_archive("dist/rootfs", 'zip', temp.name + "/rootfs")

# Clear the temp dir
temp.cleanup()
