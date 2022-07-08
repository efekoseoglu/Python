from flask import Flask
from flask_restful import Api, Resource

app= Flask(__name__)
api=Api (app)

city_names={"kastamonu":{"temperature":10,"location":"blacksea"},
            "adana":{"temperature":20,"location":"mediterranean"}}

@app.route("/")
def index():
    return "Efe Köseoðlu"

@app.route("/city")
class Show_info (Resource):
    def get(self,city):
        return city_names[city]
    def post(self):
        return {"data":"posted"}

api.add_resource(Show_info,"/<string:city>")

if __name__ == "__main__":
    app.run(debug=True)