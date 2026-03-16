# LambdaLens: An AI-Powered AWS Lambda Debugger

> Stop staring at CloudWatch logs. Let AI tell you exactly what went wrong and how to fix it.

LambdaLens is a CLI tool that automatically fetches your AWS Lambda CloudWatch logs, sends them to **Amazon Nova 2 Lite** via Amazon Bedrock for analysis, and opens a beautiful diagnostic report in your browser, all with a single command.

Built for the **Amazon Nova AI Hackathon** 

---

## Demo

```
$ lambda-debug --function my-api-handler --region us-east-2 --hours 24

⚡ LambdaLens: AI-Powered Lambda Debugger
Analyzing function: my-api-handler in us-east-2

Fetching Lambda logs and metadata...
✓ Lambda metadata fetched successfully
✓ Found 4 log streams in the last 24 hours
✓ Fetched 142 log events successfully

Analyzing logs with Amazon Nova 2 Lite...
✓ Analysis complete

Opening report in browser...
```

Your browser opens automatically at `http://localhost:8000/report` showing a full diagnostic report.

---

## Features

- **One command debugging**: point it at any Lambda function and get instant AI-powered diagnosis
- **Powered by Amazon Nova 2 Lite**: advanced reasoning model identifies root causes, not just error names
- **Beautiful visual report**: dark-themed dashboard with color-coded severity cards opens automatically in your browser
- **Specific actionable fixes**: not generic advice, but exact steps tailored to your function's configuration and actual log lines
- **Zero extra setup** :uses your existing AWS credentials, no API keys or logins needed
- **Privacy first**: your logs never leave your machine except to AWS APIs you already use
- **Works with any Lambda**: runtime agnostic, works with Python, Node.js, Java, Go, and more

---

## Architecture

```
lambda-debug CLI (Click)
        ↓
core/fetcher.py
  → boto3 fetches Lambda metadata from AWS Lambda API
  → boto3 fetches CloudWatch log streams + events
        ↓
core/analyzer.py
  → Builds structured prompt with function context + logs
  → Calls Amazon Nova 2 Lite via Amazon Bedrock
  → Returns structured JSON diagnosis
        ↓
server/app.py
  → FastAPI serves report at localhost:8000
  → Jinja2 renders diagnosis into HTML
  → Browser opens automatically
        ↓
server/templates/report.html
  → Dark themed dashboard
  → Color coded error cards
  → Collapsible log lines
```

---

## Prerequisites

- Python 3.10+
- **AWS credentials configured**: LambdaLens uses your AWS credentials to call Lambda, CloudWatch, and Bedrock. Configure them via the AWS CLI:
  ```bash
  aws configure
  ```
  You'll need an AWS account with access to:
  - AWS Lambda
  - Amazon CloudWatch Logs
  - Amazon Bedrock (Nova 2 Lite model)

---

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/prithishsamanta/Lambda_Lens.git
cd Lambda_Lens
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv

# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Install the package**

```bash
pip install -e .
```

This installs all dependencies and registers the `lambda-debug` command globally in your terminal.

**4. Configure AWS credentials (required for the tool to work)**

LambdaLens needs your AWS credentials to fetch Lambda metadata, CloudWatch logs, and to call Bedrock. If you haven't already:

```bash
aws configure
```

Provide:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g. `us-east-2`)

---

## Usage

### Basic usage

```bash
lambda-debug --function YOUR_FUNCTION_NAME
```

### With all options

```bash
lambda-debug --function YOUR_FUNCTION_NAME --region us-east-2 --hours 24
```

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `--function` | Lambda function name (required) | — |
| `--region` | AWS region | `us-east-2` |
| `--hours` | How many hours of logs to analyze | `24` |

### Examples

```bash
# Analyze a function in the last 24 hours
lambda-debug --function my-api-handler

# Analyze a function in a specific region
lambda-debug --function payment-processor --region ap-south-1

# Analyze only the last 6 hours of logs
lambda-debug --function data-pipeline --region us-west-2 --hours 6
```

