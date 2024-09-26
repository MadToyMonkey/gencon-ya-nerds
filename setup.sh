#!/bin/bash

# Function to check if Python is installed
check_python() {
    if command -v python3 &>/dev/null; then
        PYTHON="python3"
    elif command -v python &>/dev/null; then
        PYTHON="python"
    else
        echo "Python is not installed. Please install Python 3.x before proceeding."
        exit 1
    fi
}

# Check if virtual environment exists, if not, create it
if [ ! -d "gencon-venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv geoncon-venv
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source gencon-venv/bin/activate

# Upgrade pip to the latest version
echo "Upgrading pip..."
pip install --upgrade pip

# Install or update packages from requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Installing/Updating packages..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found."
fi

echo "Setup complete!"
