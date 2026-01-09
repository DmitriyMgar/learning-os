.PHONY: install test lint format check

install:
	pip install -r requirements.txt -r requirements-dev.txt

test:
	pytest -q

lint:
	ruff check .

format:
	ruff format .

check: lint test progress

progress:
	python scripts/update_progress.py
