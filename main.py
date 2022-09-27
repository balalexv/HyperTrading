from datetime import datetime, timedelta

from utils.utils import get_token, get_link, cast_money, get_history_all_time, get_folder
from tinkoff.invest import Client
from tinkoff.invest.schemas import CandleInterval
from tinkoff.invest import Client, RequestError, CandleInterval, HistoricCandle

figi = 'BBG0013HJJ31'

df = get_history_all_time(figi = figi, token=get_token())

df.to_csv(get_folder() + figi + '.csv', index = False)