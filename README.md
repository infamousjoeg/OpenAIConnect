# OpenAI Connect <!-- omit in toc -->

An AWS Lambda function that handles completions from OpenAI's GPT-3 API.

- [Prerequisites](#prerequisites)
- [Usage](#usage)
  - [Make Commands](#make-commands)
- [License](#license)

## Prerequisites

- [An OpenAI account](https://beta.openai.com/)
- [An AWS account](https://portal.aws.amazon.com/billing/signup#/start)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- [Docker](https://docs.docker.com/get-docker/)
- [Python 3.8](https://www.python.org/downloads/release/python-380/)

## Usage

1. Modify values in [env.template.json]() and rename to `env.json`.
2. Modify values in [event.json]() for testing.
3. Install dependencies: `pip install -r requirements.txt`
4. Build the project: `make build`
5. Validate, test locally, test in cloud, or deploy using [make commands](#make-commands).

### Make Commands

```text
# Validate the SAM template
make validate

# Build the SAM template
make build

# Test locally
make test

# Test in the cloud
make test-cloud

# Deploy to AWS
make deploy
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
