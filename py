
ifeq ($(OS),Windows_NT)
    detected_OS := Windows
    PYTHON := venv\Scripts\python.exe
    VENV_ACTIVATE := venv\Scripts\activate
else
    detected_OS := $(shell uname -s)
    PYTHON := venv/bin/python3
    VENV_ACTIVATE := venv/bin/activate
endif
default: ?


# הכנת הסביבה הווירטואלית
init:
	test -d venv || python3 -m venv venv
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

# הפעלת הסביבה הווירטואלית
active:
	@echo "השתמש בפקודה הבאה להפעלת הסביבה:"
	@echo "source $(VENV_ACTIVATE)"

# התקנת הקבצים התלויים
install:
	$(PYTHON) -m pip install -r requirements.txt

# יצירת רשימת התלויות
req:
	$(PYTHON) -m pip freeze > requirements.txt

# הרצת הקוד
run $(TARGET):
	$(PYTHON) $(TARGET).py

# ניקוי הסביבה הווירטואלית
clean:
ifeq ($(detected_OS),Windows)
	del /F /Q venv
else
	rm -rf venv
endif

exit:
ifeq ($(detected_OS),Windows)
    @echo "Deactivating virtual environment (Windows)"
    @call $(VENV_ACTIVATE) && deactivate
else
    @echo "Deactivating virtual environment (Unix)"
    @deactivate
endif

# Help target
help:
    @echo "Available targets:"
    @echo ""
    @echo "init      - Initialize the virtual environment and install dependencies."
    @echo "active    - Instructions for manually activating the virtual environment."
    @echo "install   - Install dependencies from requirements.txt."
    @echo "req       - Generate a list of dependencies into requirements.txt."
    @echo "run xxx   - Run the code (replace xxx with the name of your Python script without .py)."
    @echo "clean     - Clean the virtual environment."
    @echo "exit      - Deactivate the virtual environment."
    @echo ""
    @echo "Usage: make <target>"
