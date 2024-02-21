"""Seed file to make sample data for db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Make a bunch of departments
p1 = Pet(name='Smiley', photo_url='https://images.unsplash.com/photo-1615751072497-5f5169febe17?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y3V0ZSUyMGRvZ3xlbnwwfHwwfHx8MA%3D%3D', species='dog', age=3, notes='Loves laying in bed!')
p2 = Pet(name='Pom Pom', photo_url='https://images.unsplash.com/photo-1582456891925-a53965520520?q=80&w=1587&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', species='dog', age=5, notes='Wiggles while she walks!', available=False)
p3 = Pet(name='Curly', photo_url='https://images.unsplash.com/photo-1620189507187-1ecc7e2e9cff?q=80&w=1587&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', species='dog', age=1, notes='Loves to run!')
p4 = Pet(name='Buddy', photo_url='https://images.unsplash.com/photo-1552053831-71594a27632d?q=80&w=1562&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', species='dog', age=6, notes="Ultimate companion dog!")
p5 = Pet(name='Milo', photo_url='https://images.unsplash.com/photo-1621371236495-1520d8dc72a5?q=80&w=1629&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', species='dog', age=10, notes="Enjoys relaxing outdoors.")
p6 = Pet(name='Happy', photo_url='https://images.unsplash.com/photo-1626736637845-53045bb9695b?q=80&w=1611&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', species='dog', age=11, notes="Loves walks around the neighborhood!", available=False)
p7 = Pet(name='Shadow', photo_url='https://images.unsplash.com/photo-1610902280143-d3a528844921?q=80&w=1587&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', species='dog', age=7, notes="Social butterfly!", available=False)

# p1 = Pet(name='sans', photo_url='https://static.wikia.nocookie.net/undertale/images/0/0f/Sans_battle_idle.gif', species='skeleton', age=20, notes='The easiest enemy. Can only deal 1 damage', available=True)
# p2 = Pet(name='Papyrus', photo_url='https://media1.tenor.com/m/cHVqk_UoNO4AAAAC/papyrus-undertale.gif', species='skeleton', age=18, notes='He likes to say: Nyeh heh heh!', available=True)
# p3 = Pet(name='Toby', photo_url='https://art.ngfiles.com/images/2521000/2521753_mikedueye_toby-fox.gif?f1652652213', species='dog', age=32, notes='Arf arf arf!', available=False)
# p4 = Pet(name='Greater Dog', photo_url='https://static.wikia.nocookie.net/topstrongest/images/a/a5/Greater_Dog_Sprite.gif', species='dog', age=12, notes="It's so excited that it thinks fighting is just play.", available=False)
# p5 = Pet(name='Lancer', photo_url='https://i.redd.it/sqct4z0kwhp71.gif', species='card', age=11, notes="Weeeeoo weeeeoo weeeeoo...", available=True)
# p6 = Pet(name='Berdly', photo_url='https://art.pixilart.com/sr2ebd1c5f722aws3.gif', species='card', age=13, notes="My queeeeiiinnnn...", available=False)
# p7 = Pet(name='Queen', photo_url='https://static.wikia.nocookie.net/fridaynightfunking/images/9/92/QueenRight.gif/', species='card', age=22, notes="OHHHHHH HO HO HO HOOOOOO.... THANK YOU FOR PICKING ME, FAITH FAITH!!", available=False)

db.session.add_all([p1, p2, p3, p4, p5, p6, p7])

db.session.commit()