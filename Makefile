.PHONY: lint test black

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

## Run tests using pytest
lint:
	python -m pylint --version
	python -m pylint src

## Format your code using black
test:
	python -m pytest --version
	python -m pytest tests

## Run ci part
black:
	python -m black --version
	python -m black .


.PHONY: ci
	ci: precommit lint test