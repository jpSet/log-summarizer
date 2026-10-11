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

Set your API key as an environment variable (Windows):
```
set ANTHROPIC_API_KEY=your-key-here
```

## Usage
```
python summarized_log.py samples\sample_ticket_log.txt
```

## Screenshot
```
<img width="2909" height="1362" alt="{957FEB54-1925-4B47-9FE4-877C188ACCEF}" src="https://github.com/user-attachments/assets/dfb2bb62-629b-464f-b9bf-d6b1a65f9d07" />

```
