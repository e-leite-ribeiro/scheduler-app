# Scheduling App

A simple Python application that reads events from a CSV file and adds them to a Google Calendar. Dockerized for easy deployment.

---

## Features

- Reads events from a CSV (`schedule.csv`)
- Sends events to Google Calendar using a service account
- Handles timezone-aware scheduling
- Fully containerized with Docker and Docker Compose

---

## Requirements

- Docker
- Docker Compose
- Google service account with access to the target calendar

---

## Project Structure

credentials, data and .env file should be provided by the user. Check the .env.example file for the necessary data please.

```bash
.
├── app/
│ ├── main.py
│ └── config.py
├── credentials/
│ └── credentials.json
├── data/
│ └── schedule.csv
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── .env
```

## CSV Format

The CSV file must have the following columns:

`summary,start,end,description,location`

**Example:**

Technical Interview,2026-01-04T16:00:00,2026-01-04T16:30:00,Discuss project,GoogleMeet
Gym,2026-01-04T18:00:00,2026-01-04T19:00:00,Training,Gym
Doctor apointment,2026-01-04T20:00:00,2026-01-04T20:30:00

- Dates must be in **ISO 8601 format** (`YYYY-MM-DDTHH:MM:SS`)
- `start` and `end` must include time; timezone is handled separately via `TIMEZONE`.

## How to Run

Build and start the container:

```bash
docker compose up --build
```

The app will now read schedule.csv and push events to the Google Calendar specified in your service account.

## Notes

Make sure the service account has write access to the target calendar.
Events will appear in the calendar corresponding to the calendar ID specified in config.py.
