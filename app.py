from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
  'id' :1,
  'title' : 'Desktop Supprt',
  'location' : 'Karachi',
  'salary' : 'Rs. 70,000',
  },
  {
    'id' :2,
    'title' : 'Desktop Supprt',
    'location' : 'Karachi',
  },

  {
  'id' :3,
  'title' : 'Desktop Supprt',
  'location' : 'Karachi',
  'salary' : 'Rs. 70,000',
  },

  {
  'id' :4,
  'title' : 'Desktop Supprt',
  'location' : 'Karachi',
  'salary' : 'Rs. 70,000',
  },
]
  
@app.route('/')
def hello_waseem():
  return render_template('home.html', jobs=JOBS)
  
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)