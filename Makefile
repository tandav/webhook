lint:
	python3 -m isort --force-single-line-imports main.py
	python3 -m flake8 --ignore E221,E501,W503,E701,E704,E741,I100,I201 main.py
