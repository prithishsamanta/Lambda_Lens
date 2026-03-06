from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import webbrowser
import threading
import uvicorn

# global variable to store diagnosis data
diagnosis_data = {}

templates = Jinja2Templates(directory="server/templates")

app = FastAPI()

def start_server(diagnosis: dict):
    global diagnosis_data
    diagnosis_data = diagnosis

    # open browser after 1.5 seconds to give uvicorn time to start
    threading.Timer(1.5, lambda: webbrowser.open("http://localhost:8000/report")).start()
    
    # start the server
    uvicorn.run(app, host="0.0.0.0", port=8000)

@app.get("/report")
def get_report(request: Request):
    return templates.TemplateResponse("report.html", {
        "request": request,
        "data": diagnosis_data
    })