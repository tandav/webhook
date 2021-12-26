run:
	#uvicorn server:app --host 0.0.0.0 --port 8090 --limit-concurrency 2 --ssl-keyfile privkey.pem --ssl-certfile fullchain.pem
	uvicorn server:app --host 0.0.0.0 --port 8090 --limit-concurrency 2

install_deps:
	apt update
	apt upgrade -y
	apt install -y python3-pip
	python3 -m pip install uvicorn fastapi
	sudo curl -L "https://github.com/docker/compose/releases/download/v2.2.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
	chmod +x /usr/local/bin/docker-compose

lint:
	python3 -m isort --force-single-line-imports server.py
	python3 -m flake8 --ignore E221,E501,W503,E701,E704,E741,I100,I201 server.py
