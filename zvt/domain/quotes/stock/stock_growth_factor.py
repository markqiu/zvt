# -*- coding: utf-8 -*-
# this file is generated by gen_kdata_schema function, dont't change it
from sqlalchemy.ext.declarative import declarative_base

from zvt.contract.register import register_schema
from zvt.domain.quotes import StockGrowthFactorCommon

FactorBase = declarative_base()


class StockGrowthFactor(FactorBase, StockGrowthFactorCommon):
    @classmethod
    def important_cols(cls):
        return [
            'financing_cash_growth_rate',
            'net_asset_growth_rate', 'net_operate_cashflow_growth_rate',
            'net_profit_growth_rate', 'np_parent_company_owners_growth_rate',
            'operating_revenue_growth_rate', 'PEG',
            'total_asset_growth_rate', 'total_profit_growth_rate',
        ]

    __tablename__ = 'stock_growth_factor'


register_schema(providers=['joinquant'], db_name='stock_growth_factor', schema_base=FactorBase)

__all__ = ['StockGrowthFactor']
