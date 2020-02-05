@setlocal

@set python_file_path=%1

@if not defined %python_file_path (
    @set python_file_path=python
)

"%python_file_path%" -m venv "venv"
"venv\Scripts\python" -m pip install --upgrade pip==19.0.3
"venv\Scripts\pip" install -e .

@endlocal