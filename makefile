

start_app: # Start the app
	@echo "Starting the app..."
	uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
	@echo "App started"


ruff_me: # Run ruff
	@echo "Running ruff..."
	poetry run ruff format .
	@echo "Ruff done"
