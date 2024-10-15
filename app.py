from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from models import db, SoilData
from flask_migrate import Migrate
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/soil_sensor_db'
db.init_app(app)
migrate = Migrate(app, db)

# Impor model
from models import SoilData, Pump

@app.route('/')
def index():
    # Menampilkan data terbaru
    data = SoilData.query.order_by(SoilData.timestamp.desc()).limit(10).all()
    return render_template('index.html', data=data)

@app.route('/data')
def data():
    # Menampilkan semua data
    data = SoilData.query.order_by(SoilData.timestamp.desc()).all()
    return render_template('data.html', data=data)

@app.route('/tanaman/<jenis_tanaman>')
def data_per_tanaman(jenis_tanaman):
    data = SoilData.query.filter_by(tanaman=jenis_tanaman).order_by(SoilData.timestamp.asc()).all()
    
    # Mempersiapkan data untuk grafik
    timestamps = [d.timestamp.strftime('%Y-%m-%d %H:%M:%S') for d in data]
    temperature = [d.temperature for d in data]
    moisture = [d.moisture for d in data]
    pH = [d.pH for d in data]
    conductivity = [d.conductivity for d in data]
    nitrogen = [d.nitrogen for d in data]
    phosphorus = [d.phosphorus for d in data]
    potassium = [d.potassium for d in data]
    
    return render_template('data_per_tanaman.html', data=data, jenis_tanaman=jenis_tanaman,
                           timestamps=timestamps,
                           temperature=temperature,
                           moisture=moisture,
                           pH=pH,
                           conductivity=conductivity,
                           nitrogen=nitrogen,
                           phosphorus=phosphorus,
                           potassium=potassium)


@app.route('/tanaman_no/<int:tanaman_no>')
def data_per_tanaman_no(tanaman_no):
    data = SoilData.query.filter_by(tanaman_no=tanaman_no).order_by(SoilData.timestamp.asc()).all()
    
    # Mempersiapkan data untuk grafik
    timestamps = [d.timestamp.strftime('%Y-%m-%d %H:%M:%S') for d in data]
    temperature = [d.temperature for d in data]
    moisture = [d.moisture for d in data]
    pH = [d.pH for d in data]
    conductivity = [d.conductivity for d in data]
    nitrogen = [d.nitrogen for d in data]
    phosphorus = [d.phosphorus for d in data]
    potassium = [d.potassium for d in data]
    
    return render_template('data_per_tanaman_no.html', data=data, tanaman_no=tanaman_no,
                           timestamps=timestamps,
                           temperature=temperature,
                           moisture=moisture,
                           pH=pH,
                           conductivity=conductivity,
                           nitrogen=nitrogen,
                           phosphorus=phosphorus,
                           potassium=potassium)


@app.route('/tanaman/<jenis_tanaman>/nomor/<int:tanaman_no>')
def data_tanaman(jenis_tanaman, tanaman_no):
    data = SoilData.query.filter_by(tanaman=jenis_tanaman, tanaman_no=tanaman_no).order_by(SoilData.timestamp.asc()).all()
    
    # Mempersiapkan data untuk grafik
    timestamps = [d.timestamp.strftime('%Y-%m-%d %H:%M:%S') for d in data]
    temperature = [d.temperature for d in data]
    moisture = [d.moisture for d in data]
    pH = [d.pH for d in data]
    conductivity = [d.conductivity for d in data]
    nitrogen = [d.nitrogen for d in data]
    phosphorus = [d.phosphorus for d in data]
    potassium = [d.potassium for d in data]
    
    return render_template('data_tanaman.html',
                           data=data,
                           jenis_tanaman=jenis_tanaman,
                           tanaman_no=tanaman_no,
                           timestamps=timestamps,
                           temperature=temperature,
                           moisture=moisture,
                           pH=pH,
                           conductivity=conductivity,
                           nitrogen=nitrogen,
                           phosphorus=phosphorus,
                           potassium=potassium)

