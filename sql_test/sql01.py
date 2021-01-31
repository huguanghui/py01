# -*- coding: utf-8 -*-

import sqlalchemy as db

Connection = None
Table = None
TableName = "danjuan_fund_2020_4"


def init_conn():
    global Connection, Table
    url = "mysql+pymysql://root:123789@119.45.214.139:23306/testdb"
    engine = db.create_engine(url)
    metadata = db.MetaData()
    Connection = engine.connect()
    Table = db.Table(TableName, metadata, autoload=True, autoload_with=engine)


def save_mysql(fund_code, fund_name, managers, enddate, detail_json):
    query = db.insert(Table).values(
        fund_name=fund_name,
        fund_code=fund_code,
        managers=managers,
        enddate=enddate,
        detail_json=detail_json,
    )
    Connection.execute(query)


def main():
    save_mysql("aa", "bb", "cc", "dd", "ee")


if __name__ == "__main__":
    init_conn()
    main()
