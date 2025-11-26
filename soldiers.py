from pydantic import BaseModel, Field

class Soldier(BaseModel):
    Personal_number:int
    first_name:str
    last_name:str
    sex:str
    city:str
    distance:int


def list_soldiers(csvreader):
    soldiers=[]
    for soldier in csvreader:
        soldier=Soldier(**soldier)
        soldiers.append(soldier)
    return soldiers