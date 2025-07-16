from fastapi import FastAPI, Response, Query
from fastapi.responses import StreamingResponse
import pandas as pd

app = FastAPI()

df = pd.read_csv("data/accumulation-accounts-2008-2023-provisional.csv")

# print(df.head())
@app.get("/")
def main():
    headers = {'Content-Disposition': 'attachment; filename="data/accumulation-accounts-2008-2023-provisional.csv"'}
    return Response(df.to_json(orient="records"), media_type="application/json")