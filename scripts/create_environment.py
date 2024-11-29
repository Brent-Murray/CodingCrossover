import os
import subprocess


def create_conda_env(env_name, packages):
    """
    Create a new Conda environment and install required packages.

    Args:
        env_name (str): Name of the Conda environment.
        packages (list): List of packages to install.
    """
    try:
        # Create the environment
        print(f"Creating Conda environment '{env_name}'...")
        subprocess.run(["conda", "create", "-n", env_name, "-y"], check=True)

        # Activate the environment and install packages
        print(f"Installing packages in '{env_name}'...")
        subprocess.run(
            ["conda", "install", "-n", env_name, "-y"] + packages, check=True
        )

        # Install the environment in Jupyter
        print("Installing Jupyter kernel for the new environment...")
        subprocess.run(
            ["conda", "run", "-n", env_name, "pip", "install", "ipykernel"], check=True
        )
        subprocess.run(
            [
                "conda",
                "run",
                "-n",
                env_name,
                "python",
                "-m",
                "ipykernel",
                "install",
                "--user",
                "--name",
                env_name,
                "--display-name",
                f"Python ({env_name})",
            ],
            check=True,
        )

        print(f"Conda environment '{env_name}' is ready and accessible in Jupyter.")
        print(f"Starting Jupyter Lab")
        subprocess.run(["conda", "activate", env_name])
        subprocess.run(["jupyter", "lab"])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        print("Ensure that Conda is installed and accessible from your shell.")


# Example usage
if __name__ == "__main__":
    env_name = "my_new_environment"  # Name of the environment
    packages = [
        "jupyterlab",
        "numpy",
        "pandas",
        "geopandas",
        "matplotlib",
        "scikit-learn",
        "scikit-image",
        "rasterio",
        "matplotlib",
        "shapely",
    ]  # Required packages
    create_conda_env(env_name, packages)
