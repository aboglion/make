
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
run:
	$(PYTHON) main.py

# ניקוי הסביבה הווירטואלית
clean:
ifeq ($(detected_OS),Windows)
	del /F /Q venv
else
	rm -rf venv
endif

# עזרה
help ?:
	@echo "אפשרויות הפקודות השונות:"
	@echo ""
	@echo "init    - הכנת הסביבה הווירטואלית. יוצר את הסביבה ומתקין את התלות."
	@echo "active  - הוראות להפעלת הסביבה הווירטואלית בצורה ידנית."
	@echo "install - התקנת הקבצים התלויים מקובץ ה-requirements.txt."
	@echo "req     - יצירת רשימת התלויות לקובץ requirements.txt."
	@echo "run     - הרצת הקוד הראשי (main.py)."
	@echo "clean   - ניקוי הסביבה הווירטואלית."
	@echo ""
	@echo "השתמש ב'make <שם הפקודה>' כדי להפעיל את הפקודה המתאימה."
