# # -*- coding: utf-8 -*-
# import pandas as pd
# from EmQuantAPI import *
#
# from zvt.api import TIME_FORMAT_DAY, get_str_schema
# from zvt.contract.api import df_to_db
# from zvt.contract.recorder import TimeSeriesDataRecorder
# from zvt.domain import HolderTrading
# from zvt.domain import StockDetail
# from zvt.recorders.emquantapi.common import mainCallback, to_em_entity_id
# from zvt.utils.pd_utils import pd_is_not_null
# from zvt.utils.time_utils import now_pd_timestamp, to_time_str
#
#
# class EmDividendDetailRecorder(TimeSeriesDataRecorder):
#     entity_provider = 'joinquant'
#     entity_schema = StockDetail
#
#     # 数据来自jq
#     provider = 'emquantapi'
#
#     data_schema = HolderTrading
#
#     def __init__(self, entity_type='stock', exchanges=['sh', 'sz'], entity_ids=None, codes=None, batch_size=10,
#                  force_update=False, sleeping_time=5, default_size=2000, real_time=False,
#                  fix_duplicate_way='add', start_timestamp=None, end_timestamp=None, close_hour=0,
#                  close_minute=0) -> None:
#         self.data_schema = get_str_schema('HoldTradeDetail')
#         super().__init__(entity_type, exchanges, entity_ids, codes, batch_size, force_update, sleeping_time,
#                          default_size, real_time, fix_duplicate_way, start_timestamp, end_timestamp, close_hour,
#                          close_minute)
#         # 调用登录函数（激活后使用，不需要用户名密码）
#         loginResult = c.start("ForceLogin=1", '', mainCallback)
#         if (loginResult.ErrorCode != 0):
#             print("login in fail")
#             exit()
#
#     def on_finish(self):
#         # 退出
#         loginresult = c.stop()
#         if (loginresult.ErrorCode != 0):
#             print("login in fail")
#             exit()
#
#     def record(self, entity, start, end, size, timestamps):
#         if not end:
#             end = to_time_str(now_pd_timestamp())
#         start = to_time_str(start)
#         em_code = to_em_entity_id(entity)
#         columns_list = list(self.data_schema.get_data_map(self))
#         data = c.ctr("HoldTradeDetailInfo", columns_list,
#                      "secucode=" + em_code + ",StartDate=" + start + ",EndDate=" + end + ",HoldType=0")
#
#         df = pd.DataFrame(data.Data).T
#         df.columns = columns_list
#         df = df.sort_values("NOTICEDATE", ascending=True)
#         df['TOTALSHARE'] = df.NOTICEDATE.apply(
#             lambda x: c.css(em_code, "TOTALSHARE", "EndDate=" + x + ",ispandas=1").TOTALSHARE[0])
#         # 变动比例（千分位） h = (df['变动_流通股数量(万股)'] / (df['变动后_持股总数(万股)'] / (df['变动后_占总股本比例(%)'] / 100)))
#         df['CHANGENUM'] = df['CHANGENUM'] * 10000
#         df['BDHCGZS'] = df['BDHCGZS'] * 10000
#         df['change_pct'] = abs(df['CHANGENUM'] / df['TOTALSHARE']).astype(float)*1000
#         df['change_pct'] = df['change_pct'].round(5)
#         if pd_is_not_null(df):
#             df.reset_index(drop=True, inplace=True)
#             df.rename(columns=self.data_schema.get_data_map(self), inplace=True)
#             df['entity_id'] = entity.id
#             df['timestamp'] = pd.to_datetime(df.holder_start_date)
#             df['provider'] = 'emquantapi'
#             df['code'] = entity.code
#
#             # def generate_id(se):
#             #     return "{}_{}_{}".format(se['entity_id'], to_time_str(se['timestamp'], fmt=TIME_FORMAT_DAY), se.name)
#
#             def generate_id(se):
#                 return "{}_{}".format(se['entity_id'], to_time_str(se['timestamp'], fmt=TIME_FORMAT_DAY))
#
#             df['id'] = df[['entity_id', 'timestamp']].apply(generate_id, axis=1)
#
#             df.to_excel("/mnt/c/Users/32771/Desktop/高管及相关人员持股变动zvt.xlsx")
#             df_to_db(df=df, data_schema=self.data_schema, provider=self.provider, force_update=self.force_update)
#         return None
#
#
# __all__ = ['EmDividendDetailRecorder']
#
# if __name__ == '__main__':
#     # 上证50
#     EmDividendDetailRecorder(codes=['050002']).run()
#     # JqChinaEtfValuationRecorder(codes=['512290']).run()
