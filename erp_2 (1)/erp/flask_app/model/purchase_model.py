from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash




class Purchase:
    def __init__(self, data):
        self.id = data["id"]
        self.article_id = data["article_id"]
        self.purchased_quantity = data["purchased_quantity"]
        self.purchased_price = data["purchased_price"]
        self.date = data["date"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    

    @classmethod
    def create(cls,data):
        print("🦋"*20,data)
        query="""INSERT INTO purchases 
                        (article_id,purchased_quantity,date,purchased_price,owner_id)
                        VALUES (%(article_id)s,%(purchased_quantity)s,%(date)s,%(purchased_price)s,%(owner_id)s);"""
        x=connectToMySQL(DATABASE).query_db(query,data)
        print("❤️"*10,x)
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_all(cls,data):
        query = "SELECT * FROM purchases WHERE owner_id=%(owner_id)s;"
        results=connectToMySQL(DATABASE).query_db(query,data)
        allpurchases=[]
        for row in results:
            
            allpurchases.append(cls(row))
        return allpurchases
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM purchases WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0]) if result else None
    @classmethod
    def get_by_id(cls,data):
        query="""SELECT * FROM purchases WHERE id=%(id)s;"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return cls(result[0])
        return None
   
    @classmethod
    def destroy(cls,data):
        query="""DELETE FROM purchases WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod   
    def validate(data):
        is_valid=True
        if len(data['article_id'])==None:
            is_valid=False
            flash("choose article")
        if len(data['date'])== "":
            is_valid=False
            flash(" date is required")
        if (data['purchased_price'])==None:
            is_valid=False
            flash("purchased_price must be provided")
        if (data['purchased_quantity'])==None:
            is_valid=False
            flash("purchased_quantity must be provided")
        print(is_valid)
        return is_valid