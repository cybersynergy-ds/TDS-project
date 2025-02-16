import os
import subprocess
import sys


def install_uv():
    try:
        subprocess.run(["pip", "install", "uv"], check=True)
        print("Successfully installed 'uv' package.")
    except subprocess.CalledProcessError:
        print("Failed to install 'uv' package.")
        sys.exit(1)


def run_datagen_script(email):
    try:
        # Check if the file already exists before downloading
        if not os.path.exists("datagen.py"):
            subprocess.run(
                [
                    "curl",
                    "-O",
                    "https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py",
                ],
                check=True,
            )
            print("Successfully downloaded 'datagen.py' script.")
        else:
            print("'datagen.py' already exists. Skipping download.")

        # Run the datagen.py script with the user's email as argument
        subprocess.run(["python", "datagen.py", email], check=True)
        print("Successfully ran 'datagen.py' with the provided email.")

    except subprocess.CalledProcessError as e:
        print(f"Failed to run 'datagen.py' script. Error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    # Install 'uv' package
    install_uv()

    # Set the user email (you can also pass this as an argument or environment variable)
    user_email = "24f1001586@ds.study.iitm.ac.in"

    # Run the datagen.py script with the user email
    run_datagen_script(user_email)


if __name__ == "__main__":
    main()
