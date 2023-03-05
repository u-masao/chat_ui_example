

ui:
	poetry run gradio src/visualization/visualize.py 
lint:
	poetry run isort src
	poetry run black src -l 79
	poetry run flake8 src
