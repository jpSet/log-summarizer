import sqlite3
import textwrap
import os
from anthropic import Anthropic
import argparse

# Outtput format
def print_summary(row):
    id_, source_file, summary, created_at = row
    print("=" * 70)
    print(f"ID:          {id_}")
    print(f"Source file: {source_file}")
    print(f"Created at:  {created_at}")
    print("-" * 70)
    print(textwrap.fill(summary, width=70))
    print("=" * 70)

#Command line argument parsing
parser=argparse.ArgumentParser(description='Open file with the text to summarize.')

parser.add_argument('file_name', help='The file with the text to send to the Anthropic API')
args=parser.parse_args()

#Get the API key from the environment variable and create an Anthropic client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

#Catch the file content and prepare it for sending to the API
if args.file_name:
    with open(args.file_name, 'r') as file:
        text_to_summarize = file.readlines()
        
fileContent = [line.strip() for line in text_to_summarize]
text_to_send = "\n".join(fileContent) 

#Prompt definition for the Anthropic API
prompt = (
    "Summarize the following support ticket in a few sentences. "
    "Focus on the issue, root cause, and resolution. "
    "Respond in plain text only, with no markdown formatting "
    "(no #, **, -, or other symbols).\n\n"
    "--- TICKET CONTENT START ---\n"
    f"{text_to_send}\n" #Ticket content from the file is inserted here
    "--- TICKET CONTENT END ---"
)

#Send the prompt to the Anthropic API and get the summary
response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=300,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

#Store the summary in a SQLite database
summary = response.content[0].text
conn = sqlite3.connect("logsum.db")

conn.execute("""
    CREATE TABLE IF NOT EXISTS summaries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_file TEXT,
        summary TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

conn.execute(
    "INSERT INTO summaries (source_file, summary) VALUES (?, ?)",
    (args.file_name, summary)
)

#Retrieve and print all summaries from the database
cursor = conn.cursor()
cursor.execute("SELECT * FROM summaries")
rows = cursor.fetchall()

for row in rows:
   # print(f"ID: {row[0]}, Source File: {row[1]}, Summary: {row[2]}, Created At: {row[3]}")
   print_summary(row)
    
conn.commit()
conn.close()