# AWS Nova Lambda Debugger

Analyze AWS Lambda CloudWatch logs using **AWS Bedrock Nova 2 Lite**. Fetches function metadata and recent logs, runs an AI-powered diagnosis, and opens an HTML report in your browser.

## What it does

- **Fetches** Lambda configuration and CloudWatch log streams (configurable time window)
- **Analyzes** logs with Nova 2 Lite and returns a structured diagnosis (summary, health, errors with causes and fixes)
- **Serves** an HTML report at `http://localhost:8000/report` with the diagnosis and metadata

## Prerequisites

- **Python 3.9+**
- **AWS credentials** configured (e.g. `~/.aws/credentials` or env vars)
- **AWS Bedrock** access in your account (Nova 2 Lite model)
- Lambda and CloudWatch Logs in the same region you use below

## Setup

1. **Clone and enter the project**
   ```bash
   cd aws_nova_project
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment variables** (optional; create a `.env` in the project root)
   - `AWS_REGION` – e.g. `us-east-2` (used by the analyzer/Bedrock client; fetcher uses the region you pass in code)

## Usage

Edit `test_app.py` to set your Lambda function name, region, and lookback window:

```python
data = fetch_all_data(
    function_name="your-lambda-function-name",
    region="us-east-2",
    hours=24
)
```

Then run:

```bash
python test_app.py
```

The script will:

1. Fetch Lambda metadata and recent CloudWatch logs
2. Send them to Nova 2 Lite for analysis
3. Print the diagnosis to the terminal
4. Start a local server and open the report in your browser at `http://localhost:8000/report`

## Project structure

```
aws_nova_project/
├── core/
│   ├── fetcher.py   # Lambda metadata + CloudWatch log fetching (boto3)
│   └── analyzer.py # Log analysis via Bedrock Nova 2 Lite
├── server/
│   ├── app.py       # FastAPI app; serves /report and opens browser
│   └── templates/
│       └── report.html
├── test_app.py      # Main entry: fetch → analyze → print → start server
├── test_analyzer.py # Fetch + analyze only (no server)
├── requirements.txt
└── README.md
```

## License

Use and modify as needed for your project.
