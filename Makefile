all: build start migrate test seed

build:
	docker-compose build

start:
	docker-compose up -d --remove-orphans

stop:
	docker-compose down

restart:
	docker-compose restart

logs:
	docker-compose logs -f

migrate:
	./bin/manage migrate

superuser:
	./bin/manage createsuperuser

shell:
	./bin/manage shell_plus

test:
	./bin/pytest

coverage:
	./bin/pytest -v -x --cov --reuse-db --cov-report term-missing

upgrade:
	pip-compile --upgrade requirements.in
	./bin/npm upgrade

requirements:
	pip-compile requirements.in
