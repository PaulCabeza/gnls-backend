from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Carrier(BaseModel):
    name: str
    trucks_per_day: int


ROUTES = {
    ("New York", "Washington DC"): [
        Carrier(name="Knight-Swift Transport Services", trucks_per_day=10),
        Carrier(name='J.B. Hunt Transport Services Inc', trucks_per_day=7),
        Carrier(name='YRC Worldwide', trucks_per_day=5)
    ],
    ('San Francisco', 'Los Angeles'): [
        Carrier(name="XPO Logistics", trucks_per_day=9),
        Carrier(name="Schneider", trucks_per_day=6),
        Carrier(name="Landstar Systems", trucks_per_day=2),
    ]
}

DEFAULT_CARRIERS = [
    Carrier(name="UPS Inc.", trucks_per_day=11),
    Carrier(name="FedEx Corp", trucks_per_day=9),
]

@app.get('/search', response_model=List[Carrier])
def search_carriers(from_city: str = Query(...), to_city: str = Query(...)):
    def normalize(city: str) -> str:
        return city.split(',')[0].strip()
    key = (normalize(from_city), normalize(to_city))
    return ROUTES.get(key, DEFAULT_CARRIERS)