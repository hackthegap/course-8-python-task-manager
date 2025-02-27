
---

# To-Do List Manager

**Created by Fabricio Braga**  
**Last Updated: February 27, 2025**

---

## Project Overview

A simple command-line **To-Do List Manager** written in Python. This project demonstrates **Python coding practices**, **unit testing**, and **packaging**. It allows users to:

- Add tasks.
- Mark tasks as completed.
- List all tasks.

---

## Features

- **Add Tasks**: Add new tasks to the to-do list.
- **Complete Tasks**: Mark tasks as completed.
- **List Tasks**: View all tasks with their completion status.

---

## Prerequisites

Before running the project, ensure you have the following installed:

### 1. **Python**
- Download and install Python from [https://www.python.org/](https://www.python.org/).
- Verify the installation:
  ```bash
  python --version
  ```

### 2. **Git (Optional)**
- Git is used for version control. You can download it from [https://git-scm.com/](https://git-scm.com/).

---

## Getting Started

Follow these steps to set up and run the project locally.

### 1. **Clone the Repository**

Clone the repository to your local machine:

```bash
git clone https://github.com/hackthegap/course-8-python-task-manager.git
cd todo-list-manager
```

### 2. **Set Up a Virtual Environment**

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. **Install the Package**

Install the package in development mode:

```bash
pip install -e .
```

---

## Usage

Run the application using the command-line interface:

```bash
todo-cli
```

### Available Options:
1. **Add Task**: Add a new task to the to-do list.
2. **Complete Task**: Mark a task as completed by entering its index.
3. **List Tasks**: View all tasks with their completion status.
4. **Exit**: Exit the application.

---

## Running Tests

The project includes unit tests to ensure the functionality works as expected. Run the tests using the following command:

```bash
python -m unittest discover tests
```

---

## Project Structure

```
todo-list-manager/
├── todo_manager/
│   ├── __init__.py
│   ├── todo.py          # To-Do List logic
│   ├── cli.py           # Command-line interface
├── tests/
│   ├── __init__.py
│   ├── test_todo.py     # Unit tests for To-Do List logic
├── setup.py             # Packaging configuration
├── README.md            # Project documentation
```

---

## Key Concepts

### 1. **Python Coding Practices**
- Follows **PEP 8** style guidelines.
- Uses meaningful variable and function names.
- Includes docstrings for functions.

### 2. **Unit Testing**
- Uses `unittest` to test the To-Do List logic.
- Tests cover adding tasks, completing tasks, and listing tasks.

### 3. **Packaging**
- Uses `setuptools` to package the application.
- Includes a command-line interface (CLI) for easy usage.

---

## Contributing

If you'd like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## Acknowledgments

- This project was created as part of a course to teach Python coding practices, unit testing, and packaging.
- Special thanks to the Python community for providing excellent resources and tools.

---

## Questions?

If you have any questions or need further assistance, feel free to reach out to the instructor or open an issue in the repository.

---
