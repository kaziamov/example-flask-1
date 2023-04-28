start:
	poetry run flake8 financialprogramm

dev:
	poetry run flask --app financialprogramm/routing --debug run
