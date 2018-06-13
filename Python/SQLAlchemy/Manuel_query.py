from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


#Model
from sqllitealchemy import Column, Integer, Numeric, String

class Cookie(Base)
    __tablename__ = 'cookies'
    
    cookie_id = Column(Integer,primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recie_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12,2))
    


Base.metadata.create_all(engine)

cc_cookie = Cookie(...)
session.add(cc_cookie)
session.commit()
print(cc_cookie.cookie_id)
#save several objects together
#c1,c2 = Cookie(...)
session.bulk_save_objects([c1,c2])
session.commit()


#Select statement
cookies = session.query(Cookie).all()

    
