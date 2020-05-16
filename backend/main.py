from flask import Flask, request, render_template
from prediction import cleanandtransform


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('search.html')


@app.route('/report/', methods=['GET'])
def report():
    searchText = request.args.get('searchText').encode('ascii', 'ignore').decode('ascii')
    prediction = cleanandtransform.clean_typed_data(str(searchText))
    return render_template('report.html', text=prediction)


@app.route('/analysis')
def analysis():
    return render_template('analysis.html')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(port=5000, debug=True,threaded=True)
