
from fastapi import FastAPI, File, UploadFile
import csv
from soldiers import add_solder,ensure_table_soldiers
from buildings  import Buildings,ensure_table_buildings

app =FastAPI()

@app.post("/assignWithCsv")
async def upload_single_file(file: UploadFile = File(...)):
    ensure_table_soldiers()
    ensure_table_buildings()
    building1=Buildings(1)
    building2=Buildings(2)

    with open(file.filename,encoding="utf8")as data:
        csvreader=csv.DictReader(data)
        for solder in csvreader:
            add_solder(solder)
    return {"filename": file.filename}

