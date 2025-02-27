from setuptools import setup, find_packages

setup(
    name="todo_manager",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "todo-cli = todo_manager.cli:main",
        ],
    },
    install_requires=[],  # Add dependencies here if needed
    python_requires=">=3.6",
)