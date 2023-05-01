test:
	sam local invoke OpenAIConnect -n env.json -e event.json

test-cloud:
	sam sync --stack-name {{OpenAIConnect}} --watch

build:
	sam build

validate:
	sam validate

deploy:
	sam deploy --guided

clean:
	rm -rf .aws-sam