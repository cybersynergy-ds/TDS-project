import os
import subprocess

def format_markdown_with_prettier():
    # Define the markdown file path relative to the current working directory
    markdown_file_path = os.path.join("data", "format.md")  # using forward slash
    
    # Print the absolute path to verify
    print(f"Checking file at: {os.path.abspath(markdown_file_path)}")

    # Check if the file exists
    if not os.path.exists(markdown_file_path):
        raise FileNotFoundError(f"The file {markdown_file_path} does not exist.")
    
    print(f"File exists: {markdown_file_path}")

    # Step 1: Install Prettier if not installed already
    try:
        subprocess.run(["npm", "install", "prettier@3.4.2"], check=True)
        print("Prettier installed successfully.")
    except subprocess.CalledProcessError:
        print("Prettier installation failed. Trying to run Prettier without installation.")

    # Step 2: Run Prettier to format the Markdown file in-place
    try:
        subprocess.run(["npx", "prettier", "--write", markdown_file_path], check=True)
        print(f"Markdown file {markdown_file_path} formatted successfully.")
    except subprocess.CalledProcessError:
        raise Exception(f"Failed to format the file {markdown_file_path} with Prettier.")

    return "Markdown formatting completed successfully."

# Call the function to run the task
try:
    result = format_markdown_with_prettier()
    print(result)
except Exception as e:
    print(f"Error: {str(e)}")
