from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SoilData(db.Model):
    __tablename__ = 'soil_data'

    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    moisture = db.Column(db.Float)
    pH = db.Column(db.Float)
    conductivity = db.Column(db.Float)
    nitrogen = db.Column(db.Float)
    phosphorus = db.Column(db.Float)
    potassium = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    
    # Kolom baru
    tanaman = db.Column(db.String(50))
    tanaman_no = db.Column(db.Integer)

    def __repr__(self):
        return f'<SoilData {self.id}>'