"""
holidayテーブルの定義
"""

from holiday import db

# すでにholidayテーブルは作成済み
class Holiday(db.Model):
    __tablename__ ='holiday'
    holi_date = db.Column(db.Date, primary_key=True)
    holi_text = db.Column(db.String(20))

def __init__(self, holi_date, holi_text):
    self.holi_date=holi_date
    self.holi_text = holi_text

