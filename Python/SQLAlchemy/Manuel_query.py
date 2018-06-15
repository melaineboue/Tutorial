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
cookie = session.query(Cookie.cookie_name,Cookie.quantity).first()
cookies = session.query(Cookie).order_by(Cookie.quantity)
cookies = session.query(Cookie).order_by(desc(Cookie.quantity))
cookies = session.query(Cookie).order_by(Cookie.quantity).limit(2)
                      
                        
#print([result.cookie_name for result in cookies])
for cookie in cookies:
    print(cookie)
    print('{:3} - {}'.format(cookie.quantity, cookie.cookie_name))
     
                       
#Database functions
inv_count = session.query(func.sum(Cookie.quantity)).scalar()
print(inv_count)
rec_count = session.query(func.count(Cookie.cookie_name)).first()
rec_count = session.query(func.count(Cookie.cookie_name).label('inventory_count')).first()
print(rec_count.keys())
print(rec_count.inventory_count)
record = session.query(Cookie).filter_by(cookie_name='chocolate chip').first()                       
record = session.query(Cookie).filter(cookie_name == 'chocolate chip').first()
cookies = session.query(Cookie).filter(Cookie.cookie_name.like('%chocolate%')) 
query = session.query(Cookie.cookie_name, cast((Cookie.quantity * Cookie.unit_cost),Numeric(12,2)).label('inv_cost'))  
#OR(or_) AND(and_) NOT(not_)                      
query = session.query(Cookie).filter(or_(Cookie.quantity.between(10,50),Cookie.cookie_name.contains('chip')))
#Others functions
between(cleft,cright) : find where the column is between cleft and cright                       
distinct()            : find only unique values for column             
in_([list])           :  find where the column is in the list                    
is_(None)             : find where column is None                      
contains('string')    : find where the column has 'string in it, Case sensitive                      
endswitch('string')   : find where column end with 'string', Case sensitive                       
startswitch('string')                       
                       
 #UPDATE                       
 cc_cookie = session.query(Cookie).filer(...).first()
 cc_cookie.quantity = cc_cookie.quantity + 120
 session.commit()

 #DELETE
 dcc_cookie = session.query(Cookie).filter(Cookie.cookie_name == "peanut butter").one()                      
 session.delete(dcc_cookie)
 session.commit()                      
                       
Good example               
http://www.leeladharan.com/sqlalchemy-query-with-or-and-like-common-filters
