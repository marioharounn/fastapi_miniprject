# Fastapi Mini Project

Build Docker image: ```docker build -t fastapi-app .```
Run Docker container: ```docker run -d -p 8000:8000 --name fastapi-container fastapi-app```


Stop Docker container: ```docker stop fastapi-container```
Remove containers run:  ```docker rm fastapi-container```

curl -X POST http://127.0.0.1:8000/calculate-sum \
-H "Content-Type: application/json" \
-d '{"number1": 10, "number2": 5}'
