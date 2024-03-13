import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def insertTaqvim(self,hafta_kuni,saharlik_vaqti,iftorlik_vaqti):
        try:
            self.cursor.execute(
                "INSERT INTO taqvim(hafta_kuni,saharlik_vaqti,iftorlik_vaqti) VALUES(?,?,?);",
                (hafta_kuni,saharlik_vaqti,iftorlik_vaqti)
            )
            self.conn.commit()
            res = {
                'status': True,
                'desc': 'Successfully inserted'
            }
        except Exception as e:
            res = {
                'status': False,
                'desc': 'Something error, please, try again'
            }
        return res

    def deleteTaqvim(self,id):
        try:
            self.cursor.execute(
                "DELETE FROM taqvim WHERE id=?",
                (id,)
            )
            self.conn.commit()
            res = {
                'status': True,
                'desc': 'Successfully deleted'
            }
        except Exception as e:
            res = {
                'status': False,
                'desc': 'Something error, please, try again'
            }
        return res

    def saharlik_vaqti(self):
        vaqt = self.cursor.execute(
            "SELECT saharlik_vaqti FROM taqvim "
        )
        return vaqt
    def iftorlik_vaqti(self):
        vaqt = self.cursor.execute(
            "SELECT iftorlik_vaqti FROM taqvim "
        )
        return vaqt

    def get_user_id(self, user_id):
        db_user_id = self.cursor.execute(
            "SELECT u_id FROM taqvim WHERE u_id = ?", (user_id,)
        ).fetchone()

        if db_user_id is None:
            self.cursor.execute(
                "INSERT INTO taqvim (u_id) VALUES (?)", (user_id,)
            )
            self.conn.commit()
            return user_id
        else:
            return db_user_id

