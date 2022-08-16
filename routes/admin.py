from flask import Blueprint, request,jsonify
import bcrypt
from functions_jwt import validate_token
from database import mydb
user_admin = Blueprint('admin',__name__)

print(__name__)

# @user_admin.before_request
# def verify_token_middleware():
#     token = request.headers['Authorization'].split(" ")[1]
#     return validate_token(token,output=False)

@user_admin.route('/createUser',methods=['POST'])
def createUser():
    #reciving datap
    username = request.json['username']
    nombre =  request.json['nombre']
    apellido =  request.json['apellido']
    password = request.json['password']
    dni =  request.json['dni']
    rol = request.json['rol_id']

    # -------- END DATA ------------- # 
    if username and nombre and password and apellido and dni and rol:
        hashed_password = bcrypt.hashpw(request.json['password'].encode('utf-8'),bcrypt.gensalt(10))
        print(hashed_password)
        id = mydb.users.insert_one({'username':username,'_id':str(dni),'password':hashed_password,'apellido':apellido,'nombre':nombre,'rol_id':rol}).inserted_id
        
        response = jsonify({
            '_id': str(id),
            'nombre': nombre,
        })
        response.status_code = 201
        return response
    else:
        return not_found()