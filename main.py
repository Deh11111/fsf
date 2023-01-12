from flask import Flask
from flask_restful import Api,Resource,reqparse,abort
from gevent.pywsgi import WSGIServer
from bd import server,error,server_hour

app = Flask(__name__)
api=Api()

parser = reqparse.RequestParser()
parser.add_argument("server",type=str)

class Main(Resource):
    def get(self,server_code):
        try:
            if server_code == "all":
                return server
            else:
                return server[server_code]
        except:
            if server_code not in server:
                abort(404, message="Not founds")
            else:
                return error 

    # def delete(self,server_code):
    #     del server[server_code]
    #     return server

    # def post(self,server_code): 
    #     server[server_code] = parser.parse_args()
    #     return server

    # def put(self,server_code):
    #     server[server_code] = parser.parse_args()
    #     return server

class Day(Resource):
    def get(self,server_code,key_id):
        if f"{server_code}/{key_id}"==str(f"{server_code}/1"):
            return server_hour[server_code]["result"]
        else:
            return server_hour[server_code]["result"][key_id]


api.add_resource(Main,"/api/v1/server/<string:server_code>")
api.add_resource(Day,"/api/v1/server/<string:server_code>/<int:key_id>")

api.init_app(app)

if __name__=="__main__":
    print("start")
    app.run(debug=True,port=3000,host="127.0.0.1")
    # http_server = WSGIServer(('', 3000), app)
    # http_server.serve_forever()