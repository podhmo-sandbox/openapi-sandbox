run: .local/swagger.yml
	python main.py --port 8080 --swagger=swagger.yml

setup:
	pip install -r requirements.txt

.local/swagger.yml: ../swagger.yml
	dictknife transform --fn _transform.py:withapp --src $^ --dst $@
