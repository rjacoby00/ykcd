from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
	return '''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>ykcd</title>

  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
  <link rel="stylesheet" href="https://code.getmdl.io/1.2.1/material.indigo-pink.min.css">
  <script defer src="https://code.getmdl.io/1.2.1/material.min.js"></script>
  <link rel="stylesheet" href="https://rawgit.com/rjacoby00/ykcd/master/styles/index.css">
</head>

<body>

  <header>
    <h1>ykcd</h1>
  </header>

  <main>
    <p>Welcome to ykcd, the pointless site.</p>
  </main>
</body>
</html>
	
'''
if __name__ == "__main__":
	app.run()
