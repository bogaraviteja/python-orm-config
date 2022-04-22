# use this command before you run pip3 install SQLAlchemy or run command pip3 install requirement.txt
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, BigInteger, String, ForeignKey, Boolean, Date, Text, event, Sequence, DateTime, BigInteger, LargeBinary, Text,Float
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relation
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('postgresql+psycopg2://postgres:ravi@localhost:5432/pythonConfig')

# please uncomment the below statement to use SQLITE database
# engine = create_engine('sqlite:///source_data.db', echo=True)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()
Model = declarative_base()

class UserInfo(Model):
    __tablename__='userinformation'
    user_id = Column('user_id',Integer,primary_key=True)
    user_name = Column(Text)
    user_mobile = Column(BigInteger)
    user_email = Column(String(100))

import datetime
def _get_date():
    return datetime.datetime.now()

class EmailSent(Model):
    __tablename__='emailsent'
    id = Column('id', Integer, primary_key=True)
    user_id = Column(Integer)
    created_at = Column(Date, default=_get_date)
    updated_at = Column(Date, default=_get_date)
    email_sent=Column(String(100))

    def __repr__(self):
        return " id='%s',user_id='%s',created_at='%s',update_at='%s',email_sent='%s' " % (
            self.id,self.user_id,self.created_at,self.updated_at,self.email_sent
        )

Model.metadata.create_all(engine)