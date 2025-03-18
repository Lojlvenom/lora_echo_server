from fastapi import FastAPI
import uvicorn
app = FastAPI()

sensor_data_db = []


@app.post("/sensors")
async def show_sensor_data(sensor_data):
    sensor_data_db.append[sensor_data]
    return sensor_data_db[-1]


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')