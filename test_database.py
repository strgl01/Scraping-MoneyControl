from database import Database

def test_conn():
    db = Database()
    assert db.cursor and db.conn

def test_data_loser():
    db1 = Database()
    assert db1.read("select id from loser where name = 'semo'")

def test_data_gainer():
    db2 = Database()
    db2.add_data('gainer', [( 'asd', 22.3, '2002-10-01' )])
    assert db2.read("select id from gainer where name = 'asd'")