from datetime import datetime
from sqlachemy import DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref

#USER MODEL
class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer(),primary_ky=True)
    username = Column(String(15), nullable=False, unique=True)
    email_address = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=da...)
    
    
#ORDER MODEL
class Order(Base):
    __tablename__ = 'orders'
    
    order_id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.user_id'))
    shipped = Column(Boolean(), default=False)
    
    user = relationship("User", backref=backref('orders, order_by=...)

#LINEITEM MODEL
class LineItem(Base):
    __tablename__ = 'line_items'
    
    line_item_id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.order_id'))                    
    cookie_id = Column(Integer(), ForeignKey('cookies.cookie_id'))
    quantity = Column(Integer())
    extended_cost = Column(Numeric(12,2))
    
    order = relationship("Order", backref=backref('line_items', order...)
    cookie = relationship("Cookie", uselist=False)   
                         
#PERSIST THEM
Base.metadata.create_all(engine)  
                         
cookiemon = User(...)
session.add(cookiemon)
o1 = Order()
o1.user = cookiemon
session.add(o1)      

line = LineItem(...)
line.cookie = cc_cookie
o1.line_items.append(line)
o1.line_items.append(line2)
session.commit()                         

#JOIN EXAMPLE                         
query = session.query(Order.order_id, User.username, User.phone, Cookie.cookie_name, LineItem.quantity, LineItem.extended_cost)
query.join(User).join(LineItem).join(Cookie)
results = query.filter(User.username == 'cookiemon').all()

#ANOTHER JOIN EXAMPLE                         
query = session.query(User.username, func.count(Order.order_id))
query = query.outerjoin(Order).group_by(User.username)
                         
                         
                                                  
