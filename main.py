from flask import Flask, Response, send_from_directory, current_app 
import os
app = Flask(__name__)

# @app.route("/")
# def hello():
#     return '''
#         <html><body>
#         Hello. <a href="/getPlotCSV">Click me.</a>
#         </body></html>
#         '''

@app.route("/download/<path:filename>", methods=['GET', 'POST'])
def download_file(filename):
    print(current_app.root_path)
    uploads = os.path.join(r'E:')
    print(uploads)
    return send_from_directory(directory=uploads, path=os.path.join(uploads, filename), filename=filename)

if __name__ == '__main__':
    app.run(debug=True)