from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, String, create_engine, DateTime, func, Text
from sqlalchemy.orm import relationship, sessionmaker, validates

Base = declarative_base()

level_1 = """...............................................................wwwww...................................
...........................................................................*...........................
..........................................................................ggg..........................
.......................................................................................*...............
......................................................................................ggg..............
...........................................................................*...........................
..........................................................................ggg..........................
..............................................................%%%%%....................................
..............................................................ggggg....................................
......................................................$$$..............................................
......................................................ggg..............................................
...........................................###.........................................................
...........................................ggg.........................................................
..............................55555....................................................................
..............................ggggg....................................................................
...................11111...............................................................................
...................ggggg...............................................................................
.........111...........................................................................................
.........ggg...........................................................................................
.p.....................................................................................................
ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"""

level_2 = """..............................................................................................................................................................................................................................................................................................................
..............................................................................................................................................................................................................................................................................................................
..............................................................................................................................................................................................................................................................................................................
..............................................................................................................................................................................................................................................................................................................
..............................................................................................................................................................................................................................................................................$*$.............................
......................................................................................................................................................................................................................555.................................................ggggggggg...........................
.....................................................................................................................................................................................................................ggggg....................................................................................
.........................................................................................................................................................................................................11511.......................#.............#...........5$5............................................
............................................................................................................................................*............................................................ggggg.....................ggggg.........ggggn........ggggg...........................................
..........................................................................................................................................gggg.......ggg.......................................11511..........................................................................................................
...............................................................................................................................................................................................ggggg..........................................................................................................
.............................................................................................................................................................gggg......ggggg...................................................................................................%..............................
.......................................................................................................................1111..................#...................................gggxxxggg....................................................................................ggg.............................
................................................................................................................5......gggg......jjjj......gggg......gggg.....................................................................................................................................................
...............................................................................................................ggg...................................................................................................................................................................#........................
..........................................................................................111........1111...........................................................................................................................................................................ggg..........www..........
..........................................................................................ggg........gggg.....................................................................................................................................................................................................
...............................................................................1111...........................................................................................................................................................................................................................
.p.............gggggg....1....5.....#..g...a.....g......*......................gggg...........................................................................................................................................................................................................................
ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg..........gggnnnnnggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"""

level_3 = """.......................................................................................................................
.......................................................................................................................
..................................................................................$*$..................................
.................................................................................bbbbbbwwwb............................
.......................................................................................................................
...................................................................................................nbbbb...............
.......................................................................................%...............................
.....................................................................................ngggg.............................
.......................................................................11111...........................................
.......................................................................bbbbb...........................................
.........................................................5#5#5.........................................................
.........................................................bbbbb.........................................................
............................................%*%........................................................................
...........................................bbbbb.......................................................................
.............................#####.....................................................................................
.............................bbbbb.....................................................................................
.......................................................................................................................
................55555..................................................................................................
................bbbbb..................................................................................................
.....11111.............................................................................................................
.....bbbbb.............................................................................................................
.................1515..................................................................................................
.................bbbb..................................................................................................
..............................1111.....................................................................................
..............................bbbb..........5555.......................................................................
............................................bbbb.......................................................................
..........................................................#5............$..............................................
.........................................................bbbb.........bbbbb............................................
.......................................................................................................................
...................................................................................5555..........#*#...................
...................................................................................bbbb.........bbbbb..................
......................................................................5151.............................................
......................................................................bbbb.............................................
.........................................................1111..........................................................
.........................................................bbbb..........................................................
..............................................5151.....................................................................
..............................................bbbb.....................................................................
.................................1111..................................................................................
.................................bbbb..................................................................................
........1111.........1111..............................................................................................
........bbbb.........bbbb..............................................................................................
.......................................................................................................................
..p....................................................................................................................
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"""

level_4 = """...............................................................................5##5.............................................................5#5................................................................................
..............................................................................5....5...........................................................ggggg...............................................................................
.............................................................................5......5.............$.................*................%...................g..a...*...a..g..........##...............................................
...........................................................................gg........gg.........ggggg..............................ggggg.................ggggggggggggggg.........gggg..........##..................................
................................................................##.........xxxxxxxxxxxx....*.................$$...........$$..................................................................gggg..........##.....................
.......................................51515...................gggg........................g................gggg.........gggg..............................................................................gggg....................
.......................................ggggg.........jjnnnnnnnngggg.....................................................................................................................................................wwww.......
..........................11511....................................................................................................................................................................................................
..........................ggggg....................................................................................................................................................................................................
...p.........11111.................................................................................................................................................................................................................
..ggg........ggggg.................................................................................................................................................................................................................
...................................................................................................................................................................................................................................
..................................................................................................................................................................................................................................."""


class Levels(Base):
    __tablename__ = 'Levels'
    id = Column(Integer, primary_key=True)
    level_layout = Column(Text, nullable=False)
    best_stars = Column(Integer, default=0)
    best_time = Column(Integer, default=0)
    best_score = Column(Integer, default=0)
    background = Column(Text, default="Game/Assets/Background_1.png")
    

engine = create_engine('sqlite:///Game/Levels.db', echo=True)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
sesja = Session()

lvl1 = Levels(level_layout=level_1)
lvl2 = Levels(level_layout=level_2)
lvl3 = Levels(level_layout=level_3)
lvl4 = Levels(level_layout=level_4)

sesja.add(lvl1)
sesja.add(lvl2)
sesja.add(lvl3)
sesja.add(lvl4)

sesja.commit()

sesja.close()
