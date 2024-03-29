@echo /-------------------------------------------------------------------------------
@echo * Installing Python virtual environment
@echo --------------------------------------------------------------------------------
call python -m venv venv

@echo /-------------------------------------------------------------------------------
@echo * Activating Python virtual environment
@echo --------------------------------------------------------------------------------
call venv\Scripts\activate.bat

@echo /-------------------------------------------------------------------------------
@echo * Installing Python packages
@echo --------------------------------------------------------------------------------
call pip install -r requirements.txt

@echo /-------------------------------------------------------------------------------
@echo * ALL DONE!
@echo --------------------------------------------------------------------------------
