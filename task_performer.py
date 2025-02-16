import subprocess

from fastapi import HTTPException
from fastapi.responses import JSONResponse


def task_manager_AI(task: dict):
    # Check if the task description contains "install uv" and handle accordingly
    task_response = task.get("response", "").lower().strip()  # Clean input

    # Install 'uv' if task includes that request
    if "install uv" in task_response:
        try:
            subprocess.run(
                ["pip", "install", "uv"], check=True, capture_output=True, text=True
            )
        except subprocess.CalledProcessError as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to install 'uv' package. Error: {e.stderr}",
            )

    # Install 'uvicorn' if task includes that request
    elif "install uvicorn" in task_response:
        try:
            subprocess.run(
                ["pip", "install", "uvicorn"],
                check=True,
                capture_output=True,
                text=True,
            )
        except subprocess.CalledProcessError as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to install 'uvicorn' package. Error: {e.stderr}",
            )

    # Download and run the Python script if requested
    elif "run the script" in task_response:
        try:
            subprocess.run(
                [
                    "curl",
                    "-O",
                    "https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py",
                ],
                check=True,
                capture_output=True,
                text=True,
            )
        except subprocess.CalledProcessError as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to download the script. Error: {e.stderr}",
            )

        # Use an email passed as part of the task description
        user_email = task.get("user_email", "default@example.com")

        try:
            subprocess.run(
                ["python", "datagen.py", user_email],
                check=True,
                capture_output=True,
                text=True,
            )
        except subprocess.CalledProcessError as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to run the Python script. Error: {e.stderr}",
            )

    else:
        raise HTTPException(status_code=400, detail="Task description is not valid.")

    return JSONResponse(content={"message": "Task completed successfully"})