---

## What the Report Shows

The report opens automatically in your browser and includes:

**Header**
- Function name and AWS region
- Runtime version
- Live health status badge (Healthy / Degraded / Critical)

**AI Diagnosis Summary**
- One sentence overall assessment from Nova 2 Lite
- Total issues found, critical count, warning count

**Function Configuration**
- Memory allocation, timeout setting, handler, last modified date

**Error Cards** (one per detected issue)
- Error type with severity badge (Critical / Warning / Info)
- **What happened**: plain English explanation
- **Root cause**: why it happened
- **How to fix**: ready-to-use fixes: corrected code patterns, exact IAM policy JSON, or specific configuration changes depending on the error type
- **Relevant log lines**: collapsible section showing exact log lines that triggered the error

---

## What LambdaLens Can Detect

- Runtime exceptions (ZeroDivisionError, TypeError, NameError, etc.)
- Function timeouts with root cause analysis
- IAM permission errors with exact missing permissions
- Memory limit issues and optimization suggestions
- Cold start performance problems
- VPC connectivity failures
- Dependency and import errors
- Custom application errors in logs

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| CLI | Python + Click |
| AWS Integration | boto3 |
| AI Model | Amazon Nova 2 Lite |
| AI Platform | Amazon Bedrock |
| Backend Server | FastAPI + Uvicorn |
| Templating | Jinja2 |
| Frontend | Tailwind CSS + Alpine.js |
| Terminal Output | Rich |

---

## Project Structure

```
Lambda_Lens/                 # or your clone directory
├── cli/
│   ├── __init__.py
│   └── main.py              # CLI entry point (lambda-debug command)
├── core/
│   ├── __init__.py
│   ├── fetcher.py           # CloudWatch log fetching via boto3
│   └── analyzer.py          # Nova 2 Lite analysis via Bedrock
├── server/
│   ├── __init__.py
│   ├── app.py               # FastAPI local server
│   └── templates/
│       └── report.html      # Visual diagnostic report
├── setup.py                 # Package configuration
├── requirements.txt         # Dependencies
├── .env                     # Environment variables (not committed)
└── README.md
```

---

## What's Next

- **Multi-function fleet analysis**: Analyze all Lambda functions in your account at once and get a health dashboard ranked by severity.
- **Beyond Lambda**: Extend the same AI-powered diagnosis to other CloudWatch log sources (API Gateway, RDS, ECS, etc.).
- **CI/CD integration**: Run LambdaLens in your deployment pipeline to catch issues before they reach users.
- **IDE plugin**: Bring the same debugging intelligence into VS Code so you never leave your editor.

---

## Privacy & Security

- **No data storage**: logs are fetched, analyzed, and displayed in memory only
- **No external transmission**: your logs only go to AWS APIs (Lambda, CloudWatch, Bedrock) that you already use
- **Uses existing credentials**: no new API keys or accounts needed
- **Local report**: the report is served locally on your machine only, never hosted externally
- **Credentials never touched**: LambdaLens uses boto3's standard credential chain, never reads or stores your AWS keys directly

---

## Contributing

Contributions are welcome. Please open an issue first to discuss what you'd like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License, see the [LICENSE](LICENSE) file for details.

---

## Author

**Prithish Samanta**

Built with Amazon Nova 2 Lite for the Amazon Nova AI Hackathon.

---

## Acknowledgements

- [Amazon Nova](https://aws.amazon.com/ai/nova/), for the powerful reasoning model
- [Amazon Bedrock](https://aws.amazon.com/bedrock/), for the managed AI infrastructure
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), for the excellent AWS SDK
- [FastAPI](https://fastapi.tiangolo.com/), for the lightweight local server
- [Rich](https://rich.readthedocs.io/), for the beautiful terminal output
