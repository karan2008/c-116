# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "karan" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

@app.route('/father')
def father_page():
    return render_template('father.html')

@app.route('/mother')
def mother_page():
    return render_template('mother.html')

@app.route('/friend')
def friend_page():
    return render_template('friend.html')

if __name__ == '__main__':
    app.run(debug=True)




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
