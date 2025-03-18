from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
app = FastAPI()

sensor_data_db = []

class SensorData(BaseModel):
    data: dict


@app.get("/sensors/history")
def history():
    return sensor_data_db


@app.get("/sensors")
def get_latest():
    return sensor_data_db[-1]


@app.post("/sensors")
async def show_sensor_data(sensor_data: SensorData):
    data = sensor_data.data
    sensor_data_db.append(data)
    return sensor_data.data


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')