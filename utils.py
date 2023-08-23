from exceptions import NegativeTitlesError, InvalidYearCupError
from exceptions import ImpossibleTitlesError
from datetime import datetime

# data = {
#     "name": "França",
#     "titles": -3,
#     "top_scorer": "Zidane",
#     "fifa_code": "FRA",
#     "first_cup": "1932-10-18",
# }


def data_processing(info_dic):
    now = datetime.now()
    first_cup_year = 1930
    years_cup = []
    quant_cups_possibles = []

    for i in range(first_cup_year, now.year, 4):
        years_cup.append(i)

    for i in range(int(info_dic["first_cup"][:4]), int(int(now.year)), 4):
        quant_cups_possibles.append(i)

    if years_cup.count(int(info_dic["first_cup"][:4])) == 0:
        raise InvalidYearCupError("there was no world cup this year")

    if info_dic["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    if info_dic["titles"] > len(quant_cups_possibles):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")


# data_processing(data)
