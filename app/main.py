import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo
from google.oauth2 import service_account
from googleapiclient.discovery import build
from .config import CSV_PATH, TIMEZONE, GOOGLE_APPLICATION_CREDENTIALS, CALENDAR_ID

SCOPES = ["https://www.googleapis.com/auth/calendar"]
credentials = service_account.Credentials.from_service_account_file(
    GOOGLE_APPLICATION_CREDENTIALS, scopes= SCOPES
)
service = build("calendar", "v3", credentials=credentials)


try:
    df = pd.read_csv(CSV_PATH)
except FileNotFoundError:
    print(f".csv not found at {CSV_PATH}")
    exit(1)


required_columns = {"summary", "start", "end"}
if not required_columns.issubset(df.columns):
    print(f".csv must have columns {required_columns}")
    exit(1)

for _, row in df.iterrows():
    start_dt = datetime.fromisoformat(row["start"]).replace(tzinfo=ZoneInfo(TIMEZONE))
    end_dt   = datetime.fromisoformat(row["end"]).replace(tzinfo=ZoneInfo(TIMEZONE))
    event = {
        "summary": row["summary"],
        "start": {"dateTime": start_dt.isoformat(), "timeZone": TIMEZONE},
        "end": {"dateTime": end_dt.isoformat(), "timeZone": TIMEZONE},
        "description": row.get("description", ""),
        "location": row.get("location", ""),
    }
    created_event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    print(f"Created event: {created_event.get('summary')} at {created_event.get('start')['dateTime']}")


