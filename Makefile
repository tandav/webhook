lint:
	python3 -m isort --force-single-line-imports server.py
	python3 -m flake8 --ignore E221,E501,W503,E701,E704,E741,I100,I201 server.py
run:
	uvicorn server:app --host 0.0.0.0 --port 8090 --limit-concurrency 2
