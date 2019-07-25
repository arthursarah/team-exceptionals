from flask import Flask, render_template, request,redirect
import os

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("home.html")

@app.route('/get_loc')
def get_loc():
    location=request.args.get('location')
    return redirect("/",code=302)
    print(location)
    
    
    
    
if __name__ == '__main__':
    port=os.environ.get('PORT', 5000)
    app.run(debug=True, host='0.0.0.0', port=port)