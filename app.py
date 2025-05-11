from flask import Flask
import json

app = Flask( __name__ )

@app.route( '/' )
def flikker():
    json_file = 'usuarios.json'

    with open( json_file, encoding='utf-8' ) as file:
        json_file = json.load( file )

    return json_file

if __name__ == '__main__':
    app.run()
