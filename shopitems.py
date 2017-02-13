from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Store, Base, ShopItem, User

engine = create_engine('sqlite:///storelist.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="David Todd", email="dtodd@gmail.com",
             picture='http://code-love.com/wp-content/uploads/2015/11/logo-udacity.png')
session.add(User1)
session.commit()

# Denali Store
store1 = Store(user_id=1, name="Denali")

session.add(store1)
session.commit()

shopItem1 = ShopItem(user_id=1, name="The Underground",
                     description="a tour of a young slave",
                     price="$3.59", category="Book", store=store1)

session.add(shopItem1)
session.commit()

shopItem2 = ShopItem(user_id=1, name="USB Adapter",
                     description="Dual-Band, Wireless-N",
                     price="$25.50", category="Electronic", store=store1)

session.add(shopItem2)
session.commit()

shopItem3 = ShopItem(user_id=1, name="Step Ladder",
                     description="folding 3-step, steel fram",
                     price="$33.99", category="Tool", store=store1)

session.add(shopItem3)
session.commit()

shopItem4 = ShopItem(user_id=1, name="HDMI Cable",
                     description="6 feet, high speed",
                     price="$5.99", category="Electronic", store=store1)

session.add(shopItem4)
session.commit()

shopItem5 = ShopItem(user_id=1, name="Kettlebell", description="12 pound",
                     price="$12.99", category="Sport", store=store1)

session.add(shopItem5)
session.commit()


# Rainier Store
store2 = Store(user_id=1, name="Rainier")

session.add(store2)
session.commit()


shopItem1 = ShopItem(user_id=1, name="Remote Control",
                     description="for sound bar, universal",
                     price="$27.99", category="Electronic", store=store2)

session.add(shopItem1)
session.commit()

shopItem2 = ShopItem(user_id=1, name="TV Stick",
                     description="with voice control, streaming media player",
                     price="$35.99", category="Electronic", store=store2)

session.add(shopItem2)
session.commit()


# Pikes Store
store3 = Store(user_id=1, name="Pikes")

session.add(store3)
session.commit()


shopItem1 = ShopItem(user_id=1, name="TV Gaming",
                     description="affordable gaming oin your HDTV",
                     price="$118.99", category="Electronic", store=store3)

session.add(shopItem1)
session.commit()

shopItem2 = ShopItem(user_id=1, name="The Wolf",
                     description="a story of lost in the wilderness",
                     price="$7.89", category="Book", store=store3)

session.add(shopItem2)
session.commit()

shopItem3 = ShopItem(user_id=1, name="VR Camera",
                     description="360 degree, real high resolution",
                     price="$229.95", category="Electronic", store=store3)

session.add(shopItem3)
session.commit()


# Longs Store
store4 = Store(user_id=1, name="Longs")

session.add(store4)
session.commit()


shopItem1 = ShopItem(user_id=1, name="Thermostat",
                     description="works with voice control",
                     price="$222.99", category="Tool", store=store4)

session.add(shopItem1)
session.commit()

shopItem2 = ShopItem(user_id=1, name="Earbuds",
                     description="for fitness with activity tracker",
                     price="$125.99", category="Electronic", store=store4)

session.add(shopItem2)
session.commit()

shopItem3 = ShopItem(user_id=1, name="Outlet Coverplate",
                     description="with LED night lights",
                     price="$16.50", category="Tool", store=store4)

session.add(shopItem3)
session.commit()

shopItem4 = ShopItem(user_id=1, name="Elegy",
                     description="a personal analysis of a culture in crisis",
                     price="$8.95", category="Book", store=store4)

session.add(shopItem4)
session.commit()


# Sanford Store
store5 = Store(user_id=1, name="Sanford")

session.add(store5)
session.commit()


shopItem1 = ShopItem(user_id=1, name="Charding Stand",
                     description="wireless charge, fast",
                     price="$33.95", category="Electronic", store=store5)

session.add(shopItem1)
session.commit()

shopItem2 = ShopItem(user_id=1, name="Printer",
                     description="wireless with mobile printing",
                     price="$64.95", category="Electronic", store=store5)

session.add(shopItem2)
session.commit()

shopItem3 = ShopItem(user_id=1, name="Projector",
                     description="LED video projector, supprot 1080P",
                     price="$96.95", category="Electronic", store=store5)

session.add(shopItem3)
session.commit()

shopItem4 = ShopItem(user_id=1, name="Multifunction Scale",
                     description="with LCD display",
                     price="$23.95", category="Tool", store=store5)

session.add(shopItem4)
session.commit()


print "added shop items!"
