#!/usr/bin/env python3.5

import json
import configparser
from aiohttp import web
from pprint import pprint
from sqlalchemy import create_engine, Column, Table, Text, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

config = configparser.ConfigParser()
config.read("config.ini")
user = config.get("database", "user")
password = config.get("database", "password")
host = config.get("database", "host")
db_name = config.get("database", "db_name")

engine = create_engine(
  'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(
      user, password, host, db_name
    )
  )
#engine.execute('SET NAMES utf8')
#engine.execute('SET character_set_connection=utf8;')
conn = engine.connect()
meta = MetaData()
Base = declarative_base(metadata=meta)
Session = sessionmaker()
Session = sessionmaker(bind=engine)
session = Session()

class Movie(Base):
  __tablename__ = 'movie'
  id = Column(Integer(), primary_key=True, nullable=False)
  level = Column(Integer())
  title = Column(Text())
  description = Column(Text())
  actors = Column(Text())
  genre = Column(Text())
  year = Column(Integer())
  country = Column(Text())
  director = Column(Text())

  def __repr__(self):
      return "<Movie(title='%s', description='%s', actors='%s')>" % (
                              self.title, self.description, self.actors)

mvs=[]
for m in session.query(Movie).order_by(Movie.id).filter(Movie.title.isnot(None)):
  mvs.append({'name':m.title, 'description':m.description, 'actors':m.actors})

async def movies(request):
  data = json.dumps({'result':mvs}, sort_keys=True)
  return web.Response(text=data, content_type='application/json')

app = web.Application()
app.router.add_get('/movies', movies)

web.run_app(app, host='0.0.0.0', port=8080)


