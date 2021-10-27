from flask import  Flask, request, make_response,jsonify





POSTS = {
    "id":1,
    "title":"sample1",
    "text":"sample text"
},
{
    "id":3,
    "title":"sample2",
    "text":"sample text2",
},
{
    "id":3,
    "title":"sample3",
    "text":"sample text3",
}

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

@app.route("/search", methods=["GET", "POST"])
def search():
    response_data = {
        "success":True,
        "data":[]      
        }
    if request.method == "GET":
        response_data["data"] = POSTS
        return jsonify(response_data)
    elif request.method == "POST":
        data = request.json
        if "id" not in response_data or "title" not in response_data or "text" not in response_data:
            response_data["success"] = False
            response_data["error"] = "Pleace all information"
            response = jsonify(response_data)
            response.status_code = 400
        else:
            POSTS.append(data)
            response_data["data"] = POSTS
            response = jsonify(response_data)
            response.status_code = 201
        
        return response



if __name__=="__main__":
    app.run(debug=True)

