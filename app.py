import flask
import json
import datetime
import logging
from logging.handlers import RotatingFileHandler
import src.Database
app = flask.Flask(__name__)
db = src.Database.DatabaseAccesser('./src/db/')

app.logger.setLevel(logging.DEBUG)
debug_file_handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=10)
app.logger.addHandler(debug_file_handler)

@app.route('/')
def index():
    icons_html = ''
    for data in db.Loads():
        icons_html += data.GetImgString()
#        icons_html += data.GetHtmlString()
    return flask.render_template('index.html', icons=flask.Markup(icons_html))

@app.route('/AppendUrl', methods=['POST'])
def post_append_url():
    app.logger.debug('-------------------------------- post_append_url()')
    urls = flask.request.json['Urls']
    result = ''
    html = ''
    css = {}
    exception = ''
    message = ''
    return_data = {}
    for line in urls.split('\n'):
        app.logger.debug('debug message: {0}'.format(line))
        if 0 == len(line.strip()):
            continue;
        try:
            app.logger.debug('-------------------------------- InsertGet前')
            data = db.InsertGet(line)
            app.logger.debug('-------------------------------- InsertGet後:{0}'.format(data))
            # return {class_name: {'href': '', 'title': '', 'data_url_string': ''}}, }
            # JS側で新規追加と更新を行う。class_nameが既存なら更新、無いなら新規追加する
            if None is not data:
#                html += data.GetImgString()
#                result += "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) + " 追加/更新 " + line + '\n'
                return_data.update({data.Classname: {'href': data.Url, 'title': data.Title, 'src': data.DataUri}})
            else:
#                result += "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) + " 既存 " + line + '\n'
                message += '既存 ' + line + '\n'
                pass
        except Exception as e:
#            result += "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) + " 失敗 " + line + str(e.args) +'\n'
            exception += "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) + " 失敗 " + line + str(e.args) +'\n'
#    return_data = {"result": result, "html": html, "css": css}
#    return_data.update({"result": result})
    if 0 < len(message.strip()):
        return_data.update({'message': message})
    if 0 < len(exception.strip()):
        return_data.update({'exception': exception})
    return flask.jsonify(ResultSet=json.dumps(return_data))

if __name__ == '__main__':  
    app.run() # localhost:5000
#    app.run(host="127.0.0.1", port=8080)

