# log-summarizer
Python CLI tool that reads log/text files and uses the Anthropic Claude API to summarize   them.

## Features
- Summarizes log/ticket files using Claude
- Stores each summary in a local SQLite database
- Prints the summary history in a readable format

## Requirements
- Python 3.x
- An Anthropic API key

## Installation
```
git clone https://github.com/jpSet/log-summarizer.git
cd log-summarizer
pip install -r requirements.txt
```
Set your API key as an environment variable:
```
# Windows
set ANTHROPIC_API_KEY=your-key-here

# macOS/Linux
export ANTHROPIC_API_KEY=your-key-here
```

## Usage
```
python summarized_log.py samples/sample_ticket_log.txt
```

## Example output

Running the tool on the sample ticket:

```
python summarized_log.py samples/sample_ticket_log.txt
```

Each summary is stored in `logsum.db`, and the tool prints the full history. Example entry:

```
======================================================================
ID:          5
Source file: samples/sample_ticket_log.txt
Created at:  2026-10-24 21:23:07
----------------------------------------------------------------------
Employee M. Silva reported that an extra hours request submitted on
August 14 remained stuck in "Pending Manager Approval" status even
though the manager had successfully approved it through the dashboard.
The root cause was a race condition where an AI agent's background re-
evaluation process was overwriting the Status field back to "Pending"
after the manager's manual approval. The development team resolved the
issue by modifying the agent flow to include a guard condition that
prevents the Status field from being overwritten if a manual approval
timestamp is newer than the agent's last read time. The fix was
verified in staging and deployed, allowing the request to correctly
transition to "ManagerApproved" status.
======================================================================
```
