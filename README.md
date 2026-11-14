## StudyMate API

Install the dependencies and start the development server:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Open http://127.0.0.1:8000/ to verify that the API is running. The `/ask?question=...`
endpoint uses the `NEBIUS_API_KEY` value from `.env`.