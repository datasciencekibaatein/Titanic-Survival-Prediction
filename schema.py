from pydantic import BaseModel


class Passenger(BaseModel):
    Pclass:int
    Sex:str
    Age:float
    SibSp:int
    Parch:int
    Fare:float
    Embarked:str

    model_config = {
        "json_schema_extra":{
            "examples":[
                {
                "Pclass":3,'Sex':"male","Age":22.0,
                "SibSp":1,"Parch":0,'Fare':7.34,'Embarked':"S"
                }
            ]
        }
    }