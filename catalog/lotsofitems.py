from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, Base, CategoryItem, User

engine = create_engine('sqlite:///categoryitems.db')
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
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# CategoryItem for Soccer
category1 = Category(user_id=1, name="Soccer")
session.add(category1)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Soccer Cleats",
                            description="Float right past the competition, running so incredibly light and cushioned that you'll be hauntingly hard to catch!",
                            category=category1)

session.add(categoryItem1)
session.commit()


categoryItem2 = CategoryItem(user_id=1, name="Soccer Jersey",
                            description="Fit for the field in energetic colors, this men's soccer jersey features sweat-wicking climalite fabric to keep you dry and comfortable.",
                            category=category1)

session.add(categoryItem2)
session.commit()


# CategoryItem for Hockey
category2 = Category(user_id=1, name="Hockey")
session.add(category2)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Stick",
                            description="High impact glass filled nylon blade.",
                            category=category2)

session.add(categoryItem1)
session.commit()


categoryItem2 = CategoryItem(user_id=1, name="Hockey Jersey",
                            description="Blue custom 'Slap Shot' hockey jersey.",
                            category=category2)

session.add(categoryItem2)
session.commit()


# CategoryItem for Basketball
category3 = Category(user_id=1, name="Basketball")
session.add(category3)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Ball",
                            description="Premium Outdoor Cover with Durable Soft Grip Technology .",
                            category=category3)

session.add(categoryItem1)
session.commit()


categoryItem2 = CategoryItem(user_id=1, name="NBA Jersey",
                            description="Get Your Future Nba Star Outfitted In The Same Jersey As Their Nba Superstar With The Official Nba Replica Jersey By Adidas.",
                            category=category3)

session.add(categoryItem2)
session.commit()

print "added category items!"
