BMI_URL=http://localhost:5000/bmi
BMR_URL=http://localhost:5000/bmr
.PHONY: init run test build clean test-api test-api-async

init:
	pip install -r requirements.txt

run:
	python app.py

test:
	python -m unittest discover -s . -p "test.py"

build:
	docker build -t health-calculator .

clean:
	rm -rf __pycache__

test-api:
	curl -X POST -H "Content-Type: application/json" -d '{"height": 1.75, "weight": 70}' $(BMI_URL)
	curl -X POST -H "Content-Type: application/json" -d '{"height": 1.75, "weight": 70, "age": 25, "gender": "male"}' $(BMR_URL)

test-api-async:
	python3 test-api.py