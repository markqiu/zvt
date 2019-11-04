# -*- coding: utf-8 -*-
from sqlalchemy import Column, Float
from sqlalchemy.ext.declarative import declarative_base

from zvdata.contract import register_schema
from zvt.domain.quotes import KdataCommon

# 指数日k线
Index1dKdataBase = declarative_base()


class Index1dKdata(Index1dKdataBase, KdataCommon):
    __tablename__ = 'index_1d_kdata'
    turnover_rate = Column(Float)

    # ETF 累计净值（货币 ETF 为七日年化)
    cumulative_net_value = Column(Float)
    # ETF 净值增长率
    change_pct = Column(Float)


register_schema(providers=['exchange'], db_name='index_1d_kdata', schema_base=Index1dKdataBase)