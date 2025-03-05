import click  # Import the `click` library to create a CLI
import json  # Import `json` to save and load tasks from a file
import os  # Import `os` to check if the file exists

TODO_FILE = "todo.json"  # Define the filename where tasks are stored

# Function to ensure todo.json exists (optional, for safety)
def ensure_todo_file():
    if not os.path.exists(TODO_FILE):
        with open(TODO_FILE, "w") as file:
            json.dump([], file)  # Write empty list if file doesn't exist


# Function to load tasks from the JSON file (handles empty/corrupt files)
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []  # No file exists, return empty list

    try:
        with open(TODO_FILE, "r") as file:
            content = file.read().strip()  # Remove extra spaces/newlines
            if not content:  # Handle empty file
                return []
            return json.loads(content)  # Parse JSON
    except json.JSONDecodeError:
        click.echo("Warning: todo.json is corrupted. Initializing with an empty task list.")
        return []  # Return empty list if JSON is invalid


# Function to save tasks to the JSON file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)  # Save tasks with indentation


@click.group()  # Main CLI group
def cli():
    """Simple To-Do List Manager"""
    ensure_todo_file()  # Ensure file exists when CLI starts
    pass


@click.command()  # Command to add a new task
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Task added: {task}")


@click.command()  # Command to list all tasks
def list():
    """List all tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks found!")
        return

    for index, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        click.echo(f"{index}. {task['task']} [{status}]")


@click.command()  # Command to mark a task as complete
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} marked as completed!")
    else:
        click.echo("Invalid task number.")


@click.command()  # Command to remove a task
@click.argument("task_number", type=int)
def remove(task_number):
    """Remove a task from the list"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Removed task: {removed_task['task']}")
    else:
        click.echo("Invalid task number.")


# Register commands with the CLI
cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)

# Run the CLI if script is executed directly
if __name__ == "__main__":
    cli()
