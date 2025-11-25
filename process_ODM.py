import os
import subprocess

# ==== CONFIGURE THESE ====
PROJECT_FOLDER = r"C:\Users\jay.philip\Desktop\ODM_Project"  # Folder containing 'images' and 'output'
IMAGES_FOLDER = os.path.join(PROJECT_FOLDER, "images")
OUTPUT_FOLDER = os.path.join(PROJECT_FOLDER, "output")
ODM_DOCKER_IMAGE = "opendronemap/odm:latest"  # or your specific ODM image

# Ensure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Docker command
docker_cmd = [
    "docker", "run", "--rm",
    "-v", f"{PROJECT_FOLDER}:/datasets/odm_dataset",
    "-v", f"{OUTPUT_FOLDER}:/datasets/odm_output",
    ODM_DOCKER_IMAGE,
    "/datasets/odm_dataset",
    "--orthophoto-resolution", "5",
    "--fast-orthophoto",
    "--force-gps"

]

print("Running OpenDroneMap orthophoto processing...")
print("Command:", " ".join(docker_cmd))

# Run the command
result = subprocess.run(docker_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Print output
print(result.stdout)
print(result.stderr)