@app.route('/daily_data')
def daily_data():
    # Query untuk mendapatkan rata-rata harian
    daily_data_query = db.session.query(
        func.date(SoilData.timestamp).label('date'),
        func.avg(SoilData.temperature).label('avg_temperature'),
        func.avg(SoilData.moisture).label('avg_moisture'),
        func.avg(SoilData.pH).label('avg_pH'),
        func.avg(SoilData.conductivity).label('avg_conductivity'),
        func.avg(SoilData.nitrogen).label('avg_nitrogen'),
        func.avg(SoilData.phosphorus).label('avg_phosphorus'),
        func.avg(SoilData.potassium).label('avg_potassium')
    ).group_by(func.date(SoilData.timestamp)).order_by(func.date(SoilData.timestamp)).all()

    # Mempersiapkan data untuk template
    dates = [d.date.strftime('%Y-%m-%d') for d in daily_data_query]
    avg_temperature = [float(d.avg_temperature or 0) for d in daily_data_query]
    avg_moisture = [float(d.avg_moisture or 0) for d in daily_data_query]
    avg_pH = [float(d.avg_pH or 0) for d in daily_data_query]
    avg_conductivity = [float(d.avg_conductivity or 0) for d in daily_data_query]
    avg_nitrogen = [float(d.avg_nitrogen or 0) for d in daily_data_query]
    avg_phosphorus = [float(d.avg_phosphorus or 0) for d in daily_data_query]
    avg_potassium = [float(d.avg_potassium or 0) for d in daily_data_query]

    return render_template('daily_data.html',
                           dates=dates,
                           avg_temperature=avg_temperature,
                           avg_moisture=avg_moisture,
                           avg_pH=avg_pH,
                           avg_conductivity=avg_conductivity,
                           avg_nitrogen=avg_nitrogen,
                           avg_phosphorus=avg_phosphorus,
                           avg_potassium=avg_potassium)

@app.route('/pump')
def pump_data():
    data = Pump.query.order_by(Pump.timestamp.desc()).all()
    
    # Memformat timestamp
    timestamps = [d.timestamp.strftime('%Y-%m-%d %H:%M:%S') for d in data]
    air = [d.air for d in data]
    nutrisi = [d.nutrisi for d in data]
    tanaman = [d.tanaman for d in data]
    tanaman_no = [d.tanaman_no for d in data]
    
    return render_template('pump.html',
                           data=data,
                           timestamps=timestamps,
                           air=air,
                           nutrisi=nutrisi,
                           tanaman=tanaman,
                           tanaman_no=tanaman_no)


@app.route('/add_pump_data', methods=['POST'])
def add_pump_data():
    # Mendapatkan data dari form POST
    air = request.form.get('air')
    nutrisi = request.form.get('nutrisi')
    tanaman = request.form.get('tanaman')
    tanaman_no = request.form.get('tanaman_no')

    # Membuat objek Pump baru
    new_pump_data = Pump(
        air=air,
        nutrisi=nutrisi,
        tanaman=tanaman,
        tanaman_no=tanaman_no
    )

    try:
        db.session.add(new_pump_data)
        db.session.commit()
        return redirect(url_for('pump_data'))
    except Exception as e:
        db.session.rollback()
        return f'Terjadi kesalahan: {e}', 500



@app.route('/add_data', methods=['POST'])
def add_data():
    # Memeriksa kunci API (opsional untuk keamanan)
    api_key = request.form.get('api_key')
    if api_key != app.config.get('API_SECRET_KEY', 'kunci-api-anda'):
        return 'Unauthorized', 401

    # Mendapatkan data dari form POST
    temperature = request.form.get('temperature')
    moisture = request.form.get('moisture')
    pH = request.form.get('pH')
    conductivity = request.form.get('conductivity')
    nitrogen = request.form.get('nitrogen')
    phosphorus = request.form.get('phosphorus')
    potassium = request.form.get('potassium')
    tanaman = request.form.get('tanaman')
    tanaman_no = request.form.get('tanaman_no')

    # Membuat objek SoilData baru
    new_data = SoilData(
        temperature=temperature,
        moisture=moisture,
        pH=pH,
        conductivity=conductivity,
        nitrogen=nitrogen,
        phosphorus=phosphorus,
        potassium=potassium,
        tanaman=tanaman,
        tanaman_no=tanaman_no
    )

    try:
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        db.session.rollback()
        return f'An error occurred: {e}', 500


if __name__ == '__main__':
    app.run(debug=True)
